#coding=utf-8

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def merge(self, pHead1, pHead2):
        head = ListNode(0)
        tmp = head

        while pHead1 is not None \
            and pHead2 is not None:
            if pHead1.val <= pHead2.val:
                tmp.next = pHead1
                pHead1 = pHead1.next
            else:
                tmp.next = pHead2
                pHead2 = pHead2.next
            tmp = tmp.next

        if pHead1 is None:
            tmp.next = pHead2
        elif pHead2 is None:
            tmp.next = pHead1

        return head.next

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

    def printListFromHeadToTail(self, listNode):
        if listNode.val == None:
            return
        l =[]
        head = listNode
        while head:
            l.append( head.val)
            head = head.next
        return l


def main():

    l1 = [1,3,5,7]
    l2 = [2,4,6,8]
    s = Solution()

    node1 = s.constructList(l1)
    node2 = s.constructList(l2)

    tmp = s.merge(node1, node2)
    print (s.printListFromHeadToTail(tmp))



if __name__ == '__main__':
    main()