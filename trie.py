'''문자열 처리의 가장 좋은방법중 하나인
Trie구조.
Trie는 검색을 뜻하는 retrieval 에서 온 단어임.
Tree와 혼동을피하기위해서 Trie로 씀 ㅋㅋ
어떤 문자열을 검색할 때의 시간 복잡도는 항상 O(m)밖에 안됨. m:문자열의 최대 길이
'''
#python을 통한 구현

#1. Node 구현
class Node(object):
    """
    A single node of a trie.
    
    Children of nodes are defined in a dictionary
    where each (key, value) pair is in the form of
    (Node.key, Node() object).
    """
    def __init__(self, key, data=None):
        self.key = key
        self.data = data # data is set to None if node is not the final char of string
        self.children = {}

#2. Trie 구현
#2-1. insert(string) : 트라이에 문자열 삽입
#2-2. search(string) : 주어진 단어 string이 트라이에 존재하는지 여부 반환
#2-3. starts_with(prefix) : 주어진 prefix로 시작하는 단어들을 BFS로 트라이에서 찾아 리스트 형태로 반환

class Trie(object):
    """
    A simple Trie with insert, search, and starts_with methods.
    """
    def __init__(self):
        self.head = Node(None)
    
    """
    Inserts string in the trie.
    """
    def insert(self, string):
        curr_node = self.head
        
        for char in string:
            if char not in curr_node.children:
                curr_node.children[char] = Node(char)
                
            curr_node = curr_node.children[char]
            
        # When we have reached the end of the string, set the curr_node's data to string.
        # This also denotes that curr_node represents the final character of string.
        curr_node.data = string
    
    
    """
    Returns if string exists in the trie
    """
    def search(self, string):
        curr_node = self.head
        
        for char in string:
            if char in curr_node.children:
                curr_node = curr_node.children[char]
            else:
                return False
            
        # Reached the end of string,
        # If curr_node has data (i.e. curr_node is not None), string exists in the trie
        if (curr_node.data != None):
            return True
    
    """
    Returns a list of words in the trie
    that starts with the given prefix.
    """
    def starts_with(self, prefix):
        curr_node = self.head
        result = []
        subtrie = None
        
        # Locate the prefix in the trie,
        # and make subtrie point to prefix's last character Node
        for char in prefix:
            if char in curr_node.children:
                curr_node = curr_node.children[char]
                subtrie = curr_node
            else:
                return None
            
        # Using BFS, traverse through the prefix subtrie,
        # and look for nodes with non-null data fields.
        queue = list(subtrie.children.values())
        
        while queue:
            curr = queue.pop()
            if curr.data != None:
                result.append(curr.data)
            
            queue += list(curr.children.values())
                
        return result

'''
출처 : https://blog.ilkyu.kr/entry/%ED%8C%8C%EC%9D%B4%EC%8D%AC%EC%97%90%EC%84%9C-Trie-%ED%8A%B8%EB%9D%BC%EC%9D%B4-%EA%B5%AC%ED%98%84%ED%95%98%EA%B8%B0
'''