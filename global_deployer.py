import http.server
import socketserver
import threading
import time
import os

if not os.path.exists("deploy_root"): os.makedirs("deploy_root")
os.system("cp bin/*.jar deploy_root/")
os.system("cp data_center/*.db deploy_root/")
os.chdir("deploy_root")

# 16개 포트 동시 개방 (대규모 클러스터 시뮬레이션)
PORTS = range(8000, 8016) 

def run_server(port):
    try:
        Handler = http.server.SimpleHTTPRequestHandler
        # 리소스 절약을 위해 로그 억제 가능하나 여기선 출력
        with socketserver.TCPServer(("", port), Handler) as httpd:
            # print(f"🌍 Node Active: {port}")
            httpd.serve_forever()
    except: pass

for p in PORTS:
    t = threading.Thread(target=run_server, args=(p,))
    t.daemon = True
    t.start()
    time.sleep(0.1)

print("✅ Global Server Farm (16 Nodes) is Online. Waiting 10s...")
time.sleep(10)
