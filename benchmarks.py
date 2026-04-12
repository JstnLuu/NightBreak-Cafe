import time

from system import HashTable
from system import NightbreakCafeSystem
from system import SLLQueue
from system import merge_sort


def run_benchmarks():
    results = {}

    system = NightbreakCafeSystem()
    for _ in range(100):
        system.create_order(
            "Bench User",
            "pickup",
            "",
            [
                {"item_id": "NB100", "quantity": 1},
                {"item_id": "NB102", "quantity": 1},
            ],
        )

    start = time.perf_counter()
    for _ in range(100):
        order = system.advance_queue()
        system.advance_order_status(order["order_id"])
        system.advance_order_status(order["order_id"])
    results["100_order_workflow_seconds"] = round(time.perf_counter() - start, 6)

    hash_table = HashTable(101)
    for index in range(2000):
        hash_table.set("order-" + str(index), index)

    start = time.perf_counter()
    for index in range(2000):
        hash_table.get("order-" + str(index))
    results["2000_hash_lookups_seconds"] = round(time.perf_counter() - start, 6)

    queue = SLLQueue()
    start = time.perf_counter()
    for index in range(2000):
        queue.enqueue(index)
    for _ in range(2000):
        queue.dequeue()
    results["2000_queue_ops_seconds"] = round(time.perf_counter() - start, 6)

    values = list(range(2000, 0, -1))
    start = time.perf_counter()
    merge_sort(values)
    results["merge_sort_2000_values_seconds"] = round(time.perf_counter() - start, 6)

    return results


if __name__ == "__main__":
    benchmark_results = run_benchmarks()
    for key in benchmark_results:
        print(key + ": " + str(benchmark_results[key]))
