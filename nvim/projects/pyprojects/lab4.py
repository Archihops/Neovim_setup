#Name: Carlos Martinez Luna

#exercise 1
var1=float(input("How many grams do you want to convert? "))
var2=input("Choose (o)ounces, (p)pounds or (k)kilograms: ")

#Statements
calc1=var1*0.0353
calc2=var1*0.00221
calc3=var1*0.001

if var2=="o":
    print(f"{var1:.0f} grams is {calc1:.3f} ounces.")
elif var2=="p":
    print(f"{var1:.0f} grams is {calc2:.4f} pounds.")
elif var2=="k":
    (print(f"{var1:.0f} grams is {calc3:.4f} kilograms."))
else:
    print("There was an error made in the choice.")

#exercise 2
print("\n")
var3=float(input("What is the current yearly pay? "))
var4=float(input("How many years have been worked? "))

#statements
if 3<=var4<=5:
    pay_increase=var3*0.03
    total_pay=pay_increase+var3
    pay1=pay_increase
    pay2=total_pay
    print(f"Yearly pay: ${var3:.2f}")
    print(f"Pay Raises: ${pay1:.2f}")
    print(f"New yearly pay: ${pay2:.2f}")
elif var4>=6 and var4<=12:
    pay_increase2=var3*0.04
    pay3=pay_increase2
    total_pay2=var3+pay_increase2
    print(f"Yearly pay: ${var3:.2f}")
    print(f"Pay Raises: ${pay3:.2f}")
    print(f"New yearly pay: ${total_pay2:.2f}")
if var4<3:
    print(f"Yearly pay: ${var3:.2f}")
    print(f"Pay Raises: ${var3*0:.2f}")
    print(f"New yearly pay: ${var3:.2f};")




