# Databricks notebook source
# MAGIC %md
# MAGIC DATA READING

# COMMAND ----------

# DBTITLE 1,Cell 2

# we can check the file 
dbutils.fs.ls('/Volumes/workspace/big_data/pyspark_tutorial_data_1')

# COMMAND ----------


# DATA READING
df = spark.read.format('csv').option('inferschema',True).option('header',True).load('/Volumes/workspace/big_data/pyspark_tutorial_data_1/BigMart Sales.csv')


# COMMAND ----------


# df.show(vertical=True)
df.display()

# COMMAND ----------

# MAGIC %md
# MAGIC Data Reading JSON 

# COMMAND ----------


# how can we read json file 
df_json = spark.read.format('json')\
    .option('inferSchema', True) \
    .load('/Volumes/workspace/big_data/pyspark_tutorial_data_1/drivers.json') \

''' how can we read json file 
df_json = spark.read.format('json')\
    .options(inferSchema = True) \
    .load('/Volumes/workspace/big_data/pyspark_tutorial_data_1/drivers.json') \
'''
# df_json.show()
df_json.display() #only provided by databricks 
# read_2.show()

# COMMAND ----------

# MAGIC %md
# MAGIC DDL Schema
# MAGIC

# COMMAND ----------



df.printSchema()
df.display()

# COMMAND ----------


# my_DDL_Schema = '''
#   Item_Weight string,
#   Item_Fat_Content string ,
#   Item_Visibility double ,
#   Item_Type string ,
#   Item_MRP double ,
#   Outlet_Identifier string ,
#   Outlet_Establishment_Year integer ,
#   Outlet_Size string ,
#   Outlet_Location_Type string ,
#   Outlet_Type string ,
#   Item_Outlet_Sales double
# '''

# df = spark.read.format('csv')\
#     .option('header',True)\
#     .schema(my_DDL_Schema)\
#     .load('/Volumes/workspace/big_data/pyspark_tutorial_data_1/BigMart Sales.csv')

# df.printSchema()
# df.show()

# COMMAND ----------


# Changing the schema with one column only
my_DDL_Schema_2 = '''
  Item_Weight string
'''

df_DDL = spark.read.format('csv') \
    .option('header', True) \
    .schema(my_DDL_Schema_2) \
    .load('/Volumes/workspace/big_data/pyspark_tutorial_data_1/BigMart Sales.csv')


df_DDL.show()

# COMMAND ----------


df.printSchema()
df.display()
df_DDL.printSchema()

# COMMAND ----------

# MAGIC %md
# MAGIC TRANSFORMATION

# COMMAND ----------

# MAGIC %md
# MAGIC  --- SELECT

# COMMAND ----------

# DBTITLE 1,Transformation

from pyspark.sql.functions import col

# # # Approach 
app_1 = df.select('Outlet_Identifier', 'Item_Weight', 'Item_Fat_Content')
app_1.display()


# # # Approach 2 
app_2 = df.select(col('Outlet_Identifier'), col('Item_Weight'), col('Item_Fat_Content'))
app_2.display()
df.display()

# COMMAND ----------

# MAGIC %md
# MAGIC ALIAS (AS)

# COMMAND ----------

# DBTITLE 1,select with column

v = df.select(col('Item_MRP'))
v.display()

# COMMAND ----------

# MAGIC %md
# MAGIC FILTER 
# MAGIC
# MAGIC

# COMMAND ----------


# 673 ms
weight_col = col('Item_Weight') 
less_weight = df.select('*').where((weight_col < 10) & (col('Item_Fat_Content') == 'Regular'))
less_weight.display()

# 447 ms
# 438 ms : after declaring the variable 
fat_content_col = col('Item_Fat_Content')
filter_res = df.filter(fat_content_col == 'Regular')
filter_res.display()

# COMMAND ----------

# DBTITLE 1,Filter( )

# Filter Scenario 2 
df.display()
# res = df.filter((col('Item_Type') == 'Soft Drinks') | (col('Item_Weight') < 6)).display()

# COMMAND ----------


# Scenario 3 : Outlet size is null and tier 1 & 2 
outlet_type_col = col('Outlet_Size')
tier_col =  col('Outlet_Location_Type')

res = df.filter(
    outlet_type_col.isNull() &
    tier_col.isin('Tier 1', 'Tier 2')
)
res.display()

# COMMAND ----------

# DBTITLE 1,withColumnRenamed( )

from pyspark.sql.functions import col

updated_col = df.withColumnRenamed('Item_MRP', 'new_MRPs')
print(type(col('new_MRPs')))
updated_col
updated_col = updated_col.withColumn('double_Mrps', col('new_MRPs') + 2)

updated_col.display()
# print(type(updated_col))

# COMMAND ----------

# MAGIC %md
# MAGIC # Existing Column Updating 

# COMMAND ----------

# DBTITLE 1,withColumn( )

from pyspark.sql.functions import regexp_replace
# df.groupBy('Item_Fat_Content').count().show()
# item_fat_content
 
updated_name = {
    'Low Fat' : 'LF',
    'Regular' : 'REG'
}

# BUG there is only the last modified value will be store in the dataset because each time it will create the new dataframe
for name, new_name in updated_name.items() : 
    print(name,"",new_name)
    new_replace_values = df.withColumn('Item_Fat_Content', regexp_replace(col('Item_Fat_Content'), name, new_name))
# new_replace_values = df.withColumn('Item_Fat_Content', regexp_replace(col('Item_Fat_Content'), 'Low Fat', 'LF'))\
#     .withColumn('Item_Fat_Content', regexp_replace(col('Item_Fat_Content'), 'Regular', 'Reg'))

new_replace_values.show()

# COMMAND ----------

# DBTITLE 1,cast( )

# ATI
from pyspark.sql.functions import col  
from pyspark.sql.types import StringType
df.printSchema()

df2 = df.select(
    '*',
    col('Item_Weight').cast(StringType())
    .alias("String_Weights")
)

df.printSchema()

# COMMAND ----------

# DBTITLE 1,sort / order by

from pyspark.sql.functions import col
df.show(3)
ans = df.sort('Item_Visibility', "Item_Weight", ascending=[0,1])
ans.show()

# COMMAND ----------

# DBTITLE 1,limit( )

df.show(2)
ans = df.limit(2).show(1)

# COMMAND ----------

# MAGIC %md
# MAGIC # **Intermediate PySpark**

# COMMAND ----------

# DBTITLE 1,DROP( )

df.display()

# if we have duplicates we can use distinct() to remove the duplicates


# COMMAND ----------

# DBTITLE 1,Drop Duplicates(subset=None ) / Drop_Duplicates(subset=None ) / distinct( )
# MAGIC %skip
# MAGIC duplicated_data = df 
# MAGIC
# MAGIC unique_data = df.dropDuplicates(subset='')
# MAGIC
# MAGIC

# COMMAND ----------

# DBTITLE 1,union () / union by name()


# COMMAND ----------

# MAGIC %md
# MAGIC ### String Functions
# MAGIC

# COMMAND ----------

# DBTITLE 1,INITCAP( ) / Upper( ) / Lower( )

from pyspark.sql.functions import col
from pyspark.sql.functions import lower

df.show(2)
ans = df.withColumn('Item_Identifier', lower(col('Item_Identifier')))
ans.show(2)

# COMMAND ----------

# MAGIC %md
# MAGIC ### Date Functions

# COMMAND ----------

# DBTITLE 1,Date Functions

from pyspark.sql.functions import date_add, date_sub, date_diff, date_format, now
# date_now()
df = df.withColumn('Item_Dates', now())
df.show()

# date_add()
df.withColumn('Item_Dates', date_add(col('Item_Dates'), 10))

# date_sub()
# date_diff() 
# date_format()


# COMMAND ----------

# MAGIC %md
# MAGIC ## Handling NULLs
# MAGIC

# COMMAND ----------

# DBTITLE 1,droping NULLs

# dropna() : 'any', 'all'
# dropna() : using subset = ['']


# COMMAND ----------

# DBTITLE 1,filling NULLs

# fillna(replaced_value)
# fillna('replaced_value', subset=[column_name])

# COMMAND ----------

# MAGIC %md
# MAGIC ## Split and Indexing
# MAGIC

# COMMAND ----------

# DBTITLE 1,split

# df.withColumn('col_name', split('col_name', 'separator_condition'))

# COMMAND ----------

# DBTITLE 1,indexing

# df.withColumn('col_name', split('col_name', 'separator_condition')[index_value])



# COMMAND ----------

# DBTITLE 1,explode()

# explode : this function is used when we have to break the list 



# COMMAND ----------

# DBTITLE 1,ARRAY_CONTAINS( )
# MAGIC %skip
# MAGIC

# COMMAND ----------

# DBTITLE 1,Group_By( )
from pyspark.sql.functions import col, sum, avg
# df.show(2)
ans = df.groupBy('Item_Type').agg(
                                sum('Item_MRP').alias('Total_MRPs'),
                                avg('Item_MRP').alias('Avg_MRPs'))
ans.printSchema()
ans.display()



# COMMAND ----------

# DBTITLE 1,collect_list()
df.show()

# COMMAND ----------

# DBTITLE 1,pivot()


# COMMAND ----------

# MAGIC %md
# MAGIC ### When - otherwise 
# MAGIC

# COMMAND ----------

# MAGIC %md
# MAGIC #### Scenerio 1 
# MAGIC

# COMMAND ----------

# DBTITLE 1,when otherwise
from pyspark.sql.functions import when
df.show(4)
catagorial_data = df.withColumn('Food_Type', 
              when(col('Item_Type') == 'Meat', 'Non-Veg')
              .otherwise('Veg'))\

catagorial_data.show()

# COMMAND ----------

# MAGIC %md
# MAGIC #### Scenerio 2

# COMMAND ----------

# catagorial_data.display()
catagorial_data = catagorial_data.withColumn('Rate', 
                                             when((col('Food_Type') == 'Veg') & (col("Item_MRP") < 100), 'Cheaper')
                                            .when((col('Food_Type') == 'Veg') & (col('Item_MRP') > 100), 'Expensive')
                                            .otherwise('Non Veg'))
catagorial_data.show()

# COMMAND ----------

# MAGIC %md
# MAGIC ### JOINS
# MAGIC

# COMMAND ----------

# DBTITLE 1,JOINS
display(
    dbutils.fs.ls(
        "/Volumes/workspace/big_data/pyspark_tutorial_data_1/"
    )
)
# error - 2
''' employees = spark.read \
    .option("mode", "PERMISSIVE") \
    .json("/Volumes/workspace/big_data/pyspark_tutorial_data_1/Employees.json")

    employees.printSchema()
    employees.show(truncate=False)
'''

# COMMAND ----------

# MAGIC %md
# MAGIC #### Attempt 1 

# COMMAND ----------

from pyspark.sql.functions import col

employees = spark.read.option("multiline", True).json('dbfs:/Volumes/workspace/big_data/pyspark_tutorial_data_1/Employees.json')
department = spark.read.option("multiline", True).json('dbfs:/Volumes/workspace/big_data/pyspark_tutorial_data_1/Department.json')
employees.show()
department.show()

join_emp_dep = employees.join(department, "dept_id", 'left')
join_emp_dep.show()
join_emp_dep.filter(col("dept_name").isNull()).show()
# 1)

# COMMAND ----------

# MAGIC %md
# MAGIC ## Window Functions

# COMMAND ----------

# DBTITLE 1,Window Functions
from pyspark.sql.functions import rank, dense_rank, row_number
from pyspark.sql import Window

from pyspark.sql.functions import col

df.show(10)

# approach 1 
'''
df.withColumn('rank', rank().over(Window.orderBy('Item_Identifier'))).show()
df.withColumn('Row_Number', row_number().over(Window.orderBy('Item_Identifier'))).show()
df.withColumn('dense_rank', dense_rank().over(Window.orderBy('Item_Identifier'))).show()
'''

# approach 2 
df.withColumn('rank', rank().over(Window.orderBy('Item_Identifier')))\
.withColumn('Row_Number', row_number().over(Window.orderBy(col('Item_Identifier').asc())))\
.withColumn('dense_rank', dense_rank().over(Window.orderBy('Item_Identifier'))).show()

# approach 3 



# COMMAND ----------

# DBTITLE 1,comulative sum


# COMMAND ----------

# MAGIC %md
# MAGIC ### User Defined Functions
# MAGIC

# COMMAND ----------

# DBTITLE 1,UDF
# my custom function 
def square(number) : 
    return number * number 

# COMMAND ----------

# DBTITLE 1,UDF
# using that custom function inside the select statement
df.select(
    'Item_MRP',
    square(col('Item_MRP')).alias('squared')
).show()


# COMMAND ----------

df.show()

# COMMAND ----------

# MAGIC %md
# MAGIC

# COMMAND ----------

# MAGIC %md
# MAGIC

# COMMAND ----------

# MAGIC %md
# MAGIC

# COMMAND ----------

# MAGIC %md
# MAGIC # Practice Questions 

# COMMAND ----------

# DBTITLE 1,Practice questions

# 3. Create a new column Item_Visibility_Percent by multiplying Item_Visibility by 100 and casting it to double.
# df.show()
df_extra_col = df.withColumn(
    'Item_Visibility_Percent', col("Item_Visibility") * 100
)
df_extra_col.printSchema()
df_extra_col.display()


# COMMAND ----------



# 4. Select Item_Identifier, Item_MRP, and Item_Outlet_Sales, ensuring their output data types are correct
from pyspark.sql.functions import col
from pyspark.sql.types import  StringType, DoubleType

df.printSchema() 
df.select(
    col("Item_Identifier").cast(StringType()),
    col("Item_MRP").cast(DoubleType()),
    col("Item_Outlet_Sales").cast(DoubleType())
).show()


# COMMAND ----------


# 5. Use printSchema() to verify the types of your transformed columns.
# 1. Check whether Item_Weight contains NULL values. Count the missing values.
from pyspark.sql.functions import col 

# df.select("Item_Weight").show()
null_cols = df.select(col('Item_Weight').isNull())

# COMMAND ----------
