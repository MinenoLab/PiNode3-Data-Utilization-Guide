#!/bin/bash

# クエリを設定
QUERY='from(bucket: "pinode")
  |> range(start: -1h)
  |> filter(fn: (r) => r._measurement == "00")
  |> filter(fn: (r) => r._field== "temperature")
  |> yield(name: "mean")
  '

# curlコマンドを実行してデータを取得
response=$(curl --request POST \
  "${INFLUXDB_URL}/api/v2/query?org=${INFLUXDB_ORG}&bucket=get-started" \
  --header "Authorization: Token ${INFLUXDB_TOKEN}" \
  --header "Content-Type: application/vnd.flux" \
  --header "Accept: application/csv" \
  --data "query=${QUERY}" \
)


# エラーチェック
if [ $? -ne 0 ]; then
    echo "curlコマンドの実行中にエラーが発生しました。"
    exit 1
fi

# データをCSV形式で保存
echo "${response}" > ./influxdb_data.csv