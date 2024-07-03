from influxdb_client import InfluxDBClient

# 環境変数の設定
INFLUXDB_URL = "http://pinode05.local:8086"
INFLUXDB_TOKEN = "JhOQHJBtQ5dBx9ZZPhIegXGv51dHVlbWKAL1KNmSDdltdY83hxB3HkXZew6I2J42ZZ2hULpmxbU8OGesrTsAlg=="
INFLUXDB_ORG = "pinode"
INFLUXDB_BUCKET = "pinode"

# InfluxDBクライアントの作成
client = InfluxDBClient(url=INFLUXDB_URL, token=INFLUXDB_TOKEN, org=INFLUXDB_ORG)

# クエリを設定
query = """
from(bucket: "pinode")
    |> range(start: -1h)
    |> filter(fn: (r) => r._measurement == "00")
    |> filter(fn: (r) => r._field == "temperature")
    |> yield(name: "mean")
"""

# クエリを実行
df = client.query_api().query_data_frame(query)

# CSVファイルに保存
df.to_csv("influxdb_data.csv", index=False)