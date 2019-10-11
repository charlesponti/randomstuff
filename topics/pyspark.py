from pyspark import SparkContext, SQLContext
import pandas as pd
from flask import Flask
import csv
app = Flask(__name__, static_folder='./app/build')

sc = SparkContext(appName='transactions')
sqlContext = SQLContext(sparkContext=sc)

tr = (sqlContext
    .read
    .format("com.databricks.spark.csv")
    .option("header", "true")
    .option("mode", "DROPMALFORMED")
    .load("../data/transactions.csv"))

print(tr.select('Date', 'Amount').show())