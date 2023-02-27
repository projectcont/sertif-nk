class Category (object):

    def setpr(self,prod):
        self.product_id=prod.product_id
        self.category_id = prod.category_id
        self.product_ordering = 2

    def __str__(self):
        str1 = " product_id=" + str( self.product_id )
        str2 = " category_id=" + str(self.category_id)
        sum = str1 + '______' + str2
        return sum

    pass


