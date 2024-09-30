#Name: Carlos Martinez Luna

#Exercise 1
var1 = int(input("Enter the starting value in grams: "))
var2 = int(input("Enter the ending value in grams: "))
var3 = int(input("Enter the step value: "))

print(f"{'Grams':>10}{'Ounces':>15}{'Pounds':>15}{'Kilograms':>15}")
for i in range(var1,var2+1,var3):
    grams = "{:.0f}".format(i)
    ounces = "{:.3f}".format(i*0.0353)
    pounds = "{:.4f}".format(i*0.00221)
    kilograms = "{:.4f}".format(i*0.001)

    print(f"{grams:>10}{ounces:>15}{pounds:>15}{kilograms:>15}")

#exercise 2
print("\n")

num_img = int(input("How many images are there? "))
above_1000 = 0
under_1000 = 0
equal_1000 = 0
for u in range(1,num_img+1):
    ques = int(input(f"What is the width of image {u} in pixels "))
    if ques > 1000:
        above_1000 += 1
    if ques < 1000:
        under_1000 += 1
    if ques == 1000:
        equal_1000 += 1

print("\n")
print(f"Total images whose width are < 1000 pixels: {under_1000}")
print(f"Total images whose width are = 1000 pixels: {equal_1000}")
print(f"Total images whose width are > 1000 pixels: {above_1000}")
