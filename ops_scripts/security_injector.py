import os, datetime
HEADER = f"// (C) {datetime.datetime.now().year} FUTURE OPS. SECURE.\n"
def inject():
    for root, dirs, files in os.walk("."):
        if any(x in root for x in ["bin", ".git", "docs"]): continue
        for file in files:
            if file.endswith(('.java', '.cpp')):
                try:
                    path = os.path.join(root, file)
                    with open(path, 'r+', encoding='utf-8') as f:
                        c = f.read()
                        if "FUTURE OPS" not in c:
                            f.seek(0, 0)
                            f.write(HEADER + c)
                except: pass
if __name__ == "__main__": inject()
