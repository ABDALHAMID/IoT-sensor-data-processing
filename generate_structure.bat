@echo off
REM ---------------------------------------------
REM generate_structure.bat
REM Generates project folders & empty files
REM Run this inside IoT-sensor-data-processing/
REM ---------------------------------------------

:: Create folders
mkdir api
mkdir nifi
mkdir postgres

:: Create empty files in api/
type nul > api\producer.py
type nul > api\requirements.txt
type nul > api\Dockerfile

:: Create empty file in postgres/
type nul > postgres\init.sql

:: Create root-level files
type nul > .env.example
type nul > .gitignore
type nul > README.md
type nul > docker-compose.yml

echo Folder structure and files created.
pause

