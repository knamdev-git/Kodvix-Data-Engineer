json_data = spark.read.format("json") \
    .option("mode", "DROPMALFORMED") \
    .load("/Volumes/workspace/big_data/pyspark_tutorial_data_1/sample_json_file.json")

json_data.show()
