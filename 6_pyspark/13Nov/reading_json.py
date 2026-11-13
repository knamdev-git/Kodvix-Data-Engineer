from pyspark.sql.types import StructType, StructField, IntegerType, StringType, BooleanType

my_schema_format = StructType([
    StructField("id", IntegerType(), True),
    StructField("name", StringType(), True),
    StructField("role", StringType(), True),
    StructField("active",BooleanType(), True)
])

json_data = spark.read.format("json")\
    .schema(my_schema_format)\
    .load("/Volumes/workspace/big_data/pyspark_tutorial_data_1/sample_json_file.json")

json_data.show()
