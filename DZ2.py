x = int(input('Type x:'))
left, right = divmod(x, 1000)
print(left)
left, right = divmod(x, 100)
print(left % 10)
print(right // 10)
print(right % 10)





