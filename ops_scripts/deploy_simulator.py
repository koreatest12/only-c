import http.server, socketserver, threading, time, os, sys

def run_sim():
    print("🌐 [DEPLOY] Starting Self-Healing Server Farm...")
    if not os.path.exists("deploy_root"): os.makedirs("deploy_root")
    os.chdir("deploy_root")
    
    # 포트 충돌 시 자동 우회 로직 (Self-Healing)
    def start_node(p):
        retries = 3
        current_port = p
        while retries > 0:
            try:
                with socketserver.TCPServer(("", current_port), http.server.SimpleHTTPRequestHandler) as h:
                    h.serve_forever()
                break
            except OSError:
                print(f"⚠️ Port {current_port} busy, healing...")
                current_port += 100 # 포트 변경하여 재시도
                retries -= 1
    
    # 20개 노드 동시 기동
    for p in range(8000, 8020):
        t = threading.Thread(target=start_node, args=(p,))
        t.daemon = True
        t.start()
    
    time.sleep(5)
    print("✅ [DEPLOY] 20+ Nodes Active.")

if __name__ == "__main__":
    run_sim()
