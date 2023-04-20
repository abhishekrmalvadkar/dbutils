-- Databricks notebook source
create widget TEXT firstname DEFAULT 'Abhishek'

-- COMMAND ----------

CREATE WIDGET DROPDOWN gender DEFAULT 'Male' CHOICES SELECT 'Male','Female'

-- COMMAND ----------

remove widget gender

-- COMMAND ----------

-- MAGIC %python
-- MAGIC data = [(1,"abhishek","male"),(2,"ravindra","male"),(3,"jyoti","female"),(4,"karan","female")]
-- MAGIC columns = ["id","name","gender"]
-- MAGIC 
-- MAGIC df = spark.createDataFrame(data, schema=columns)

-- COMMAND ----------

-- MAGIC %python
-- MAGIC df.show()
-- MAGIC df.createOrReplaceTempView("persons")

-- COMMAND ----------

SELECT * from persons


-- COMMAND ----------

CREATE WIDGET DROPDOWN genderDF DEFAULT "male" CHOICES SELECT distinct gender from persons

-- COMMAND ----------

select * from persons where gender = getargument("genderDF")

-- COMMAND ----------

CREATE TABLE IF NOT EXISTS employeess (
  employee_id INT,
  first_name STRING,
  last_name STRING,
  department STRING
)using DELTA;



-- COMMAND ----------

INSERT INTO employeess VALUES
  (1, 'abc', 'abc', 'Sales'),
  (2, 'def', 'def', 'Marketing'),
  (3, 'hij', 'hij', 'Sales'),
  (4, 'klm', 'klm', 'HR'),
  (5, 'nop', 'nop', 'Marketing');

-- COMMAND ----------

CREATE WIDGET TEXT department_name DEFAULT 'Sales' 


-- COMMAND ----------

SELECT getArgument("department_name") as department_name

-- COMMAND ----------

SELECT *
FROM employeess
WHERE department = getArgument("department_name")

-- COMMAND ----------


