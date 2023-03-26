x = int(input('Type 4-digit number:'))
left, right = divmod(x, 1000)
print(left)
left, right = divmod(x, 100)
print(left % 10)
print(right // 10)
print(right % 10)





