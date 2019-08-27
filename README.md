## Solution
**Automatically trigger and reverse the time sensitvie schedule task with input detail accordingly**, will introduce use case in below topic and things that need to be noticed while using.


## Use Case

* [OfferObject](#class-offergroupcursoroffer_id-kwargs)
  * [group_display()](#function-group_displaykwargs)
  * [group_append()](#function-group_appendkwargs)
  * setup_rules
  * save_task
  
### structure




#### class _OfferGroupCursor(offer_id, kwargs**)_

#### Parameters :
| Parameter | Type | Required | Description |
|----|----|----|----|
|_offer_id_|_int_|_Required_|_Id of the offer which will be used to initialize the object with attributes_|
|_branch_at_|_string_|_Optional_|_To get the offer setting in specific moment_|

```Python
from GroupSchedule import OfferGroupCursor

# get offer 1544 current setting.
cursor = OfferGroupCursor(1544)

# get offer 1544 setting at 2019-01-01 18:00:00
cursor = OfferGroupCursor(1544, branch_at='2019-01-01 18:00:00')
```
#### Return :
```Python
None
```

---

#### function _group_display(kwargs**)_

###### Search groups by names or value and return dictionary information.

#### Parameters :
| Parameter | Type | Required | Description |
|----|----|----|----|
|_text_filter_|_string_|_Optional_|_Key for group name search_|
|_value_filter_|_string_|_Optional_|_Key for group value search_|
|_return_object_|_string_|_Optional_|_Return list with eligible groups_|

```Python
groups = cursor.group_display(text_filter='AU')
```

#### Return :
```Python
# Dictionary in list
[{'name': 'AU',
  'description': 'AU Group',
  'affiliates': [],
  'rules': [{'id': '1234',
    'cashflow_group_id': '2345',
    'field': 'field7',
    'operator': 'IN',
    'value': ['rule_value_1'],
    'negate': '0'},
   {'id': '4567',
    'cashflow_group_id': '2345',
    'field': 'field8',
    'operator': 'IN',
    'value': ['rule_value_2'],
    'negate': '1'}],
  'cashflow_group_id': '2345',
  'offer_id': 1544,
  'percent': '10',
  'rate': None,
  'follow': 1}]
  
  # Group object in list if return_object=True
  [GroupSchedule.Group]
```
---

#### function _group_append(cashflow_group_id, kwargs**)_

###### add group into cursor object and define its value, at least one kind of value need to be defined.

#### Parameters :
| Parameter | Type | Required | Description |
|----|----|----|----|
|_cashflow_group_id_|_int_|_Required_|_id of cashflowgroup object_|
|_percent_|_float_|_Optional_|_percent(%) value_|
|_rate_|_float_|_Optional_|_rate($) value_|

```Python
cursor.group_append(2000, percent=5.5, rate=30)
```
---
### setup_value

*function* ___setup_default_value(kwargs**)___


