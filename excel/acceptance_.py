import pandas
import datetime
def acceptance (pr):

    accept = 1

    # checking ean
    if   ('product_ean' not in pr.keys() ) :
        #print(f"          строка  ( {pr['name_ru-RU']}) не принята, ошибка в номере сертификата ")
        not_accepted_error='ошибка в номере сертификата'
        accept = 0
    elif pr['product_ean'] == 'nan':
            print(f"          строка  ( {pr['name_ru-RU']}) не принята, ошибка в номере сертификата ")
            accept = 0


    # checking category_id  (vid)
    if   ( pr['category_id'] == -1 ) :
        not_accepted_error = 'ошибка в виде контроля'
        #print(f"          строка  ( {pr['name_ru-RU']}, {pr['product_ean']}) не принята, ошибка в виде контроля ")
        accept = 0

    # checking vendor_id  (status)
    if (pr['vendor_id'] == -1):
        not_accepted_error = 'ошибка в статусе'
        accept = 0



    # checking manufacturer_id  (level)
    if   ( 'product_manufacturer_id' not in pr.keys() ) :
        not_accepted_error = 'ошибка в уровне квалификации'
        #print(f"          строка  ( {pr['name_ru-RU']}) не принята, ошибка в уровне квалификации ")
        accept = 0
    elif pr['product_manufacturer_id'] == 'nan':
            #print(f"          строка  ( {pr['name_ru-RU']}) не принята, ошибка в уровне квалификации ")
            accept = 0

    # checking expire
    if  (pr['manufacturer_code']==-1):
        #print(f"          строка  ( {pr['name_ru-RU']}) не принята, ошибка в дате сертификата ")
        not_accepted_error = 'ошибка в дате сертификата'
        accept = 0

    if accept == 0:
        with open("not_accepted.txt", "a") as file:
            file.write(f" {pr['name_ru-RU']} не принята, {not_accepted_error}   \n")



    expiry = pr['manufacturer_code']
    if isinstance(expiry, str):
        index = expiry.rfind('.') + 1
        year = int(expiry[index:])
        if year<2022:
            not_accepted_error = ''
            #not_accepted_error = 'год сертификата <2022'
            #print(f"          строка  ( {pr['name_ru-RU']}) не принята, год сертификата <2022 ")
            accept = 0


    return accept

