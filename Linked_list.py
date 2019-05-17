class Node:
    def __init__(self,data):
        self.data=data;
        self.next=None;
class ssl:
    def __init__(self):
        self.head=None
        
    def Insertion(self):
            temp.next=self.head
            self.head=temp
    def printssl(self):
        temp=self.head
        while (temp!=None):
             print(temp.data)
             temp=temp.next
    def Deletion(self):
        if(self.head!=None):
             temp=self.head
             self.head=self.head.next
             temp.next=None
        else:
            print("There is no data")
        
          
ssl_obj=ssl()
choice=0
while(choice!=4):
    print("   LINK LIST IMPLEMENTATION  \n 1.Insertion \n 2.Deletion \n 3.print \n 4.exit")
    choice=int(input("Enter Your Choice: "))
    if (choice==1):
        data=input("Enter the data: ")
        temp=Node(data)
        ssl_obj.Insertion()
        ssl_obj.printssl()
    elif(choice==2):
        ssl_obj.Deletion()
        ssl_obj.printssl()
