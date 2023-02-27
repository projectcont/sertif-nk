from sqlalchemy import Table, MetaData, Column, Integer, VARCHAR, Text, ForeignKey, DateTime, Boolean, DECIMAL
from sqlalchemy.dialects.mysql import VARCHAR,INTEGER, DECIMAL, TINYINT, SMALLINT, DATETIME, MEDIUMINT, FLOAT

def get_customb (metadata):

    customb = Table(
    'e92gs_jshopping_custom_fields_values', metadata,
    Column('id', INTEGER(11), primary_key=True, nullable=False, index = True),
    Column('id_product', INTEGER(11),  nullable=False),
    Column('lang', VARCHAR(100), nullable=False),
    Column('ba_custom_field_1', VARCHAR(255)),
    Column('ba_custom_field_2', VARCHAR(255)),
    Column('ba_custom_field_3', VARCHAR(255)),
    Column('ba_custom_field_4', VARCHAR(255))

    )
    return customb