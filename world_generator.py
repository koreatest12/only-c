import os
import sys

sys.stdout.reconfigure(encoding='utf-8')

SERVICES = [
    "Banking", "Stock", "Insurance", "PublicData", "Crypto", "RealEstate", "GovTax",
    "Logistics", "HealthCare", "Metaverse", "AI_Core", "IoT_Network", 
    "Education_Hub", "Energy_Grid", "Defense_Sys"
]

def safe_makedirs(path):
    if not os.path.exists(path): os.makedirs(path, exist_ok=True)

# 1. Java Services & Data
def generate_services():
    print(f"🚀 Generating {len(SERVICES)} Global Services & Data...")
    safe_makedirs("src/main/java/com/global")
    safe_makedirs("data_center") # 데이터 저장소
    
    for svc in SERVICES:
        # Java App
        base = f"src/main/java/com/global/{svc.lower()}"
        safe_makedirs(base)
        with open(f"{base}/{svc}Application.java", "w") as f:
            f.write(f"package com.global.{svc.lower()};\npublic class {svc}Application {{ }}")
        
        # Dummy Sensitive Data (SQL/Config) - 암호화 대상
        with open(f"data_center/{svc}_sensitive.sql", "w") as f:
            f.write(f"-- CONFIDENTIAL DATA FOR {svc.upper()}\nINSERT INTO accounts VALUES (1, 'SECRET_{svc}');")
        with open(f"data_center/{svc}_config.xml", "w") as f:
            f.write(f"<config><apiKey>KEY_{svc}_12345</apiKey></config>")

# 2. C++ Crypto Engine Core (Simple XOR Cipher for demo)
def generate_crypto_core():
    print("🔐 Generating C++ Crypto Engine Source...")
    safe_makedirs("cpp_core")
    cpp_code = """
#include <iostream>
#include <fstream>
#include <string>
#include <vector>

// 단순 XOR 암호화/복호화 (데모용)
void process_file(const std::string& input_path, const std::string& output_path, char key) {
    std::ifstream infile(input_path, std::ios::binary);
    std::ofstream outfile(output_path, std::ios::binary);
    char buffer;
    while (infile.get(buffer)) {
        outfile.put(buffer ^ key); // XOR 연산
    }
    std::cout << "Processed: " << input_path << " -> " << output_path << std::endl;
}

int main(int argc, char* argv[]) {
    if (argc != 4) {
        std::cerr << "Usage: <mode:enc|dec> <input_file> <output_file>" << std::endl;
        return 1;
    }
    std::string mode = argv[1];
    std::string input = argv[2];
    std::string output = argv[3];
    char secret_key = 'X'; // 예제 키

    if (mode == "enc" || mode == "dec") {
        process_file(input, output, secret_key);
    } else {
        std::cerr << "Invalid mode." << std::endl; return 1;
    }
    return 0;
}
    """
    with open("cpp_core/crypto_engine.cpp", "w") as f:
        f.write(cpp_code)

if __name__ == "__main__":
    generate_services()
    generate_crypto_core()
    safe_makedirs("bin")
    safe_makedirs("downloads")
    safe_makedirs("encrypted_vault") # 암호화된 파일 저장소
    print("✅ World & Crypto Generation Complete.")
