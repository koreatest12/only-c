import http.server
import socketserver
import threading
import time
import os
os.chdir("deploy_root")
def run_server(port):
    try:
        with socketserver.TCPServer(("", port), http.server.SimpleHTTPRequestHandler) as httpd:
            httpd.serve_forever()
    except: pass
# 16개 포트 (8000~8015)
for p in range(8000, 8016):
    t = threading.Thread(target=run_server, args=(p,))
    t.daemon = True
    t.start()
    time.sleep(0.05)
time.sleep(60) # 서버 유지 시간
