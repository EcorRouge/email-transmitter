#!/bin/bash

python version.py

if [ "$APP_ENV" != "production" ]
then
    watchmedo auto-restart --recursive --pattern="*.py" --directory="/src/" python app.py
else
    python app.py
fi
