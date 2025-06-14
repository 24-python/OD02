# Определение класса Node (узел дерева)
class Node():
    # Конструктор узла
    def __init__(self, key):
        self.left = None    # Левый потомок (изначально отсутствует)
        self.right = None   # Правый потомок (изначально отсутствует)
        self.value = key    # Значение узла

# Функция вставки нового значения в дерево
def insert(root, key):
    # Если текущий узел пуст - создаем новый узел
    if root is None:
        return Node(key)
    else:
        # Если вставляемое значение больше текущего - идем в правое поддерево
        if root.value < key:
            root.right = insert(root.right, key)
        # Иначе - в левое поддерево
        else:
            root.left = insert(root.left, key)
    return root  # Возвращаем измененное дерево

# Функция красивого вывода дерева
def print_tree(root, level=0, prefix="Root: "):
    if root is not None:
        # Вывод текущего узла с отступами согласно его уровню
        print(" " * (level * 4) + prefix + str(root.value))
        # Рекурсивный вывод левого и правого поддеревьев
        if root.left or root.right:
            print_tree(root.left, level + 1, "L--- ")
            print_tree(root.right, level + 1, "R--- ")

# Функция обхода дерева in-order (левый-корень-правый)
def in_order_traversal(root):
    if root:
        in_order_traversal(root.left)   # Сначала левое поддерево
        print(root.value, end=" ")     # Затем значение текущего узла
        in_order_traversal(root.right) # Затем правое поддерево

# ===== Создание и наполнение дерева =====
root = Node(70)         # Создаем корень со значением 70
root = insert(root, 30) # Вставляем остальные значения
root = insert(root, 56)
root = insert(root, 89)
root = insert(root, 45)
root = insert(root, 60)
root = insert(root, 73)
root = insert(root, 98)
root = insert(root, 84)

# ===== Вывод результатов =====
print("Бинарное дерево поиска:")
print_tree(root)  # Визуализация структуры дерева

print("\nIn-order обход (сортированный):")
in_order_traversal(root)  # Вывод значений в отсортированном порядке