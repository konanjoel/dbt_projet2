from snowflake.snowpark.functions import upper, col

def model(dbt, session):
    dbt.config(materialized="table")
    df = dbt.source("donne_brute" , "TRANSACTIONS")
    df_result = df.select(
        upper(col("HASH")).alias("HASH"),
        col("DATE"),
        col("VALUE")
    )
    return df_result