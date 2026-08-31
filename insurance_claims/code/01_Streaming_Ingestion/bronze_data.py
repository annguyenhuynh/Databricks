""" 
Since the source project provides telematics data, there is no need to consume live streaming data.
The below script was written and run on Databricks.
"""
import dlt

@dlt.table(
    name="telematics_bronze",
    comment="Raw telematics data",
    table_properties={"quality": "bronze"}
)
def bronze_table():

    return spark.read.parquet(
        "dbfs:/Workspace/Users/nhuynh27@gmu.edu/Databricks/insurance_claims/data/telematics"
    )