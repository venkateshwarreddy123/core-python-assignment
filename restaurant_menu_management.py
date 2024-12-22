def add_item_to_menu(menu, item):
    menu.append(item)
    return menu

def remove_item_from_menu(menu, item):
    if item in menu:
        menu.remove(item)
    else:
        print(f"Item '{item}' not found in the menu.")
    return menu

def check_item_availability(menu, item):
    if item in menu:
        return f"{item} is available"
    else:
        return f"{item} is not available"

initial_menu = ["Pizza", "Burger", "Pasta", "Salad"]

add_item = "Tacos"
updated_menu = add_item_to_menu(initial_menu, add_item)

remove_item = "Salad"
updated_menu = remove_item_from_menu(updated_menu, remove_item)

check_item = "Pizza"
availability = check_item_availability(updated_menu, check_item)

print(f"Updated menu: {updated_menu}")
print(f'Availability: {availability}')
