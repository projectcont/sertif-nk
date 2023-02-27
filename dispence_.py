from prodcateg.product import Product
from prodcateg.category import Category
import sqlf.сountprod
import traceback
import time


def dispence (session, prod_list_excel):
    '''
    functuion obtains list of employers (instances)
    :param session, prod_list_excel
    :return: prod_list_add
    '''


    print()
    print('DISPENCE')



    count=0
    prod_list_add = []
    allprod = session.query(Product)
    allcategs = session.query(Category)


    print('allprod size= ', allprod.count())
    print('allcategs size= ', allcategs.count())
    print('prod_list_excel size= ', len(prod_list_excel))


    categ_ids = {}
    for ct_ in allcategs:
        categ_ids[ct_.product_id] = ct_.category_id

    def digits_only(string_):
        # function get string(mixed chars and digits) and returns only digits
        result_list = [n for n in string_ if n in '0123456789']
        result_ = ''.join(result_list)
        result2 = str(result_)
        return result2

    def unif_id_excel(prod):
        # function returns unificated id for product
        unif_id = str(digits_only(prod.product_ean)) + '-' + str(prod.category_id)
        return unif_id

    def unif_id_base(prod):
        # function returns unificated id for product
        v1=str(digits_only(prod.product_ean))
        try:
            v2=str(categ_ids[prod.product_id])
        except:
            v2 = ''
        unif_id = v1 + '-' + v2

        return unif_id



    for n in prod_list_excel:

        #print(getattr(n, 'name_ru-RU'), 'n considered')
        prev=0

        for prod_ in allprod:

            # comparison
            if unif_id_base (prod_)== unif_id_excel (n)   :


                prod_.product_manufacturer_id = n.product_manufacturer_id
                prod_.manufacturer_code = n.manufacturer_code
                prod_.vendor_id = n.vendor_id
                #descr_ = getattr(n, 'description_ru-RU')
                #setattr(prod_, 'description_ru-RU', descr_)

                #session.flush()
                #session.refresh(prod_)

                count = count + 1
                prev = 1
                print(count, ' меняется ', getattr(prod_, 'name_ru-RU'), f' (серт.№ {prod_.product_ean}) ', )


        #session.flush()
        #session.commit()

        if prev == 0:
            prod_list_add.append(n)




    session.flush()
    session.commit()

    print()
    print('на сайте меняется    анкет =', count)
    print('на сайте добавляется анкет =', len(prod_list_add))


    sqlf.сountprod.Countprod.update =count
    sqlf.сountprod.Countprod.add = len(prod_list_add)




    return prod_list_add






