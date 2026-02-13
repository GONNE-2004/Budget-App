13th-2-2026

# Budget App (FreeCodeCamp – Python OOP, class and Objects)

## Overview

This project implements a simple budget management system using **Object-Oriented Programming (OOP)** in Python. It allows users to create spending categories, track deposits and withdrawals, transfer funds between categories, and generate a visual chart showing spending distribution.

This project reinforces:

* Class design and encapsulation
* State management using object attributes
* String formatting and precise output control

____________________________________________________________________________________________________________

## Features

### Category Class

Each budget category:

* Stores transactions in a ledger
* Tracks balance automatically
* Supports:

  * Deposits
  * Withdrawals (with balance checks)
  * Transfers between categories
  * Clean, formatted string output

### Spending Chart

* Displays **percentage spent per category**
* Percentages are rounded **down to the nearest 10**
* Output is an ASCII bar chart with exact spacing (as required by FreeCodeCamp)

____________________________________________________________________________________________________________

## Key Concepts Practiced

* Classes and objects
* Encapsulation of data and behavior
* Method reuse (`transfer` uses `withdraw` + `deposit`)
* Iteration and aggregation
* Precise string formatting and alignment

____________________________________________________________________________________________________________

## How to Run

```bash
python budget_app.py
```

Make sure the following block is at the **file level**:

```python
if __name__ == "__main__":
    main()
```

____________________________________________________________________________________________________________

## Notes

* Output formatting (including spaces) is **intentional and required**
* The project is designed to match FreeCodeCamp’s automated tests exactly

____________________________________________________________________________________________________________

This project focuses on **thinking in systems**, not just writing code.
