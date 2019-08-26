from GroupSchedule import OfferGroupsCursor, api_req, api_url, config_params
from dateutil.parser import parse
import pymysql

database = pymysql.connect(host='54.238.199.106', port=3306, user='Ops', password='iloveShopBack!4', database='ShopBack', charset='utf8', autocommit='true')

def ss_app_portal(even, context) : 
    response = []
    offer_id = even[0]['offer_id']
    offset = []
    db_cursor = database.cursor(pymysql.cursors.DictCursor)
    db_cursor.execute('''SELECT * FROM GroupSchedule WHERE offer_id = '%s' and group_type = 'base' '''%offer_id)
    base = db_cursor.fetchall()
    if len(base) == 0 : # Setup base when it's empty to fallback.
        base_cursor = OfferGroupsCursor(offer_id)
        base_cursor.setup_period(is_base=True)
        base_cursor.push_cursor()
    for e in even :
        d = {'actived_from' : e['actived_from'], 'actived_to' : e['actived_to']}
        if d not in offset :
            offset.append(d)
    for o in offset :
        cursor = OfferGroupsCursor(offer_id, branch_at=o['actived_from'])
        offset_checker = []
        for e in even :
            if {'actived_from' : e['actived_from'], 'actived_to' : e['actived_to']} == o :
                if e['group_name'] == 'ba$e' :
                    cursor.setup_default_value(rate=e['rate'], percent=e['percent'])
                    offset_checker.append({'index' : e['index'], 'status': True, 'note': None})
                    continue
                elif len(cursor.group_display(text_filter=e['group_name'])) != 1 :
                    n = len(cursor.group_display(text_filter=e['group_name']))
                    if n == 0 :
                        r = api_req(api_url, [
                            config_params,
                            {'Target':'CashflowGroup'},
                            {'Method':'findCashflowGroups'},
                            {'filters[name]' : e['group_name']}
                        ])
                        if r.json()['response']['data']['records'] :
                            cursor.group_append(r.json()['response']['data']['records'][0]['id'], rate=e['rate'], percent=e['percent'])
                            offset_checker.append({'index' : e['index'], 'status': True, 'note': None})
                            print('[Note] Append %s(%s) Externally.'%e['group_name'], r.json()['response']['data']['records'][0]['id'])
                            continue
                    offset_checker.append({'index' : e['index'], 'status' : False, 'note' : '[Error] Bad Name With %s Group(s) Found'%n})
                    break
                cursor.group_display(text_filter=e['group_name'], return_object=True)[0].setup_value(rate = e['rate'], percent = e['percent'])
                offset_checker.append({'index' : e['index'], 'status': True, 'note': None})
        cursor.setup_period(actived_from=o['actived_from'], actived_to=o['actived_to'])
        if False not in [x['status'] for x in offset_checker] : cursor.push_cursor() 
        response += offset_checker       
    return response 