# EventFilter

Filter on change events in a storage backend.  The `prefix` and `suffix` properties are conditions on the object path (not including the bucket name). When not specified, all paths in the bucket will selected.  The `events` property can contain `put` and/or `delete` values, corresponding to create/update and deletion events. When not specified, only the create/update events are filtered.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**prefix** | **str** |  | [optional] 
**suffix** | **str** |  | [optional] 
**events** | [**List[VENTTYPE]**](VENTTYPE.md) |  | [optional] [default to ["put"]]
**description** | **str** |  | [optional] 
**queue** | **str** |  | [optional] 

## Example

```python
from waylay.services.storage.models.event_filter import EventFilter

# TODO update the JSON string below
json = "{}"
# create an instance of EventFilter from a JSON string
event_filter_instance = EventFilter.from_json(json)
# print the JSON string representation of the object
print EventFilter.to_json()

# convert the object into a dict
event_filter_dict = event_filter_instance.to_dict()
# create an instance of EventFilter from a dict
event_filter_form_dict = event_filter.from_dict(event_filter_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


