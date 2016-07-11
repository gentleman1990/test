python getGraphanaDataOneDay.py
del grafanaData15Minutes.csv

python parseCSVLogs.py
del result.csv

java -jar Klasyfikatory.jar %cd% ttom_data_grafana.csv 0 grafanaData15Minutes.csv

echo ""
type result.csv
echo ""
echo ""