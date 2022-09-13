



class Solution:
    #Function to sort a linked list of 0s, 1s and 2s.
    def segregate(self, head):
        #code here
        
        pointer = head

        value = []
        while pointer:
            value.append(pointer.data)
            
            pointer = pointer.next
        v = sorted(value)
        new = head
        new_head = new
        
        for i in v:
            new.data = i
            new = new.next
            
            
        return new_head
            
        
        
