from format import *
from excel.records import *
from excel.acceptance_ import acceptance
import pandas as pd
import excel.get_column_numbers as gcn
import math


def get_pr_list_from_excel (file, number_or_lines ):
    index2=number_or_lines

    def is_not_nan(num): return num == num

    def is_nan(num): return num != num


    try:
        df=pd.read_excel(file)
    except:
        # traceback.print_exc()
        print('ОШИБКА: ВЕРОЯТНО, EXCEL-ФАЙЛ НЕПРАВИЛЬНОГО ФОРМАТА ')
        quit()

    rows_nubmer=df.shape[0]
    columns_nubmer=df.shape[1]
    print('Excel-файл строк =', rows_nubmer)
    print('Excel-файл колонок =', columns_nubmer)

    #print('Excel-файл колонки =',type(df.columns.tolist())  )

    # get columns number (in dataframe) for each expert's option
    cn=gcn.get_cn(df)

    pr_list = [] #product properties

    print()
    printf('EXCEL всего анкет       =', rows_nubmer)
    if index2==0: index2=rows_nubmer
    if index2 > rows_nubmer: index2 = rows_nubmer
    printf('EXCEL анкет извлекается =', index2)
    printf()

    for rx in range(index2):

        line_ =df.iloc[rx]

        # check is it real product line
        if is_not_nan(line_[  cn['vid']   ]):



            if (isinstance(line_[ cn['name'] ], str) and isinstance(line_[cn['surname']], str) and isinstance(line_[cn['otch']], str)):
                fio=line_[ cn['surname'] ].strip(' ') + ' ' + line_[ cn['name']] .strip(' ') + ' ' + line_[ cn['otch'] ].strip(' ')
            else:
                fio = line_[cn['surname']].strip(' ')

            print(rx, fio, line_[ cn['number']], line_[ cn['expire'] ] )

            description=""

            rowline={ 'rv_fio':   fio,
                      'rv_vid':    line_[ cn['vid']  ],
                      'rv_status': line_[ cn['status'] ],
                      'rv_sector': line_[ cn['sector'] ],
                      'rv_level':  line_[ cn['level'] ],
                      'rv_object': line_[ cn['object'] ],
                      'rv_org':    line_[ cn['org'] ],
                      'rv_expire': line_[ cn['expire'] ],
                      'rv_exam':   line_[ cn['exam'] ],
                      'rv_number': line_[ cn['number'] ] ,
                      'rv_descr':  description
                     }

            # convert excel-data to  pr-list
            pr=records_ (rowline)

            if (  acceptance(pr)==1 ):
                pr_list.append(pr)

                #print('accepted ', rx, fio, line_[cn['number']], line_[cn['expire']])


    if not pr_list:
        printf('ОШИБКА EXCEL-ФАЙЛА - ВЕРОЯТНО НЕТ ДАННЫХ В ФАЙЛЕ')
        quit()



    return pr_list














