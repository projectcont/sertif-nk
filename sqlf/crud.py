
from prodcateg.category import Category
from prodcateg.custom import Custom
import traceback
import time



def prodlist_add (prod_list_add,session):
    '''
    for all 'products' in 'prod_list'
    function adds each 'product' to database
    :param prod_list: list of products
    :param session:  session
    :return:
    '''

    print()
    print('crud1 ЭКСПОРТ ДАННЫХ НА САЙТ')


    counter=0

    for prod in prod_list_add:


        try:

            timedfn0 = time.perf_counter() * 100

            session.add(prod)
            session.flush()
            session.refresh(prod)

            timefn1 = time.perf_counter() * 100; timefn=timefn1 - timedfn0
            print('          ', counter,  ' добавлено ', getattr(prod, 'name_ru-RU'), f' (серт.№ {prod.product_ean}) ')

            ctp = Category()
            ctp.setpr(prod)
            session.add(ctp)



            custom_ru=Custom()
            custom_ru.setpr(prod,lang="ru-RU")



            custom_eng = Custom()
            custom_eng.setpr(prod, lang="en-GB")



            session.add(custom_ru)
            session.add(custom_eng)





            session.commit()

            '''
            print()
            print("          (inside crud) prod =", prod.product_ean)
            print("          (inside crud) product_id=", prod.product_id)
            print("          (inside crud) product_ct=", prod.category_id)
            print(prod)
            print('          (inside crud) ctp=', ctp)
            '''



        except:
            traceback.print_exc()
            print('ОШИБКА СОЕДИНЕНИЯ С БАЗОЙ ДАННЫХ')
            session.rollbask()
            raise
        finally:
            session.close()

        counter = counter+1



        #print('timefn= ', timefn1 - timefn0, timefn2 - timefn1, timefn3 - timefn2, timefn4 - timefn3)

    print('crud2 ЭКСПОРТ ДАННЫХ НА САЙТ ВЫПОЛНЕН')
    print()

