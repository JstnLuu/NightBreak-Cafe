class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def insert(self, newNode):
        if self.head is None:
            self.head = newNode
        else:
            lastNode = self.head
            while(lastNode.next):
                lastNode = lastNode.next
            lastNode.next = newNode

    def remove(self, value):
        previousNode = None
        currentNode = self.head

        while(currentNode is not None):
            if currentNode.data == value:
                if previousNode is None:
                    self.head = currentNode.next
                else:
                    previousNode.next = currentNode.next
                return currentNode.data
            previousNode = currentNode
            currentNode = currentNode.next
        return None

    def to_list(self):
        values = []
        currentNode = self.head
        while(currentNode is not None):
            values.append(currentNode.data)
            currentNode = currentNode.next
        return values

    def __len__(self):
        count = 0
        currentNode = self.head
        while(currentNode is not None):
            count += 1
            currentNode = currentNode.next
        return count


class IsEmptyError(Exception):
    pass


class SLLQueue:
    class Node:
        def __init__(self, element, _next):
            self.element = element
            self._next = _next

    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0

    def __len__(self):
        return self.size

    def is_empty(self):
        return self.size == 0

    def enqueue(self, element):
        new = self.Node(element, None)
        if self.is_empty():
            self.head = new
        else:
            self.tail._next = new
        self.tail = new
        self.size += 1

    def dequeue(self):
        if self.is_empty():
            raise IsEmptyError("Empty queue so cannot dequeue.")
        result = self.head.element
        self.head = self.head._next
        self.size -= 1
        if self.is_empty():
            self.tail = None
        return result

    def peek(self):
        if self.is_empty():
            return None
        return self.head.element

    def to_list(self):
        values = []
        currentNode = self.head
        while(currentNode is not None):
            values.append(currentNode.element)
            currentNode = currentNode._next
        return values


class BSTNode:
    def __init__(self, data):
        self.left = None
        self.right = None
        self.data = data

    def insert(self, data):
        if(self.data == data):
            raise Exception("Data already exist within tree")
        elif(self.data > data):
            if(self.left):
                self.left.insert(data)
            else:
                self.left = BSTNode(data)
        else:
            if(self.right):
                self.right.insert(data)
            else:
                self.right = BSTNode(data)


class BST:
    def __init__(self):
        self.root = None

    def insert(self, data):
        if(self.root):
            self.root.insert(data)
        else:
            self.root = BSTNode(data)


def inorder(node, results):
    if node is not None:
        inorder(node.left, results)
        results.append(node.data)
        inorder(node.right, results)


def merge_sort(arr):
    if len(arr) > 1:
        left_arr = arr[:len(arr)//2]
        right_arr = arr[len(arr)//2:]

        merge_sort(left_arr)
        merge_sort(right_arr)

        i = 0
        j = 0
        k = 0

        while i < len(left_arr) and j < len(right_arr):
            if left_arr[i] < right_arr[j]:
                arr[k] = left_arr[i]
                i += 1
            else:
                arr[k] = right_arr[j]
                j += 1
            k += 1

        while i < len(left_arr):
            arr[k] = left_arr[i]
            i += 1
            k += 1

        while j < len(right_arr):
            arr[k] = right_arr[j]
            j += 1
            k += 1

    return arr


def binary_search(lo, hi, condition):
    while lo <= hi:
        mid = (lo + hi) // 2
        result = condition(mid)

        if result == "found":
            return mid
        elif result == "left":
            hi = mid - 1
        else:
            lo = mid + 1

    return -1


def helper(cards, mid, query):
    mid_number = cards[mid]

    if mid_number == query:
        if mid - 1 >= 0 and cards[mid - 1] == query:
            return "left"
        else:
            return "found"
    elif mid_number < query:
        return "right"
    else:
        return "left"


def binary_search_first(cards, query):
    low, high = 0, len(cards) - 1

    while low <= high:
        mid = (low + high) // 2
        decision = helper(cards, mid, query)

        if decision == "found":
            return mid
        elif decision == "left":
            high = mid - 1
        else:
            low = mid + 1

    return -1


def find_menu_item_by_id(menu, item_id):
    currentNode = menu.head

    while(currentNode is not None):
        item = currentNode.data
        if item["item_id"] == item_id:
            return item
        currentNode = currentNode.next

    return None


def sort_orders_by_number(order_list):
    sortable = []
    currentNode = order_list.head

    while(currentNode is not None):
        order = currentNode.data
        order_number = int(order["order_id"].split("-")[1])
        sortable.append((order_number, order))
        currentNode = currentNode.next

    merge_sort(sortable)
    return sortable


def find_order_by_id(order_list, order_id):
    if "-" not in order_id:
        return None

    try:
        target_number = int(order_id.split("-")[1])
    except ValueError:
        return None

    sortable = sort_orders_by_number(order_list)
    if len(sortable) == 0:
        return None

    numbers = []
    index = 0

    while(index < len(sortable)):
        numbers.append(sortable[index][0])
        index += 1

    position = binary_search_first(numbers, target_number)
    if position == -1:
        return None

    return sortable[position][1]


def queue_position(queue, order_id):
    position = 1
    currentNode = queue.head

    while(currentNode is not None):
        if currentNode.element == order_id:
            return position
        position += 1
        currentNode = currentNode._next

    return None


def order_view(order, queue):
    position = None
    orders_ahead = None
    message = "Order received."

    if order["status"] == "RECEIVED":
        position = queue_position(queue, order["order_id"])
        if position is not None:
            orders_ahead = position - 1

        if orders_ahead is None:
            message = "Order received."
        elif orders_ahead == 0:
            message = "Your order is next in line."
        else:
            message = "There are " + str(orders_ahead) + " orders ahead of you."

    elif order["status"] == "PREPARING":
        message = "Your order is being prepared."

    elif order["status"] == "READY":
        message = "Your order is ready for pickup."

    elif order["status"] == "COMPLETED":
        message = "Your order has been completed."

    return {
        "order_id": order["order_id"],
        "customer_name": order["customer_name"],
        "order_type": order["order_type"],
        "location_details": order["location_details"],
        "items": order["items"],
        "item_count": order["item_count"],
        "subtotal": order["subtotal"],
        "status": order["status"],
        "queue_position": position,
        "orders_ahead": orders_ahead,
        "message": message,
    }


class NightbreakCafeSystem:
    def __init__(self):
        self.menu = LinkedList()
        self.menu_by_price = BST()
        self.orders = LinkedList()
        self.kitchen_queue = SLLQueue()
        self.next_order_number = 1
        self.load_menu()

    def reset(self):
        self.__init__()

    def load_menu(self):
        menu_items = [
            {"item_id": "NB100", "name": "Latte", "category": "Drink", "price": 5.00},
            {"item_id": "NB101", "name": "Tea", "category": "Drink", "price": 3.50},
            {"item_id": "NB102", "name": "Croissant", "category": "Food", "price": 4.00},
            {"item_id": "NB103", "name": "Muffin", "category": "Food", "price": 3.00},
            {"item_id": "NB104", "name": "Sandwich", "category": "Food", "price": 6.50},
        ]

        for item in menu_items:
            self.menu.insert(Node(item))
            self.menu_by_price.insert((item["price"], item["item_id"], item))

    def list_menu(self):
        sorted_values = []
        inorder(self.menu_by_price.root, sorted_values)

        items = []
        index = 0
        while(index < len(sorted_values)):
            items.append(sorted_values[index][2])
            index += 1

        return items

    def create_order(self, customer_name, order_type, location_details, cart_items):
        if cart_items is None or len(cart_items) == 0:
            raise ValueError("Cart cannot be empty.")

        if customer_name.strip() == "":
            customer_name = "Guest"

        items = []
        subtotal = 0
        item_count = 0

        index = 0
        while(index < len(cart_items)):
            raw_item = cart_items[index]
            menu_item = find_menu_item_by_id(self.menu, raw_item["item_id"])

            if(menu_item is None):
                raise ValueError("Menu item was not found.")

            quantity = 1
            if "quantity" in raw_item:
                quantity = raw_item["quantity"]
            if(quantity < 1):
                quantity = 1

            line_total = round(menu_item["price"] * quantity, 2)
            items.append(
                {
                    "item_id": menu_item["item_id"],
                    "name": menu_item["name"],
                    "quantity": quantity,
                    "unit_price": menu_item["price"],
                    "line_total": line_total,
                }
            )
            subtotal += line_total
            item_count += quantity
            index += 1

        order_id = "NB-" + str(self.next_order_number)
        self.next_order_number += 1

        order = {
            "order_id": order_id,
            "customer_name": customer_name,
            "order_type": order_type,
            "location_details": location_details,
            "items": items,
            "item_count": item_count,
            "subtotal": round(subtotal, 2),
            "status": "RECEIVED",
        }

        self.orders.insert(Node(order))
        self.kitchen_queue.enqueue(order_id)
        return order_view(order, self.kitchen_queue)

    def track_order(self, order_id):
        order = find_order_by_id(self.orders, order_id)

        if(order is None):
            raise ValueError("Order was not found.")

        return order_view(order, self.kitchen_queue)

    def advance_queue(self):
        order_id = self.kitchen_queue.dequeue()
        order = find_order_by_id(self.orders, order_id)

        if(order is None):
            raise ValueError("Order was not found.")
        if(order["status"] != "RECEIVED"):
            raise ValueError("Only received orders can start here.")

        order["status"] = "PREPARING"
        return order_view(order, self.kitchen_queue)

    def advance_order_status(self, order_id):
        order = find_order_by_id(self.orders, order_id)

        if(order is None):
            raise ValueError("Order was not found.")

        if(order["status"] == "PREPARING"):
            order["status"] = "READY"
            return order_view(order, self.kitchen_queue)

        if(order["status"] == "READY"):
            order["status"] = "COMPLETED"
            return order_view(order, self.kitchen_queue)

        raise ValueError("Order must be preparing or ready.")

    def queue_snapshot(self):
        order_ids = self.kitchen_queue.to_list()
        queue_orders = []

        index = 0
        while(index < len(order_ids)):
            order = find_order_by_id(self.orders, order_ids[index])
            if(order is not None):
                queue_orders.append(order_view(order, self.kitchen_queue))
            index += 1

        return queue_orders


LinkedQueue = SLLQueue
BinarySearchTree = BST
