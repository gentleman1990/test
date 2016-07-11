#!/bin/bash

python getGraphanaDataOneDay.py
rm grafanaData15Minutes.csv

python parseCSVLogs.py
rm result.csv

java -jar Klasyfikatory.jar ./ ttom_data_grafana.csv 0 grafanaData15Minutes.csv

echo ""
cat result.csv
echo ""
echo ""