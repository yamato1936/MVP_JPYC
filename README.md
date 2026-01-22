# 🚛 Synapse Flow: 自律型産業金融OS

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Python](https://img.shields.io/badge/Python-3.9%2B-blue)](https://www.python.org/)
[![Framework](https://img.shields.io/badge/Streamlit-1.30-red)](https://streamlit.io/)
[![Blockchain](https://img.shields.io/badge/Avalanche-Fuji_Testnet-red)](https://www.avax.network/)

> **JPYC Innovation Challenge 2026 ファイナリスト選出プロジェクト**

## 📖 プロジェクト概要
**「待ったら、増える。走ったら、すぐ貰える。」**

Synapse Flow（シナプス・フロー）は、物流業界最大の課題である「荷待ち時間の無報酬化」と「多重下請け構造による資金詰まり」を解決する、**自律型産業金融オペレーティングシステム**です。

物理的な事実（DIMO車両データ）をAIが客観的に判定し、スマートコントラクト（Avalanche）とステーブルコイン（JPYC）を用いて、即座に価値を還元します。

---

## 🚀 デモアプリ (MVP) の機能

本リポジトリには、プレゼンテーションで使用した実証実験用プロトタイプ（MVP）が含まれています。

### 主な機能
1.  **リアルタイム監視 (Physical Layer):**
    * OpenStreetMap (Folium) を用いた車両位置のトラッキング。
    * DIMO APIを模したテレメトリデータの可視化。
2.  **異常検知と自律判断 (Intelligence Layer):**
    * AIエージェントによる「待機時間超過（Detention）」の自動検知。
    * 120分の閾値を超えた瞬間、ペナルティ料金を自律的に算出。
3.  **即時決済 (Settlement Layer):**
    * Avalanche Fuji TestnetへのRPC接続。
    * JPYCを用いた中抜きのない直接送金シミュレーション。

---

## 🛠 クイックスタート

手元のPCでデモを起動する手順です。

### 1. インストール
```
pip install -r requirements.txt
```


### 2. アプリケーション起動
以下のコマンドを実行すると、ブラウザでダッシュボードが立ち上がります。

```
streamlit run app.py
```

### 3. 操作方法
サイドバーの 「経過待機時間」スライダー を動かしてください。

120分 を超えるとアラートが発動し、地図上のピンが赤色に変化します。

「JPYC即時払い承認」ボタン を押すと、ブロックチェーン上での決済トランザクションが発行されます。
