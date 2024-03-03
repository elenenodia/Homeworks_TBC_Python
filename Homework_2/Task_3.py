number = int(input("If you want to find simple divisors of numbers from 1 to 10, enter the number: "))
if number == 2 or number == 4 or number == 8:
    print(2)
elif number == 3 or number == 9:
    print(3)
elif number == 5:
    print(5)
elif number == 6:
    print(2, 3)
elif number == 7:
    print(7)
elif number == 10:
    print(2, 5)
elif number == 1:
    print(1, "is neither a prime nor a composite.")
else:
    print("Invalid")
