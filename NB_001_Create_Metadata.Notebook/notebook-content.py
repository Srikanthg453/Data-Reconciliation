# Fabric notebook source

# METADATA ********************

# META {
# META   "kernel_info": {
# META     "name": "synapse_pyspark"
# META   },
# META   "dependencies": {
# META     "lakehouse": {
# META       "default_lakehouse": "64f5b532-9551-4196-a497-a03ba19e1f52",
# META       "default_lakehouse_name": "LH_Metadata",
# META       "default_lakehouse_workspace_id": "2d758a21-70b2-45bd-9123-c1efb4902295",
# META       "known_lakehouses": [
# META         {
# META           "id": "64f5b532-9551-4196-a497-a03ba19e1f52"
# META         }
# META       ]
# META     }
# META   }
# META }

# MARKDOWN ********************

# Metadata DDL Scripts

# CELL ********************

spark.sql("""CREATE TABLE meta_source_config
(
    source_id STRING,
    source_name STRING,
    source_type STRING,
    file_pattern STRING,
    landing_path STRING,
    processed_path STRING,
    parser_type STRING,
    active_flag STRING
)
USING DELTA""")

# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "synapse_pyspark"
# META }

# CELL ********************

spark.sql("""INSERT INTO meta_source_config VALUES
(
'1',
'MT950',
'SWIFT',
'*.txt',
'Files/MT950/Incoming/',
'Files/MT950/Processed/',
'MT950',
'Y'
)""")

# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "synapse_pyspark"
# META }

# CELL ********************

spark.sql("""CREATE TABLE meta_swift_tag_definition
(
    message_type STRING,
    tag_code STRING,
    tag_name STRING,
    mandatory_flag STRING
)
USING DELTA""")

# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "synapse_pyspark"
# META }

# CELL ********************

spark.sql("""INSERT INTO meta_swift_tag_definition VALUES
('MT950','20','Transaction Reference','Y'),
('MT950','25','Account Identification','Y'),
('MT950','28C','Statement Number','Y'),
('MT950','60F','Opening Balance','Y'),
('MT950','61','Statement Line','Y'),
('MT950','62F','Closing Balance','Y'),
('MT950','64','Available Balance','N'),
('MT950','65','Forward Available Balance','N')""")

# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "synapse_pyspark"
# META }

# CELL ********************

spark.sql("""CREATE TABLE meta_parser_config
(
    message_type STRING,
    statement_table STRING,
    transaction_table STRING,
    multi_message_delimiter STRING
)
USING DELTA""")

# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "synapse_pyspark"
# META }

# CELL ********************

spark.sql("""INSERT INTO meta_parser_config VALUES
(
'MT950',
'sl_mt950_statement',
'sl_mt950_transaction',
'-}'
);""")

# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "synapse_pyspark"
# META }

# CELL ********************

spark.sql("""CREATE TABLE meta_file_control
(
    file_name STRING,
    source_name STRING,
    load_timestamp TIMESTAMP,
    process_timestamp TIMESTAMP,
    status STRING,
    record_count INT
)
USING DELTA""")

# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "synapse_pyspark"
# META }

# CELL ********************

spark.sql("SHOW TABLES").show(truncate=False)


# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "synapse_pyspark"
# META }

# CELL ********************

spark.sql("SELECT current_database()").show(truncate=False)

# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "synapse_pyspark"
# META }
