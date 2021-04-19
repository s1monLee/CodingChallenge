class Node:
    
    def __init__(self, val = -1):
        self.val = val
        self.next = None

class MyLinkedList:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.head = None
        self.size = -1

    def get(self, index: int) -> int:
        """
        Get the value of the index-th node in the linked list. If the index is invalid, return -1.
        """
        if self.size < index: return -1
        
        h = self.head
        while h:
            if index == 0:
                return h.val
            h = h.next
            index -= 1
        return -1

    def addAtHead(self, val: int) -> None:
        """
        Add a node of value val before the first element of the linked list. After the insertion, the new node will be the first node of the linked list.
        """
        self.size += 1
        
        if self.head:
            tmp = Node(val)
            tmp.next = self.head
            self.head = tmp
        else:
            self.head = Node(val)

    def addAtTail(self, val: int) -> None:
        """
        Append a node of value val to the last element of the linked list.
        """
        self.size += 1
        
        if self.head:
            h = self.head
            while h.next:
                h = h.next
            h.next = Node(val)
        else:
            self.head = Node(val)

    def addAtIndex(self, index: int, val: int) -> None:
        """
        Add a node of value val before the index-th node in the linked list. If index equals to the length of linked list, the node will be appended to the end of linked list. If index is greater than the length, the node will not be inserted.
        """
        if self.size + 1 < index: return
        if index == 0:
            self.addAtHead(val)
            return
        if self.size+1 == index:
            self.addAtTail(val)
            return
        self.size += 1
        h = self.head
        while h:
            if index == 1:
                tmp = Node(val)
                tmp.next = h.next
                h.next = tmp
                return
            h = h.next
            index -= 1
            
    def deleteAtIndex(self, index: int) -> None:
        """
        Delete the index-th node in the linked list, if the index is valid.
        """
        if not self.head or self.size < index: return
        
        h = self.head
        if not h.next:
            self.head = None
            return
        if index == 0: 
            self.head = self.head.next
            return
        
        while h.next:
            if index == 1:
                h.next = h.next.next
                return
            h = h.next
            index -= 1
        self.size -= 1

# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)
