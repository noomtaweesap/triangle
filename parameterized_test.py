import unittest
from triangle import is_triangle


class TriangleTest(unittest.TestCase):
    valid_triangles = [
        (1, 1, 1),
        (3, 4, 5),
        (3, 4, 6),
        (8, 10, 12),
        (100, 101, 200),
        (0.9, 1.0, 1.1)
    ]

    def test_valid_triangle(self):
        for a, b, c in self.valid_triangles:
            with self.subTest():
                msg = f"side lengths ({a},{b},{c})"
                self.assertTrue(is_triangle(a, b, c), msg)

    not_triangles = [
        (21, 10, 10),
        (2, 1, 1),
        (6, 10, 4),
        (6, 20, 4),
        (10, 10, 30)
    ]

    def test_not_triangle(self):
        for a, b, c in self.not_triangles:
            with self.subTest():
                msg = f"side lengths ({a},{b},{c})"
                self.assertFalse(is_triangle(a, b, c), msg)

    invalid_argument_raises_exception = [
        (-1, 2, 2),
        (1, 0, 2),
        (1, -1, 2),
        (1, 2, -1),
        (1, 2, 0),
        (3, 4, 5),
        (-1, -1, -1),
        (0, 0, 0)
    ]

    def test_invalid_argument_raises_exception(self):
        for a, b, c in self.invalid_argument_raises_exception:
            with self.subTest():
                msg = f"side lengths ({a},{b},{c})"
                with self.assertRaises(ValueError):
                    b1 = is_triangle(a, b, c)
