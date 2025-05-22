@echo off
REM ----------------------------------------------------------
REM initialiseProject.bat
REM Run this inside the IoT-sensor-data-processing folder
REM It builds Docker containers and starts the stack
REM ----------------------------------------------------------

echo === Copying .env.example to .env ===
IF NOT EXIST .env (
    copy .env.example .env
    echo .env created.
) ELSE (
    echo .env already exists, skipping copy.
)

echo === Building API Docker image ===
docker-compose build

echo === Starting all services ===
docker-compose up -d

echo === Showing container status ===
docker ps

echo === Project initialized successfully ===
pause
