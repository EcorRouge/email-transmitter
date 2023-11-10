#!/bin/bash

python src/version.py

if [ "$ENV" != "production" ]
then
    watchmedo auto-restart --recursive --pattern="*.py" --directory="/src/" python src/process.py
else
    python src/process.py
fi
