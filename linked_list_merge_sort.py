class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, value):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = new_node

    def size(self) -> int:
        current = self.head
        count = 0
        while current:
            count += 1
            current = current.next
        return count
    
    def node_at_index(self, index: int) -> Node:
        if index == 0:
            return self.head
        current = self.head
        count = 0
        while count < index:
            current = current.next
            count += 1
        return current
    
    def add(self, value):
        new_node = Node(value)
        new_node.next = self.head
        self.head = new_node

    def __str__(self):
        values = []
        current = self.head
        while current:
            values.append(current.value)
            current = current.next
        return str(values)
    
    def __repr__(self):
        '''
        Return a string representation of the linked list
        '''
        values = []
        current = self.head
        while current:
            values.append(current.value)
            current = current.next
        return str(values)
    


def merge_sort(linked_list: LinkedList) -> LinkedList:
    '''
    Sorts a linked list in ascending order
    - Recursively divide the linked list into sublists containing a single node
    - Repeatedly merge the sublists to produce sorted sublists until one remains
    
    Returns a sorted linked list
    '''
    if linked_list.head is None or linked_list.head.next is None:
        return linked_list
    
    left_half, right_half = split(linked_list)
    left = merge_sort(left_half)
    right = merge_sort(right_half)
    
    return merge(left, right)

def split(linked_list: LinkedList) -> tuple[LinkedList, LinkedList]:
    '''
    Divide the unsorted list at midpoint into two halves
    '''
    if linked_list is None or linked_list.head is None:
        left_half = linked_list
        right_half = LinkedList()
        return left_half, right_half
    
    else:
        size = linked_list.size()
        mid = size // 2

        mid_node = linked_list.node_at_index(mid-1)
        
        # Create new linked lists for both halves
        left_half = LinkedList()
        right_half = LinkedList()
        
        # Set the heads
        left_half.head = linked_list.head
        right_half.head = mid_node.next
        
        # Break the connection
        mid_node.next = None

        return left_half, right_half
            
def merge(left, right):
    '''
    Merges two linked lists, sorting by data in nodes
    Returns a new merged list
    '''
    # Create a new linked list that contains nodes from merging left and right
    merged = LinkedList()

    # Add a fake head that is discarded later
    merged.add(0)

    # Set current to the head of the linked list
    current = merged.head

    # Obtain head nodes for left and right linked lists
    left_head = left.head
    right_head = right.head

    # Iterate over left and right until we reach the tail node of either
    while left_head or right_head:
        # If the current node on the left is None, we're past the tail
        # Add the node from right to merged linked list
        if left_head is None:
            current.next = right_head
            # Call next on right to set loop condition to False
            right_head = right_head.next
        # If the current node on the right is None, we're past the tail
        # Add the node from left to merged linked list
        elif right_head is None:
            current.next = left_head
            # Call next on left to set loop condition to False
            left_head = left_head.next
        else:
            # Not at either tail node
            # Obtain node data to perform comparison operations
            left_data = left_head.value
            right_data = right_head.value

            # If data on left is lesser than right, set current to left node
            if left_data < right_data:
                current.next = left_head
                # Move left head to next node
                left_head = left_head.next
            # If data on right is lesser than left, set current to right node
            else:
                current.next = right_head
                # Move right head to next node
                right_head = right_head.next

        # Move current to next node
        current = current.next
        
    # Discard fake head and return the next node
    head = merged.head.next
    merged.head = head
    return merged


'''
Test cases
'''
sample_list = LinkedList()
sample_list.add(10)
sample_list.add(2)
sample_list.add(44)
sample_list.add(5)
sample_list.add(63)

print(sample_list)

sorted_linked_list = merge_sort(sample_list)
print(sorted_linked_list)


