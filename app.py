import streamlit as st
import time
import random

# ページ設定
st.set_page_config(page_title="Synapse Flow MVP", layout="wide")

st.title("🚛 Synapse Flow: Autonomous Industrial Finance OS")
st.markdown("### 物理的事実(DIMO) × 知能(AI) × 決済(JPYC)")

# サイドバー設定
st.sidebar.header("Simulation Settings")
wait_time = st.sidebar.slider("待機時間 (分)", 0, 240, 145)
score = st.sidebar.number_input("現在のKOUKAスコア", value=780)

# 2カラムレイアウト
col1, col2 = st.columns(2)

with col1:
    st.header("1. Physical Layer (DIMO)")
    st.info("車両からのリアルタイムデータを受信中...")
    
    # データを表示するコンテナ
    dimo_container = st.empty()
    
    if st.button("📡 DIMOデータ取得"):
        with st.spinner("Fetching Telemetry..."):
            time.sleep(1.5)
            status = "IDLING" if wait_time > 10 else "MOVING"
            dimo_data = {
                "vehicle_id": "v_12345",
                "location": "Aichi Logistics Center",
                "status": status,
                "wait_time": f"{wait_time} min"
            }
            dimo_container.json(dimo_data)
            
            if wait_time > 120:
                st.error(f"⚠️ 待機時間超過 ({wait_time}分 > 120分)")
                st.session_state['detention'] = True
            else:
                st.success("✅ 正常範囲内")
                st.session_state['detention'] = False

with col2:
    st.header("2. Settlement & Trust Layer")
    
    if st.session_state.get('detention'):
        st.warning("AI Agent: 待機料請求プロセスを開始します")
        
        if st.button("💸 JPYC即時決済を実行"):
            # 決済フロー
            with st.spinner("Executing Smart Contract on Avalanche..."):
                time.sleep(2)
                tx_hash = "0x" + "".join([random.choice("0123456789abcdef") for _ in range(64)])
                st.success(f"Payment Sent: 3,000 JPYC")
                st.code(f"Tx Hash: {tx_hash}", language="text")
            
            # 信用スコア更新
            with st.spinner("Updating CAC KOUKA Score..."):
                time.sleep(1)
                new_score = score + 15
                st.metric(label="New KOUKA Score", value=new_score, delta=15)
                st.balloons()

    else:
        st.info("待機時間の超過がないため、決済アクションは不要です。")

# フッター（アーキテクチャ図の代わりにテキストで補足）
st.markdown("---")
st.caption("Architecture: Physical(DIMO) -> Intelligence(AI) -> Settlement(JPYC) -> Trust(CAC)")