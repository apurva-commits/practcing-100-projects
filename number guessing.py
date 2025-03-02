start=int(input(f"Enter starting "))
end=int(input(f"Enter ending "))
even=[]
odd=[]
for i in range(start, end + 1):
    if i%2==0:
        even.append(i)

    else:

        odd.append(i)
print(f"Odd numbers are :{odd}")
print(f"Even numbers are :{even}")