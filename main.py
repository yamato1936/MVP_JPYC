import time
import json
import random

class SynapseFlowMVP:
    def __init__(self):
        self.score = 780 # 初期KOUKAスコア
        print("\n=== Synapse Flow System Initialized ===")
        print(">> Layer 1: DIMO Connection [OK]")
        print(">> Layer 2: Avalanche Subnet [OK]")
        print(">> Layer 3: JPYC Contract [OK]")
        print(">> Layer 4: AI Agent (ERC-8004) [Standby]")
        
    def run_cycle(self):
        # --- Layer 1: Physical (DIMO) ---
        print("\n[Layer 1: Physical] 📡 Fetching DIMO Telemetry...")
        time.sleep(1.5)
        # 待機時間 145分 (閾値120分超過)
        vehicle_data = {"vehicle_id": "v_12345", "status": "IDLING", "wait_time_min": 145, "lat": 35.05, "lng": 136.85}
        print(f"   > Vehicle ID: {vehicle_data['vehicle_id']}")
        print(f"   > Location: Aichi Logistics Center (Lat: {vehicle_data['lat']}, Lng: {vehicle_data['lng']})")
        print(f"   > Status: {vehicle_data['status']} | Duration: {vehicle_data['wait_time_min']} min")
        
        # --- Layer 4: Intelligence (AI Decision) ---
        print("\n[Layer 4: Intelligence] 🧠 AI Agent Analyzing...")
        time.sleep(1.5)
        if vehicle_data["wait_time_min"] > 120:
            claim_amount = 3000
            print(f"   > ALERT: Detention Detected (>120min).")
            print(f"   > DECISION: Execute Payment of {claim_amount} JPYC.")
            
            # --- Layer 3: Settlement (JPYC) ---
            self.execute_settlement(claim_amount)
            
            # --- Layer 5: Finance & Viz (SF & CAC) ---
            self.update_trust_score()
            self.mint_scb()
        else:
            print("   > Status Normal. No action.")

    def execute_settlement(self, amount):
        print(f"\n[Layer 3: Settlement] 💸 Sending JPYC on Avalanche...")
        time.sleep(2)
        # ランダムなTxハッシュ生成
        tx_hash = "0x" + "".join([random.choice("0123456789abcdef") for _ in range(64)])
        print(f"   > Transaction Sent: {amount} JPYC")
        print(f"   > Tx Hash: {tx_hash} (Confirmed)")

    def update_trust_score(self):
        print(f"\n[Layer 5: Visualization] 📊 CAC KOUKA Score Update...")
        self.score += 15
        print(f"   > 'Prompt Payment' Verified.")
        print(f"   > New Score: {self.score} (Rank A+)")

    def mint_scb(self):
        print(f"\n[Layer 5: Finance] 🏦 Secured Finance Integration...")
        print(f"   > Smart Commercial Bill (SCB) Minted as NFT.")
        print(f"   > Status: Available for immediate factoring.")

if __name__ == "__main__":
    app = SynapseFlowMVP()
    app.run_cycle()
    print("\n=== Demo Sequence Complete ===")