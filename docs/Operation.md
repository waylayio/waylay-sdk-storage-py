

# REST _operation methods_

The SDK service module `waylay.services.storage.service` is a generated
plugin for the Waylay Python SDK.

For each of the operations described in the
[OpenAPI specification](https://docs.waylay.io/openapi/sdk/redocly/storage.html)
of the service, a python _operation_ method is generated.

These _operation methods_ have a standard sequence of (_positional_ and _named_) arguments,
 as illustrated by this example REST operation
`POST /demo/v5/gadgets/{id}/trinkets/combatulate` with _operationId_ `combatulateTrinket`

## Example request

```python
response = await waylay_client.demo.gadgets.combatulate_trinket(
    # required path parameters (positional), for the `id` path parameter
    '23456',
    # required or optional query parameters (named)
    query={
        'compression_level': 15
    },
    # request body named arguments (named)
    # in this case using generated model for an `application/json` request
    json=CombatulationRecipe(mode='traditional', decoration='minimal'),
    # optional http headers (named)
    headers: {
        'accept' : 'text/csv'
    },
    # optional named arguments that specify how the response should be rendered (named)
    raw_response=False,
    select_path=None,
    response_type=None,
    # optional named arguments passed to the http client  (named)
    timeout=10.0,
)
```

# <a id='req_arg'></a> Supported request arguments

Each _operation method_ of this SDK uses the following arguments:

## Argument overview
* [`*path_args: str`](#req_arg_path) required positional path parameters
* [`query: QueryRequest`](#req_arg_query) url query parameters
* [request body](#req_arg_body) arguments
  * [`json: Any`](#req_arg_json) a model instance or python data structure for a json request (`application/json`)
  * [`content: ContentRequest`](#req_arg_content) raw bytes of any content type
  * [`files: FilesRequest`](#req_arg_files) a multi-part request (`multipart/form-data`)
  * [`data: DataRequest`](#req_arg_data) an url-encoded form (`application/x-www-form-urlencoded`), or additional non-file parts of a multi-part request.
* [`headers: HeadersRequest`](#req_arg_headers) http request headers
* [response rendering](#req_arg_render) arguments that specify how the response is presented
  * [`raw_response: bool`](#req_arg_raw): if `True` returns a http `Response` object
  * [`select_path: str`](#req_arg_select): used on a `json` `dict` response to select the relevant part of the response.
  * [`response_type: Type | None`](#req_arg_response_type): parse the response as an instance of specified type.
* [http client](#req_arg_client) arguments that influence the handling of the http call.

## Typing of arguments
The generated methods of this SDK will include additional type information, including
* the actual names of the the path arguments
* model types for the `json` request argument
* keys and values for documented `query`, `header` and `data`

The most relevant request body arguments (of `json`, `files`, `data`, `content`)
are explicitly documented, leaving the others as optional `**kwargs` named parameters.

But even if not explicitly documented in the typed signature, you can use the other request body arguments,
assuming the server supports it.

## Using `content` to send a request body.
The `content` argument is always available as named argument.
Even if e.g. the typing of `combatulate_trinket` method suggests to use a `json` argument,
you can alternatively specify a binary `content` request to stream an already json-encoded request from file.

```python
binary_req_body = b'{"mode":"traditional","decoration":"minimal"}'
response = await waylay_client.demo.gadgets.combatulate_trinket(
    '23456',
    content=binary_req_body,
    headers={'content-type' : 'application/json'}
)
```

## <a id='req_arg_path'></a> Path parameter arguments
In case the REST operation supports path parameters that configure the request URL,
they are presented as required (positional) initial parameters of type `str`.

In the example above, the first `'23456'` corresponds to the `id` path parameter,
and leads to a call with url 
```
POST /demo/v5/gadgets/23456/trinkets/combatulate
```

## <a id='req_arg_query'></a> Query parameter arguments
```python
query: QueryRequest
```
with types
```python
QueryRequest = QueryMap | QueryEntries | QueryString | Model
PrimitiveData = str | int | float | bool | None
# a mapping of query keys to values or list of values
QueryMap = Mapping[str, Union[PrimitiveData, Sequence[PrimitiveData]]]
# a list of query tuples, with repeated keys
QueryEntries = List[Tuple[str, PrimitiveData]] | Tuple[Tuple[str, PrimitiveData], ...]
# a query string, to be used as is on the request
QueryString = str | bytes
```

The named `query` argument holds all url query parameters.
Any query arguments described in the OpenAPI document will typed, but undocumented
query parameters will be forwarded. E.g. using
```
query={ 'compression_level': 15, 'debug': True }
```
Will lead to a request with url query parameters
```
POST /demo/v5/gadgets/23456/trinkets/combatulate?compression_level=15&debug=true
```

Any model instance specified as an argument will be converted to its `dict` representation first,
which has to be compatible with a `QueryMap`

##  <a id='req_arg_body'></a> Request body arguments
The following cases are supported for request body arguments
* [`json: Any`](#req_arg_json) a model instance or python data structure for a json request (`application/json`)
* [`content: ContentRequest`](#req_arg_content) raw bytes of any content type
* [`files: FilesRequest`](#req_arg_files) a multi-part request (`multipart/form-data`)
* [`data: DataRequest`](#req_arg_data) an url-encoded form (`application/x-www-form-urlencoded`), or additional non-file parts of a multi-part request.

###  <a id='req_arg_json'></a>  JSON request argument `json`
The `json` argument allows the user to specify a `application/json` request body, using a
generated instance of a generated _Model_ class, or as a python data structure.

```python
json: Any
```

Most REST operations use a JSON (`application/json`) request body, and the SDK service module
will provide typed _model_ classes for them.

These requests can be passed as a `json` named parameter, either as _model instances_ or as plain
python `dict`, `array` or primitive types that are JSON-serializable.

#### Example
The following examples assume that the server supports `application/json` requests.

```python
response = await waylay_client.demo.gadgets.combatulate_trinket(
    '43466',
    json=CombatulationRecipe(mode='traditional', decoration='minimal')
)
```
```python
response = await waylay_client.demo.gadgets.combatulate_trinket(
    '43466',
    json={'mode':'traditional', 'decoration':'minimal'}
)
```
Will both send a json request with payload `{"mode":"traditional","decoration":"minimal"}` to the server,

assuming that `CombatulationRecipe` is a model class that does not include additional default attributes.

### <a id='req_arg_content'></a>  Binary request argument `content`
The `content` argument allows the user to specify a raw binary request of any content type.

```python
content: ContentRequest
```
with types
```python
ContentRequest = bytes | str | Iterable[bytes] | AsyncIterable[bytes] | IO[bytes]
```

For operations with non-JSON request bodies, the request body must be specified in its binary form 
using the `content` argument.

Unless a default `content-type` is defined in the OpenAPI specification, or at the server, you need
to specify a `content-type` header.

Supported values for the `content` argument are:
* a `bytes` instance such as `b'abc'`
* `str` instances will be converted to `bytes` using the `utf-8` encoding.
* an `Iterable` that produces `bytes`
* an `AsyncIterable` that produces bytes
* a `IO[bytes]` object that is converted to a `Iterable[bytes]` (if it not yet is).

When the SDK can infer a total length of the bytes stream (e.g. when attached to a file),
the request will be uploaded as one stream with a `content-length` header indicating the length.

Otherwise, the content is sent in chuncks (using `"Transfer-Encoding": "chunked"`),
looping over the iterable or buffered reads from the stream.

#### examples
Using a bytes string:
```python
response = await waylay_client.demo.gadgets.combatulate_trinket(
    '23456',
    content=b'{"mode":"traditional","decoration":"minimal"}',
    headers={'content-type' : 'application/json'}
)
```
Using an iterator with `bytes` chunks:
```python
def generate_chunks():
    yield b'{"mode":'
    yield b'"traditional",'
    yield b'"decoration":"minimal"'
    yield b'}'
response = await waylay_client.demo.gadgets.combatulate_trinket(
    '23456',
    content=generate_chunks(),
    headers={'content-type' : 'application/json'}
)
```

From file, assuming the server supports xml requests:
```python
with open('~/combatulation_requests/example_23456.xml') as xml_file:
    response = await waylay_client.demo.gadgets.combatulate_trinket(
        '23456',
        content=xml_file,
        headers={'content-type' : 'text/xml'}
    )
```

### <a id='req_arg_files'></a> Multipart file request argument `files` (and `data`)
The `files` argument triggers the composition of a `multipart/form-data` request.
```python
files: FilesRequest
data: DataRequest
```
with types
```python
FilesRequest = Mapping[str, FileTypes] | Sequence[Tuple[str, FileTypes]]
DataRequest = Optional[Mapping[str, bytes | PrimitiveData]]

FileTypes = FileContent | FileNameContent | FileNameContentType | FileNameContentTypeHeaders

# the raw content as bytes (stream)
FileContent = Union[IO[bytes], bytes, str]
# a file name and content
FileNameContent = [Optional[str], FileContent]
# a file name, content and mediatype string
FileNameContentType = [Optional[str], FileContent, Optional[str]]
# a file name, content, mediatype and additional headers
FileNameContentTypeHeaders = [Optional[str], FileContent, Optional[str], Mapping[str, str]]

PrimitiveData = str | int | float | bool | None
```

When the REST operation supports a multipart file request (content type `multipart/form-data`),
use the `files` named argument to construct such request.
Each entry in the `files` argument ends up as one part of a multipart request, using the specified 
part name.

You can provide the raw bytes (stream) only,
or optionally specify the `filename`, `content-type` or additional `headers` for each part.

When a `data` argument is specified, these will be added as additional non-file parts,

#### Example
The following examples assume that the server supports `multipart/form-data` requests.
```python
response = await waylay_client.demo.gadgets.combatulate_trinket(
    '43466',
    files={'background': open('~/images/deepblue.png)},
    data={'mode':'traditional', 'decoration':'minimal'}
)
```

Will send the data as `multipart/form-data`, with three sections `background`, `mode` and `decoration`.

```python
response = await waylay_client.demo.gadgets.combatulate_trinket(
    '43466',
    files={
        'background': ['deepblue.png', open('~/images/deepblue.png),'image/png']
    },
    data={'mode':'traditional', 'decoration':'minimal'}
)
```
sends the same data, but a filename and content type is added to the `background` part.




### <a id='req_arg_data'></a> Url-encoded form data `data`
The `data` argument triggers the composition of an `application/x-www-form-urlencoded` html form request.

```python
data: Optional[Mapping[str, bytes | PrimitiveData]]
```

For operations that use url-encoded form data (content type `application/x-www-form-urlencoded`),
use the `data` named argument (without a `files` argument).

The http client will in that case use that content-type and encode the using that style.

These type of operations are normally meant to support [simple html forms](https://developer.mozilla.org/en-US/docs/Web/HTTP/Methods/POST#example).

#### Example
The following example assumes that the server supports `application/x-www-form-urlencoded` requests.

```python
response = await waylay_client.demo.gadgets.combatulate_trinket(
    '43466',
    data={'mode':'traditional', 'decoration':'minimal'}
)
```
Will send the data with content-type `application/x-www-form-urlencoded`, as if an html form submitted
this request with form inputs `mode` and `decoration`.

## <a id='req_arg_headers'></a> Request `headers` argument

TODO

## <a id='req_arg_render'></a> Response rendering arguments

### <a id='req_arg_raw'></a> Render a raw http response: `raw_response`
TODO

### <a id='req_arg_select'></a> Select a part of the response: `select_path`
TODO

### <a id='req_arg_response_type'></a> Parse the 2XX response as an instance of type: `response_type`
TODO

## <a id='req_arg_http'></a> Http client arguments

TODO
