import unittest

from system import BST
from system import LinkedList
from system import NightbreakCafeSystem
from system import Node
from system import SLLQueue
from system import binary_search_first
from system import inorder
from system import merge_sort


class DataStructureTests(unittest.TestCase):
    def test_linked_list_insert_and_remove(self):
        linkedList = LinkedList()
        linkedList.insert(Node("latte"))
        linkedList.insert(Node("tea"))
        linkedList.insert(Node("muffin"))

        removed = linkedList.remove("tea")

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

    def test_bst_inorder(self):
        tree = BST()
        tree.insert((5.00, "NB100", "Latte"))
        tree.insert((3.50, "NB101", "Tea"))
        tree.insert((4.00, "NB102", "Croissant"))

        results = []
        inorder(tree.root, results)

        self.assertEqual(
            results,
            [
                (3.50, "NB101", "Tea"),
                (4.00, "NB102", "Croissant"),
                (5.00, "NB100", "Latte"),
            ],
        )

    def test_merge_sort_and_binary_search(self):
        prices = [6, 3, 5, 4, 3]
        merge_sort(prices)

        self.assertEqual(prices, [3, 3, 4, 5, 6])
        self.assertEqual(binary_search_first(prices, 3), 0)
        self.assertEqual(binary_search_first(prices, 5), 3)


class NightbreakSystemTests(unittest.TestCase):
    def setUp(self):
        self.system = NightbreakCafeSystem()

    def test_menu_is_sorted_by_price(self):
        menu = self.system.list_menu()

        self.assertEqual(
            [item["item_id"] for item in menu],
            ["NB103", "NB101", "NB102", "NB100", "NB104"],
        )

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
        self.assertEqual(order["queue_position"], 1)
        self.assertEqual(self.system.kitchen_queue.peek(), order["order_id"])

    def test_track_order_shows_orders_ahead(self):
        self.system.create_order(
            "Alex",
            "pickup",
            "",
            [{"item_id": "NB100", "quantity": 1}],
        )
        second_order = self.system.create_order(
            "Taylor",
            "pickup",
            "",
            [{"item_id": "NB103", "quantity": 1}],
        )

        tracked = self.system.track_order(second_order["order_id"])

        self.assertEqual(tracked["status"], "RECEIVED")
        self.assertEqual(tracked["queue_position"], 2)
        self.assertEqual(tracked["orders_ahead"], 1)

    def test_queue_then_complete_order(self):
        order = self.system.create_order(
            "Casey",
            "pickup",
            "",
            [{"item_id": "NB103", "quantity": 1}],
        )

        preparing = self.system.advance_queue()
        self.assertEqual(preparing["status"], "PREPARING")

        ready = self.system.advance_order_status(order["order_id"])
        self.assertEqual(ready["status"], "READY")

        completed = self.system.advance_order_status(order["order_id"])
        self.assertEqual(completed["status"], "COMPLETED")

        tracked = self.system.track_order(order["order_id"])
        self.assertEqual(tracked["status"], "COMPLETED")

    def test_queue_snapshot(self):
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

        queue = self.system.queue_snapshot()

        self.assertEqual(len(queue), 2)
        self.assertEqual(queue[0]["order_id"], first_order["order_id"])
        self.assertEqual(queue[1]["order_id"], second_order["order_id"])

    def test_track_missing_order_raises_error(self):
        with self.assertRaises(ValueError):
            self.system.track_order("NB-999")


if __name__ == "__main__":
    unittest.main()
