lst1 = ["hello", 2, "Bye"]
lst2 = ["GM", 8, "GN"]

print(lst1)
print(lst2)

print(len(lst1))

print(lst1+lst2)
lst1.append(lst2)
print(lst1)

lst1.extend(lst2)
print(lst1)

for i in lst1:
    print(i)

for i in range(len(lst2)):
    print(lst2[i])

print(lst1)
lst1.pop(0)
print(lst1)
del lst1[2]
print(lst1)

lst1.remove(8)
print(lst1)

lst2.clear()
print(lst2)

print(lst1)
lst1.reverse()
print(lst1)

print(lst1[::-1])

print(lst1[-4:-1])


ls = [1,3,3]
print(ls.count(3))
print(ls.index(3))
print(1 in ls)
print(max(ls))
print(sum(ls))
print(ls*3)

