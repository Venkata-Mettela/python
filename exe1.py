n1 = int(input("Enter 1st Number:"))
n2 = int(input("Enter 2nd Number:"))
n3 = int(input("Enter 3rd Number:"))
if n1 > n2 and n1 > n3:
    highest = n1
elif n2 > n1 and n2 > n3:
    highest = n2
else:
    highest = n3
print("The biggest number is", highest)
