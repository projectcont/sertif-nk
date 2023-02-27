import pandas as pd
def get_cn(df) :
    rows_nubmer = df.shape[0]
    columns_nubmer = df.shape[1]
    ctl=df.columns.tolist()
    cn_vid, cn_status, cn_sector, cn_level, cn_object, cn_org, cn_surname, cn_name, cn_otch, cn_expire, cn_exam, cn_number= -1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1

    for i in range(columns_nubmer):
        column_title = ctl[i]
        #print(i,column_title)
        if  'вид' in column_title.lower():
            cn_vid=i; print('Колонка - вид контроля, позиция= ',i)
        if  'статус' in column_title.lower():
            cn_status=i;            print('Колонка - статус, позиция= ',i)
        if  'сектор' in column_title.lower():
            cn_sector=i;            print('Колонка - произв. сектор, позиция= ',i)
        if  'уров' in column_title.lower():
            cn_level=i;            print('Колонка - уровень квал., позиция= ',i)
        if  'объект' in column_title.lower():
            cn_object=i;            print('Колонка - объект контроля, позиция',i)
        if  'организац' in column_title.lower():
            cn_org=i;            print('Колонка - организация, позиция',i)
        if  'фамилия' in column_title.lower():
            cn_surname=i;            print('Колонка - фамилия, позиция',i)
        if  'имя' in column_title.lower():
            cn_name=i;            print('Колонка - имя, позиция',i)
        if 'отчество' in column_title.lower():
            cn_otch = i; print('Колонка - отчество, позиция', i)
        if  'срок' in column_title.lower():
            cn_expire=i;            print('Колонка - дата, позиция',i)
        if 'экзам' in column_title.lower():
            cn_exam = i; print('Колонка - экзам.центр, позиция', i)
        if  '№' in column_title.lower():
            cn_number=i; print('Колонка - № сертификата, позиция= ',i)

    cn_numbers= { 'vid':cn_vid,
                  'status':cn_status,
                    'sector':cn_sector,
                    'level':cn_level,
                    'object':cn_object,
                    'org':cn_org,
                    'surname':cn_surname,
                    'name':cn_name,
                    'otch':cn_otch,
                    'expire':cn_expire,
                    'exam':cn_exam,
                    'number':cn_number }

    empty=[]

    for key in cn_numbers:
        if cn_numbers[key]==-1:
            empty.append(key)


    if -1 in cn_numbers.values():
        print()
        print('ОШИБКА В ФОРМАТЕ EXCEL-ФАЙЛА, НЕ ОПРЕДЕЛЕНЫ КОЛОНКИ', empty)
        raise SystemExit

    return  cn_numbers
