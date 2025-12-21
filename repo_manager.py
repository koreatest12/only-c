import os
import datetime
import math
import hashlib

# ---------------------------------------------------------
# [설정] 저작권 및 보안 설정
# ---------------------------------------------------------
OWNER = "koreatest12"
REPO_URL = "https://github.com/koreatest12/only-c"
COPYRIGHT_TEXT = f"// (C) {datetime.datetime.now().year} {OWNER}. All rights reserved.\n// Strictly Prohibited for Unauthorized Copying or Reproduction.\n"

IGNORE_DIRS = {'.git', '.github', '__pycache__', 'build', 'output', 'release_pkg', 'release_dist', 'release_assets'}
IGNORE_FILES = {'repo_manager.py', '.gitignore', '.DS_Store', 'README.md', 'LICENSE'}

# ---------------------------------------------------------
# [기능 1] 보안 관리자 (Security Manager)
# ---------------------------------------------------------
class SecurityManager:
    @staticmethod
    def inject_watermark():
        """모든 소스코드(.cpp, .h)에 저작권 헤더 강제 주입"""
        injected_count = 0
        for root, dirs, files in os.walk("."):
            dirs[:] = [d for d in dirs if d not in IGNORE_DIRS]
            for file in files:
                if file.endswith(('.cpp', '.h', '.hpp', '.c')):
                    filepath = os.path.join(root, file)
                    try:
                        with open(filepath, 'r', encoding='utf-8') as f:
                            content = f.read()
                        
                        # 이미 워터마크가 있는지 확인
                        if "Strictly Prohibited" not in content:
                            with open(filepath, 'w', encoding='utf-8') as f:
                                f.write(COPYRIGHT_TEXT + "\n" + content)
                            injected_count += 1
                    except Exception as e:
                        print(f"Skipping {file}: {e}")
        return injected_count

    @staticmethod
    def generate_integrity_hash():
        """리포지토리 전체 무결성 해시 생성 (위변조 탐지)"""
        sha256_hash = hashlib.sha256()
        for root, dirs, files in os.walk("."):
            dirs[:] = [d for d in dirs if d not in IGNORE_DIRS]
            for names in sorted(files):
                if names in IGNORE_FILES: continue
                filepath = os.path.join(root, names)
                try:
                    with open(filepath, "rb") as f:
                        for byte_block in iter(lambda: f.read(4096), b""):
                            sha256_hash.update(byte_block)
                except: pass
        return sha256_hash.hexdigest()

# ---------------------------------------------------------
# [기능 2] 파일 분석기 (File Analyzer)
# ---------------------------------------------------------
def convert_size(size_bytes):
    if size_bytes == 0: return "0 B"
    size_name = ("B", "KB", "MB", "GB", "TB")
    i = int(math.floor(math.log(size_bytes, 1024)))
    p = math.pow(1024, i)
    s = round(size_bytes / p, 2)
    return f"{s} {size_name[i]}"

def get_description(filename):
    name_lower = filename.lower()
    if name_lower == 'dockerfile': return "🐳 Container Definition"
    if name_lower.endswith('.cpp'): return "⚡ C++ Source (Protected)"
    if name_lower.endswith('.h'): return "📚 Header (Protected)"
    if name_lower.endswith('.csv'): return "📊 Heavy Data Set"
    if name_lower.endswith('.exe') or 'binary' in name_lower: return "🪟 Compiled Binary"
    return "📄 Resource"

def generate_file_report():
    table_rows = []
    total_size = 0
    file_count = 0
    
    for root, dirs, files in os.walk("."):
        dirs[:] = [d for d in dirs if d not in IGNORE_DIRS]
        for file in files:
            if file in IGNORE_FILES or file == "README.md": continue
            
            file_path = os.path.join(root, file)
            try:
                size = os.path.getsize(file_path)
                total_size += size
                file_count += 1
                rel_path = os.path.relpath(file_path, ".")
                desc = get_description(file)
                
                # 변경사항 추적을 위한 날짜
                mtime = datetime.datetime.fromtimestamp(os.path.getmtime(file_path)).strftime('%Y-%m-%d %H:%M')
                
                link = f"[{rel_path}]({REPO_URL}/blob/main/{rel_path})"
                table_rows.append(f"| {link} | {desc} | {convert_size(size)} | {mtime} |")
            except: pass

    md_table = "\n### 📂 Real-time Repository Status (5-min Update)\n\n"
    md_table += f"**Total Files:** {file_count} | **Total Volume:** {convert_size(total_size)}\n\n"
    md_table += "| File Path 📁 | Description 📝 | Size 💾 | Last Modified 🕒 |\n"
    md_table += "| :--- | :--- | :---: | :---: |\n"
    md_table += "\n".join(sorted(table_rows))
    return md_table

# ---------------------------------------------------------
# 메인 로직 실행
# ---------------------------------------------------------
# 1. 워터마크 주입 실행
watermarked_files = SecurityManager.inject_watermark()

# 2. 무결성 해시 생성
integrity_hash = SecurityManager.generate_integrity_hash()

# 3. 리포트 생성
file_report = generate_file_report()
current_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S UTC")

# 4. README 작성
markdown_content = f"""
# 🚀 Welcome to My Tech Stack Journey

### Aspiring Systems Architect | Passionate about C++ & Docker Technology

> ⚠️ **COPYRIGHT WARNING & LEGAL NOTICE**
>
> This repository contains proprietary code and intellectual property.
> **Unauthorized copying, reproduction, or distribution of any file in this repository is strictly prohibited.**
> All source codes are digitally watermarked and monitored.

---

## 🛡️ Security & Integrity Check

This repository is protected by an automated integrity system.

| Metric | Status |
| :--- | :--- |
| **Copyright Protection** | ✅ Active (Source Code Watermarked) |
| **Integrity Hash** | `{integrity_hash}` |
| **Last Verified** | {current_time} |
| **Protected Files** | {watermarked_files} new files secured |

---

## 🛠️ Core Technical Focus

<div align="center">
  <img src="https://img.shields.io/badge/Protection-Active-red?style=for-the-badge&logo=security&logoColor=white" alt="Security" />
  <img src="https://img.shields.io/badge/Modern%20C%2B%2B-17%2F20-00599C?style=for-the-badge&logo=c%2B%2B&logoColor=white" alt="C++" />
  <img src="https://img.shields.io/badge/Docker-Containerization-2496ED?style=for-the-badge&logo=docker&logoColor=white" alt="Docker" />
</div>

---

## 🎯 Live System Status

### 🐳 Docker & DevOps
- **Auto-Publish:** Docker images pushed to GHCR automatically.
- **Security:** Automated container scanning enabled.

### ⚡ High-Performance Computing
- **Massive Data:** 20MB+ Stress Test Data generation.
- **GCC Optimization:** `-O3` flag applied for max speed.

---

{file_report}

---
<p align="center">
  <em>🔒 Secured & Updated via GitHub Actions: {current_time}</em>
</p>
"""

with open("README.md", "w", encoding="utf-8") as f:
    f.write(markdown_content)

print("✅ Security protocols applied and README updated.")
