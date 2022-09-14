class Solution:
    
    def add_first(self, head, x) :
        if head :
            new = Node(x)
            new.next = head
            head = new
        else:
            head = Node(x)
            head.next = None
        
        
        return head
        
        
        # print(head.data)
        
   
    #Function to add two numbers represented by linked list.
    
    
    def reverse(self, head):
        prev = None
        succ = head
        
        while head :
            
            
            succ = head.next
            head.next = prev
            prev =  head
            head = succ
            
        
        head = prev
        return head
        
    
    def addTwoLists(self, first, second):
        # code here
        # return head of sum list
        add_list = 0

        # head1 = first
        # head2 = second
        # add_list =Node(0)
        l = []
        
        reverse_one = self.reverse(first)
        
        reverse_sec =  self.reverse(second)
        
        
    
        p1 = reverse_one
        p2 =reverse_sec
        carry = 0
        while p1 or p2 :   
            
            s = 0
            
            if p1:
                
                s += p1.data
            if p2:
                s  +=  p2.data
            
            s = s +carry
            
            carry  = int(s/10)
            s =int(s%10)
            
            
            add_list = self.add_first(add_list, s)
        
            if p1:
                p1 = p1.next
            
            
            if p2:
                p2 = p2.next
                
            
        if carry:
            
            add_list = self.add_first(add_list, carry)
        
        
         
        
        return add_list
        
