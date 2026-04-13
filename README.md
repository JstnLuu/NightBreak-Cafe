# Nightbreak Cafe Mobile Ordering System

This is our CSCI 046 final project. We kept the project simple so the data structures are easy to see, explain, and defend during the presentation.

The program shows a small cafe ordering workflow:

- show the menu
- filter the menu by category or price
- recommend an item under a budget
- create an order
- move the order through the kitchen queue
- track completed orders
- show simple sales results

## Data Structures and Algorithms

- `LinkedList`
  Stores the menu and the completed-order history.
- `SLLQueue`
  Stores the kitchen line in first-in, first-out order.
- `HashTable`
  Stores menu items by id, active orders by id, and sales totals.
- `BST`
  Stores menu items by price.
- `merge_sort`
  Sorts values and sales results.
- `binary_search`
  Finds exact values and the best item under a budget.

## Menu

- `NB100` Latte
- `NB101` Tea
- `NB102` Croissant
- `NB103` Muffin
- `NB104` Sandwich

## Files

- `app.py`
  Terminal demo.
- `system.py`
  Data structures and main ordering logic.
- `tests.py`
  Unit tests.
- `benchmarks.py`
  Small timing script.
- `benchmark_results.txt`
  Saved benchmark output.
- `Nightbreak_Cafe_Final_Report.docx`
  Final report.
- `Nightbreak_Cafe_Presentation.pptx`
  Final presentation.
- `Nightbreak_Cafe_Presentation_Script.docx`
  Speaking notes for the slides.

## Run

```bash
python3 app.py
```

## Test

```bash
python3 tests.py
```

## Benchmark

```bash
python3 benchmarks.py
```

## Notes

- The final version stays in the terminal on purpose so the custom data structures stay front and center.
- Personal placeholders are still left in the report and slide deck for names, date, and images.
