triangle = " * "

for i in range(0, 9):
    print(triangle)
    i = " * "
    triangle += str(i)
    
print("__________________________\n")

j = 9

for i in range(1, 10, 2):
    print(" "*j + i*"*")
    j = j - 1
    
print("__________________________\n")


j=1

for i in range(9, 0, -2):
    print("    "+j*" "+i*"*")
    j = j + 1
    
print("__________________________\n") 

j = 9

for i in range(1, 11, 2):
    print(" "*j + i*"*")
    j = j - 1

j=1

for i in range(9, 0, -2):
    print("    "+j*" "+i*"*")
    j = j + 1

print("__________________________\n")

for i in range(8):
    for j in range(i):
        print("* ", end = "")
    print()
    
for i in range(8):
    for j in range(8-i):
        print("* ", end = "")
    print()
