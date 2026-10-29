class node:
    def __init__(self,data):
        self.data = data
        self.next=None
        
first=node(10)
print(first.data)
print(first.next)

second = node(20)
first.next = second
head=first

newnode=node(5)
newnode.next=head
head=newnode
def insert_at_end(head, value):
    new_node = Node(value)

    if head is None:
        return new_node

    current = head

    while current.next is not None:
        current = current.next

    current.next = new_node
    return head

print(insert_at_end(head, 30).data)
