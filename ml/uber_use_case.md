# Uber’s Big Data Platform: 100+ Petabytes with Minute Latency

- [link](https://www.uber.com/blog/uber-big-data-platform/)

- forecasting rider demand during high traffic events
- identifying and addressing bottlenecks in our driver-partner sign-up process
- Apache Hadoop based Big DAta platform

## Generation 1: The beginning of Big Data at Uber

- before 2014, data - a few traditional online transaction processing (OLTP) databases - MySQL/PostgreSQL
- to make Uber as data-driven as possible, we needed to ensure that analytical data was accessible to analysts, all in one place

Data Users:

1. City operations teams (thousands of users)
1. Data scientists and anlysts (hundreds of users)
1. Engineering teams (hundresds of users)

- [Vertica](https://en.wikipedia.org/wiki/Vertica?uclick_id=b6203983-97f3-4de0-8848-f7044e48c258) - data warehouse software
- ad hoc ETL (Extract, Transform, and Load) jobs

Limitations:

- we lacked a formal schema communication mechanism, data reliability became a concern
- the lack of a formal contract between the services producing the data and the downstream data consumers

## Generation 2: The arrival of Hadoop

- all raw data was ingested from different online data stores only once and with no transformation during ingestion
- [Presto](https://prestodb.io/?uclick_id=b6203983-97f3-4de0-8848-f7044e48c258) - interactie ad hoc user queries
- [Apache Spark](https://spark.apache.org/?uclick_id=b6203983-97f3-4de0-8848-f7044e48c258) - programmatic access to raw data
- [Apache Hive](https://hive.apache.org/?uclick_id=b6203983-97f3-4de0-8848-f7044e48c258) - extremely large queries
- Use apache parquet - saving storage costs and query performance
- built a central schema service to collect, store and serve schemas as well as different client libraries to integrate different services with this central schema service

Limitations:

- the massive amount of small files stored in our HDFS
- data latency was still far from what our business needed
- all ingestion jobs needed to create new snapshots from the updated source data

## Generation 3: Rebuilidng our Big Data platform for the long term

1. HDFS scalability limitation: leveraging ViewFS and using DHFS NameNode Federation
1. Faster data in Hadoop: re-architect our pipeline to the incremental ingestion of only updated and new data
1. Support of updates and deletes in Hadoop and Parquet
1. Faster ETL and modeling

Introducing Hudi

- Hadoop Upserts anD Deletes (HUDI), an open source Spark library that provides an abstraction layer on top of HDFS and Parquet to support the required update and delte operations.
- data ingestion platform, Marmaray, raw data ingestion framework an EL platform as opposed to a traditional ETL platform
- separation of transformation
- incrementally fetch only the changed data from the source table -> latest mode view / incremental mode view

Standardize data model

- changelog history table
- merged snapshot table

## Generation 4: What's next?

- Data quality - non-schema-conforming data, the quality of the actual data content
- Data latency - goal is to reduce latency to five minutes for raw data, and to ten minutes for modeled tables
- Data efficiency - service dockerization, unified resource manager
- Scalability and reliablity - unified data ingestion and updated parquet
