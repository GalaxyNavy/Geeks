

# Example 1:

# Input:
# N = 2
# LinkedList: 1->2->3->4->5->6->7->8->9
# Output: 8
# Explanation: In the first example, there
# are 9 nodes in linked list and we need
# to find 2nd node from end. 2nd node
# from end os 8.  


# Example 2:

# Input:
# N = 5
# LinkedList: 10->5->100->5
# Output: -1
# Explanation: In the second example, there
# are 4 nodes in the linked list and we
# need to find 5th from the end. Since 'n'
# is more than the number of nodes in the
# linked list, the output is -1.


# Your Task:
# The task is to complete the function getNthFromLast() which takes two arguments: reference to head and N and you need to return Nth from the end or -1 in case node doesn't exist..

# Complexity :
# Time = O(n)
# Space = O(1)




#Function to find the data of nth node from the end of a linked list
def getNthFromLast(head,n):
    #code here
    
    
    p = head
    length = 0  
   
    while p:
        length += 1
        p = p.next
        
    m = head 
    place = length-n
    
    #print(count)
    count = -1
    temp = head
    while temp:
        count  = count + 1
        
        if count ==  place :
            # print(temp.data)
            return temp.data   
            
        temp =  temp.next
        
    
    return -1
