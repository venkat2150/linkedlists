# -*- coding: utf-8 -*-
"""
Created on Tue Jul 28 11:54:33 2020
@author: venkata kautilya
"""
class node:
    def __init__(self, val):
        self.val=val
        self.next=None
        
class linklist:
    def __init__(self):
        self.head=None
        
    def insert(self, x: int, y: int):
        t=self.head
        if 0<y<=self.length()+1 and t:
            ct=1
            while t.next and ct!=y-1:
                t=t.next
            temp=node(x)
            temp.next=t.next
            t.next=temp
        else:
            print("invalid")
                
    def insert_at_begin(self, x:int):
        t=self.head
        if t==None:
            self.head=node(x)
        else:
            self.head=node(x)
            self.head.next=t
            
    def insert_at_end(self, x:int):
        
        t=self.head
        if not t:
            self.insert_at_begin(x)
            return
        while t.next!=None:
            t=t.next
        temp=node(x)
        t.next=temp
        
    def delete(self, x:int):    #remove element by index
        i=0
        prev=t=self.head
        if x!=1:
            while i<x-1:
                if t.next:
                    prev=t
                    t=prev.next
                else:
                    print("")
                    print("invalid")
                    break
                i+=1
            prev.next=t.next
        else:
            self.head=t.next
            
    def remove(self, x:int):  #remove element by comparision
        t=self.head
        count=0
        while t and t.val!=x:
            count+=1
            t=t.next    
        self.delete(count+1)
                
    def length(self) -> int:
        t=self.head
        count=0
        while t:
            count+=1
            t=t.next
        return count
        
    def swap(self, a:int, b:int) :
        t1=self.head
        i=0
        while  t1 and i<a-1:
            t1=t1.next
            i+=1
        i=0
        t2=self.head
        while t2 and i<b-1:
            t2=t2.next
            i+=1
            
        if t1 and t2:    
            t1.val,t2.val=t2.val, t1.val
        else:
            print("invalid")
        
    def pos(self, x:int)->int:
        t=self.head
        count=0
        while t and t.val!=x:
            t=t.next
            count+=1    
        if not t:
            return -1
        else:
            return count+1
        
    def sinsert(self, srtd: object, nn: object)-> object:
        t=None
        if not srtd or srtd.val<=nn.val:
            nn.next=srtd
            srtd=nn
        else:
            t=srtd
            while t.next and t.next.val> nn.val:
                t=t.next
            nn.next=t.next
            t.next=nn    
        return srtd
    
    def sort(self):
        srtd=None
        t=self.head
        while t:
            temp=t.next
            srtd=self.sinsert(srtd, t)
            t=temp       
        self.head=srtd
            
    def prt(self):
        t=self.head
        print("")
        while t!=None:
            print(t.val, end="")
            if t.next:
                print("-->", end="")
            else:
                print("")
            t=t.next
            
if __name__ == "__main__":
    l1=linklist()
    
    print("enter 0 to insert")
    print("enter 1 for insertion at begin")
    print("enter 2 for insertion at end")
    print("enter 3 for removing an element")
    print("enter 4 for deleting an element based on the index")
    print("enter 5 for to get the length of the linked list")
    print("enter 6 to print the link list") 
    print("enter 7 to find the position of particular elemenet in the linked list")
    print("enter 8 to swap two elements of an array")
    print("enter 9 to sort the linked list")
    print("enter anything more than 9 to stop the program")
          
    while True:
        c=int(input("enter choice"))
        if c==0:
            print("")
            x=int(input("enter the number to be inserted: "))
            y=int(input("enter the position to be inserted in:"))
            l1.insert(x, y)
        elif c==1:
            print("")
            x=int(input("enter number to insert:"))
            l1.insert_at_begin(x)
        elif c==2:
            print("")
            x=int(input("enter number to insert:"))
            l1.insert_at_end(x)
        elif c==3:
            print("")
            x=int(input("enter the element that must be removed"))
            l1.remove(x)
        elif c==4:
            print("")
            x=int(input("enter the position of the element that must be deleted: "))
            l1.delete(x)
        elif c==5:
            print("")
            print("length is: "+str(l1.length()))    
        elif c==6:
            l1.prt()
        elif c==7:
            x=int(input("enter the element to find its position: "))
            print(l1.pos(x))
        elif c==8:
            print("")
            x1=int(input("enter the position of the first element: "))
            print("")
            x2=int(input("enter the position of the second element: "))
            l1.swap(x1, x2)
        elif c == 9:
            print("")
            l1.sort()
        else:
            break
