#n trie (árbol de prefijos) es una excelente opción para implementar una función de autocompletar.
#Defina los métodos que necesitará, como 'insert(word)' y 'autocomplete (prefix)'.

class TrieNode:
    def __init__(self):
        self.children = {}  # Diccionario: letra -> TrieNode
        self.is_end_of_word = False

class AutocompleteSystem:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        node = self.root
        for char in word:
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]
        node.is_end_of_word = True

    def autocomplete(self, prefix):
        node = self.root
        for char in prefix:
            if char not in node.children:
                return []  # prefijo no encontrado
            node = node.children[char]
        
        # realizar DFS desde este nodo
        results = []
        self._dfs(node, prefix, results)
        return results

    def _dfs(self, node, prefix, results):
        if node.is_end_of_word:
            results.append(prefix)
        for char, child in node.children.items():
            self._dfs(child, prefix + char, results)

############################# prueba #####################################
# para crear el sistema
ac = AutocompleteSystem()

# se einsertan las palabras
words = ["carro", "casa", "camino", "camisa", "calle", "perro", "pelo", "pelota"]
for w in words:
    ac.insert(w)

# Autocompletar
print("Sugerencias para 'ca':", ac.autocomplete("ca"))   # carro, casa, camino, camisa, calle
print("Sugerencias para 'pe':", ac.autocomplete("pe"))   # perro, pelo, pelota
print("Sugerencias para 'z':", ac.autocomplete("z"))     # []

