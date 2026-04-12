from system import NightbreakCafeSystem


def print_line():
    print("\n" + "-" * 50)


def show_menu(system):
    print_line()
    print("Nightbreak Cafe Menu")
    for item in system.list_menu():
        print(
            item["item_id"]
            + " | "
            + item["name"]
            + " | "
            + item["category"]
            + " | $"
            + format(item["price"], ".2f")
        )


def show_recommendation(system):
    print_line()
    budget = float(input("Budget: ").strip())
    item = system.recommend_under_budget(budget)

    if item is None:
        print("No item fits that budget.")
    else:
        print(
            "Recommended:"
            + " "
            + item["name"]
            + " ($"
            + format(item["price"], ".2f")
            + ")"
        )


def show_order(order):
    print_line()
    print("Order:", order["order_id"])
    print("Customer:", order["customer_name"])
    print("Status:", order["status"])
    print("Subtotal: $" + format(order["subtotal"], ".2f"))
    print("Items:")
    for item in order["items"]:
        print("  " + str(item["quantity"]) + " x " + item["name"])


def create_order(system):
    print_line()
    print("Create Order")
    name = input("Customer name: ").strip()
    order_type = input("Order type: ").strip()
    location = input("Notes: ").strip()

    cart_items = []
    while True:
        item_id = input("Item id (or done): ").strip()
        if item_id.lower() == "done":
            break
        quantity = int(input("Quantity: ").strip())
        cart_items.append({"item_id": item_id, "quantity": quantity})

    order = system.create_order(name, order_type, location, cart_items)
    show_order(order)


def start_next_order(system):
    order = system.advance_queue()
    show_order(order)


def advance_order(system):
    print_line()
    order_id = input("Order id: ").strip()
    order = system.advance_order_status(order_id)
    show_order(order)


def show_dashboard(system):
    dashboard = system.dashboard()

    print_line()
    print("Dashboard")
    print("Menu items:", dashboard["menu_count"])
    print("Queue length:", dashboard["queue_length"])
    print("Active orders:", dashboard["active_order_count"])
    print("Completed orders:", dashboard["completed_order_count"])
    print("Total revenue: $" + format(dashboard["total_revenue"], ".2f"))

    print_line()
    print("Popular Items")
    if len(dashboard["popular_items"]) == 0:
        print("None")
    else:
        for item in dashboard["popular_items"]:
            print(item["name"] + " | sold: " + str(item["quantity"]))


def run_demo(system):
    system.reset()
    first_order = system.create_order(
        "Mia",
        "pickup",
        "",
        [
            {"item_id": "NB100", "quantity": 1},
            {"item_id": "NB102", "quantity": 1},
        ],
    )
    second_order = system.create_order(
        "Leo",
        "pickup",
        "",
        [{"item_id": "NB103", "quantity": 2}],
    )

    print("Created", first_order["order_id"])
    print("Created", second_order["order_id"])

    started = system.advance_queue()
    print("Started", started["order_id"])
    ready = system.advance_order_status(started["order_id"])
    print("Moved to", ready["status"])
    completed = system.advance_order_status(started["order_id"])
    print("Moved to", completed["status"])
    show_dashboard(system)


def print_menu():
    print_line()
    print("Nightbreak Cafe")
    print("1. Show menu")
    print("2. Recommend item")
    print("3. Create order")
    print("4. Start next order")
    print("5. Advance order")
    print("6. Show dashboard")
    print("7. Run demo")
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
                show_recommendation(system)
            elif choice == "3":
                create_order(system)
            elif choice == "4":
                start_next_order(system)
            elif choice == "5":
                advance_order(system)
            elif choice == "6":
                show_dashboard(system)
            elif choice == "7":
                run_demo(system)
            elif choice == "0":
                print("Goodbye.")
                break
            else:
                print("Try again.")
        except ValueError as error:
            print("Error:", error)
        except Exception as error:
            print("Error:", error)


if __name__ == "__main__":
    main()
