#!/bin/bash

script/python-3.11.0-amd64.exe /passive InstallAllUsers=1 PrependPath=1

python -m venv venv

.\venv\Scripts\activate

pip install -r requirements.txt

python manage.py runserver

echo "All done"