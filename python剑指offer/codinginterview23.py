#coding=utf-8

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def meetingNode(self, pHead):
        if pHead == None:
            return None

        pSlow = pHead.next
        if pSlow == None:
            return None
        pFast = pSlow.next
        while pFast:
            if pSlow == pFast:
                return pSlow
            pSlow = pSlow.next
            pFast = pFast.next

            if pFast:
                pFast = pFast.next

    def entryNodeOfLoop(self, pHead):
        meetingNode = self.meetingNode(pHead)
        if not meetingNode:
            return None

        nodeLoop = 1
        flagNode = meetingNode
        while flagNode.next != meetingNode:
            nodeLoop += 1
            flagNode = flagNode.next

        print (nodeLoop)

        pNode1 = pHead

        for i in range(nodeLoop):
            pNode1 = pNode1.next

        pNode2 = pHead
        while pNode1 != pNode2:
            pNode1 = pNode1.next
            pNode2 = pNode2.next

        return pNode1

    #--------------辅助函数
    def findKthToTail(self, head, k):
        if head == None or k <= 0:
            return None

        pAHead = head
        pBehind = None

        for i in range(k-1):
            if pAHead.next != None:
                pAHead = pAHead.next
            else:
                return None
        pBehind = head

        while pAHead.next != None:
            pAHead = pAHead.next
            pBehind = pBehind.next
        return pBehind


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
    node3 = node1.next.next
    print (node3.val)
    node6 = s.findKthToTail(node1, 1)
    node6.next = node3

    print (s.entryNodeOfLoop(node1).val)



if __name__ == '__main__':
    main()