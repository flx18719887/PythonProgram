# 元组是一个不可改变的列表。元组只是逗号分隔的序列(不带括号的列表)。
# 为了增强代码可读性，通常将元组放在一对圆括号中。
mtuple = (1, 2, 3, 4)
print(mtuple)
print(type(mtuple))
print( mtuple[:3])

mt = 1,
print(mt)
print(type(mt))
mt1 = ()
print(mt1)



# Python的元组与列表类似，元组也是序列，唯一的差别在于元组是不能修改的。
# 元组语法很简单，只要将一些值用逗号分隔，就能自动创建一个元组
1, 2, 3    # (1, 2, 3)
# 通常采用圆括号的形式表示
aTupe = (1, 2, 3)
print(aTupe)   # (1, 2, 3)
tp = (1)   # 这样定义出来的是数字，而不是元组。虽然只有一个值，也必须在它后面加上逗号
print(tp)   # 1

tp1 = (1, )
print(tp1)    # (1,)

# 函数tuple的工作原理与list很像：它将一个序列作为参数，并将其转换为元组。
# 如果参数已经是元组，那么就原封不动地返回它。
tuple([1, 2, 3, 5, 6, 7])    # (1, 2, 3, 5, 6, 7)
tuple((1, 2, 3, 7, 8, 9))     # (1, 2, 3, 7, 8, 9)

# 表面上看，tuple的元素确实变了，但其实变得不是tuple的元素而是list的元素。tuple一开始指向的list并没有改成别
# 的list，所以tuple所谓的 ”不变“ 是指，tuple的每个元素，指向永远不变。即指向’a'，就不能改成指向‘b'，
# 指向一个 list，就不能改成指向其他对象，但指向的这个list本身是可变的！
tp2 = ('a', 'b', ['A', 'B'])
print(tp2)    # ('a', 'b', ['A', 'B'])
tp2[2][0] = 'X'
print(tp2)    # ('a', 'b', ['X', 'B'])
tp2[2][1] = 'Y'
print(tp2)    # ('a', 'b', ['X', 'Y'])

# 同其他序列一样，元组的拼接用+号连接，元组的重复仍使用*n的方式。
# 元组的创建方式及其元素的访问方式与其他序列是相同的，但在元组中，增、删、改是不被允许的。
# 元组与列表区别：
# 元组和列表很类似，它们经常被用来在不同的情况和不同的用途。
# 元组有很多用途。例如(x,y)坐标对，数据库中的员工记录等等。
# 元组就像是字符串，是不可变的。通常包含不同种类的元素并通过分拆或索引访问。
# 列表内容是可变的，它们的元素通常是相同类型的，并通过迭代访问。
# 对于某些领域来说，能用元组，就不用列表，因为；元组速度更快，它是敞亮的。
#使用元组不需要对修改的数据进行写保护，使得数据更安全。



mtuple = (1, 2, 3, ["a", "bc", "D"], 7, 8, 9)
print(mtuple)
mtuple[3][1] = "BC"    # 元组元素为列表时，其中的列表可变
print(mtuple)
# mtuple[1] = "R"    # 报错，元组不可变
# print(mtuple)



