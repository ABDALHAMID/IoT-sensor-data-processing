CREATE DATABASE mydatabase;

connect mydatabase;

CREATE TABLE IF NOT EXISTS machine_data (
    machine_id TEXT,
    temperature FLOAT,
    vibration FLOAT,
    status TEXT,
    runtime_hours FLOAT,
    timestamp TIMESTAMP,
    location TEXT
);
