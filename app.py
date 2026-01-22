import streamlit as st
import time
import pandas as pd
import random
import folium
from streamlit_folium import st_folium
from web3 import Web3

# --- ページ設定 ---
st.set_page_config(
    page_title="Synapse Flow Dashboard",
    page_icon="🚛",
    layout="wide",
    initial_sidebar_state="expanded"
)

# --- 定数設定 ---
RPC_URL = "https://api.avax-test.network/ext/bc/C/rpc"

# --- サイドバー (操作パネル) ---
st.sidebar.header("🛠️ シミュレーション設定")

# 待機時間をスライダーで操作
wait_time = st.sidebar.slider("経過待機時間 (分)", 0, 300, 45, help="120分を超えるとペナルティが発生します")
if wait_time > 120:
    st.sidebar.error(f"⚠️ 閾値超過 (+{wait_time - 120}分)")
else:
    st.sidebar.success("✅ 許容範囲内")

vehicle_id = st.sidebar.text_input("対象車両ID", "DIMO-Vehicle-8823")
location_name = st.sidebar.text_input("現在地名称", "愛知県 飛島村 物流センター")

# --- メインエリア ---
st.title("🚛 Synapse Flow: 自律型物流OS")
st.markdown(
    """
    <style>
    .big-font { font-size:20px !important; }
    </style>
    **Physical (DIMO) × Intelligence (AI) × Settlement (JPYC)**
    """, unsafe_allow_html=True
)

# 2カラムレイアウト
col_left, col_right = st.columns([1, 1])

# === 左側: 物理層 (DIMO) ===
with col_left:
    st.subheader("1. DIMO車両モニタリング")
    
    # ステータス判定
    is_detention = wait_time > 120
    
    # ピンの色とアイコン設定
    if is_detention:
        pin_color = "red"
        icon_type = "exclamation-triangle"
        status_text = "⚠️ DETENTION (待機割増発生中)"
    else:
        pin_color = "green"
        icon_type = "truck"
        status_text = "✅ NORMAL (正常稼働中)"

    # --- Folium (OpenStreetMap) による地図表示 ---
    # 愛知県飛島村の座標
    lat, lon = 35.051, 136.852
    
    # 地図の作成 (APIキー不要)
    m = folium.Map(location=[lat, lon], zoom_start=13)

    # マーカーの追加
    folium.Marker(
        [lat, lon],
        popup=location_name,
        tooltip=status_text,
        icon=folium.Icon(color=pin_color, icon=icon_type, prefix='fa')
    ).add_to(m)

    # Streamlitに表示
    st_folium(m, width="100%", height=300)

    # テレメトリデータ表示
    st.info(f"📍 現在地: {location_name}")
    
    st.markdown("##### 📡 リアルタイム・テレメトリ (DIMO API)")
    dimo_data = {
        "tokenId": vehicle_id,
        "timestamp": time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime()),
        "gps": {"lat": lat, "lon": lon},
        "engineStatus": "OFF (Idling)",
        "signals": {
            "currentWaitTime": f"{wait_time} min",
            "detentionThreshold": "120 min"
        }
    }
    st.json(dimo_data)


# === 右側: 金融・決済層 (Avalanche/JPYC) ===
with col_right:
    st.subheader("2. 決済・信頼 (Avalanche / JPYC)")

    # RPC接続チェック
    with st.expander("🔗 ブロックチェーン接続ステータス", expanded=True):
        try:
            w3 = Web3(Web3.HTTPProvider(RPC_URL))
            if w3.is_connected():
                st.success(f"✅ Avalanche Fuji Testnet 接続確立")
                st.caption(f"RPC: {RPC_URL}")
                st.metric("Latest Block", f"#{w3.eth.block_number:,}")
            else:
                st.error("❌ ネットワーク接続エラー")
        except Exception as e:
            st.error(f"接続待機中... ({e})")

    st.markdown("---")

    # AIエージェントの判断ログ
    st.markdown("##### 🧠 自律エージェント (ERC-8004) 処理ログ")
    log_placeholder = st.empty()

    if is_detention:
        penalty = 3000 + (wait_time - 120) * 50
        
        log_text = f"""
        [ALERT] 閾値超過検知: {wait_time}分 (規定: 120分)
        [QUERY] 財務DB参照... 支払い能力 OK
        [CALC] 待機料算出: 基本給 + 超過分 = {penalty:,} JPYC
        [ACTION] スマートコントラクト実行準備完了
        """
        log_placeholder.code(log_text, language="bash")

        # 決済ボタン
        if st.button("💸 JPYC即時払い承認 (AI Agent)", type="primary"):
            progress_bar = st.progress(0)
            status_text_ph = st.empty()
            
            # トランザクション演出
            steps = [
                "署名生成中 (Private Key Signing)...",
                "Avalancheへブロードキャスト中...",
                "ブロック取り込み待ち (Confirming)...",
                "最終承認完了 (Finalized)"
            ]
            
            for i, step in enumerate(steps):
                status_text_ph.text(f"処理中: {step}")
                progress_bar.progress((i + 1) * 25)
                time.sleep(0.5)
            
            # 完了表示
            tx_hash = "0x" + "".join([random.choice("0123456789abcdef") for _ in range(64)])
            st.success("🎉 即時決済完了 (Settlement Completed)")
            
            # レシート風表示
            st.markdown(f"""
            > **Transaction Receipt**
            > * **To:** {vehicle_id}
            > * **Amount:** `{penalty:,} JPYC`
            > * **Tx Hash:** [`{tx_hash}`](https://testnet.snowtrace.io/)
            """)
            
            st.balloons()
            st.info("📈 CAC KOUKA (信用スコア) 更新: **780** ➡ **805** (+25)")

    else:
        log_placeholder.code("[INFO] 待機監視中... 正常範囲内 (No Action)", language="bash")
        st.info("現在、支払いを実行する必要はありません。")

# フッター
st.markdown("---")
st.caption("Synapse Flow MVP - Powered by DIMO, JPYC, Avalanche, Secured Finance, CAC")