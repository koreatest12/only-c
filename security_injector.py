import os
import datetime
HEADER = f"// (C) {datetime.datetime.now().year} GLOBAL CYBERNETICS. ENCRYPTED SYSTEM.\n"
def inject():
    for root, dirs, files in os.walk("."):
        if "bin" in root or ".git" in root: continue
        for file in files:
            if file.endswith(('.java', '.cpp', '.sql', '.xml')):
                path = os.path.join(root, file)
                try:
                    with open(path, 'r', encoding='utf-8') as f: content = f.read()
                    if "GLOBAL CYBERNETICS" not in content:
                        with open(path, 'w', encoding='utf-8') as f:
                            f.write(HEADER + content)
                except: pass
if __name__ == "__main__": inject()
