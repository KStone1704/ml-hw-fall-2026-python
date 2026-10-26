# Python Number Lookup

A small command-line program for reading a sequence of numbers and locating a target value. Prepared for the Fall 2026 machine learning Python exercise.

## Requirements

Python 3.9 or newer. No third-party packages are required.

## Run

```bash
python3 module4.py
```

The program asks for a positive integer N, reads N numbers one at a time, and then asks for an integer X. It prints the first 1-based position of X, or -1 when X is absent.

For example, enter N = 3, then 4, 7, and 9, and finally X = 7. The result is 2.

Repeated values return the first occurrence. Decimal input is supported for the sequence; X must be an integer. Decimal arithmetic avoids rounding large integers through floating-point conversion. Input is expected to be well formed; a nonpositive N raises a ValueError.

## Test

```bash
python3 -B -m unittest discover -s tests -v
```

Tests cover first/middle/last positions, missing values, duplicate values, negative values, large integers, decimal input, and invalid N.

## Files

- `module4.py`: interactive program and lookup function.
- `tests/test_module4.py`: standard-library tests.

The repository contains only this learning exercise. It does not include employer code or data.

## Assistance

This project was completed with assistance from OpenAI Codex.
