# EventFilter

Filter on change events in a storage backend.  The `prefix` and `suffix` properties are conditions on the object path (not including the bucket name). When not specified, all paths in the bucket will selected.  The `events` property can contain `put` and/or `delete` values, corresponding to create/update and deletion events. When not specified, only the create/update events are filtered.

**Source:** `waylay.services.storage.models.event_filter`




## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**prefix** | **str** |  | [optional] 
**suffix** | **str** |  | [optional] 
**events** | [**List[EVENTTYPE]**](EVENTTYPE.md) |  | [optional] [default to ["put"]]
**description** | **str** |  | [optional] 
**queue** | **str** |  | [optional] 


## Example

```python
from waylay.services.storage.models.event_filter import EventFilter

event_filter = EventFilter(
    prefix=..., suffix=..., events=..., description=..., queue=...
)

# Create from JSON
event_filter = EventFilter.from_json(
    '{ "prefix": ..., "suffix": ..., "events": ..., "description": ..., "queue": ... }'
)

# Export to dictionary
event_filter_dict = event_filter.to_dict()
```



[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


