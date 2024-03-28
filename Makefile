printMsg=printf "\033[36m\033[1m%-15s\033[0m\033[36m %-30s\033[0m\n"

.PHONY: help test
## use triple hashes ### to indicate main build targets
help:
	@awk 'BEGIN {FS = ":[^#]*? ### "} /^[a-zA-Z0-9_\-\.]+:[^#]* ### / {printf "\033[1m\033[36m%-30s\033[0m %s\n", $$1, $$2}' $(MAKEFILE_LIST)
	@awk 'BEGIN {FS = ":[^#]*? ## "} /^[a-zA-Z0-9_\-\.]+:[^#]* ## / {printf "\033[36m%-30s\033[0m %s\n", $$1, $$2}' $(MAKEFILE_LIST)
.DEFAULT_GOAL := help

SERVICE_NAME=storage

API_FOLDER=waylay-sdk-${SERVICE_NAME}
API_SRC=${API_FOLDER}/src
TYPES_FOLDER=waylay-sdk-${SERVICE_NAME}-types
TYPES_SRC=${TYPES_FOLDER}/src
TEST_FOLDER=test
TEST_RUN_FOLDER=${TEST_FOLDER}/_run

CMD_FORMAT=ruff format --no-respect-gitignore --preview
CMD_FIX=ruff check --fix --unsafe-fixes --no-respect-gitignore --preview
CMD_CHECK=ruff check --no-respect-gitignore --preview

# disables test QA unless set to empty string
TEST_QA_PREFIX?=echo DISABLED

VENV_DIR=.venv
VENV_TYPES_DIR=.venv/types
VENV_TYPES_ACTIVATE_CMD=${VENV_TYPES_DIR}/bin/activate
VENV_TYPES_ACTIVATE=. ${VENV_TYPES_ACTIVATE_CMD}

${VENV_TYPES_ACTIVATE_CMD}:
	python3 -m venv ${VENV_TYPES_DIR}
	${VENV_TYPES_ACTIVATE} && make exec-dev-install-types

VENV_NOTYPES_DIR=.venv/notypes
VENV_NOTYPES_ACTIVATE_CMD=${VENV_NOTYPES_DIR}/bin/activate
VENV_NOTYPES_ACTIVATE=. ${VENV_NOTYPES_ACTIVATE_CMD}

${VENV_NOTYPES_ACTIVATE_CMD}:
	python3 -m venv ${VENV_NOTYPES_DIR}
	${VENV_NOTYPES_ACTIVATE} && make exec-dev-install-api


install-types: ${VENV_TYPES_ACTIVATE_CMD}

install-notypes: ${VENV_NOTYPES_ACTIVATE_CMD}

install: install-types

clean:
	rm -fr ${VENV_DIR}
	rm -fr .*_cache
	rm -fr */.*_cache
	rm -fr */src/*.egg-info
	rm -fr **/__pycache__
	rm -rf ${TEST_RUN_FOLDER}

lint: install ### Run linting checks
	@${VENV_TYPES_ACTIVATE} && make exec-lint

typecheck: install ### Run type checks
	@${VENV_TYPES_ACTIVATE} && make exec-typecheck

code-qa: install ### perform code quality checks
	@${VENV_TYPES_ACTIVATE} && make exec-code-qa

test: test-types test-notypes ### Run unit tests with and without types installed

test-types: install-types ### Run unit tests with types installed
	@${VENV_TYPES_ACTIVATE} && make exec-test
	@${printMsg} 'tests with types package installed' 'OK'

test-notypes: install-notypes ### Run unit tests with types installed
	@${VENV_NOTYPES_ACTIVATE} && make exec-test
	@${printMsg} 'tests without types package installed' 'OK'

format: install ### Format code
	@${VENV_TYPES_ACTIVATE} && make exec-format

exec-lint: ### Run linting checks
	cd ${API_FOLDER} && ${CMD_CHECK}
	@${printMsg} 'lint ${API_FOLDER}' 'OK'
	cd ${TYPES_FOLDER} && ${CMD_CHECK}
	@${printMsg} 'lint ${TYPES_FOLDER}' 'OK'
	${CMD_CHECK}
	@${printMsg} 'lint test' 'OK'

exec-typecheck: ### Run type checks
	cd ${API_SRC}/ && mypy --namespace-packages -p waylay
	@${printMsg} 'typecheck api' 'OK'
	cd ${TYPES_SRC}/ && mypy --namespace-packages -p waylay
	@${printMsg} 'typecheck types' 'OK'
	${TEST_QA_PREFIX} mypy ${TEST_FOLDER}
	@${printMsg} 'typecheck test' '${TEST_QA_PREFIX} OK'

${TEST_RUN_FOLDER}: # workaround for JSF schema resolution
	mkdir -p ${TEST_RUN_FOLDER}
	cp -r openapi ${TEST_RUN_FOLDER}/openapi
	# let JSF loader resolve './xx.yaml' to 'openapi/xx.yaml.json'
	# and make contentEncoding=base64 work
	cd ${TEST_RUN_FOLDER}/openapi && for f in `ls *.yaml`; \
		do \
			cat $$f | yq 'tojson' | sed -e 's/"base64"/"base-64"/' > $$f.json; \
			cd .. && ln -s openapi/$$f.json $$f; cd openapi; \
		done

exec-test: ${TEST_RUN_FOLDER} ### Run unit tests
	cd ${TEST_RUN_FOLDER} && pytest ..

exec-format: ### Format code
	${CMD_FIX} ${API_FOLDER}
	${CMD_FORMAT} ${API_FOLDER}
	@${printMsg} 'format api' 'OK'
	${CMD_FIX} ${TYPES_FOLDER}
	${CMD_FORMAT} ${TYPES_FOLDER}
	@${printMsg} 'format types' 'OK'
	${CMD_FIX} ${TEST_FOLDER}
	${CMD_FORMAT} ${TEST_FOLDER}
	@${printMsg} 'format test' 'OK'

exec-code-qa: exec-lint exec-typecheck ### perform code quality checks

ci-code-qa: exec-code-qa ### perform ci code quality checks

exec-dev-install-types: exec-dev-install-api ### Install the development environment including types
	pip install -e ${TYPES_FOLDER}[dev]

exec-dev-install-api: _install_requirements ### Install the minimal development environment
	pip install -e ${API_FOLDER}[dev]

ci-install-types: ci-install-api ### Install the environment including types with frozen requirements
	pip install './${TYPES_FOLDER}[dev]'

ci-install-api: _install_requirements ### Install the minimal environment with frozen requirements
	pip install './${API_FOLDER}[dev]'

ci-test: exec-test ### perform ci unit tests

_install_requirements:
	pip install --upgrade pip
	pip install -r requirements.txt

_GENERATED_FOLDER?=.
_GENERATED_FILES=.openapi-generator/FILES

_clean_gen:  ### Removes all code-generated files
	@test -s ${_GENERATED_FOLDER}/${_GENERATED_FILES} || ( \
		${printMsg} 'clean-generated ${_GENERATED_FOLDER}' 'FAILED (no ${_GENERATED_FILES}).' \
		&& exit -1 \
	)
	cd ${_GENERATED_FOLDER} && xargs rm -f < ${_GENERATED_FILES} && find . -empty -type d -delete
	@${printMsg} 'clean-generated ${_GENERATED_FOLDER}' 'OK'
	
clean-generated:  ### Removes all code-generated files
	@make clean
	@_GENERATED_FOLDER=${TYPES_FOLDER} make _clean_gen
	@_GENERATED_FOLDER=${API_FOLDER} make _clean_gen
	@_GENERATED_FOLDER='.' make _clean_gen
