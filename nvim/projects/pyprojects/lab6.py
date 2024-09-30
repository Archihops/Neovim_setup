import random

#Name: Carlos Martinez Luna

#Exercise 1
start=int(input("Enter the starting value: "))
end=int(input("Enter the ending value: "))
step=int(input("Enter the step value: "))

print(f"{'Grams':>15}{'Ounces':>15}{'Pounds':>15}{'kilograms':>15}")

i=start+step
while i>end:
    i-=step
    ounces1=i*0.0353
    pounds1=i*0.00221
    kilograms1=i*0.001
    if i==end:
        break
    print(f"{i:>15}{ounces1:>15.3f}{pounds1:>15.4f}{kilograms1:>15.4f}")

#exercise 2
print("\n")    


total_problems=0
total_wins=0 
again=input("Do you want a problem to solve? y/n: ")
print("\n")

while again.lower()=="y":
    x=random.randint(140,170)
    y=random.randint(70,80)
    z=random.randint(13,16)
    sol=(x-y)//z
    expression=f'{x}-{y}//{z}'
    ans=int(input(f"What is {expression}? "))
    print("\n")
####if ans is correct###
    if int(sol)==int(ans):
        print("Correct!")
        total_wins+=1
        total_problems+=1
        PERC=(total_wins/total_problems)*100
        print("\n")
        print(f"Total wins: {total_wins}")
        print(f"Total problems {total_problems}")
        print(f"Percentage won : {PERC:.0f}%")
        print("\n")
        again=input("Do you want another problem to solve: y/n: ")
###if ans isnt correct###
    elif int(sol)!=int(ans):
        print("The correct answer is", int(sol))
        print("\n")
        total_wins-=1<=0
        total_problems+=1
        perc=(total_wins/total_problems)*100
        print(f"Total problems {total_problems}")
        print(f"Total wins: {total_wins}")
        print(f"Percentage won : {perc:.0f}%")
        print("\n")
        again=input("Do you want another problem to solve: y/n: ")
###if user doesn't wanna play
while again.lower()=='n':
    print("\n")
    total_wins-=1<=0
    total_problems+=1
    PERC=(total_wins/total_problems)*100
    print(f"Total problems {total_problems}")
    print(f"Total wins: {total_wins}")
    print(f"Percentage won : {perc:.0f}%")
    break
