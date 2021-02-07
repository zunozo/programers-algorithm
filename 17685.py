17685 자동완성

trie

from collections import deque
class Node(object):
    def __init__(self,key,data=None):
        self.data=data
        self.key=key
        self.possible_word=0
        self.children={}

class Trie(object):
    def __init__(self):
        self.head=Node(None)

    def insert(self,string):
        curr_node = self.head
        for char in string:
            curr_node.possible_word+=1
            if char not in curr_node.children:
                curr_node.children[char]=Node(char)
            curr_node=curr_node.children[char]
        curr_node.data=string
        curr_node.possible_word+=1

    def search(self,string):
        curr_node = self.head

        for char in string:
            if char in curr_node.children:
                curr_node=curr_node.children[char]
            else:
                return False
        if curr_node.possible_word==1:
            return True
        return False


def solution(words):
    answer = 0
    t=Trie()
    for word in words:
        t.insert(word)
    count=0
    for word in words:
        allready_find=False
        for i in range(1,len(word)+1):
            if t.search(word[:i]):
                count+=i
                allready_find=True
                break
        if not allready_find:
            count+=len(word)
    return count

'''
trie를 처음이용해봤는데, 우선 알게된사실은 init에 대한 기본이 부족해서, class가 처음 실행되어질때, 초기화된다는것을 몰랐다는것이다. 그래서 이러한 실수가 나왔다.
code내에서 
if char not in curr_node.children:
                curr_node.children[char]=Node(char)
            curr_node=curr_node.children[char]
이러한 부분이 있었는데, curr_node=Node(char)로 쓰는게 더 짧은거 아니야? 해서 값을 확인해봤는데 원하는데로 안나와서 보니, 값이 초기화가 되고있던것이다.. 이제는 __init__에 대해서 헷갈려하지 않아야지!
그리고 다른방식도 있겠지만, 각 node를 지나올때마다 Node의 possible_word에 가능한 개수를 저장하는 식으로했는데, 이게 최선인지는 잘 모르겠다. 더좋은방법이 있을것도같은데..
사실 문자열 Algorithm인  kmp, trie에 대한 두려움이 많았었는데, 이번기회로 trie에대해서 두려움은 조금이나마 사라진것같아 기분이좋다.
'''