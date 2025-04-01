

print("Welcome to python Pizza deliveries !")

total_cost = 0
size = (input("What size pizza do you want to have ? S,M or L : ")).upper()
pepperoni = (input("Do you want pepperoni ? Y or N : ")).upper()

total_cost = 0

if size == 'S':
    total_cost += 15
    if pepperoni == 'Y':
        total_cost += 2
    elif pepperoni == 'N':
        total_cost += 0
    else :
        print("Please select  a valid option !!")
        exit()

elif size == 'M'  :
    total_cost += 20
    if pepperoni == 'Y':
        total_cost += 3
    elif pepperoni == 'N':
        total_cost += 0
    else:
        print("Please select  a valid option !!")
        exit()

elif size =='L' :
    total_cost +=25
    if pepperoni == 'Y':
        total_cost += 3
    elif pepperoni == 'N':
        total_cost += 0
    else:
        print("Please select  a valid option !!")
        exit()
else :
    print("Please select a valid size !!")
    exit()

extra_cheese = (input("Do you want extra cheese ? Y or N : ")).upper()
if extra_cheese == 'Y':
    total_cost +=1
    print(f"Total cost : {total_cost}")
elif extra_cheese == 'N' :
    total_cost +=0
    print(f"Total cost : {total_cost}")
else :
    print("Please select a valid choice !!")
    exit()



