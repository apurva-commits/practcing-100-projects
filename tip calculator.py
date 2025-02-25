
print("Welcome to the tip Calculator!")
a=float(input("What was the total Bill? : $"))
b=int(input("How much tip would you like to give? 10, 12 or 15" ))
c=int(input("How many people to split the bill?"))
d=(((a*b/100)+a)/c)
""" here explanation so 
total bill * tip amount/100 + total bill / number of people splitting it
"""
d=round(d,2) #since d stores total value its round figured
print(f"Each person should pay {d}")