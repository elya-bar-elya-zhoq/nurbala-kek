# Uteulin Ilyas, Serebrennikov Kirill, Darisheva Elvira
"""
Part #1

import collections
vocab_freqs = collections.defaultdict(int)

with open("text.txt") as f_in:
    for line in f_in:
        for char in line:
            vocab_freqs[char] += 1
total = float(sum(vocab_freqs.values()))
probs = [(count / total, char) for char, count in vocab_freqs.items()]
print(probs)
"""

#Извините, у нас стоит оценка 85 за первую часть, Эльвира не предупредила, что писала на 2.7 версии,
#сейчас мы переписали на версии 3.7 или проблема была в другом? Если проблема была в конфликте версий,
#не могли бы вы тогда поменять оценку?





#Part 2

# from collections import Counter
# from queue import PriorityQueue

# class HuffmanNode:
#     def __init__(self, char, freq=0, left=None, right=None):
#         self.char = char
#         self.freq = freq
#         self.left = left
#         self.right = right

#     def __lt__(self, other):
#         return self.freq < other.freq


# def encode(text):

#     frequencies = Counter(text)
#     queue = PriorityQueue()
#     code_table = {}

#     for char, f in frequencies.items():
#         queue.put(HuffmanNode(char, f))

#     while queue.qsize() > 1:
#         l, r = queue.get(), queue.get()
#         queue.put(HuffmanNode(None, l.freq + r.freq, l, r))

#     huffman_tree = queue.get()

#     _fill_code_table(huffman_tree, "", code_table)

#     encoded_text_code = ""
#     for c in text:
#         encoded_text_code += code_table[c]

#     encoded_tree_code = _encode_huffman_tree(huffman_tree, "")

#     num = 8 - (len(encoded_text_code) + len(encoded_tree_code)) % 8
#     if num != 0:
#         encoded_text_code = num * "0" + encoded_text_code

#     print(f"frequencies: {frequencies}")
#     print(f"encoded text code: {encoded_text_code}")

#     return f"{encoded_tree_code}{num:08b}{encoded_text_code}"


# def decode(encoded_text):

#     encoded_text_ar = list(encoded_text)
#     encoded_tree = _decode_huffman_tree(encoded_text_ar)

#     number_of_extra_0_bin = encoded_text_ar[:8]
#     encoded_text_ar = encoded_text_ar[8:]
#     number_of_extra_0 = int("".join(number_of_extra_0_bin), 2)
#     encoded_text_ar = encoded_text_ar[number_of_extra_0:]

#     text = ""
#     current_node = encoded_tree
#     for char in encoded_text_ar:
#         current_node = current_node.left if char == '0' else current_node.right

#         if current_node.char is not None:
#             text += current_node.char
#             current_node = encoded_tree
#     return text


# def decompress(input_path, output_path):

#     with open(input_path, "rb") as in_file, open(output_path, "w") as out_file:
#         encoded_text = ""

#         byte = in_file.read(1)
#         while len(byte) > 0:
#             encoded_text += f"{bin(ord(byte))[2:]:0>8}"
#             byte = in_file.read(1)

#         decoded_text = decode(encoded_text)
#         out_file.write(decoded_text)


# def compress(input_path, output_path):

#     with open(input_path) as in_file, open(output_path, "wb") as out_file:
#         text = in_file.read()
#         encoded_text = encode(text)

#         b_arr = bytearray()
#         for i in range(0, len(encoded_text), 8):
#             b_arr.append(int(encoded_text[i:i+8], 2))

#         out_file.write(b_arr)


# def _fill_code_table(node, code, code_table):

#     if node.char is not None:
#         code_table[node.char] = code
#     else:
#         _fill_code_table(node.left, code + "0", code_table)
#         _fill_code_table(node.right, code + "1", code_table)


# def _encode_huffman_tree(node, tree_text):

#     if node.char is not None:
#         tree_text += "1"
#         tree_text += f"{ord(node.char):08b}"
#     else:
#         tree_text += "0"
#         tree_text = _encode_huffman_tree(node.left, tree_text)
#         tree_text = _encode_huffman_tree(node.right, tree_text)

#     return tree_text


# def _decode_huffman_tree(tree_code_ar):
#     code_bit = tree_code_ar[0]
#     del tree_code_ar[0]

#     if code_bit == "1":
#         char = ""
#         for _ in range(8):
#             char += tree_code_ar[0]
#             del tree_code_ar[0]

#         return HuffmanNode(chr(int(char, 2)))

#     return HuffmanNode(None, left=_decode_huffman_tree(tree_code_ar), right=_decode_huffman_tree(tree_code_ar))



# if __name__ == "__main__":
#     file_to_compress, decompressed, compressed = "text.txt", "decompressed", "compressed"
#     compress(file_to_compress, compressed)
#     decompress(compressed, decompressed)

#Part 3

from collections import Counter
from queue import PriorityQueue

class HuffmanNode:
    def __init__(self, char, freq=0, left=None, right=None):
        self.char = char
        self.freq = freq
        self.left = left
        self.right = right

    def __lt__(self, other):
        return self.freq < other.freq


def encode(text):

    frequencies = Counter(text)
    queue = PriorityQueue()
    code_table = {}

    for char, f in frequencies.items():
        queue.put(HuffmanNode(char, f))

    while queue.qsize() > 1:
        l, r = queue.get(), queue.get()
        queue.put(HuffmanNode(None, l.freq + r.freq, l, r))

    huffman_tree = queue.get()

    _fill_code_table(huffman_tree, "", code_table)

    encoded_text_code = ""
    for c in text:
        encoded_text_code += code_table[c]

    encoded_tree_code = _encode_huffman_tree(huffman_tree, "")

    num = 8 - (len(encoded_text_code) + len(encoded_tree_code)) % 8
    if num != 0:
        encoded_text_code = num * "0" + encoded_text_code

    print(f"frequencies: {frequencies}")
    print(f"encoded text code: {encoded_text_code}")

    return f"{encoded_tree_code}{num:08b}{encoded_text_code}"


def decode(encoded_text):

    encoded_text_ar = list(encoded_text)
    encoded_tree = _decode_huffman_tree(encoded_text_ar)

    number_of_extra_0_bin = encoded_text_ar[:8]
    encoded_text_ar = encoded_text_ar[8:]
    number_of_extra_0 = int("".join(number_of_extra_0_bin), 2)
    encoded_text_ar = encoded_text_ar[number_of_extra_0:]

    text = ""
    current_node = encoded_tree
    for char in encoded_text_ar:
        current_node = current_node.left if char == '0' else current_node.right

        if current_node.char is not None:
            text += current_node.char
            current_node = encoded_tree

    print(f"decode text: {text}")
    return text


def decompress(input_path, output_path):

    with open(input_path, "rb") as in_file, open(output_path, "w") as out_file:
        encoded_text = ""

        byte = in_file.read(1)
        while len(byte) > 0:
            encoded_text += f"{bin(ord(byte))[2:]:0>8}"
            byte = in_file.read(1)

        decoded_text = decode(encoded_text)
        out_file.write(decoded_text)


def compress(input_path, output_path):

    with open(input_path) as in_file, open(output_path, "wb") as out_file:
        text = in_file.read()
        encoded_text = encode(text)

        b_arr = bytearray()
        for i in range(0, len(encoded_text), 8):
            b_arr.append(int(encoded_text[i:i+8], 2))

        out_file.write(b_arr)


def _fill_code_table(node, code, code_table):

    if node.char is not None:
        code_table[node.char] = code
    else:
        _fill_code_table(node.left, code + "0", code_table)
        _fill_code_table(node.right, code + "1", code_table)


def _encode_huffman_tree(node, tree_text):

    if node.char is not None:
        tree_text += "1"
        tree_text += f"{ord(node.char):08b}"
    else:
        tree_text += "0"
        tree_text = _encode_huffman_tree(node.left, tree_text)
        tree_text = _encode_huffman_tree(node.right, tree_text)

    return tree_text


def _decode_huffman_tree(tree_code_ar):
    code_bit = tree_code_ar[0]
    del tree_code_ar[0]

    if code_bit == "1":
        char = ""
        for _ in range(8):
            char += tree_code_ar[0]
            del tree_code_ar[0]

        return HuffmanNode(chr(int(char, 2)))

    return HuffmanNode(None, left=_decode_huffman_tree(tree_code_ar), right=_decode_huffman_tree(tree_code_ar))



if __name__ == "__main__":
    file_to_compress, decompressed, compressed = "text.txt", "decompressed", "compressed"
    compress(file_to_compress, compressed)
    decompress(compressed, decompressed)
