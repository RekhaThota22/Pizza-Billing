print("Welcome to python Pizza deliveries !")

while True :
    total_cost = 0
    size = (input("What size pizza do you want to have ? S,M or L : ")).upper()
    if size =='S':
        total_cost += 15
    elif size == 'M'  :
        total_cost += 20
    elif size == 'L':
         total_cost +=25
    else :
        print("Please select a valid choice !!")
        continue

    while True:
        pepperoni = (input("Do you want pepperoni ? Y or N : ")).upper()
        if pepperoni == 'Y':
            if size =='S':
                total_cost += 2
            else:
                total_cost += 3
            break
        elif pepperoni == 'N':
            total_cost += 0
            break
        else :
           print("Please select  a valid option !!")
           continue
    while True:
        extra_cheese = (input("Do you want extra cheese ? Y or N : ")).upper()
        if extra_cheese == 'Y':
            total_cost += 1
            break
        elif extra_cheese == 'N':
            total_cost += 0
            break
        else:
            print("Please select a valid choice !!")

    print(f"Total cost : {total_cost}")

    replay = input("Do you want to order again? Yes or No :").upper()
    if replay!='YES':
        print("Thankyou for ordering !")
        break



