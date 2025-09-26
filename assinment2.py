import hashlib,time

def make_hash(i,t,d,p): 
    return hashlib.sha256((str(i)+str(t)+str(d)+str(p)).encode()).hexdigest()

central_chain=[]

def setBlock(data):
    i=len(central_chain); t=time.time(); p=central_chain[-1]['hash'] if central_chain else "0"
    central_chain.append({"index":i,"time":t,"data":data,"prev":p,"hash":make_hash(i,t,data,p)})

def getBlock(i): 
    return central_chain[i] if 0<=i<len(central_chain) else "Block not found"

def blocksExplorer(): 
    [print(b) for b in central_chain]

def mineBlock(data="Mined Block"): 
    setBlock(data)

setBlock("Genesis Block")
setBlock("First Record")
setBlock("Second Record")
mineBlock("Central Reward")
blocksExplorer()
print(getBlock(1))
