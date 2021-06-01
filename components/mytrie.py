'''
bare implementation of Trie tree. this implementation is use case specific. 
'''

_end = '_end_'

class MyTrie():

    def __init__(self, *words):
        self.root = dict()
        self.make_trie(*words)
    
    def make_trie(self, *words):
        for word in words:
            self.insert(word)
        return self.root

    def in_trie(self, word, root=None):
        current_dict = root or self.root
        for letter in word:
            if letter not in current_dict:
                return False
            current_dict = current_dict[letter]
        return _end in current_dict
        # return True

    def insert(self, word, root=None):
        current_dict = root or self.root
        for letter in word:
            current_dict = current_dict.setdefault(letter, {})
            if _end in current_dict:
                current_dict.pop(_end)
        current_dict[_end] = _end

    def path_until_fork(self, root=None):
        current_dict = root or self.root
        word = ''
        while _end not in current_dict:
            if len(current_dict) > 1:
                break
            else:
                letter = list(current_dict.keys())[0]
                word += letter
                current_dict = current_dict[letter]
        return word

    def common_prefixes(self) -> list:
        root = self.root
        l = []
        for letter in root.keys():
            l.append( letter + self.path_until_fork(root[letter]) )
        return l