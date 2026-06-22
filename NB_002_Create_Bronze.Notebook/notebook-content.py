# Fabric notebook source

# METADATA ********************

# META {
# META   "kernel_info": {
# META     "name": "synapse_pyspark"
# META   },
# META   "dependencies": {
# META     "lakehouse": {
# META       "default_lakehouse": "6d440bf4-fd96-4ece-a789-235bef950cce",
# META       "default_lakehouse_name": "LH_Bronze",
# META       "default_lakehouse_workspace_id": "2d758a21-70b2-45bd-9123-c1efb4902295",
# META       "known_lakehouses": [
# META         {
# META           "id": "6d440bf4-fd96-4ece-a789-235bef950cce"
# META         }
# META       ]
# META     }
# META   }
# META }

# CELL ********************

spark.sql("""
CREATE TABLE IF NOT EXISTS br_mt950_raw
(
    file_name STRING,
    load_timestamp TIMESTAMP,
    file_content STRING
)
USING DELTA
""")

# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "synapse_pyspark"
# META }
