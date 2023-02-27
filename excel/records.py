import pandas
import datetime
import math

def records_ (rowline):

    pr={}

    #correspondence between (excel) and pr


    ean=rowline['rv_number']


    if isinstance(ean, str):
        ean = ean.strip(' ')  # sert_number

        index = ean.rfind('$')
        if index>-1: ean=ean[:index]

    else:
        isNaN = math.isnan(rowline['rv_number'])
        if (isNaN):
            pr['product_ean']='0000'
            #print('ean isNaN=', isNaN)
        else:
            ean = round(rowline['rv_number'])
            ean = str(ean).strip(' ')

    pr['product_ean'] = ean  # sert_number


    pr['name_ru-RU'] =  str(rowline['rv_fio']).strip(' ')
    pr['description_ru-RU'] = str(rowline['rv_descr']).strip(' ')


    pr['custom1'] = str(rowline['rv_org']).strip(' ')
    pr['custom2'] = str(rowline['rv_exam']).strip(' ')
    pr['custom3'] = str(rowline['rv_sector']).strip(' ')
    pr['custom4'] = str(rowline['rv_object']).strip(' ')




    # formatting expire
    pr['manufacturer_code']=-1
    expire= rowline['rv_expire']
    #pr['manufacturer_code'] = rowline['rv_expire']

    if isinstance (expire, datetime.datetime) and (str(expire) != 'NaT'):
        if isinstance(expire, pandas._libs.tslibs.timestamps.Timestamp):
            panda_dt = expire
            dt = panda_dt.to_pydatetime()
            expirydate = dt.strftime("%d") + '.' + dt.strftime("%m") + '.' + dt.strftime("%Y")
            pr['manufacturer_code'] = expirydate
        else:
            dt = expire
            print('333333',expire, type(expire), isinstance (expire, datetime.datetime),  str(expire))
            expirydate = dt.strftime("%d") + '.' + dt.strftime("%m") + '.' + dt.strftime("%Y")
            pr['manufacturer_code'] = expirydate
    else:
        if str(expire) != 'NaT':
            expirydate = str(expire)
            pr['manufacturer_code'] = expirydate
            print('222222',expirydate, type(expire))
        if str(expire)=='NaT':
            #print('expire NaT= ')
            pr['manufacturer_code'] = -1



    # level - manufacturer_id
    level_=str(rowline['rv_level']).strip(' ')
    level_ = level_.replace('.', '')
    level_ = level_.replace('0', '')
    level_ = level_.replace(' ', '')


    if (level_ == 'I') or  (level_ == '1') : pr['product_manufacturer_id'] = 2
    if (level_ == 'II') or  (level_ == '2'): pr['product_manufacturer_id'] = 9
    if (level_ == 'III') or  (level_ == '3'): pr['product_manufacturer_id'] = 10





    # vid - category
    category_id=-1
    vid_=str(rowline['rv_vid']).strip(' ').lower()
    if 'эмиссионн' in vid_ :   category_id=2
    if 'вихр'  in vid_ : category_id=  8
    if 'инфра' in vid_: category_id= 9
    if 'тече' in vid_:  category_id=10
    if 'магнит' in vid_:  category_id=11
    if 'капилляр' in vid_:  category_id=12
    if 'радио' in vid_:  category_id=13
    if 'радиа' in vid_:  category_id = 13
    if 'тензо' in vid_:  category_id=14
    if 'ультразв' in vid_:  category_id=15
    if 'визуал' in vid_:  category_id=16

    if 'акуст' in vid_:  category_id = 2
    if 'термогр' in vid_:  category_id = 9


    pr['category_id']=category_id


    # status - vendor_id
    status_=str(rowline['rv_status']).strip(' ') .lower()
    pr['vendor_id']=-1
    if 'действует' in status_:
        pr['vendor_id'] = 1
    if (('не' in status_) or ('врем' in status_)) :
        pr['vendor_id']=2
    if 'закончил' in status_:
        pr['vendor_id'] = 3
    if 'прекращен' in status_:
        pr['vendor_id'] = 4



    #print(pr['name_ru-RU'],pr['vendor_id'])




    alias_ = str(rowline['rv_number'])
    alias_list = [n for n in alias_ if n in '0123456789']
    alias = ''.join(alias_list)

    alias = str(len(rowline['rv_fio']))+'-' + str(alias)+'-'+str(category_id)
    #print('alias=',alias)
    pr['alias_ru-RU'] = alias



    return pr