# -*- coding: utf-8 -*-
"""
Created on Tue Jul 28 11:54:33 2020

@author: venka
"""
class node:
    def __init__(self, val):
        self.val=val
        self.next=None
        
class linklist:
    def __init__(self):
        self.head=None
        
    def insert_at_begin(self, x:int):
        t=self.head
        if t==None:
            self.head=node(x)
        else:
            self.head=node(x)
            self.head.next=t
            
    def insert_at_end(self, x:int):
        
        t=self.head
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
    c=0
    print("enter 1 for insertion at begin")
    print("enter 2 for insertion at end")
    print("enter 3 for removing an element")
    print("enter 4 for deleting an element based on the index")
    print("enter 5 for to get the length of the linked list")
    print("enter 6 to print the link list") 
    print("enter 7 to stop the program")
          
    while c!=7:
        c=int(input("enter choice"))
        if c==1:
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
        else:
            break
                        
