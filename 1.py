class node:
    
    def __init__(self,data=0,next=None):
        
        self.data=data
        self.next=next
        
    
        
        
        
    
    
    
    
    
    
    
    


class linkedlist:
    
    def __init__(self):
        self.head=None
    
    
    def createnode(self,s):
        l1=node(s,self.head)
        self.head=l1
        
    def print(self):
        
        itr=self.head
        
        while itr:
            
            print(itr.data)
            itr=itr.next
    
     
l=linkedlist()
l.createnode(5)
l.createnode(6)
l.createnode(4)
l.print()







