class TrieNode:
    def __init__(self, char: str = "") -> None:
        self.char: str = char
        self.children: list = [None] * 26
        self.is_end_of_word: bool = False
        self.score: int = 0


class Trie:
    def __init__(self) -> None:
        self.root = TrieNode("")

    def char_to_index(self, char: str) -> int:
        # Function to convert a character to an index
        return ord(char) - ord("a")

    def insert(self, word: str) -> None:
        node: TrieNode = self.root

        for char in word:
            index: int = self.char_to_index(char)
            # If node doesn't exist
            if node.children[index] is None:
                node.children[index] = TrieNode(char)
                node = node.children[index]
            else:
                node = node.children[index]

        node.is_end_of_word = True
        node.score += 1

    def dfs(self, node: TrieNode, partial: str) -> None:
        # DFS pre-order traversal
        if node.is_end_of_word is True:
            self.output.append((partial + node.char, node.score))

        for child in node.children:
            if child:
                self.dfs(child, partial + node.char)

    def find(self, prefix: str) -> list:
        node: TrieNode = self.root
        self.output: list = []

        for char in prefix:
            index = self.char_to_index(char)
            if not node.children[index]:
                return []
            else:
                node = node.children[index]
        self.dfs(node, prefix[:-1])

        return sorted(self.output, key=lambda x: x[1], reverse=True)

    def hasChildren(self, node):
        for child in node.children:
            if child:
                return True
        return False

    def delete_node(self, node, word) -> bool:
        if not node:
            return False
        if not word:
            return False

        index = self.char_to_index(word[0])
        node = node.children[index]

        if len(word) == 1:
            if node.is_end_of_word:
                node.is_end_of_word = False
                if self.hasChildren(node):
                    return True
                else:
                    node = None
                    return True

        return self.delete_node(node, word[1:])

    def delete(self, word: str) -> bool:
        node: TrieNode = self.root
        result: bool = False

        if not node:
            return None
        # Delete a word
        result = self.delete_node(node, word)
        return result
