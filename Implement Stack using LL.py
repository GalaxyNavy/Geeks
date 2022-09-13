
class StackNode:

# Constructor to initialize a node
    def __init__(self, data):
        self.data = data
        self.next = None
    



class MyStack:

#     to Create linked list
    def __init__(self) :
        self.head = None
    
    
    def push(self, data):
        top = self.head
        Node = StackNode(data)
        if self.head == None :
            self.head = Node
            top = self.head
    
        else :
            
            Node.next = self.head
            self.head = Node
            top = self.head
            
        
        # print(top.data)
       


    #Function to remove an item from top of the stack.
    def pop(self):

        # Add code here
        if   self.head  ==  None :
            return -1
            
            
        
            
        
        
        
        top = self.head
        item =  self.head.data
        top = top.next
        self.head= top
       
 
        return item
