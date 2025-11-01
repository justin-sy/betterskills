class Node:
    def __init__(self,val = 0,next = None):
        self.val = val
        self.next = next

class linked_list:
    def __init__(self,head = None):
        self.head = head

    def generate(self,input_list):
        '''
        Generates a linked list with node values corresponding to values in a given list
        '''

        result = Node()
        head = result
        for num in input_list:
            head.next = Node(num)
            head = head.next
        return result.next
    
    def insert(self,head,index:int,val:int):
        '''
        Inserts a node into linked list at given index with given value
        '''

        # If head does not exist
        if not head:
            return None
        
        # If index is 0     
        if index < 1:
            return Node(val,head)
        
        # If index is greater than 0
        result = head
        for i in range(index-1):
            # Exit for loop when end of list is reached
            if not head.next:
                break
            head = head.next
            
        head.next = Node(val,head.next)
        return 
    
    def delete(self,head,index:int):
        '''
        Deletes the node in a linked list at given index
        '''

        # If head does not exist or is one node
        if not head or not head.next:
            return None
        
        # If index is 0
        if index < 1:
            return head.next

        # If index is greater than 0
        result = head
        for i in range(index-1):
            # Exit for loop when there is one node ahead left
            if not head.next.next:
                break
            head = head.next
        
        if head.next:
            head.next = head.next.next
        return result
    
    def update(self,head,index:int,val:int):
        '''
        Updatese the node in a linked list at a given index with a given value
        '''

        result = head
        for i in range(index):
            # Exits for loop if end of linked list is reached
            if not head.next:
                break
            head = head.next
        head.val = val
        return result
    
    def print_list(self,head):
        '''
        Prints the value of every node in a linked list
        '''

        node = head
        while node:
            print(node.val)
            node = node.next
        return
    
    def reverse(self,head):
        '''
        Reverses the order of the nodes in a linked list
        '''

        node = None
        while head:
            next = head.next
            head.next = node
            node = head
            head = next
        return node
