from doubly_linked_list import DoublyLinkedList


class RingBuffer:
    def __init__(self, capacity):
        self.capacity = capacity
        self.current_node = None
        self.storage = DoublyLinkedList()

    def append(self, item):
    # pseudocode 
        # if the len of the storgae is qual to the capacity of the linked list  
        # then we are going to return  
            # if item is < self.capacity  
                # self.storage.add_to_tail(item)
            # else:  
                # slef.storage.remove_from_head() # assuming overwritten with the newest element measns remove.


        #  if storage lengths is equal to the capacity 

        if self.storage.length < self.capacity:
             self.storage.add_to_tail(item)
             self.current_node = self.storage.tail
        if self.storage.length == self.capacity:
            self.current_node.value = item
            if self.current_node is self.storage.tail:
                self.current_node = self.storage.head


    def get(self):
        # Note:  This is the only [] allowed
        list_buffer_contents = []

        # TODO: self.sotr

        return list_buffer_contents

# ----------------Stretch Goal-------------------


class ArrayRingBuffer:
    def __init__(self, capacity):
        pass

    def append(self, item):
        pass

    def get(self):
        pass
