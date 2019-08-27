## Solution
**Automatically trigger and reverse the time sensitvie schedule task with input detail accordingly**, will introduce use case in below topic and things that need to be noticed while using.


## Use Case

* [Create_Cursor_Object](#Create_Cursor_Object)
  * [Setup_Value](#Setup_Value)
  * setup_period
  * setup_rules
  * save_task

### Create_Cursor_Object

*class* ___OfferGroupCursor(offer_id, kwargs**)___

#### Parameters :
| Parameter | Type | Required | Description |
|----|----|----|----|
|offer_id|_Int_|_Required_|Id of the offer which will be used to initialize the object with attributes|
|branch_at|_String_|_Optional_|To get the offer setting in specific moment|

```Python
from GroupSchedule import OfferGroupCursor

cursor = OfferGroupCursor(1544)
```

*function* ___group_create(kwargs**)___

#### Parameters :
| Parameter | Type | Required | Description |
|----|----|----|----|
|text_filter|_String_|_Optional_|Id of the offer which will be used to initialize the object with attributes|
|value_filter|_String_|_Optional_|To get the offer setting in specific moment|


---
### Setup_Value

*function* ___setup_default_value(kwargs**)___


