
This Python program compares **List** and **Generator** methods for filtering transactions above a given threshold.

It measures:

* Number of records processed
* Execution time
* Peak memory usage

## Requirements

* Python 3
* No external libraries required

## How to Run

```bash
python main.py
```

## Input

The program asks for:

1. Number of transactions
2. Transaction amounts
3. Threshold value

## Example

```text
Enter number of transactions: 3
Transaction 1: ₹5000
Transaction 2: ₹15000
Transaction 3: ₹20000
Enter threshold value: ₹10000
```

## Output

The program displays the processing results for both methods:

```text
List-based Processing
Records processed: 2
Execution time: ...
Peak memory: ...

Generator-based Processing
Records processed: 2
Execution time: ...
Peak memory: ...
```

## Purpose

The program demonstrates that **generators can use less memory** than lists when processing large amounts of data.


