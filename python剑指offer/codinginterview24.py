#coding=utf-8

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def reverseList(self, pHead):
        pReversedHead = None
        pNode = pHead
        pPrev = None

        while pNode != None:
            pNext = pNode.next

            if pNext == None:
                pReversedHead = pNode

            pNode.next= pPrev
            pPrev = pNode
            pNode = pNext

        return pReversedHead

    #--------------辅助函数

    def constructList(self, l):
        if not l:
            return None
        root = ListNode(l[0])
        pBehind = root

        for i in range(1,len(l)):
            pBehind.next = ListNode(l[i])
            pBehind = pBehind.next

        return root



def main():

    l = [1,2,3,4,5,6]
    s = Solution()

    node1 = s.constructList(l)


    print (s.reverseList(node1).val)



if __name__ == '__main__':
    main()