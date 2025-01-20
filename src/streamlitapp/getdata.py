# Import python packages
import streamlit as st
from snowflake.snowpark.context import get_active_session
import snowflake.connector

import logging

logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger("snowflake.connector")
logger.setLevel(logging.DEBUG)


account = "TPHNKRZ.KG97245"
user = "BRAINWORKSGCPDE2024"
password = "Brainworks@2024"
database = "BWDATABASE"
schema = "BWSCHEMA"
role = "SYSADMIN"
warehouse = "BWWAREHOUSE"
# test
connection = snowflake.connector.connect(
    user=user,
    password=password,
    account=account,
    warehouse=warehouse,
    database=database,
    schema=schema,
    enable_connection_diag=True,
  )
sql_string = """ Select segment, sum(sales) as sales from superstore group by segment"""
cursor = connection.cursor()
cursor.execute(sql_string)
data = cursor.fetchall()

# st.table(data=data)
# st.bar_chart(data=data, x='SEGMENT',y='SALES')

# st.data_editor(data)

