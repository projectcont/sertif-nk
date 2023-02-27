
class Product(object):

    def setpr(self,pr):

        for key_ in list(pr.keys()):

            setattr(self, key_, pr[key_])

            #print('    key_=',key_); print('prop=',pr[key_]); print()
            #print('setted', key_,'=', pr[key_])


    def __str__(self):
        dist='___'
        str_fio = " fio=" + str ( getattr(self, "name_ru-RU") )
        str_sertn = " sertn=" + str( getattr(self, "product_ean") )
        str_manufcode = " date=" +str( getattr(self, "manufacturer_code") )
        str_id = "id=" + str( getattr(self, "product_id") )
        str_manufid = " manuf_id=" + str(getattr(self, "product_manufacturer_id"))
        str_descr = " descr=" + str( getattr(self, "description_ru-RU") )
        str_categ = " categ=" + str(getattr(self, "category_id"))


        sum = f' {str_id}   {dist}  {str_fio}   {dist} {str_sertn}  {dist} {str_manufcode} {str_manufid} {dist}  {str_descr}  {str_categ} '

        return sum








