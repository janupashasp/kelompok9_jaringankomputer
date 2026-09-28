import unittest

from services.matrix_services import (
    determinant_3x3,
    inverse_3x3,
    matrix_3x3,
    validate_matrix_3x3,
)


class MatrixServicesTests(unittest.TestCase):
    def setUp(self):
        self.matrix = [
            [1, 2, 3],
            [0, 1, 4],
            [5, 6, 0],
        ]
        self.expected_inverse = [
            [-24, 18, 5],
            [20, -15, -4],
            [-5, 4, 1],
        ]

    def assertMatrixAlmostEqual(self, actual, expected):
        self.assertEqual(len(actual), len(expected))
        for actual_row, expected_row in zip(actual, expected):
            self.assertEqual(len(actual_row), len(expected_row))
            for actual_value, expected_value in zip(actual_row, expected_row):
                self.assertAlmostEqual(actual_value, expected_value)

    def test_determinant_3x3(self):
        self.assertEqual(determinant_3x3(self.matrix), 1)

    def test_inverse_3x3(self):
        self.assertMatrixAlmostEqual(
            inverse_3x3(self.matrix),
            self.expected_inverse,
        )

    def test_matrix_3x3_response(self):
        response = matrix_3x3(self.matrix)

        self.assertEqual(response["determinant"], 1)
        self.assertMatrixAlmostEqual(
            response["inverse"],
            self.expected_inverse,
        )


    def test_singular_matrix_has_no_inverse(self):
        singular = [
            [1, 2, 3],
            [2, 4, 6],
            [7, 8, 9],
        ]

        self.assertEqual(determinant_3x3(singular), 0)
        self.assertIsNone(inverse_3x3(singular))
        self.assertEqual(
            matrix_3x3(singular),
            {"determinant": 0, "inverse": None},
        )

    def test_rejects_invalid_matrix_shape(self):
        invalid_matrices = [
            [[1, 2], [3, 4]],
            [[1, 2, 3], [4, 5, 6]],
            [[1, 2, 3], [4, 5, 6], [7, 8]],
            [1, 2, 3],
        ]

        for matrix in invalid_matrices:
            with self.subTest(matrix=matrix):
                with self.assertRaises(ValueError):
                    validate_matrix_3x3(matrix)

    def test_rejects_non_numeric_and_boolean_values(self):
        invalid_matrices = [
            [[1, 2, 3], [4, "5", 6], [7, 8, 9]],
            [[1, 2, 3], [4, True, 6], [7, 8, 9]],
        ]

        for matrix in invalid_matrices:
            with self.subTest(matrix=matrix):
                with self.assertRaises(ValueError):
                    validate_matrix_3x3(matrix)

    def test_rejects_non_finite_values(self):
        invalid_values = [float("inf"), float("-inf"), float("nan")]

        for value in invalid_values:
            matrix = [
                [1, 2, 3],
                [4, value, 6],
                [7, 8, 9],
            ]
            with self.subTest(value=value):
                with self.assertRaises(ValueError):
                    validate_matrix_3x3(matrix)


if __name__ == "__main__":
    unittest.main()
