FROM apache/nifi:1.23.2

# Add the JDBC driver without overwriting the lib folder
COPY lib/postgresql-42.7.4.jar /opt/nifi/nifi-current/lib/postgresql-42.7.4.jar

# Add the flow file (if needed)
COPY conf/flow.xml.gz /opt/nifi/nifi-current/conf/flow.xml.gz
