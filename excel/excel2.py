from prodcateg.product import Product
from sqlf.get_pr_ import get_pr

def get_prodlist_from_excel (pr_list):
    '''
    functuion creates text list of employers (instances)
    :param nop:  number of employers
    :return: list (employers)
    '''
    pr0 = get_pr()
    prod_list = []

    print('          (ФОРМИРОВАНИЕ СПИСКА АНКЕТ ИЗ EXCEL)' );

    for pr in pr_list:
        prod = Product()
        prod.setpr(pr0)
        prod.setpr(pr)
        #prod.setpr({'category_id': categ_id, 'product_manufacturer_id': manuf_id})
        prod_list.append(prod)
        #print('          (inside excel_list) ', prod);

    print('          (ФОРМИРОВАНИЕ СПИСКА АНКЕТ ИЗ EXCEL ВЫПОЛНЕНО)');
    print('          ПОЛУЧЕНО АНКЕТ ИЗ EXCEL: ',  len(prod_list));

    return prod_list


