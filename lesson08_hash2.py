"""
Задание 2.

Доработайте пример структуры "дерево", рассмотренный на уроке.

Предложите варианты доработки и оптимизации
(например, валидация значений узлов в соответствии
 с требованиями для бинарного дерева). При валидации приветствуется генерация
 собственного исключения

Поработайте с оптимизированной структурой,
протестируйте на реальных данных - на клиентском коде
"""


class NodeValueError(Exception):
    """Кастомное исключение для неверных значений узлов."""
    pass


class BinaryTree:
    def __init__(self, root_obj):
        self.root = root_obj
        self.left_child = None
        self.right_child = None

    def insert_left(self, new_node):
        if new_node >= self.root:
            raise NodeValueError(
                "Значение левого узла должно быть меньше значения корня")

        if self.left_child is None:
            self.left_child = BinaryTree(new_node)
        else:
            tree_obj = BinaryTree(new_node)
            tree_obj.left_child = self.left_child
            self.left_child = tree_obj

    def insert_right(self, new_node):
        if new_node <= self.root:
            raise NodeValueError(
                "Значение правого узла должно быть больше значения корня")

        if self.right_child is None:
            self.right_child = BinaryTree(new_node)
        else:
            tree_obj = BinaryTree(new_node)
            tree_obj.right_child = self.right_child
            self.right_child = tree_obj

    def get_right_child(self):
        return self.right_child

    def get_left_child(self):
        return self.left_child

    def set_root_val(self, obj):
        self.root = obj

    def get_root_val(self):
        return self.root

    def find(self, value):
        """Поиск значения в дереве."""
        if value == self.root:
            return True
        elif value < self.root and self.left_child:
            return self.left_child.find(value)
        elif value > self.root and self.right_child:
            return self.right_child.find(value)
        else:
            return False

    def delete(self, value):
        """Удаление узла с заданным значением."""
        if value < self.root:
            if self.left_child:
                self.left_child = self.left_child.delete(value)
        elif value > self.root:
            if self.right_child:
                self.right_child = self.right_child.delete(value)
        else:
            if self.left_child is None:
                return self.right_child
            if self.right_child is None:
                return self.left_child

            min_larger_node = self.right_child.find_min()
            self.root = min_larger_node.root
            self.right_child = self.right_child.delete(min_larger_node.root)

        return self

    def find_min(self):
        """Поиск минимального значения в дереве."""
        current_node = self
        while current_node.left_child:
            current_node = current_node.left_child
        return current_node

    def in_order_traversal(self):
        """Симметричный (in-order) обход дерева."""
        elements = []
        if self.left_child:
            elements += self.left_child.in_order_traversal()
        elements.append(self.root)
        if self.right_child:
            elements += self.right_child.in_order_traversal()
        return elements

    def pre_order_traversal(self):
        """Прямой (pre-order) обход дерева."""
        elements = [self.root]
        if self.left_child:
            elements += self.left_child.pre_order_traversal()
        if self.right_child:
            elements += self.right_child.pre_order_traversal()
        return elements

    def post_order_traversal(self):
        """Обратный (post-order) обход дерева."""
        elements = []
        if self.left_child:
            elements += self.left_child.post_order_traversal()
        if self.right_child:
            elements += self.right_child.post_order_traversal()
        elements.append(self.root)
        return elements


# Пример использования
r = BinaryTree(8)
print("Корень дерева:", r.get_root_val())

# Вставка узлов
r.insert_left(3)
r.insert_right(10)
r.insert_left(1)
r.insert_right(14)
r.get_right_child().insert_left(9)

# Вывод дерева в порядке in-order
print("In-order traversal:", r.in_order_traversal())

# Поиск значения
print("Поиск 9:", r.find(9))
print("Поиск 15:", r.find(15))

# Удаление узла
r.delete(10)
print("In-order traversal после удаления:", r.in_order_traversal())
