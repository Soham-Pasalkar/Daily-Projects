print("Welcome to our Restaurant! Here's the menu: ")
menu = {
    "cold coffee" : 80,
    "cappacino"   : 80,
    "espresso"    : 90,
    "americano"   : 100, 
    "latte"       : 100,
    "frappe"      : 120
}
print(menu)


total_bill = 0
order = ""

def parse_order(order):
    cleaned = order.lower().replace(","," ")
    return cleaned.split()

while(True):
    print("Enter the items you want to Order : ")
    order = input()
    order_list = parse_order(order)
    flag = True

    for i in order_list:
        if i == "cold":
            total_bill += 80
        elif i == "coffee":
            continue
        elif i not in menu:
            print(f"{i} not available")
            flag = False
        else:
            total_bill += menu[i]

    if flag != False:
        print("Your Order has been added!")

    choice = input("Do you want to Order anything else ? (y/n) -> ")
    if choice == "n":
        break


print("Your Total Bill is: ",total_bill)




