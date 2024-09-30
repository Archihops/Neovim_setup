#Carlos Martinez Luna

#exercise 1
print("Which Funtion do you want to call? ")     
print("A. Lab Assignment 1, Program 1") 
print("B. Lab Assignment 1, Program 2 ")
q1=input("Enter your choice here: ")
def lab1():
    if q1=="A":
        print("\n")
        print("My first name is Carlos.")
        print("My last name is Martinez Luna.")
        print("My faculty is science.")
        print("My year is one.")
        print("\n")
lab1()
def lab2():
    if q1=="B":
        print("\n")
        print("This is my first initial:\n")
        print("************************************")
        print("*                                  *")
        print("*                                  *")
        print("*                   CCCCCCCCCC     *")
        print("*                CCCCCCCCCCC       *")
        print("*             CCCCCCCCCC           *")
        print("*          CCCCCCCCCC              *")
        print("*       CCCCCCCCC                  *")
        print("*     CCCCCCCCC                    *")
        print("*    CCCCCC                        *")
        print("*   CCCCC                          *")
        print("*   CCCC                           *")
        print("*   CCCC                           *")
        print("*   CCCCC                          *")
        print("*   CCCCCC                         *")
        print("*    CCCCCCCCC                     *")
        print("*       CCCCCCCCC                  *")
        print("*          CCCCCCCCCC              *")
        print("*             CCCCCCCCCC           *")
        print("*                CCCCCCCCCCC       *")
        print("*                   CCCCCCCCCC     *")
        print("*                                  *")
        print("*                                  *")
        print("*                                  *")
        print("************************************")
lab2()

#Exercise 2

def converter(first,second,third):
    start=int(input("Enter the starting value: "))
    end=int(input("Enter the ending value: "))
    step=int(input("Enter the step value: "))
    print(f"{'Grams':>15}{'Ounces':>15}{'Pounds':>15}{'kilograms':>15}")
    i=start+step
    while i>end:
        i-=step
        ounces1=i*first 
        pounds1=i*second
        kilograms1=i*third
        if i==end:
            break
        print(f"{i:>15}{ounces1:>15.3f}{pounds1:>15.4f}{kilograms1:>15.4f}")
converter(first=0.0353,second=0.00221,third=0.001)
    
