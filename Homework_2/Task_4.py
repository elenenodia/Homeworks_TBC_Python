speed = int(input("Enter the speed of the car: "))
if speed > 120:
    print("VERY FAST")
elif speed > 60:
    print("FAST")
elif speed > 30:
    print("MODERATE")
else:
    print("SLOW")
