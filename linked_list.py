class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

    def __str__(self):
        return f"({self.value}, {self.next})"

class LinkedList:
    def __init__(self, head=None):
        self.head = head

    def append(self, new_item):
        current=self.head
        if current:
            while current.next:
                current=current.next
            current.next=new_item
        else:
            self.head=new_item

    def print(self):
        current=self.head
        while current:
            print(current.value, end=" ")
            current=current.next
        print()

    def insert(self, position, new_value):
        current=self.head
        if position==0:
            new_value.next=current
            self.head=new_value
        else:
            for i in range(position-1):
                current=current.next
            new_value.next=current.next
            current.next=new_value

    def delete(self, value):
        current=self.head
        if current.value==value:
            self.head=current.next
            del current
        else:
            while current:
                if current.next.value==value:
                    del_item=current.next
                    current.next=current.next.next
                    del del_item
                    break
                else:
                    current=current.next



#my_data = LinkedList()
#my_data.append(Node(3))
#my_data.append(Node(5))
#my_data.insert(1, Node(20))
#my_data.insert(1, Node(30))
#my_data.insert(3, Node(34))
#my_data.insert(0, Node(1))
#my_data.insert(1, Node(12))
#my_data.print()
#my_data.delete(1)
#my_data.print()
