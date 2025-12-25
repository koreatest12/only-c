import os
import datetime

# [FIX] C++ 컴파일 에러 방지를 위한 명확한 줄바꿈(\n) 포함
COPYRIGHT_HEADER = f"// (C) {datetime.datetime.now().year} GLOBAL ENTERPRISE. STRICTLY PROTECTED.\n"

def inject_security():
    print("[SEC] Injecting Safe Watermarks...")
    for root, dirs, files in os.walk("."):
        if any(x in root for x in ["bin", ".git", "__pycache__"]): continue
        
        for file in files:
            if file.endswith(('.java', '.cpp', '.js', '.yaml', '.sql')):
                path = os.path.join(root, file)
                try:
                    with open(path, 'r', encoding='utf-8') as f:
                        content = f.read()
                    
                    # 중복 방지 체크
                    if "STRICTLY PROTECTED" not in content:
                        with open(path, 'w', encoding='utf-8') as f:
                            # [CRITICAL FIX] 헤더 + 줄바꿈 + 원본 순서로 결합
                            f.write(COPYRIGHT_HEADER + "\n" + content)
                except Exception as e:
                    print(f"Skipped {file}: {e}")
    print("[SEC] Injection Completed.")

if __name__ == "__main__":
    inject_security()
