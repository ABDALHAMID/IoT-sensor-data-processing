FROM apache/nifi:1.23.2

# Copy the PostgreSQL JDBC driver
COPY lib/postgresql-42.7.4.jar /opt/nifi/nifi-current/lib/

# Copy the flow configuration file
COPY conf/flow.xml.gz /opt/nifi/nifi-current/conf/flow.xml.gz
