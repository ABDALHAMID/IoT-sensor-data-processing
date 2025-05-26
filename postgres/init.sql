-- Create the database if it doesn't exist
DO
$$
BEGIN
   IF NOT EXISTS (
      SELECT FROM pg_database WHERE datname = 'mydatabase'
   ) THEN
      CREATE DATABASE mydatabase;
   END IF;
END
$$;

-- Connect to the new database (optional, for clarity)
\connect mydatabase;

-- Create the table if it doesn't exist
CREATE TABLE IF NOT EXISTS machine_data (
    machine_id TEXT,
    temperature FLOAT,
    vibration FLOAT,
    status TEXT,
    runtime_hours FLOAT,
    timestamp TIMESTAMP,
    location TEXT
);
