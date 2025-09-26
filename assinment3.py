import hashlib,time

def make_hash(i,t,d,p): return hashlib.sha256((str(i)+str(t)+str(d)+str(p)).encode()).hexdigest()
chain=[]

def setBlock(data):
    i=len(chain); t=time.time(); p=chain[-1]['hash'] if chain else "0"
    chain.append({"index":i,"time":t,"data":data,"prev":p,"hash":make_hash(i,t,data,p)})

def getBlock(i): return chain[i] if 0<=i<len(chain) else "Block not found"
def blocksExplorer(): [print(b) for b in chain]
def mineBlock(data="Mined Block"): setBlock(data)

setBlock("Genesis")
setBlock("First")
setBlock("Second")
mineBlock("Reward")
blocksExplorer()
print(getBlock(1))
