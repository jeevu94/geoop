#!/bin/bash

script/python-3.11.0-amd64.exe /passive InstallAllUsers=1 PrependPath=1

python -m venv venv

.\venv\Scripts\activate

pip install -r requirements.txt

python manage.py runserver

echo "All done"

# Windows firewall disable or add port
# To Open port to the public world: Windows firewall in control panel add the port in advanced settings
# REF: https://learn.microsoft.com/en-us/answers/questions/291348/can39t-open-ports-in-windows-10.html