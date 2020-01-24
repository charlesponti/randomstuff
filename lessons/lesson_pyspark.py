from pyspark import SparkContext, SQLContext
import pandas as pd
import csv

sc = SparkContext(appName="transactions")
sqlContext = SQLContext(sparkContext=sc)

transactions = (
    sqlContext.read.format("com.databricks.spark.csv")
    .option("header", "true")
    .option("mode", "DROPMALFORMED")
    .load("./data/transactions.csv")
)

print(transactions.select("Date", "Amount").show())
