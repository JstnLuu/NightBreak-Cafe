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

    def find(self, predicate):
        currentNode = self.head
        while(currentNode is not None):
            if predicate(currentNode.data):
                return currentNode.data
            currentNode = currentNode.next
        return None

    def remove(self, predicate):
        previousNode = None
        currentNode = self.head

        while(currentNode is not None):
            if predicate(currentNode.data):
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

    def __iter__(self):
        currentNode = self.head
        while(currentNode is not None):
            yield currentNode.data
            currentNode = currentNode.next

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


class HashNode:
    def __init__(self, key, value, nextNode):
        self.key = key
        self.value = value
        self.next = nextNode


class HashTable:
    def __init__(self, capacity=11):
        self.capacity = capacity
        self.table = [None] * capacity
        self.size = 0

    def hash_function(self, key):
        text = str(key)
        total = 0
        for letter in text:
            total = total + ord(letter)
        return total % self.capacity

    def set(self, key, value):
        index = self.hash_function(key)
        currentNode = self.table[index]

        while(currentNode is not None):
            if currentNode.key == key:
                currentNode.value = value
                return
            currentNode = currentNode.next

        newNode = HashNode(key, value, self.table[index])
        self.table[index] = newNode
        self.size += 1

    def get(self, key, default=None):
        index = self.hash_function(key)
        currentNode = self.table[index]

        while(currentNode is not None):
            if currentNode.key == key:
                return currentNode.value
            currentNode = currentNode.next
        return default

    def delete(self, key):
        index = self.hash_function(key)
        currentNode = self.table[index]
        previousNode = None

        while(currentNode is not None):
            if currentNode.key == key:
                if previousNode is None:
                    self.table[index] = currentNode.next
                else:
                    previousNode.next = currentNode.next
                self.size -= 1
                return currentNode.value
            previousNode = currentNode
            currentNode = currentNode.next
        return None

    def increment(self, key, amount=1):
        value = self.get(key, 0)
        value = value + amount
        self.set(key, value)
        return value

    def items(self):
        pairs = []
        for bucket in self.table:
            currentNode = bucket
            while(currentNode is not None):
                pairs.append((currentNode.key, currentNode.value))
                currentNode = currentNode.next
        return pairs

    def values(self):
        values = []
        for key, value in self.items():
            values.append(value)
        return values

    def __len__(self):
        return self.size


class BSTNode:
    def __init__(self, data, item):
        self.left = None
        self.right = None
        self.data = data
        self.items = [item]

    def insert(self, data, item):
        if(self.data == data):
            self.items.append(item)
        elif(data < self.data):
            if(self.left is None):
                self.left = BSTNode(data, item)
            else:
                self.left.insert(data, item)
        else:
            if(self.right is None):
                self.right = BSTNode(data, item)
            else:
                self.right.insert(data, item)

    def range_query(self, minimum, maximum, results):
        if(minimum < self.data and self.left != None):
            self.left.range_query(minimum, maximum, results)
        if(minimum <= self.data and self.data <= maximum):
            for item in self.items:
                results.append(item)
        if(maximum > self.data and self.right != None):
            self.right.range_query(minimum, maximum, results)

    def inorder(self, results):
        if(self.left != None):
            self.left.inorder(results)
        for item in self.items:
            results.append(item)
        if(self.right != None):
            self.right.inorder(results)


class BST:
    def __init__(self):
        self.root = None

    def insert(self, data, item):
        if(self.root is None):
            self.root = BSTNode(data, item)
        else:
            self.root.insert(data, item)

    def range_query(self, minimum, maximum):
        results = []
        if(self.root):
            self.root.range_query(minimum, maximum, results)
        return results

    def inorder(self):
        results = []
        if(self.root):
            self.root.inorder(results)
        return results


def merge_sort(arr, key=None):
    if key is None:
        key = lambda value: value

    if len(arr) > 1:
        left_arr = arr[:len(arr)//2]
        right_arr = arr[len(arr)//2:]

        # recursion
        merge_sort(left_arr, key)
        merge_sort(right_arr, key)

        # merge
        i = 0
        j = 0
        k = 0

        while i < len(left_arr) and j < len(right_arr):
            if key(left_arr[i]) <= key(right_arr[j]):
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


def binary_search_exact(arr, target, key=None):
    if key is None:
        key = lambda value: value

    low = 0
    high = len(arr) - 1

    while(low <= high):
        mid = (low + high) // 2
        if(key(arr[mid]) == target):
            return arr[mid]
        elif(key(arr[mid]) < target):
            low = mid + 1
        else:
            high = mid - 1
    return None


def binary_search_best_affordable(arr, budget, key=None):
    if key is None:
        key = lambda value: value

    low = 0
    high = len(arr) - 1
    best = None

    while(low <= high):
        mid = (low + high) // 2
        if(key(arr[mid]) <= budget):
            best = arr[mid]
            low = mid + 1
        else:
            high = mid - 1
    return best


def reverse_list(values):
    reversed_values = []
    index = len(values) - 1
    while(index >= 0):
        reversed_values.append(values[index])
        index -= 1
    return reversed_values


class NightbreakCafeSystem:
    def __init__(self):
        self.menu = LinkedList()
        self.menu_by_id = HashTable(17)
        self.menu_by_price = BST()
        self.active_orders = HashTable(23)
        self.completed_orders = LinkedList()
        self.item_sales = HashTable(17)
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
            self.menu_by_id.set(item["item_id"], item)
            self.menu_by_price.insert(item["price"], item)

    def categories(self):
        categories = []
        for item in self.menu:
            if item["category"] not in categories:
                categories.append(item["category"])
        merge_sort(categories)
        return ["All"] + categories

    def list_menu(self, category="All", max_price=None):
        if max_price is None:
            items = self.menu.to_list()
        else:
            items = self.menu_by_price.range_query(0, max_price)

        filtered = []
        for item in items:
            if(category == "All" or item["category"] == category):
                filtered.append(item)

        merge_sort(filtered, key=lambda item: item["price"])
        return filtered

    def recommend_under_budget(self, budget, category="All"):
        items = self.menu_by_price.inorder()
        if(category != "All"):
            filtered = []
            for item in items:
                if(item["category"] == category):
                    filtered.append(item)
            items = filtered
        return binary_search_best_affordable(items, budget, key=lambda item: item["price"])

    def create_order(self, customer_name, order_type, location_details, cart_items):
        if(len(cart_items) == 0):
            raise ValueError("Cart cannot be empty.")

        if customer_name.strip() == "":
            customer_name = "Guest"

        items = []
        subtotal = 0
        item_count = 0

        for raw_item in cart_items:
            menu_item = self.menu_by_id.get(raw_item["item_id"])
            if(menu_item is None):
                raise ValueError("Menu item was not found.")

            quantity = raw_item.get("quantity", 1)
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

        self.active_orders.set(order_id, order)
        self.kitchen_queue.enqueue(order_id)
        return order

    def advance_queue(self):
        order_id = self.kitchen_queue.dequeue()
        order = self.active_orders.get(order_id)
        if(order is None):
            raise ValueError("Order was not found.")
        if(order["status"] != "RECEIVED"):
            raise ValueError("Only received orders can start here.")
        order["status"] = "PREPARING"
        return order

    def advance_order_status(self, order_id):
        order = self.active_orders.get(order_id)
        if(order is None):
            raise ValueError("Order was not found.")

        if(order["status"] == "PREPARING"):
            order["status"] = "READY"
            return order

        if(order["status"] == "READY"):
            order["status"] = "COMPLETED"
            for item in order["items"]:
                self.item_sales.increment(item["item_id"], item["quantity"])
            self.completed_orders.insert(Node(order))
            self.active_orders.delete(order_id)
            return order

        raise ValueError("Order must be preparing or ready.")

    def queue_snapshot(self):
        queue_ids = self.kitchen_queue.to_list()
        queue_orders = []
        for order_id in queue_ids:
            order = self.active_orders.get(order_id)
            if(order is not None):
                queue_orders.append(order)
        return queue_orders

    def active_order_list(self):
        orders = self.active_orders.values()
        merge_sort(orders, key=lambda order: int(order["order_id"].split("-")[1]))
        return orders

    def completed_order_list(self):
        orders = self.completed_orders.to_list()
        merge_sort(orders, key=lambda order: int(order["order_id"].split("-")[1]))
        return orders

    def find_completed_order_binary(self, order_id):
        if("-" not in order_id):
            return None

        target_number = int(order_id.split("-")[1])
        orders = self.completed_order_list()
        return binary_search_exact(
            orders,
            target_number,
            key=lambda order: int(order["order_id"].split("-")[1]),
        )

    def popular_items(self):
        counts = []
        for item_id, quantity in self.item_sales.items():
            menu_item = self.menu_by_id.get(item_id)
            if(menu_item is not None):
                counts.append(
                    {
                        "item_id": item_id,
                        "name": menu_item["name"],
                        "quantity": quantity,
                    }
                )
        merge_sort(counts, key=lambda item: item["quantity"])
        return reverse_list(counts)

    def total_revenue(self):
        total = 0
        for order in self.completed_orders:
            total += order["subtotal"]
        return round(total, 2)

    def dashboard(self):
        return {
            "menu_count": len(self.menu),
            "queue_length": len(self.kitchen_queue),
            "active_order_count": len(self.active_orders),
            "completed_order_count": len(self.completed_orders),
            "total_revenue": self.total_revenue(),
            "queue": self.queue_snapshot(),
            "active_orders": self.active_order_list(),
            "completed_orders": self.completed_order_list(),
            "popular_items": self.popular_items(),
        }


LinkedQueue = SLLQueue
BinarySearchTree = BST
