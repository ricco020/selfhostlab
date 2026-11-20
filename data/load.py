import json,time,threading,urllib.request,subprocess,sys
N=int(sys.argv[1]);C=int(sys.argv[2]);n=int(sys.argv[3])
def rss():
    o=subprocess.run("ps -eo rss,args",shell=True,capture_output=True,text=True).stdout
    return sum(int(l.split()[0]) for l in o.splitlines()[1:] if ('n8n start' in l and 'npm exec' not in l and 'sh -c' not in l) or 'disallow-code-generation' in l)//1024
peak=[0];stop=[0];lat=[];err=[0];lock=threading.Lock()
def mon():
    while not stop[0]:
        peak[0]=max(peak[0],rss());time.sleep(0.3)
def w(k):
    for _ in range(k):
        t=time.time()
        try:
            r=urllib.request.urlopen(urllib.request.Request('http://localhost:5799/webhook/mes',data=json.dumps({"n":n}).encode(),headers={'content-type':'application/json'}),timeout=60);r.read()
            with lock: lat.append(time.time()-t)
        except Exception: 
            with lock: err[0]+=1
m=threading.Thread(target=mon);m.start()
t0=time.time();ts=[threading.Thread(target=w,args=(N//C,)) for _ in range(C)];[t.start() for t in ts];[t.join() for t in ts]
d=time.time()-t0;stop[0]=1;m.join();lat.sort()
print(f"N={N} C={C} n={n} ok={len(lat)} err={err[0]} duree={d:.1f}s debit={len(lat)/d:.1f}/s p50={lat[len(lat)//2]*1000:.0f}ms p95={lat[int(len(lat)*.95)]*1000:.0f}ms rss_pic={peak[0]}MB rss_apres={rss()}MB",flush=True)
