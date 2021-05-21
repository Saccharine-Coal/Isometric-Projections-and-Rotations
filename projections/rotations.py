import math

import projections.linear_transformations


class XRotationMatrix(projections.linear_transformations.LinearTransformation):
    """Rotation around the X axis about (0, 0, 0)."""
    def __init__(self, degrees=0):
        """@param degrees to rotate"""
        rad = (degrees / 180) * math.pi
        std_matrix_repr = [
                           [1, 0, 0],
                           [0, math.cos(rad), -math.sin(rad)],
                           [0, math.sin(rad), math.cos(rad)]
                           ]
        super().__init__(std_matrix_repr)


class YRotationMatrix(projections.linear_transformations.LinearTransformation):
    """Rotation around the Y axis about (0, 0, 0)."""
    def __init__(self, degrees=0):
        """@param degrees to rotate"""
        rad = (degrees / 180) * math.pi
        std_matrix_repr = [
                           [math.cos(rad), 0, math.sin(rad)],
                           [0, 1, 0],
                           [-math.sin(rad), 0, math.cos(rad)]
                           ]
        super().__init__(std_matrix_repr)


class ZRotationMatrix(projections.linear_transformations.LinearTransformation):
    """Rotation around the Z axis about (0, 0, 0)."""
    def __init__(self, degrees=0):
        """@param degrees to rotate"""
        rad = (degrees / 180) * math.pi
        std_matrix_repr = [
                           [math.cos(rad), -math.sin(rad), 0],
                           [math.sin(rad), math.cos(rad), 0],
                           [0, 0, 1]
                           ]
        super().__init__(std_matrix_repr)


