# ds_seminar
Kafka and ksql demo

Installation:
- Download confluent kafka bundled with KSQL. For this demo, I used confluent-5.2.1.

- To start kafka run: /[path to confluent-kafka]/bin/confluent start

- To start ksql cmd line run: /[path to confluent kafka]/bin/ksql http://localhost:8088


To add movieAbbr UDF to ksql server.
- Download Java and Apache Maven. This demo was performed using Java 8 and Apache Maven 3.6.3

- Build a jar using the ksql_udf java code or you can directly download jar from the ksql_udf/target folder

- Stop the kafka server

- Navigate to the ksql folder: /[path to confluent-kafka]/etc/ksql

- If a ext folder is not present, create a new ext folder

- Copy the jar to the ext folder

- Go back to ksql folder. Open ksql-server.properties on the editor of your choice.

- Add the following line to the file:
       ksql.extension.dir=/[path to confluent-kafka]/etc/ksql/ext

Please download attached keynote (kafka.key) for the slides
