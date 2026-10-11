from databricks.connect import DatabricksSession

spark = DatabricksSession.builder.remote(cluster_id  =   "1001-065424-83x69ssg").getOrCreate()
spark.sql("SELECT 1").show()