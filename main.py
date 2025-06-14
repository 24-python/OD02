# class Stack:
#     def __init__(self):
#         self.items = []
#     def is_empty(self):
#         return self.items == []
#     def push(self, item):
#         self.items.append(item)
#     def pop(self):
#         return self.items.pop()
#     def peek(self):
#         return self.items[-1]
# stack = Stack()
# print(stack.is_empty())
# stack.push(1)
# stack.push(2)
# stack.push(3)
# print(stack.is_empty())
# print(stack.peek())

# class Queue:
#     def __init__(self):
#         self.items = []
#     def is_empty(self):
#         return self.items == []
#     def enqueue(self, item):
#         self.items.insert(0, item)
#     def dequeue(self):
#         return self.items.pop()
#         # removes the first item [5, 4, 3, 2, 1]
#         # добавляются в конец очереди, а конец очереди - это начало нашего списка.
#         # А удаление идет с конца. 1 2 3 4
#     def size(self):
#         return len(self.items)
#
# queue = Queue()
# print(queue.is_empty())
# queue.enqueue(1)
# queue.enqueue(2)
# queue.enqueue(3)
# queue.enqueue(4)
# queue.enqueue(5)
# print(queue.is_empty())
# print(queue.size())
# print(queue.dequeue())
# print(queue.size())


#Код бинарного дерева поиска

# class Node():
#     def __init__(self, key):
#         self.left = None
#         self.right = None
#         self.value = key
#
# def insert(root, key):
#     if root is None:
#         return Node(key)
#     else:
#         if root.value < key:
#             root.right = insert(root.right, key)
#         else:
#             root.left = insert(root.left, key)
#
#     return root
#
# root = Node(70)
# root = insert(root, 30)
# root = insert(root, 56)
# root = insert(root, 89)
# root = insert(root, 45)
# root = insert(root, 60)
# root = insert(root, 73)
# root = insert(root, 98)
# root = insert(root, 84)

class Graph():
    def __init__(self):
        self.graph = {}
    def addEdge(self, u, v):
        if u not in self.graph:
            self.graph[u] = []
        self.graph[u].append(v)

    def print_Graph(self):
# {0: [1, 2], 1: [0, 2], 2: [0, 1, 3], 3: [2]}
        for node in self.graph:
            print(node, "->", " -> ".join(map(str, self.graph[node])))

g = Graph()
g.addEdge(0, 1)
g.addEdge(0, 2)
g.addEdge(1, 2)
g.addEdge(2, 0)
g.addEdge(2, 3)
g.addEdge(3, 4)
g.print_Graph()

