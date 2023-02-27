class Custom (object):

    def setpr(self,prod,lang):
        self.id_product=prod.product_id
        self.ba_custom_field_1=prod.custom1
        self.ba_custom_field_2=prod.custom2
        self.ba_custom_field_3 = prod.custom3
        self.ba_custom_field_4 = prod.custom4
        self.lang = lang

    def __str__(self):
        str1 = " product_id=" + str( self.id_product )
        str2 = " field_1=" + str(self.ba_custom_field_1)
        str3 = " field_2=" + str(self.ba_custom_field_2)
        str4 = " lang=" + str(self.lang)

        sum = str1 + '______' + str2 + '______' + str3+ '______' + str4
        return sum




