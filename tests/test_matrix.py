import unittest

from services.matrix_services import determinant_3x3, inverse_3x3, matrix_3x3


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


if __name__ == "__main__":
    unittest.main()
