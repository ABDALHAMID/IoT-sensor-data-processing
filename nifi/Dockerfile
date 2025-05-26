FROM apache/nifi:1.23.2

# Copy your flow file and JDBC driver
COPY conf/flow.xml.gz /opt/nifi/nifi-current/conf/flow.xml.gz
COPY lib/postgresql-42.7.4.jar /opt/nifi/nifi-current/lib/postgresql-42.7.4.jar
