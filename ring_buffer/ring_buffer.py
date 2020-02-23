from doubly_linked_list import DoublyLinkedList


class RingBuffer:
    def __init__(self, capacity):
        self.capacity = capacity
        self.current_node = None
        self.storage = DoublyLinkedList()

    def append(self, item):

        if self.capacity > self.storage.__len__(): 
            self.storage.add_to_head(item)
        else:
            self.storage.remove_from_tail()
            self.storage.add_to_head(item)

  # pseudocode 
        # if the len of the storgae is less then the capacity of the linked list  
        # then we're going to access storage and add item to tail 
        # then we are going to asign the current node to be at the tail of the linked list


    def get(self):
        # Note:  This is the only [] allowed
        list_buffer_contents = []
        num = 0

        while num < self.storage.__len__(): # create a loop saying while num is less then the storage it will exicute the code below
            current_head = self.storage.head # created a varible and assigned it the head node of storage
            list_buffer_contents.append(current_head.value) # adds new node to the list_buffer_contents list
            self.storage.move_to_end(current_head) # moves the current head to the beack of the list
            num += 1 # grow by one


        return list_buffer_contents

        

# ----------------Stretch Goal-------------------


class ArrayRingBuffer:
    def __init__(self, capacity):
        pass

    def append(self, item):
        pass

    def get(self):
        pass
