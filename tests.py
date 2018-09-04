
# 自己写字符串strip()方法
def right_strip(tempStr, splitStr):
    endindex = tempStr.rfind(splitStr)
    while endindex != -1 and endindex == len(tempStr) - 1:
        # 和strip一样，对两边的字符才能做到去除的效果，所以这里需要判断，分割的字符是不是被分割字符串的两边的字符
        tempStr = tempStr[: endindex]
        endindex = tempStr.rfind(splitStr)
        # 切完之后 继续循环，解决类似这种的两边是多个字符的(" sdfshhhh", "h"),可以把边上的h去光
    return tempStr


print(right_strip("sdfhhhs", "h"))


def left_strip(tempStr, splitStr):
    startindex = tempStr.find(splitStr)
    while startindex == 0:  # 只需要判断是切割字符串是 被切割字符串的最左边字符
        tempStr = tempStr[startindex+1:]
        startindex = tempStr.find(splitStr)
    return tempStr


print(left_strip(" h ", " "))

# super()的用法，广度优先查找
class A(object):
    def __init__(self):
        print("enter A") # 6
        super(A, self).__init__()
        print("leave A")


class B(object):
    def __init__(self):
        print("enter B")  # 3
        super(B, self).__init__()
        print("leave B")


class C(A):
    def __init__(self):
        print("enter C") # 4
        super(C, self).__init__()
        print("leave C")


class D(A):
    def __init__(self):
        print("enter D") # 5
        super(D, self).__init__()
        print("leave D")


class E(B, C):
    def __init__(self):
        print("enter E")  # 2
        super(E, self).__init__()
        print("leave E")


class F(E, D):
    def __init__(self):
        print("enter F")  # 1
        super(F, self).__init__()
        print("leave F")


# f = F() # 
# print(F.mro())


# 简单实现一个栈解构
class Stack(object):
    def __init__(self):
        self.value = []

    def push(self, x):
        self.value.append(x)

    def pop(self):
        self.value.pop()


stack = Stack()

stack.push(1)
stack.push(2)
stack.push(3)
print(stack.value)
stack.pop()
print(stack.value)


# 输入一个日期，返回一年中的那一天
import time
import datetime


def whice_day(year, month, day):
    return (datetime.datetime(year, month, day) - datetime.datetime(year, 1, 1)).days + 1




def whice_day2(year, month, day):
    return time.strptime("{}-{}-{}".format(year, month, day), "%Y-%m-%d").tm_yday

	
	
# 判断值是否在矩阵中(杨氏矩阵)

# 		在一个二维数组中，每一行都按照从左到右递增的顺序排序，每一列按照从上到下的顺序；
arr = [
    [1, 4, 7, 10, 15],
    [2, 5, 8, 12, 19],
    [3, 6, 9, 16, 22],
    [10, 13, 14, 17, 24],
]


def get_num(num, data=None):
    while data:
        if num in data[-1]:
            return True
        else:
            data.pop()
    return False


# print(get_num(80, arr))


arr = [
    [1, 4, 7, 10, 15],
    [2, 5, 8, 12, 19],
    [3, 6, 9, 16, 22],
    [10, 13, 14, 17, 24],
]


def get_value(data, value):
    m = len(data)-1
    n = len(data[0]) -1
    r = 0
    c = n
    while c >= 0 and r <= m:
        if value == data[r][c]:
            return True
        elif value > data[r][c]:
            r += 1
        else:
            c -= 1
    return False


# print(get_value(arr, 80))


# 最大公约数
x = 25
y = 15


def max_common(a, b):
    while b:
        a, b = b, a % b
    return a


# print(max_common(x, y))


# 最小公倍数
x1 = 5
y1 = 10


def min_common(a, b):
    c = a * b
    while b:
        a, b = b, a % b
    return c // a


print(min_common(x1, y1))

# 获取中位数

# 如果总个数是奇数，按照从小到大的顺序，取中间那个数；如过总个数是偶数，按照从小到大顺序取中间那两个数的平均数

def get_middle_num(data):
    if isinstance(data, list):
        data.sort()
        if len(data) % 2 == 1:
            i = int(((len(data)+1) / 2)) - 1
            return data[i]
        else:
            i = int(len(data) / 2) - 1
            return (data[i] + data[i+1])/2


print(get_middle_num([2, 6, 1, 5, 4, 3]))


def medin(data):
    data.sort()
    half = len(data) // 2
    print("-->", half)
    return (data[half] + data[~half]) / 2


print(medin([2, 6, 1, 5, 4, 3]))
print([1, 2, 3][~2])