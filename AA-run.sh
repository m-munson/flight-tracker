#!/bin/bash
################THIS IS THE RUN SCRIPT TO MAKE EACH PYTHON  FILE RUN IN PROPER SEQUENCE##################
/shared/sos/json/wtf-json.py
echo "data pulled"
/shared/sos/json/day-night.py
echo "map created"
/shared/sos/json/gut.py
echo "files gutted"
