# PiNode3-Data-Utilization-Guide

このリポジトリは、環境センサとカメラを搭載したマルチモーダルIoTデバイスPiNode3から収集されたデータの抽出、監視、分析方法についての包括的なガイドを提供します。
HTTP、bash、InfluxDB、Pythonを使用したデータ抽出方法、InfluxDBによるリアルタイムデータ監視の例、および画像とセンサデータの分析例を含みます。
農場環境の監視や作物の成長および収穫後の状況を分析するために、PiNode3を効果的に活用する方法をユーザに提供することを目的としています。

## 目次

1. [はじめに](#はじめに)
2. [セットアップ](#セットアップ)
3. [使い方](#使い方)
4. [ディレクトリ構成](#ディレクトリ構成)
5. [ディレクトリおよびファイルの説明](#ディレクトリおよびファイルの説明)
6. [Chapter1 : データ抽出方法](#chapter1--データ取得)
7. [Chapter2 : リアルタイムデータ監視例](#chapter2--リアルタイムデータ監視例)
8. [Chapter3 : 画像とセンサデータの分析例](#chapter3--画像とセンサデータの分析例)


## はじめに

PiNode3は、農業環境から環境および視覚データを収集するために設計された多機能IoTデバイスです。
このガイドでは、作物の成長、環境の変化、収穫後の分析に関する洞察を得るためのデータ抽出および利用方法の実践的な例を提供します。

## セットアップ

必要な依存パッケージをインストールします。
    ```bash
    pip install -r requirements.txt
    ```


## 使い方
各章ごとに、対応するファイルを開いくことで、データの取得、リアルタイム監視、データ分析の方法を確認できます。
ノートブックは notebooks ディレクトリ内にあります。


## ディレクトリ構成

```
PiNode3-Data-Utilization-Guide/
├── .gitignore
├── LICENSE
├── README.md
├── requirements.txt
├── examples/
│ ├── chapter1/
│ ├── chapter2/
│ └── chapter3/
├── notebooks/
│ ├── chapter1.md
│ ├── chapter2.md
│ ├── chapter3.ipynb
│ ├── leaf_detection_weight.pt
│ └── PiNode_DashBoard_Template.json
├── scripts/
│ ├── fetch_influxdb_data.py
│ └── fetch_influxdb_data.sh
```


### ディレクトリおよびファイルの説明

- **.gitignore**: バージョン管理から除外するファイルやディレクトリを指定するファイル。
- **README.md**: リポジトリの概要、使用方法、目次などを記載したファイル。
- **requirements.txt**: プロジェクトの依存パッケージを記載したファイル。
- **notebooks/**: 各章ごとのJupyterノートブックを含むディレクトリ。
  - **chapter1.md**: PiNodeの基礎知識（データの取得等）に関連するMarkDownファイル。
  - **chapter2.md**: リアルタイムデータ監視に関連するMarkDownファイル。
  - **chapter3.ipynb**: 画像とセンサのデータ分析に関連するノートブック。
- **examples/**: 各章ごとのサンプルデータやスクリプトを含むディレクトリ。
  - **chapter1/**: PiNodeの基礎知識（データの取得等）に関連するサンプルデータ。
  - **chapter2/**: リアルタイムデータ監視に関連するサンプルデータとスクリーンショット。
  - **chapter3/**: 画像とセンサのデータ分析に関連するサンプルデータと分析結果。
- **scripts/**: 各章で用いるスクリプトファイル
  - **fetch_influxdb_data.py/**: InfluxDBからデータを取得するPythonファイル
  - **fetch_influxdb_data.sh/**: InfluxDBからデータを取得するBashコマンド
  - **pinode_sample_downloader/**: 画像をローカルに取得するPythonファイル

## Chapter1 : データ取得

InfluxDBからデータを取得するガイドを提供します。
https://github.com/ShimadaTakutoLuke/PiNode3-Data-Utilization-Guide/blob/53cd77e619834b545cbcc426be63e544f2621e83/notebooks/chapter1.md

## Chapter2 : リアルタイムデータ監視例

InfluxDBを使用してリアルタイムデータを監視する方法について説明します。
https://github.com/ShimadaTakutoLuke/PiNode3-Data-Utilization-Guide/blob/53cd77e619834b545cbcc426be63e544f2621e83/notebooks/chapter2.md

## Chapter3 : 画像とセンサデータの分析例

PiNode3から収集した画像およびセンサデータを分析する方法について説明します。
https://github.com/ShimadaTakutoLuke/PiNode3-Data-Utilization-Guide/blob/53cd77e619834b545cbcc426be63e544f2621e83/notebooks/chapter3.ipynb