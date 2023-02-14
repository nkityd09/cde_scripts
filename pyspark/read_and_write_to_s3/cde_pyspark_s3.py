from pyspark.sql import SparkSession
from pprint import pprint

spark = SparkSession\
        .builder\
        .appName("Write_To_S3")\
        .enableHiveSupport()\
        .getOrCreate()

#S3 Object URI to Read
s3_read_location = "s3a://ankity-cdp-aw-delete/data/housing.csv"


#S3 Write Location
s3_write_location = "s3a://ankity-cdp-aw-delete/output_data/" 


# Read CSV file from S3
df = spark.read.format("csv").option("header","true").load(s3_read_location)

# Write transformed file to S3
df.write.orc(f"{s3_write_location}/housing_orc")

