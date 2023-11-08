#!/bin/bash

python src/version.py

if [ "$ENV" != "production" ]
then
    watchmedo auto-restart --recursive --pattern="*.py" --directory="/src/" python src/main.py
else
    python src/main.py
fi
