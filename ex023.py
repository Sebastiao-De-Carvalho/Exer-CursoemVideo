number = int(input("Number: "))
print("Unit: {}".format(number // 1 % 10))
print("Dozens: {}".format(number // 10 % 10))
print("Hundreds: {}".format(number // 100 % 10))
print("Thousands: {}".format(number // 1000 % 10))
