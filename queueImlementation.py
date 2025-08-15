class myqueue():
    def __init__(self):
        self.que=[]
        self.length=0
    def enqueue(self,item):
        self.que.append(item)
        self.length+=1

    def dequeue(self):
        print("dequeue",self.que[0])
        for i in range(0,self.length-1): 
            self.que[i]=self.que[i+1]
        self.length-=1

    def isempty(self):
        if self.length==0:
           print( "empty")

    def display(self): 
        for i in range(0,self.length):
            print(self.que[i])


que=myqueue()
que.isempty()
que.enqueue(1)
que.enqueue(2)
que.enqueue(3)
que.display()
que.dequeue()
que.display()
