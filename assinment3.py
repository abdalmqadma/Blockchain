import hashlib,time

def make_hash(i,t,d,p):
    return hashlib.sha256((str(i)+str(t)+str(d)+str(p)).encode()).hexdigest()

class Node:
    def __init__(self,name):
        self.name=name
        self.chain=[]
    def setBlock(self,data):
        i=len(self.chain);t=time.time();p=self.chain[-1]['hash'] if self.chain else "0"
        block={"index":i,"timestamp":t,"data":data,"prev_hash":p,"hash":make_hash(i,t,data,p)}
        self.chain.append(block);return block
    def getBlock(self,index):
        return self.chain[index] if 0<=index<len(self.chain) else "Block not found"
    def blocksExplorer(self):
        print(f"--- {self.name} ---");[print(b) for b in self.chain]
    def mineBlock(self,data="Mined Block"):
        return self.setBlock(data)

class DecentralizedSystem:
    def __init__(self,nodes):
        self.nodes=nodes
    def broadcast(self,data):
        for n in self.nodes:n.mineBlock(data)

n1=Node("Node 1")
n2=Node("Node 2")
n3=Node("Node 3")
net=DecentralizedSystem([n1,n2,n3])

net.broadcast("Genesis Block")
net.broadcast("First Transaction")
net.broadcast("Second Transaction")

n1.blocksExplorer()
n2.blocksExplorer()
n3.blocksExplorer()
print(n1.getBlock(1))
