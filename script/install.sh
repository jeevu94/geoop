#!/bin/bash

script/python-3.11.0-amd64.exe /passive InstallAllUsers=1 PrependPath=1

pip install -r requirements.txt

echo "All done"