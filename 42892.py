import sys
sys.setrecursionlimit(1000000)

class Node():
    def __init__(self,key,x):
        self.key=key
        self.x=x
        self.left=None
        self.right=None

class tree():
    def __init__(self):
        self.head=None
        self.pre_result=list()
        self.post_result=list()
        
    def insert(self,key,x):
        curr_node=self.head
        if self.head is None:
            self.head=Node(key,x)
        else:
            while True:
                if curr_node.x > x:
                    if curr_node.left:
                        curr_node=curr_node.left
                    else:
                        curr_node.left=Node(key,x)
                        break
                else:
                    if curr_node.right:
                        curr_node=curr_node.right
                    else:
                        curr_node.right=Node(key,x)
                        break

    def preorder(self):
        def _preorder(root):
            if root is None:
                pass
            else:
                self.pre_result.append(root.key)
                _preorder(root.left)
                _preorder(root.right)
        _preorder(self.head)
    
    def postorder(self):
        def _postorder(root):
            if root is None:
                pass
            else:
                _postorder(root.left)
                _postorder(root.right)
                self.post_result.append(root.key)
        _postorder(self.head)


def solution(nodeinfo):
    answer = [[]]
    for i in range(len(nodeinfo)):
        nodeinfo[i].append(i+1)
    nodeinfo_sort=sorted(nodeinfo,key=lambda x:(-x[1],x[0]))
    print(nodeinfo_sort)
    t=tree()
    for node in nodeinfo_sort:
        t.insert(node[-1],node[0])
    t.preorder()
    t.postorder()
    return [t.pre_result,t.post_result]

'''
배웠던 Trie의 숫자버전
Tree를 알고있느냐가 문제의 광건이였던 것 같다.
물론 알고있었지만, 어떤식으로 설계해야 할지가 너무나도 막막했다. 이전에 Trie구조로 문자열을 저장하는 방법은 배웠었지만, 이것을 응용해서 해보려니 너무나 달랐다. 
이것도 잘 응용해서 다른문제를 풀수있도록 기억해봐야겠다.
'''