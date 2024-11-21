class Node:
    def __init__(self, val = 0, next_node=None):
        self.value = val
        self.nextNode = next_node

    def printNode(self):
        if self.hasValue():
            print("element: {}".format(self.value))

    def setNext(self, node):
        self.nextNode = node
    
    def hasNext(self):
        return self.nextNode != None

    def hasValue(self):
        return self.value != 0

    
class LinkedList:    
    def __init__(self):
        self.head = Node()
        self.tail = Node()
        self.length = 0
        
    def printNodes(self):
        if self.length == 0:
            print("List is empty")
        else:
            print("Printing linkedList: ")

        temp = self.head
        while temp:
            temp.printNode()
            if temp.hasNext():
                temp = temp.nextNode
            else:
                break

    
    def getLastNode(self):
        temp = self.head
        while temp.hasNext():
            temp = temp.nextNode;

        return temp

    def appendValue(self, val):
        temp = self.head
        node = Node(val)

        self.getLastNode().nextNode = node
        self.length += 1

    # just to properly update length counter
    # instead of list.head = value
    # use this so length counter is also updated properly
    def attachNodes(self, node):
        self.head = node
        while node:
            node = node.nextNode
            self.length += 1
        
    def isEmpty(self):
        return self.head.nextNode == None

    def isNotEmpty(self):
        return self.head.nextNode != None
    
    def getLength(self):
        print(self.length)
   
    
def addTwoLinkedList(list1, list2):
    ans = LinkedList()

    temp = node = Node()  # 0 node

    while list1 and list2:
        if list1.value < list2.value:
            node.nextNode = list1
            list1 = list1.nextNode

        else:
            node.nextNode = list2
            list2 = list2.nextNode

        node = node.nextNode

    node.nextNode = list1 or list2

    # Below line will work but wouldn't update length, thus use attachNodes()
    #ans.head = temp.nextNode
    
    ans.attachNodes(temp.nextNode)
    return ans


list1 = LinkedList()

list1.appendValue(1)
list1.appendValue(2)
list1.appendValue(4)
list1.printNodes()

list2 = LinkedList()
list2.appendValue(1)
list2.appendValue(3)
list2.appendValue(5)
list2.printNodes()


merged = addTwoLinkedList(list1.head, list2.head)
merged.printNodes()
