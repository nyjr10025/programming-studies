

class Node:
    
    def __init__(self, data):
        self.data = data
        self.next = None
        self.previous = None



class DoublyLinkedList:

    def __init__(self):
        self.numOfNodes = 0
        self.head = None
        self.tail = None

    # insert at end 
    def append(self, data):

        new_node = Node(data)
        #  when list is empty
        if self.head is None:
            # head and tail are the new node
            self.head = new_node
            self.tail = new_node
        # one item in the data structure, keep inserting at the end of list
        else:
            # take the new_node, set the tail node behind it
            new_node.previous = self.tail 
            # set the tail node next pointer to new node
            self.tail.next = new_node
            # set the tail node as the new node
            self.tail = new_node
        return
    

    # def traverse(self, direction='forward'):
    #     current_node = self.head
    #     while current_node is not None:
    #         print(f'{current_node.data}')
    #         if direction != 'forward':
    #             current_node = current_node.previous
    #         else:
    #             current_node = current_node.next


    def traverse_forward(self):
        #  take the head node
        actual_node = self.head
        # while current node is not none 
        while actual_node is not None:
            print(f'{actual_node.data}')
            # set the current node as the next node until none
            actual_node = actual_node.next

    
    def traverse_backwards(self):
        # set the current node as the tail node
        actual_node = self.tail
        
        while actual_node is not None:
            print(f'{actual_node.data}')
            # set the current node to the previous node until none 
            actual_node = actual_node.previous

if __name__ == "__main__":

    linked_list = DoublyLinkedList()
    linked_list.append(1)
    linked_list.append(2)
    linked_list.append(3)

    linked_list.traverse_forward()
    linked_list.traverse_backwards()
     

        
        
        
