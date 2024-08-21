"""
Задание 1.

Реализуйте кодирование строки по алгоритму Хаффмана.
У вас два пути:
1) тема идет тяжело? тогда вы можете,
опираясь на примеры с урока, сделать свою версию алгоритма
Разрешается и приветствуется изменение имен переменных,
выбор других коллекций, различные изменения
и оптимизации.

2) тема понятна? постарайтесь сделать свою реализацию.
Вы можете реализовать задачу, например,
через ООП или предложить иной подход к решению.
"""
import heapq
from collections import defaultdict


class HuffmanNode:
    def __init__(self, char, freq):
        self.char = char      # символ
        self.freq = freq      # частота символа
        self.left = None      # левый потомок
        self.right = None     # правый потомок

    # для работы с heapq
    def __lt__(self, other):
        return self.freq < other.freq


class HuffmanCoding:
    def __init__(self, data):
        self.data = data
        self.heap = []
        self.codes = {}
        self.reverse_mapping = {}

    def build_frequency_dict(self):
        frequency = defaultdict(int)
        for char in self.data:
            frequency[char] += 1
        return frequency

    def build_heap(self, frequency):
        for char, freq in frequency.items():
            node = HuffmanNode(char, freq)
            heapq.heappush(self.heap, node)

    def build_huffman_tree(self):
        while len(self.heap) > 1:
            node1 = heapq.heappop(self.heap)
            node2 = heapq.heappop(self.heap)

            merged = HuffmanNode(None, node1.freq + node2.freq)
            merged.left = node1
            merged.right = node2

            heapq.heappush(self.heap, merged)

        return heapq.heappop(self.heap)

    def build_codes_helper(self, root, current_code):
        if root is None:
            return

        if root.char is not None:
            self.codes[root.char] = current_code
            self.reverse_mapping[current_code] = root.char
            return

        self.build_codes_helper(root.left, current_code + "0")
        self.build_codes_helper(root.right, current_code + "1")

    def build_codes(self):
        root = self.build_huffman_tree()
        self.build_codes_helper(root, "")

    def get_encoded_data(self):
        encoded_data = ""
        for char in self.data:
            encoded_data += self.codes[char]
        return encoded_data

    def encode(self):
        frequency = self.build_frequency_dict()
        self.build_heap(frequency)
        self.build_codes()
        return self.get_encoded_data()

    def decode(self, encoded_data):
        current_code = ""
        decoded_data = ""

        for bit in encoded_data:
            current_code += bit
            if current_code in self.reverse_mapping:
                character = self.reverse_mapping[current_code]
                decoded_data += character
                current_code = ""

        return decoded_data


# Пример использования
data = "hello huffman"
huffman = HuffmanCoding(data)

encoded_data = huffman.encode()
print(f"Encoded data: {encoded_data}")

decoded_data = huffman.decode(encoded_data)
print(f"Decoded data: {decoded_data}")


'''
Пример работы:
Исходная строка: "hello huffman"
Закодированная строка: 1100101010110000111010011101011110010000
Декодированная строка: "hello huffman"
'''
