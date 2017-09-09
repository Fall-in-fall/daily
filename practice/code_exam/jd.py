
# 题目描述：
# 异或运算是常见的二进制运算，给出两个n位二进制数a，b。a异或b的运算依次考虑二进制的每一位，若这一位相同，那么这一位的异或结果就是0，不同就是1。
# 例如a=1100, b=0100。执行a异或b的运算，a的最高位是1，b的最高位是0，两个数字不同所以最高位异或结果是1；a和b次高位都是1，所以次高位异或为0；最后两位它们都是0，所以异或结果也都是0。那么a异或b的答案就是1000。
# 现在输入两个n位二进制数，输出它们异或结果的十进制答案。上述样例中异或的二进制结果为1000，转化成十进制就是8。
# 输入
# 输入有三行，第一行一个数n(1<=n<=20)，接下来两行有两个n位二进制数。输入的二进制数可能有前导零。
# 输出
# 输出一个数，异或结果的十进制数值，不要输出前导零。
#
# 样例输入
# 4
# 1100
# 0100
# 样例输出
# 8
# #--coding:utf-8--
# import math
# wei=int(raw_input() )
# a=raw_input()
# b=raw_input()
# r=''
# for i in xrange(0,len(a)):
#     if a[i]==b[i]:
#         r=''.join([r,'0'])
#     else:
#         r=''.join([r,'1'])
# f=0
# n=wei
# for x in r:
#     if x=='1':
#         f+=math.pow(2,n-1)
#     n=n-1
# print int(f)



