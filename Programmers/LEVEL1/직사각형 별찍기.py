a, b = map(int, input().strip().split(' '))
'''
for i in range(b):
    for j in range(a):
        print("*", end="")
    print()
print(a + b)
'''

for i in range(b):
    temp = ""
    for j in range(a):
        temp += "*"
    print(temp)