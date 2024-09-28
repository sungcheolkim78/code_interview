class WordDictionary:
    def __init__(self):
        self.trie = {}

    def addWord(self, word: str) -> None:
        node = self.trie

        for ch in word:
            if not ch in node:
                node[ch] = {}
            node = node[ch]

        node['$'] = True

    def search(self, word: str) -> bool:
        def search_in_node(word: str, node: dict) -> bool:
            for i, ch in enumerate(word):
                if not ch in node:
                    if ch == '.':
                        for x in node:
                            if x != '$' and search_in_node(word[i+1:], node[x]):
                                return True
                    return False
                else:
                    node = node[ch]
            return '$' in node

        return search_in_node(word, self.trie)

    def __str__(self) -> str:
        def print_node(node: dict, indent: int) -> str:
            s = ''
            for ch in node:
                if ch == '$':
                    s += '$'
                else:
                    s += '\n' + ' ' * indent + ch
                    s += print_node(node[ch], indent + 2)
            return s

        return print_node(self.trie, 0)

if __name__ == '__main__':
    dictionary = WordDictionary()
    dictionary.addWord('hello')
    dictionary.addWord('world')
    dictionary.addWord('hello.world')
    print(dictionary)
    print(dictionary.search('hello'))
    print(dictionary.search('hello.world'))
    print(dictionary.search('world'))
    print(dictionary.trie)
