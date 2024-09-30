#Carlos Martinez Luna
#exercise 1

parcel_info = []

width = input("Enter the parcel's width: ")
height = input("Enter the parcel's height: ")
length = input("Enter the parcel's length: ")
mass = input("Enter the parcel's mass in kg: ")
num_items = input("How many items are in the package? ")
worth = input("How is the worth of the parcel? ")
shipping_fee = input("What is the shipping fee? ")
print("\n")

#Add the parcel information
parcel_info.append(width)
parcel_info.append(height)
parcel_info.append(length)
parcel_info.append(mass)
parcel_info.append(num_items)
parcel_info.append(worth)
parcel_info.append(shipping_fee)

#list's contents
# print("The parcel information is", parcel_info)
print("\n")
print("The width is", parcel_info[0])
print("The height is", parcel_info[1])
print("The length is", parcel_info[2])
print("The mass in kg is", parcel_info[3])
print("The number of items in the parcel is", parcel_info[4])
print("The worth of the parcel is", parcel_info[5])
print("The shipping fee is", parcel_info[6])

print("\n")
#Exercise 2

up_to_100mb = []
over_100mb = []
file_sizes = []

num_files = int(input("How many file sizes will be entered? "))

#Input the file sizes and store them in the list
for i in range(num_files):
    size = int(input(f"What is the size in mb for file {i+1}: "))
    file_sizes.append(size)

#Separate file sizes from up to 100mb and over 100mb lists
for size in file_sizes:
    if size <= 100:
        up_to_100mb.append(size)
    else:
        over_100mb.append(size)

#Entire list of file sizes
print("\n")
print("The file sizes are", file_sizes)
#Up to 100mb list
print("\n")
print("Up to 100 mb:", up_to_100mb)
print("Number of files:",len(up_to_100mb))
print("Smallest file size:", min(up_to_100mb))
print("\n")
#Over 100mb list
print("Over 100 mb:", over_100mb)
print("Number of files:",len(over_100mb))
print("Largest file size:", max(over_100mb))
