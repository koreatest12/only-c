import os
import sys
import sqlite3
import random

sys.stdout.reconfigure(encoding='utf-8')

# [전 세계/전 분야 서비스 목록 확장]
SERVICES = [
    "Banking", "Stock", "Insurance", "PublicData", "Crypto", "RealEstate", "GovTax",
    "Logistics", "HealthCare", "Metaverse", "AI_Core", "IoT_Network", 
    "Education_Hub", "Energy_Grid", "Defense_Sys"
]

def safe_makedirs(path):
    if not os.path.exists(path):
        os.makedirs(path, exist_ok=True)

def log(msg):
    print(f"[WORLD-GEN] {msg}")

# 1. Full-Stack Ecosystem 생성
def generate_ecosystem():
    log(f"🚀 Generating {len(SERVICES)} Global Services...")
    
    # 경로 생성
    safe_makedirs("src/main/java/com/global")
    safe_makedirs("src/main/resources/static")
    safe_makedirs("src/main/resources/config")
    safe_makedirs("global_configs")
    
    for svc in SERVICES:
        base = f"src/main/java/com/global/{svc.lower()}"
        safe_makedirs(base)
        
        # Main Application
        with open(f"{base}/{svc}Application.java", "w") as f:
            f.write(f"package com.global.{svc.lower()};\npublic class {svc}Application {{ public static void main(String[] args) {{ System.out.println(\"{svc} Service Global Online\"); }} }}")
        
        # 대량 파일 생성 (Controller, Service, DTO)
        for i in range(1, 21):
            with open(f"{base}/{svc}Controller{i}.java", "w") as f:
                f.write(f"package com.global.{svc.lower()};\npublic class {svc}Controller{i} {{ }}")
        
        # Global Configs
        with open(f"global_configs/{svc}_prod.yaml", "w") as f:
            f.write(f"service: {svc}\nregion: global\nmode: production")

# 2. Big Data Database Cluster
def generate_data_cluster():
    log("🗃️ Generating Big Data Cluster...")
    safe_makedirs("data_center")
    
    for svc in SERVICES:
        # SQL Schema
        with open(f"data_center/{svc}_schema_v3.sql", "w") as f:
            f.write(f"CREATE TABLE {svc}_global (id BIGINT, region VARCHAR(50), data TEXT);\n")
        
        # SQLite Live Data (대량 데이터 주입)
        try:
            conn = sqlite3.connect(f"data_center/{svc}_shard_01.db")
            cur = conn.cursor()
            cur.execute(f"CREATE TABLE {svc}_audit (id INT, hash TEXT)")
            # 1000건 데이터 주입
            cur.executemany(f"INSERT INTO {svc}_audit VALUES (?, ?)", [(k, f"Hash_{k}") for k in range(1000)])
            conn.commit()
            conn.close()
        except: pass

# 3. C++ High-Performance Core (Safe Init)
def generate_cpp_core():
    log("🚀 Generating C++ Core Engine...")
    safe_makedirs("cpp_core")
    # [중요] 초기 파일 생성 시 헤더가 맨 윗줄에 오도록 보장
    with open("cpp_core/world_engine.cpp", "w") as f:
        f.write('#include <iostream>\n')
        f.write('int main() { std::cout << "World Engine Active" << std::endl; return 0; }')

if __name__ == "__main__":
    generate_ecosystem()
    generate_data_cluster()
    generate_cpp_core()
    
    # 배포용 디렉토리 사전 확보
    safe_makedirs("bin")
    safe_makedirs("downloads")
    safe_makedirs("deploy_logs")
    log("✅ World Generation Complete.")
