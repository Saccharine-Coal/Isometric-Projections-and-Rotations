import numpy as np

import projections.linear_transformations
import projections.rotations


class TranslationMatrix3(projections.linear_transformations.LinearTransformation):
    """Translation by a factor (dx, dy, dz) in Euclidean 3-space."""
    def __init__(self, trans_xyz):
        """@param 3-tuple of integers to translate by."""
        self.trans_xyz = trans_xyz
        trans_x, trans_y, trans_z = trans_xyz
        std_matrix_repr = [
                           [1, 0, 0, trans_x],
                           [0, 1, 0, trans_y],
                           [0, 0, 1, trans_z],
                           [0, 0, 0, 1]
                           ]
        super().__init__(std_matrix_repr)

    # DUNDER OVERIDE
    def __neg__(self):
        negative_translation = tuple(-element for element in self.trans_xyz)
        return TranslationMatrix3(negative_translation)

    # METHOD OVERIDE
    def transform_point(self, xyz):
        # 3-tuple -> 4-tuple -> 3-tuple
        xyzw = (*xyz, 1)
        vector_repr = np.array(xyzw)
        product_arr = np.dot(self.std_matrix_repr, vector_repr)
        translated_xyzw = tuple(product_arr)
        translated_xyz = translated_xyzw[0:3]
        return translated_xyz
