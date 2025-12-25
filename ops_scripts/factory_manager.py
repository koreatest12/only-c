import os, sys, random, datetime
from PIL import Image, ImageDraw

sys.stdout.reconfigure(encoding='utf-8')

# 기존 엔터프라이즈 + 미래 기술 + 수집 서버
SERVICES = [
    "Banking", "Stock", "Insurance", "PublicData", "Crypto", "RealEstate", "GovTax",
    "Logistics", "HealthCare", "Metaverse", "AI_Core", "IoT_Network", 
    "Education_Hub", "Energy_Grid", "Defense_Sys",
    "Quantum_Compute", "Bio_Tech", "Space_Ops", "Nano_Bot", "Fusion_Energy",
    "Genomic_Seq", "Autonomous_Vehicle", "Smart_City", "Drone_Delivery", "Robotics"
]
COLLECTORS = ["Log_Aggregator", "Metric_Beat", "Trace_Collector", "Security_Auditor", "Deep_Packet_Inspector"]

def safe_makedirs(path):
    if not os.path.exists(path): os.makedirs(path, exist_ok=True)

def produce_assets():
    print(f"🚀 [FACTORY] Generating {len(SERVICES) + len(COLLECTORS)} Systems...")
    
    # 1. 디렉토리 구조 확보
    safe_makedirs("src/main/java/com/global/core")
    safe_makedirs("src/main/java/com/global/future")
    safe_makedirs("src/main/java/com/global/collection")
    safe_makedirs("docs/images")
    safe_makedirs("cpp_core")
    safe_makedirs("bin") # [중요] Python 레벨에서도 생성

    # 2. Java 코드 생성
    all_svcs = SERVICES + COLLECTORS
    for svc in all_svcs:
        # 분류
        if svc in SERVICES:
            kind = 'future' if svc in ["Quantum_Compute", "Bio_Tech"] else 'core'
        else:
            kind = 'collection'
        
        base = f"src/main/java/com/global/{kind}/{svc.lower()}"
        safe_makedirs(base)
        
        with open(f"{base}/{svc}Application.java", "w") as f:
            f.write(f"package com.global.{kind}.{svc.lower()};\npublic class {svc}Application {{ public static void main(String[] args) {{ System.out.println(\"{svc} Active\"); }} }}")

    # 3. 아키텍처 시각화 (이미지 생성)
    try:
        img = Image.new('RGB', (600, 300), color=(10, 20, 40))
        d = ImageDraw.Draw(img)
        d.rectangle([(20, 20), (580, 280)], outline="cyan", width=2)
        d.text((50, 50), f"Global System v{datetime.datetime.now().year}", fill="white")
        d.text((50, 100), f"Active Nodes: {len(all_svcs)}", fill="green")
        d.text((50, 150), "Status: SELF-HEALING ACTIVE", fill="yellow")
        img.save("docs/images/architecture_v2.png")
    except: pass

    # 4. C++ 엔진 소스
    with open("cpp_core/crypto.cpp", "w") as f:
        f.write('#include <iostream>\n#include <string>\n')
        f.write('int main(int argc, char* argv[]) { std::cout << "Crypto Engine v2.0 Online" << std::endl; return 0; }')

if __name__ == "__main__":
    produce_assets()
