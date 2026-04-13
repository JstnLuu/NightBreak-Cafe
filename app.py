from system import NightbreakCafeSystem


def print_line():
    print("\n" + "-" * 50)


def show_menu(system):
    print_line()
    print("Nightbreak Cafe Menu")

    items = system.list_menu()
    for item in items:
        print(
            item["item_id"]
            + " | "
            + item["name"]
            + " | "
            + item["category"]
            + " | $"
            + format(item["price"], ".2f")
        )


def show_order(order):
    print_line()
    print("Order:", order["order_id"])
    print("Customer:", order["customer_name"])
    print("Status:", order["status"])
    print("Subtotal: $" + format(order["subtotal"], ".2f"))

    if order["queue_position"] is not None:
        print("Queue position:", order["queue_position"])

    print(order["message"])
    print("Items:")
    for item in order["items"]:
        print("  " + str(item["quantity"]) + " x " + item["name"])


def create_order(system):
    print_line()
    print("Create Order")
    name = input("Customer name: ").strip()
    order_type = input("Order type: ").strip()
    notes = input("Notes: ").strip()

    cart_items = []
    while True:
        item_id = input("Item id (or done): ").strip()
        if item_id.lower() == "done":
            break

        quantity = int(input("Quantity: ").strip())
        cart_items.append({"item_id": item_id, "quantity": quantity})

    order = system.create_order(name, order_type, notes, cart_items)
    show_order(order)


def track_order(system):
    print_line()
    order_id = input("Order id: ").strip()
    order = system.track_order(order_id)
    show_order(order)


def start_next_order(system):
    order = system.advance_queue()
    show_order(order)


def advance_order(system):
    print_line()
    order_id = input("Order id: ").strip()
    order = system.advance_order_status(order_id)
    show_order(order)


def print_menu():
    print_line()
    print("Nightbreak Cafe")
    print("1. Show menu")
    print("2. Create order")
    print("3. Track order")
    print("4. Start next order")
    print("5. Advance order")
    print("0. Exit")


def main():
    system = NightbreakCafeSystem()

    while True:
        print_menu()
        choice = input("Choice: ").strip()

        try:
            if choice == "1":
                show_menu(system)
            elif choice == "2":
                create_order(system)
            elif choice == "3":
                track_order(system)
            elif choice == "4":
                start_next_order(system)
            elif choice == "5":
                advance_order(system)
            elif choice == "0":
                print("Goodbye.")
                break
            else:
                print("Try again.")
        except ValueError as error:
            print("Error:", error)


if __name__ == "__main__":
    main()
