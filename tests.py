import unittest

from system import BST
from system import HashTable
from system import LinkedList
from system import NightbreakCafeSystem
from system import Node
from system import SLLQueue
from system import binary_search_best_affordable
from system import binary_search_exact
from system import merge_sort


class DataStructureTests(unittest.TestCase):
    def test_linked_list_insert_and_remove(self):
        linkedList = LinkedList()
        linkedList.insert(Node("latte"))
        linkedList.insert(Node("tea"))
        linkedList.insert(Node("muffin"))

        removed = linkedList.remove(lambda value: value == "tea")

        self.assertEqual(removed, "tea")
        self.assertEqual(linkedList.to_list(), ["latte", "muffin"])

    def test_queue_fifo(self):
        queue = SLLQueue()
        queue.enqueue("NB-1")
        queue.enqueue("NB-2")
        queue.enqueue("NB-3")

        self.assertEqual(queue.dequeue(), "NB-1")
        self.assertEqual(queue.dequeue(), "NB-2")
        self.assertEqual(queue.peek(), "NB-3")

    def test_hash_table_lookup_and_increment(self):
        table = HashTable(7)
        table.set("NB100", "Latte")
        table.increment("NB102", 2)

        self.assertEqual(table.get("NB100"), "Latte")
        self.assertEqual(table.get("NB102"), 2)
        self.assertEqual(table.get("missing", "none"), "none")

    def test_bst_range_query(self):
        tree = BST()
        tree.insert(5.00, "Latte")
        tree.insert(3.50, "Tea")
        tree.insert(4.00, "Croissant")
        tree.insert(6.50, "Sandwich")

        results = tree.range_query(3.75, 5.25)

        self.assertEqual(results, ["Croissant", "Latte"])

    def test_merge_sort_and_binary_search(self):
        prices = [6.50, 3.00, 5.00, 4.00, 3.50]
        merge_sort(prices)

        self.assertEqual(prices, [3.00, 3.50, 4.00, 5.00, 6.50])
        self.assertEqual(binary_search_exact(prices, 4.00), 4.00)
        self.assertEqual(binary_search_best_affordable(prices, 4.75), 4.00)


class NightbreakSystemTests(unittest.TestCase):
    def setUp(self):
        self.system = NightbreakCafeSystem()

    def test_create_order_adds_to_queue(self):
        order = self.system.create_order(
            "Jordan",
            "pickup",
            "",
            [
                {"item_id": "NB100", "quantity": 1},
                {"item_id": "NB102", "quantity": 2},
            ],
        )

        self.assertEqual(order["status"], "RECEIVED")
        self.assertEqual(order["item_count"], 3)
        self.assertEqual(self.system.kitchen_queue.peek(), order["order_id"])
        self.assertIsNotNone(self.system.active_orders.get(order["order_id"]))

    def test_queue_then_complete_order(self):
        order = self.system.create_order(
            "Casey",
            "pickup",
            "",
            [{"item_id": "NB103", "quantity": 1}],
        )

        self.system.advance_queue()
        ready = self.system.advance_order_status(order["order_id"])
        self.assertEqual(ready["status"], "READY")
        completed = self.system.advance_order_status(order["order_id"])

        self.assertEqual(completed["status"], "COMPLETED")
        self.assertIsNone(self.system.active_orders.get(order["order_id"]))
        self.assertEqual(self.system.completed_order_list()[0]["order_id"], order["order_id"])

    def test_dashboard_popular_items(self):
        first_order = self.system.create_order(
            "Alex",
            "pickup",
            "",
            [{"item_id": "NB100", "quantity": 2}],
        )
        second_order = self.system.create_order(
            "Taylor",
            "pickup",
            "",
            [
                {"item_id": "NB100", "quantity": 1},
                {"item_id": "NB103", "quantity": 1},
            ],
        )

        self.system.advance_queue()
        self.system.advance_order_status(first_order["order_id"])
        self.system.advance_order_status(first_order["order_id"])
        self.system.advance_queue()
        self.system.advance_order_status(second_order["order_id"])
        self.system.advance_order_status(second_order["order_id"])

        dashboard = self.system.dashboard()

        self.assertEqual(dashboard["popular_items"][0]["item_id"], "NB100")
        self.assertEqual(dashboard["completed_order_count"], 2)
        self.assertEqual(dashboard["queue_length"], 0)

    def test_recommend_under_budget(self):
        recommendation = self.system.recommend_under_budget(4.25, "All")

        self.assertIsNotNone(recommendation)
        self.assertEqual(recommendation["name"], "Croissant")

    def test_completed_order_binary_search(self):
        first_order = self.system.create_order(
            "Jordan",
            "pickup",
            "",
            [{"item_id": "NB100", "quantity": 1}],
        )
        second_order = self.system.create_order(
            "Taylor",
            "pickup",
            "",
            [{"item_id": "NB102", "quantity": 1}],
        )

        self.system.advance_queue()
        self.system.advance_order_status(first_order["order_id"])
        self.system.advance_order_status(first_order["order_id"])
        self.system.advance_queue()
        self.system.advance_order_status(second_order["order_id"])
        self.system.advance_order_status(second_order["order_id"])

        found = self.system.find_completed_order_binary(second_order["order_id"])

        self.assertIsNotNone(found)
        self.assertEqual(found["order_id"], second_order["order_id"])


if __name__ == "__main__":
    unittest.main()
