#coding=utf-8

class ListNode:
    def __init__(self, x=None):
        self.val = x
        self.next = None

class Solution:
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


    node1 = ListNode(10)
    node2 = ListNode(12)
    node3 = ListNode(13)
    node1.next = node2
    node2.next = node3

    ret = Solution().printListFromTailToHead(node1)
    out = (ret)
    print (out)

if __name__ == '__main__':
    main()