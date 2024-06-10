import os

print(os.getcwd())

'''f = open("demo.txt", 'w')
f.write("One")
f.write(("\ntwo\nthree\nfour"))
f.close()'''

with open("demo.txt", 'r') as f:

    '''print(f.read(2))
    print(f.tell())
    print(f.read(5))
    print(f.seek(0))
    print(f.tell())
    print(f.read(3))'''

    print(f.readline())


