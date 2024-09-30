#Name: Carlos Martinez Luna

#Exercise 1

var1 = float(input(f"How many quarts are there? "))
var2 = float(input(f"How many pints are there? "))
var3 = float(input(f"How many litres are there? "))

print(f"\n{var1} Quarts is {float(var1*0.25)} in gallons.")
print(f"{var2} Pints is {float(var2*0.125)} in gallons.")
print(f"{var3} Litres is {float(var3*0.2642)} in gallons.")
print(f"The total volume is {var1+var2+var3}.")

#Exercise 2

print("\n")
var4 = int(input(f"Enter the number of days: "))
var5 = int(input(f"Enter the number of hours: "))
var6 = int(input(f"Enter the multiplier: "))

convert = int(var4*24+var5)
tot = int(convert*var6)
days1 = int(tot/24)
hours = int(days1*24)
hours2 = int(tot-hours)

print(f"The total time is {tot}.\nOr {days1} days and {hours2} hours.")





