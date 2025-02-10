class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def is_empty(self):
        return self.head is None

    def push(self,data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def append(self,data):
        if self.is_empty():
            self.push(data)
        else:
            new_node = Node(data)
            node = self.head
            while node.next:
                node = node.next
            node.next = new_node

    def delete_first(self):
        if (self.head == None):
            return
        temp = self.head
        self.head = temp.next
        temp = None

    def find(self,data_search):
        node = self.head
        while node:
            if node.data == data_search:
                return node
            node = node.next
        return 'N A N'

    def delete_after(self, node):
        tmp = node.next
        node.next = tmp.next
        tmp = None

    def __str__(self):
        arr = ['head']
        node = self.head
        while node:
            arr.append(f"{node.data}")
            node = node.next
        arr.append("NULL")
        str = ' -> ' .join(arr)
        return str



    def length(self):
        if self.is_empty():
            return 'the list is empty'
        node = self.head
        counter = 1
        while node:
            if node.next == None:
                return counter
            else:
                counter += 1
            node = node.next

    def find_index(self,idx):
        if self.is_empty():
            return 'the list is empty'
        node = self.head
        counter = 0
        while node:
            if idx == counter:
                return node.data
            else:
                counter += 1
            node = node.next

    def sum_value(self):
        sum = 0
        node = self.head
        while node:
            sum += node.data
            node = node.next
        return sum

    def thread(self,l_l):
        pass


list4 = LinkedList()
list3 = LinkedList()
list3.push(5)
list4.append(1)
list4.append(2)
list4.append(3)
list4.append(4)
# list4.delete_after(list4.find(2))
print(list4.find(2))
print(list3.length())
print(list4.sum_value())
print(list4.find_index(2))
print(list4)
print(list3)