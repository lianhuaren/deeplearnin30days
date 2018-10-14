#coding=utf-8

class Solution:
    def isValid(self, s):
        """
        1. 使用栈的原因：需要比较最近的括号
        2. 创建hashmap, key是入栈的，value是出栈的
        3. 遍历字符串
           字符是key：就入栈
           不是：如果栈空 或 出栈的map不等于当前字符 -> False
        4. 遍历完栈中还有就是False
        """
        # 步骤1
        parentheses = {k: v for k, v in zip('([{', ')]}')}

        # 步骤2
        stack = []

        for char in s:
            if char in parentheses:
                stack.append(char)
            else:
                if not stack or parentheses[stack.pop()] != char:
                    return False

        # 步骤3
        return not stack
    def simplifyPath(self, path):
        """
        使用栈的原因：当读到..时需要弹出最近的一个路径
        步骤：
        1. 通过re模块分割字符串
        2. 遍历分割后的字符串，遇到.忽略，遇到..如果栈中有就出栈，没有就算了，剩下的如果是非空的就入栈
        3. 再用'/'进行拼接
        """
        # 步骤一
        import re
        cleaned_path = re.split(r'/+', path)

        # 步骤二
        res = []

        for item in cleaned_path:
            # cleaned_path中可能有被分割出的空字符串
            if item == '.' or item == '':
                continue

            if item == '..':
                if res:
                    res.pop()
            else:
                res.append(item)

        # 步骤三
        return '/' + '/'.join(res)
    # s 源字符串
    def replaceSpace(self, s):
        # write code here
        if not isinstance(s, str) or len(s) <=0 or s == None:
            return
        spaceNum = 0
        for i in s:
            if i == ' ':
                spaceNum += 1

        newStrLen = len(s) + spaceNum * 2
        newStr = newStrLen * [None]
        indexOfOriginal, indexOfNew = len(s) - 1, newStrLen - 1
        while indexOfNew >= 0 and indexOfNew >= indexOfOriginal:
            if s[indexOfOriginal] == ' ':
                newStr[indexOfNew-2:indexOfNew+1] = ['%', '2', '0']
                indexOfNew -= 3
                indexOfOriginal -= 1
            else:
                newStr[indexOfNew] = s[indexOfOriginal]
                indexOfNew -= 1
                indexOfOriginal -= 1
        return "".join(newStr)

def stringToString(input):
    return input#input[1:-1].decode('string_escape')

def main():
    import sys

    # line = "()"
    # s = stringToString(line)
    # ret = Solution().isValid(s)

    # line = "/a/./b/../../c/"
    # path = stringToString(line)
    #
    # ret = Solution().simplifyPath(path)

    line = "We Are Happy"
    ret = Solution().replaceSpace(line)

    out = (ret)
    print out

if __name__ == '__main__':
    main()