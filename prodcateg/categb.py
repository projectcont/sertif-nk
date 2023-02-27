from sqlalchemy import Table, MetaData, Column, Integer, VARCHAR, Text, ForeignKey, DateTime, Boolean, DECIMAL
from sqlalchemy.dialects.mysql import VARCHAR,INTEGER, DECIMAL, TINYINT, SMALLINT, DATETIME, MEDIUMINT, FLOAT

def get_categb (metadata):
    #'e92gs_jshopping_products_to_categories'

    categb = Table(
    'e92gs_jshopping_products_to_categories', metadata,
    Column('product_id', INTEGER(11), primary_key=True, nullable=False, index = True),
    Column('category_id', INTEGER(11), primary_key=True,nullable=False, index = True),
    Column('product_ordering', INTEGER(11),   index=True)
    )
    return categb


































