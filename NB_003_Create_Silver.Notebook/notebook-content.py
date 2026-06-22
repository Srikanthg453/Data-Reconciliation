# Fabric notebook source

# METADATA ********************

# META {
# META   "kernel_info": {
# META     "name": "synapse_pyspark"
# META   },
# META   "dependencies": {
# META     "lakehouse": {
# META       "default_lakehouse": "7a6f65ce-9750-4643-9cde-44948f3b633c",
# META       "default_lakehouse_name": "LH_Silver",
# META       "default_lakehouse_workspace_id": "2d758a21-70b2-45bd-9123-c1efb4902295",
# META       "known_lakehouses": [
# META         {
# META           "id": "7a6f65ce-9750-4643-9cde-44948f3b633c"
# META         }
# META       ]
# META     }
# META   }
# META }

# CELL ********************

spark.sql("""
CREATE TABLE IF NOT EXISTS sl_mt950_statement
(
    transaction_reference STRING,
    account_id STRING,
    statement_number STRING,
    sequence_number STRING,

    opening_dc STRING,
    opening_date DATE,
    opening_currency STRING,
    opening_amount DECIMAL(18,2),

    closing_dc STRING,
    closing_date DATE,
    closing_currency STRING,
    closing_amount DECIMAL(18,2),

    available_dc STRING,
    available_date DATE,
    available_currency STRING,
    available_amount DECIMAL(18,2),

    source_file STRING
)
USING DELTA
""")

# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "synapse_pyspark"
# META }
