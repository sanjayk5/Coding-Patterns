
# Single linked list node
class SLinkedListNode:
    def __init__(self, data, next=None):
        self.data = data
        self.next = next

# Single linked list
class SLinkedList:
    def __init__(self):
        self.head = None

    # insert_node_at_beginning method will insert a Node at head of a single linked list.
    def insert_node_at_beginning(self, node):
        if self.head:
            node.next = self.head
            self.head = node
        else:
            self.head = node

    # creates single listed with given array of ints
    def create_slinked_list(self, lst):
        for x in reversed(lst):
            new_node = SLinkedListNode(x)
            self.insert_node_at_beginning(new_node)

    # returns total number of nodes in the linked list
    def get_list_length(self, head):
        temp = head
        length = 0
        while(temp):
            length += 1
            temp = temp.next
        return length
   
    
# check whether cycle exists in the single linked list
# time complexity= O(n), space = O(1)
def detect_cycle(head):
   # check if head points null
   if head is None:
       return False
   
   slow, fast = head, head
   
   while fast and fast.next:
       slow = slow.next
       fast = fast.next.next
       if slow == fast:
           return True
       
   return False

# Detect cycle in the list using hash to store unique nodes into it
# time complexity= O(n), space complexity= O(n) to store the nodes in the hash
def detect_cycle_with_hash(head):
    node_hash = set()

    while head is not None:
        # is node is already in hash, then we got the cycle in the list
        # as we are putting unique nodes in the hash
        if head in node_hash:
            return True
        
        node_hash.add(head)

        head = head.next

    return False

        
# driver code
def main():
    # create a hard coded nodes list
    # 1 -> 2 -> 3 -> 4 -> 5 -> 6
    head = SLinkedListNode(1)
    head.next = SLinkedListNode(2)
    head.next.next = SLinkedListNode(3)
    head.next.next.next = SLinkedListNode(4)
    head.next.next.next.next = SLinkedListNode(5)
    head.next.next.next.next.next = SLinkedListNode(6)

    # Creating a loop resulting in the linked list:
    # 1 -> 2 -> 3 -> 4 -> 1 -> 2 -> 3 ...
    head.next.next.next.next = head

    # if detect_cycle_with_hash(head):
    if detect_cycle(head):
        print("Cycle detected in the linked list")
    else:
        print("Cycle not detected")
        head.str()



if __name__ == '__main__':
    main()