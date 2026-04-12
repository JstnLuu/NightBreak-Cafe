# Nightbreak Cafe Mobile Ordering System

This is a smaller version of our CSCI 046 final project. We kept the idea of a cafe mobile ordering system, but we simplified the prototype so the data structures are easier to see and explain.

The program uses custom data structures from class to:

- store the menu
- place orders in a first-in, first-out kitchen queue
- look up menu items and active orders
- organize menu prices for budget recommendations
- sort data for reports

## Data Structures

- `LinkedList`
  Stores the cafe menu and completed orders.
- `SLLQueue`
  Stores orders waiting for the kitchen.
- `HashTable`
  Stores menu items by id, active orders by id, and sales counts.
- `BST`
  Stores menu items by price.
- `merge_sort`
  Sorts menu items, completed orders, and reports.
- `binary_search`
  Helps find completed orders and the best item under a budget.

## Simple Menu

- `NB100` Latte
- `NB101` Tea
- `NB102` Croissant
- `NB103` Muffin
- `NB104` Sandwich

## Files

- `app.py`
  Small terminal demo.
- `system.py`
  Data structures and order logic.
- `tests.py`
  Unit tests.
- `benchmarks.py`
  Small benchmark script.
- `benchmark_results.txt`
  Saved benchmark snapshot used in the report and slides.
- `Nightbreak_Cafe_Final_Report.docx`
  Final report synced to the simplified codebase.
- `Nightbreak_Cafe_Presentation.pptx`
  Final slide deck synced to the simplified codebase.
- `Nightbreak_Cafe_Presentation_Script.docx`
  Slide-by-slide speaking notes.

## How to Run

```bash
python3 app.py
```

## How to Test

```bash
python3 tests.py
```

## How to Benchmark

```bash
python3 benchmarks.py
```

## Notes

- The interface is terminal based on purpose so the code stays focused on data structures.
- The core project code uses plain Python and custom data structures from class.
- Personal team information can still be added in the report and presentation files.
- The remaining placeholders are intentional: team names, presentation date, GitHub link, and any images you want to insert.
