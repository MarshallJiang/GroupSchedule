## Solution
**Automatically trigger and reverse the time sensitvie schedule task with input detail accordingly**, will introduce use case in below topic and things that need to be noticed while using.


## Use Case

* [create client](#create_client)
  * [setup_value](#setup_value)
  * setup_period
  * setup_rules
  * save_task

### create_client

*class* ___OfferGroupCursor(offer_id, kwargs**)___

#### Parameters :
| Parameter | Type | Required | Description |
|----|----|----|----|
|_offer_id_|_Int_|_Required_|_Id of the offer which will be used to initialize the object with attributes_|
|_branch_at_|_String_|_Optional_|_To get the offer setting in specific moment_|

```Python
from GroupSchedule import OfferGroupCursor

# get offer 1544 current setting.
cursor = OfferGroupCursor(1544)

# get offer 1544 setting at 2019-01-01 18:00:00
cursor = OfferGroupCursor(1544, branch_at='2019-01-01 18:00:00')
```

*function* ___group_display(kwargs**)___

###### Search groups by names or value and return object.

#### Parameters :
| Parameter | Type | Required | Description |
|----|----|----|----|
|_text_filter_|_String_|_Optional_|_Key for group name search_|
|_value_filter_|_String_|_Optional_|_Key for group value search_|
|_return_object_|_String_|_Optional_|_Return list with eligible groups_|


---
### setup_value

*function* ___setup_default_value(kwargs**)___


