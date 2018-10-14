#coding=utf-8

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:

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

    def printListFromTailToHead(self, listNode):
        if listNode.val == None:
            return
        l =[]
        head = listNode
        while head:
            l.insert(0, head.val)
            head = head.next
        return l

def main():

    l = [1,2,3,4,5,6]
    s = Solution()

    node1 = s.constructList(l)

    # print (s.printListFromTailToHead(node1))

    print (s.findKthToTail(node1, 3).val)



if __name__ == '__main__':
    main()