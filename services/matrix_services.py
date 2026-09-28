"""Pure-Python services for validating and operating on 3x3 matrices."""

import math
from numbers import Real


_MATRIX_SIZE = 3


def validate_matrix_3x3(matrix):
    """Validate and return a defensive copy of a finite numeric 3x3 matrix."""
    if not isinstance(matrix, (list, tuple)) or len(matrix) != _MATRIX_SIZE:
        raise ValueError("matrix must contain exactly 3 rows")

    validated = []
    for row in matrix:
        if not isinstance(row, (list, tuple)) or len(row) != _MATRIX_SIZE:
            raise ValueError("each matrix row must contain exactly 3 values")

        validated_row = []
        for value in row:
            if isinstance(value, bool) or not isinstance(value, Real):
                raise ValueError("matrix values must be numeric and boolean values are not allowed")
            if not math.isfinite(value):
                raise ValueError("matrix values must be finite")
            validated_row.append(value)

        validated.append(validated_row)

    return validated


def _determinant_from_validated(matrix):
    a, b, c = matrix[0]
    d, e, f = matrix[1]
    g, h, i = matrix[2]
    return (
        a * (e * i - f * h)
        - b * (d * i - f * g)
        + c * (d * h - e * g)
    )


def determinant_3x3(matrix):
    """Return the determinant of a valid 3x3 matrix."""
    validated = validate_matrix_3x3(matrix)
    return _determinant_from_validated(validated)


def _inverse_from_validated(matrix, determinant):
    if math.isclose(determinant, 0.0, abs_tol=1e-12):
        return None

    a, b, c = matrix[0]
    d, e, f = matrix[1]
    g, h, i = matrix[2]

    adjugate = [
        [e * i - f * h, c * h - b * i, b * f - c * e],
        [f * g - d * i, a * i - c * g, c * d - a * f],
        [d * h - e * g, b * g - a * h, a * e - b * d],
    ]
    return [
        [value / determinant for value in row]
        for row in adjugate
    ]


def inverse_3x3(matrix):
    """Return the inverse of a valid 3x3 matrix, or None when it is singular."""
    validated = validate_matrix_3x3(matrix)
    determinant = _determinant_from_validated(validated)
    return _inverse_from_validated(validated, determinant)


def matrix_3x3(matrix):
    """Return the determinant and inverse for one validated 3x3 matrix."""
    validated = validate_matrix_3x3(matrix)
    determinant = _determinant_from_validated(validated)
    return {
        "determinant": determinant,
        "inverse": _inverse_from_validated(validated, determinant),
    }
