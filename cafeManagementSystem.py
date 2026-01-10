def display_menu(menu):
    """Display the menu in a formatted way"""
    print("\n" + "="*40)
    print("MENU".center(40))
    print("="*40)
    for item, price in menu.items():
        print(f"{item.capitalize():<25} ₹{price}")
    print("="*40 + "\n")


def parse_order(order_input, menu):
    """Parse order input and return a dictionary of items with quantities"""
    # Clean the input
    cleaned = order_input.lower().strip()
    if not cleaned:
        return {}
    
    # Replace commas with spaces
    cleaned = cleaned.replace(",", " ")
    
    # Split by spaces
    words = cleaned.split()
    
    order_dict = {}
    i = 0
    
    while i < len(words):
        # Check for quantity (number)
        quantity = 1
        if words[i].isdigit():
            quantity = int(words[i])
            i += 1
            if i >= len(words):
                break
        
        # Try to match multi-word items first (e.g., "cold coffee")
        matched = False
        for menu_item in menu.keys():
            menu_words = menu_item.split()
            if len(menu_words) > 1:
                # Check if the next words match the menu item
                if i + len(menu_words) <= len(words):
                    potential_match = " ".join(words[i:i+len(menu_words)])
                    if potential_match == menu_item:
                        order_dict[menu_item] = order_dict.get(menu_item, 0) + quantity
                        i += len(menu_words)
                        matched = True
                        break
        
        # If no multi-word match, try single word
        if not matched and i < len(words):
            word = words[i]
            if word in menu:
                order_dict[word] = order_dict.get(word, 0) + quantity
                i += 1
            else:
                print(f"⚠️  '{word}' is not available in the menu")
                i += 1
    
    return order_dict


def display_order_summary(order_dict, menu):
    """Display the current order summary"""
    if not order_dict:
        return
    
    print("\n" + "-"*40)
    print("Current Order Summary:".center(40))
    print("-"*40)
    total = 0
    for item, quantity in order_dict.items():
        price = menu[item]
        item_total = price * quantity
        total += item_total
        print(f"{item.capitalize():<25} x{quantity:>2}  ₹{item_total:>5}")
    print("-"*40)
    print(f"{'Subtotal:':<25} ₹{total:>5}")
    print("-"*40 + "\n")
    return total


def main():
    print("="*40)
    print("Welcome to our Restaurant!".center(40))
    print("="*40)
    
    menu = {
        "cold coffee": 80,
        "cappuccino": 80,
        "espresso": 90,
        "americano": 100,
        "latte": 100,
        "frappe": 120
    }
    
    display_menu(menu)
    
    total_bill = 0
    all_orders = {}
    
    while True:
        print("Enter the items you want to order (e.g., '2 latte, espresso' or 'cold coffee'):")
        order_input = input("> ").strip()
        
        if not order_input:
            print("⚠️  Please enter at least one item.\n")
            continue
        
        # Parse the order
        order_dict = parse_order(order_input, menu)
        
        if not order_dict:
            print("⚠️  No valid items found in your order. Please try again.\n")
            continue
        
        # Add to all orders
        for item, quantity in order_dict.items():
            all_orders[item] = all_orders.get(item, 0) + quantity
        
        # Display current order summary
        subtotal = display_order_summary(order_dict, menu)
        total_bill += subtotal
        
        print("✅ Your order has been added!")
        
        # Ask if they want to order more
        while True:
            choice = input("Do you want to order anything else? (y/n): ").strip().lower()
            if choice in ['y', 'yes', 'n', 'no']:
                break
            print("⚠️  Please enter 'y' or 'n'")
        
        if choice in ['n', 'no']:
            break
        print()
    
    # Final bill
    print("\n" + "="*40)
    print("FINAL BILL".center(40))
    print("="*40)
    for item, quantity in all_orders.items():
        price = menu[item]
        item_total = price * quantity
        print(f"{item.capitalize():<25} x{quantity:>2}  ₹{item_total:>5}")
    print("="*40)
    print(f"{'TOTAL BILL:':<25} ₹{total_bill:>5}")
    print("="*40)
    print("\nThank you for your order! Have a great day! 🎉")


if __name__ == "__main__":
    main()




