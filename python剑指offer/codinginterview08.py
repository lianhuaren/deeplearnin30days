#coding=utf-8

# //==================================================================
# // 《剑指Offer——名企面试官精讲典型编程题》代码
# // 作者：何海涛
# //==================================================================
#
# // 面试题8：二叉树的下一个结点
# // 题目：给定一棵二叉树和其中的一个结点，如何找出中序遍历顺序的下一个结点？
# // 树中的结点除了有两个分别指向左右子结点的指针以外，还有一个指向父结点的指针。

class TreeLinkNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
        self.parent = None

class Solution:
    def reConstructBinaryTree(self, pre, tin, parent):
        if not pre and not tin:
            return None
        root = TreeLinkNode(pre[0])
        if set(pre) != set(tin):
            return None
        i = tin.index(pre[0])
        # print (i)
        root.left = self.reConstructBinaryTree(pre[1:i+1], tin[:i], root)
        root.right = self.reConstructBinaryTree(pre[i+1:], tin[i+1:], root)
        root.parent = parent

        return root

    def getNext(self, pNode):
        if pNode == None:
            return

        h = pNode.parent.val if pNode.parent else 'None'
        print (pNode.val, h)

        pNext = None
        if pNode.right != None:
            pRight = pNode.right
            while pRight.left != None:
                pRight = pRight.left
            pNext = pRight
        elif pNode.parent != None:
            pCurrent = pNode
            pParent = pCurrent.parent
            while pParent != None and pCurrent == pParent.right:
                pCurrent = pParent
                pParent = pCurrent.parent
            pNext = pParent

        val = pNext.val if pNext else 'None'
        print (val)
        return pNext


def main():


    pre = ['a','b','d','e','h','i','c','f','g']
    tin = ['d','b','h','e','i','a','f','c','g']

    s = Solution()
    ret = s.reConstructBinaryTree(pre, tin, None)
    out = (ret)
    print (out)

    # i = 5
    # print (pre[1:i+1], pre[i+1:])
    # print (tin[:i], tin[i+1:])

    # b -> h
    print (s.getNext(ret.left))
    # a -> f
    print (s.getNext(ret))

    # d -> b
    print (s.getNext(ret.left.left))

    # f -> c
    print (s.getNext(ret.right.left))

    # i -> a
    print (s.getNext(ret.left.right.right))

    print (s.getNext(ret.right.right))

if __name__ == '__main__':
    main()