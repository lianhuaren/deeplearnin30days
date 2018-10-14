#coding=utf-8



class Solution:

    def quick_sort(self, lists, left, right):
        # 快速排序
        if left >= right:
            return lists
        key = lists[left]
        low = left
        high = right
        while left < right:
            while left < right and lists[right] >= key:
                right -= 1
            lists[left] = lists[right]
            
            print ("left:",left,"right:",right)
            while left < right and lists[left] <= key:
                left += 1
            lists[right] = lists[left]
        lists[right] = key

        print ("key:",key ,lists)
        print ("-----------------------")
        self.quick_sort(lists, low, left - 1)
        self.quick_sort(lists, left + 1, high)
        return lists

def main():



    s = Solution()

    print (s.quick_sort([49,38,65,97,76,13,27,49],0,7))


if __name__ == '__main__':
    main()