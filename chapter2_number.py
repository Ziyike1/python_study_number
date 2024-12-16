#下划线不影响python对数字的识别
universe_age = 14_000_000
print(universe_age)

#同时给多个变量赋值
universe_age, b, c = 0, 0, 0
print(universe_age,b,c)

#常数应该全大写
MAX_CONNECTIONS = 5000

print(5+3)
print(10-2)
print(2*4)
print(16/2)

# 此代码将我最喜欢的数字定义为my_favorite_num，并将之f字符串打印出来
my_favorite_num = 1999
full_line = f"my favorite number is {my_favorite_num}"
print(full_line)

print(12 ** 2) #等同于12^2