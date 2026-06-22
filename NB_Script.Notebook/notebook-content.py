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

from notebookutils import mssparkutils
from pyspark.sql import Row
from datetime import datetime

# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "synapse_pyspark"
# META }

# CELL ********************

file_path = "Files/mt950/mt950_acct1234.txt"
df = spark.read.format("text").load(file_path)

# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "synapse_pyspark"
# META }

# CELL ********************

content = mssparkutils.fs.head(file_path,10000)
display(content)
rows = [
    Row(
    file_name = "mt950_acct1234.txt",
    load_timestamp = datetime.now(),
    file_content = content
        )
]

df = spark.createDataFrame(rows)
df.write.mode("append").saveAsTable("br_mt950_raw")

# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "synapse_pyspark"
# META }

# CELL ********************

bronze_df = spark.table("br_mt950_raw")
bronze_df.show(truncate=False)

# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "synapse_pyspark"
# META }

# CELL ********************

import re
from pyspark.sql.functions import udf
from pyspark.sql.types import *

def parse_mt950(message):

    result = {}

    def get_tag(tag):
        pattern = rf":{tag}:(.*?)(?=\n:\d{{2}}|\n-\}}|\Z)"
        match = re.search(pattern, message, re.DOTALL)
        return match.group(1).strip() if match else None

    result["transaction_reference"] = get_tag("20")
    result["account_number"] = get_tag("25")
    result["statement_number"] = get_tag("28C")
    result["opening_balance"] = get_tag("60F")
    result["closing_balance"] = get_tag("62F")

    transactions = []

    lines = message.splitlines()

    current_txn = {}

    for line in lines:

        if line.startswith(":61:"):

            if current_txn:
                transactions.append(current_txn)

            current_txn = {
                "txn_line": line[4:],
                "description": None
            }

        elif line.startswith(":86:"):

            current_txn["description"] = line[4:]

    if current_txn:
        transactions.append(current_txn)

    result["transactions"] = transactions

    return result

# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "synapse_pyspark"
# META }

# CELL ********************

records = []

for row in bronze_df.collect():

    parsed = parse_mt950(row.file_content)

    parsed["file_name"] = row.file_name

    records.append(parsed)

# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "synapse_pyspark"
# META }

# CELL ********************

statement_rows = []

for r in records:

    statement_rows.append(

        (
            r["file_name"],
            r["transaction_reference"],
            r["account_number"],
            r["statement_number"],
            r["opening_balance"],
            r["closing_balance"]
        )

    )

statement_df = spark.createDataFrame(
    statement_rows,
    [
        "file_name",
        "transaction_reference",
        "account_number",
        "statement_number",
        "opening_balance",
        "closing_balance"
    ]
)

statement_df.show(truncate=False)

# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "synapse_pyspark"
# META }

# CELL ********************

display(statement_df)

# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "synapse_pyspark"
# META }

# CELL ********************


# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "synapse_pyspark"
# META }
