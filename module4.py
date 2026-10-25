"""Read N numbers and print the first 1-based position of integer X, or -1."""

from decimal import Decimal


def find_index(numbers: list[Decimal], target: Decimal) -> int:
    for index, number in enumerate(numbers, start=1):
        if number == target:
            return index
    return -1


def main() -> None:
    n = int(input("Enter N (positive integer): "))
    if n <= 0:
        raise ValueError("N must be a positive integer")

    numbers = []
    for index in range(1, n + 1):
        numbers.append(Decimal(input(f"Enter number {index}: ")))

    target = Decimal(int(input("Enter X (integer): ")))
    print(find_index(numbers, target))


if __name__ == "__main__":
    main()
