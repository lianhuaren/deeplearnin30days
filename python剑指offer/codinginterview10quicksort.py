#coding=utf-8



class Solution:

    def quick_sort(self, lists, left, right):
        # 快速排序
        if left >= right:
            return lists

        key = lists[left]
        low = left
        high = right

        print "before One iteration key:",key,lists

        while left < right:
            while left < right and lists[right] >= key:
                right -= 1
            lists[left] = lists[right]
            
            print ("change left=right left:",left,"right:",right)
            while left < right and lists[left] <= key:
                left += 1
            lists[right] = lists[left]
            print ("change right=left left:",left,"right:",right)
        lists[right] = key

        print ("after One iteration key:",key ,lists)
        print ("-----------------------")
        self.quick_sort(lists, low, left - 1)
        self.quick_sort(lists, left + 1, high)
        return lists

def main():



    s = Solution()
    arr = [49,38,65,97,76,13,27,49]
    print (s.quick_sort(arr,0,len(arr)-1))


if __name__ == '__main__':
    main()