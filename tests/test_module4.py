from decimal import Decimal
from pathlib import Path
import subprocess
import sys
import unittest

from module4 import find_index


SCRIPT = Path(__file__).resolve().parents[1] / "module4.py"


class NumberLookupTests(unittest.TestCase):
    def test_positions(self):
        cases = [
            ([2, 5, 8], 2, 1),
            ([2, 5, 8], 5, 2),
            ([2, 5, 8], 8, 3),
            ([2, 5, 8], 7, -1),
            ([2, 5, 2], 2, 1),
            ([-3, 0, 9], -3, 1),
            ([9007199254740992, 9007199254740993], 9007199254740993, 2),
        ]
        for values, target, expected in cases:
            with self.subTest(values=values, target=target):
                self.assertEqual(
                    find_index([Decimal(value) for value in values], Decimal(target)),
                    expected,
                )

    def test_decimal_cli(self):
        result = subprocess.run(
            [sys.executable, str(SCRIPT)],
            input="3\n1.5\n2.0\n7\n2\n",
            text=True,
            capture_output=True,
            check=True,
        )
        self.assertTrue(result.stdout.rstrip().endswith("2"))

    def test_missing_cli(self):
        result = subprocess.run(
            [sys.executable, str(SCRIPT)],
            input="1\n3\n8\n",
            text=True,
            capture_output=True,
            check=True,
        )
        self.assertTrue(result.stdout.rstrip().endswith("-1"))

    def test_nonpositive_n(self):
        result = subprocess.run(
            [sys.executable, str(SCRIPT)],
            input="0\n",
            text=True,
            capture_output=True,
        )
        self.assertNotEqual(result.returncode, 0)
        self.assertIn("positive integer", result.stderr)


if __name__ == "__main__":
    unittest.main()
