from pyspark.sql import  SparkSession
import requests

inputFile = ("workspaces/Learning_Spark/testweet.json")

spark = SparkSession.builder.appName("SQL").getOrCreate()
url = ""



input = spark.read.json(inputFile).show()