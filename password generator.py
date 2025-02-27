letters= ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z',
 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
symbols =['!','#','$','%','&','(',')','*','+']
import random
print("Welcome to the password generator")
pass_letters=int(input("How many letter would you like in your pass\n"))
pass_sym=int(input("HOw many symbols do you want?\n"))
pass_numb=int(input("How many numbers do you like?\n"))
password_list =[]
for letter in range(0,pass_letters):
    password_list.append(random.choice(letters))
for symbol in range(pass_sym):
    password_list.append(random.choice(symbols))
for number in range(pass_numb):
    password_list.append(str(random.choice(numbers)))
random.shuffle(password_list)
final_pass=""
for char in password_list:
    final_pass+=char
print(final_pass)

