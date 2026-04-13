import time

from system import NightbreakCafeSystem
from system import SLLQueue
from system import binary_search_first
from system import merge_sort


def run_benchmarks():
    results = {}

    system = NightbreakCafeSystem()
    for number in range(50):
        system.create_order(
            "Bench User " + str(number),
            "pickup",
            "",
            [
                {"item_id": "NB100", "quantity": 1},
                {"item_id": "NB102", "quantity": 1},
            ],
        )

    start = time.time()
    for number in range(50):
        order = system.advance_queue()
        system.advance_order_status(order["order_id"])
        system.advance_order_status(order["order_id"])
    end = time.time()
    results["50_order_workflow_seconds"] = round(end - start, 6)

    queue = SLLQueue()
    start = time.time()
    for number in range(1000):
        queue.enqueue(number)
    for number in range(1000):
        queue.dequeue()
    end = time.time()
    results["1000_queue_ops_seconds"] = round(end - start, 6)

    values = list(range(1000, 0, -1))
    start = time.time()
    merge_sort(values)
    end = time.time()
    results["merge_sort_1000_values_seconds"] = round(end - start, 6)

    start = time.time()
    binary_search_first(values, 750)
    end = time.time()
    results["binary_search_seconds"] = round(end - start, 6)

    return results


if __name__ == "__main__":
    benchmark_results = run_benchmarks()
    for key in benchmark_results:
        print(key + ": " + str(benchmark_results[key]))
    for number in range(1000):
        hash_table.get("order-" + str(number))
    end = time.time()
    results["1000_hash_lookups_seconds"] = round(end - start, 6)

    queue = SLLQueue()
    start = time.time()
    for number in range(1000):
        queue.enqueue(number)
    for number in range(1000):
        queue.dequeue()
    end = time.time()
    results["1000_queue_ops_seconds"] = round(end - start, 6)

    values = list(range(1000, 0, -1))
    start = time.time()
    merge_sort(values)
    end = time.time()
    results["merge_sort_1000_values_seconds"] = round(end - start, 6)

    return results


if __name__ == "__main__":
    benchmark_results = run_benchmarks()
    for key in benchmark_results:
        print(key + ": " + str(benchmark_results[key]))
