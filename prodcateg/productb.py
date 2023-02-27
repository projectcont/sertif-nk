
from sqlalchemy import Table, MetaData, Column, Integer, VARCHAR, Text, ForeignKey, DateTime, Boolean, DECIMAL
from sqlalchemy.dialects.mysql import VARCHAR,INTEGER, DECIMAL, TINYINT, SMALLINT, DATETIME, MEDIUMINT, FLOAT


#e92gs_jshopping_products

def get_productb(metadata):

    product = Table('e92gs_jshopping_products', metadata,
    Column('product_id', INTEGER(11), primary_key=True),

    Column('parent_id', INTEGER(11), nullable=False, default='',index = True),
    Column('product_ean', VARCHAR(32), nullable=False, default='',index = True),
    Column('manufacturer_code', VARCHAR(32), nullable=False, default=''),
    Column('product_quantity', DECIMAL(12,2), nullable=False, default=''),
    Column('unlimited', TINYINT(1), nullable=False, default='',index = True),
    Column('product_availability', VARCHAR(1), nullable=False, default=''),
    Column('product_date_added', DateTime, nullable=False, default='0000-00-00 00:00:00'),
    Column('date_modify', DateTime, nullable=False, default='0000-00-00 00:00:00'),
    Column('product_publish', TINYINT(1), nullable=False, default='',index = True),
    Column('product_tax_id', TINYINT(3), nullable=False, default='', index = True),

    Column('currency_id', INTEGER(4), nullable=False, default=''),
    Column('product_template', VARCHAR(64), nullable=False, default='default'),
    Column('product_url', VARCHAR(128), nullable=False, default=''),
    Column('product_old_price', DECIMAL(14,4), nullable=False, default=''),
    Column('product_buy_price', DECIMAL(14,4), nullable=False, default=''),
    Column('product_price', DECIMAL(18,6), nullable=False, default='',index = True),
    Column('min_price', DECIMAL(18,6), nullable=False, default='',index = True),
    Column('different_prices', TINYINT(1), nullable=False, default=''),
    Column('product_weight', DECIMAL(14,4), nullable=False, default=''),
    Column('image', VARCHAR(255), nullable=False, default=''),

    Column('product_manufacturer_id', INTEGER(11), nullable=False, default='', index = True),
    Column('product_is_add_price', TINYINT(1), nullable=False, default=''),
    Column('add_price_unit_id', INTEGER(3), nullable=False, default='',index = True),
    Column('average_rating', FLOAT(4,2), nullable=False, default='',index = True),
    Column('reviews_count', INTEGER(11), nullable=False, default='',index = True),
    Column('delivery_times_id', INTEGER(4), nullable=False, default='',index = True),
    Column('hits', INTEGER(11), nullable=False, default='',index = True),
    Column('weight_volume_units', DECIMAL(14,4), nullable=False, default=''),
    Column('basic_price_unit_id', INTEGER(3), nullable=False, default='',index = True),
    Column('label_id', INTEGER(11), nullable=False, default='',index = True),

    Column('vendor_id', INTEGER(11), nullable=False, default='',index = True),
    Column('access', INTEGER(3), nullable=False, default='1',index = True),
    Column('name_en-GB', VARCHAR(255), nullable=False, default=''),
    Column('alias_en-GB', VARCHAR(255), nullable=False, default=''),
    Column('short_description_en-GB', Text, nullable=False, default=''),
    Column('description_en-GB', Text, nullable=False, default=''),
    Column('meta_title_en-GB', VARCHAR(255), nullable=False, default=''),
    Column('meta_description_en-GB', Text, nullable=False, default=''),
    Column('meta_keyword_en-GB', Text, nullable=False, default=''),
    Column('name_ru-RU', VARCHAR(255), nullable=False, default=''),

    Column('alias_ru-RU', VARCHAR(255), nullable=False, default=''),
    Column('short_description_ru-RU', Text, nullable=False, default=''),
    Column('description_ru-RU', Text, nullable=False, default=''),
    Column('meta_title_ru-RU', VARCHAR(255), nullable=False, default=''),
    Column('meta_description_ru-RU', Text, nullable=False, default=''),
    Column('meta_keyword_ru-RU', Text, nullable=False, default=''),
    Column('extra_field_1', VARCHAR(100), nullable=False, default=''),
    Column('extra_field_2', VARCHAR(100), nullable=False, default='')
    )
    return product


































