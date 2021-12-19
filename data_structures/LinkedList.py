# learning about linked lists, a one way array like data type that helps operations at the first index 
# think about a plates in a cupboard that are stacked on one another 


class Node:
    def __init__(self, data):
        self.data = data
        self.nextNode = None


class LinkedList:

    def __init__(self):
        # head node
        self.head = None
        self.numOfNodes = 0
    
    def __len__(self):
        return self.numOfNodes

    def insert_start(self,data):
        # increment node number
        self.numOfNodes += 1
        # instantiate new Node
        new_node = Node(data)

        # if there is a head (means not empty linked list)
        if self.head:
            # move head down one
            new_node.nextNode = self.head
        # make new node the head node
        self.head = new_node
        return

        # if not self.head:
        #     self.head = new_node
        #     return
        # new_node.nextNode = self.headx
        # self.head = new_node

    def make_new_node(self,data):
        self.numOfNodes += 1
        return Node(data)

    def traverse_node(self, current_node=None):
        if self.head is None:
            return
        if current_node is None:
            current_node = self.head
            return self.traverse_node(current_node=current_node)
        
        if current_node.nextNode is None:
            print(f'Currently at: {current_node.data}, Next up: {current_node.nextNode}...Wait so now we are at the end of linked list!')
            return
        print(f'Currently at: {current_node.data}, Next up: {current_node.nextNode.data}')
        current_node = current_node.nextNode
        return self.traverse_node(current_node)

    def insert_end(self, data):
        # DRY after first show 
        new_node = self.make_new_node(data)
        
        # if empty linked list
        if not self.head:
            # insert as head node
            self.head = new_node
            return
        
        
        # self.traverse_node()
        # # after traversing all nodes, set the nextNode as the new node
        # self.head.nextNode = new_node


        # grab the head node 
        # head_node = self.head
        
        # # if next Node is not none, assign the next node as the new node
        while head_node.nextNode is not None:
            head_node = head_node.nextNode
        
        head_node.nextNode = new_node
        # # iterate per node 
        # for node in LinkedList:
        #     # if next node ref is null, replace with new_node
        #     if not node.nextNode:
        #         node = new_node
    

    def remove(self, data, current_node=None, prev_node=None):
        # check for empty list or item not found
        if self.head is None:
            return 'Empty list or item not found'
        
        # grab head node and set prev node to none
        if current_node is None:
            current_node = self.head

        prev_node = None

        # if current node data does not equal input data, then:
        if current_node.data != data:
            # set prev_node as current node
            prev_node = current_node
            print(f'{prev_node.data}')
            # set current_node as the next node after current (traversing) and go again
            current_node = current_node.nextNode
            print(f'{current_node}')
            return self.remove(data, current_node=current_node, prev_node=prev_node)

        # if your current node data does equal your input data and your prev_node is not null
        if prev_node is not None:
            # set the previous node's next node (currentnode's position) as the currentpositions NEXT node, thus removing current node all together
            prev_node.nextNode = current_node.nextNode
            return
        # if prev node is still none, then take head node and traverse down one 
        # (usually this means there was only one node to begin with)
        # self.head = self.head.nextNode
        
        
        
        
        
        
        





linked_list = LinkedList()
linked_list.insert_start(4)
linked_list.insert_start(3)
linked_list.insert_start(7)
linked_list.insert_end(10)
# linked_list.insert_end(100)
# linked_list.insert_end(1000)

linked_list.traverse_node()
linked_list.remove(10)
linked_list.traverse_node()