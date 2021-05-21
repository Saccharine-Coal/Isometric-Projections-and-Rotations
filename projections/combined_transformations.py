import projections.rotations
import projections.translations


class RotateAboutPoint:
    """Rotate shape like object about a given point."""
    def __init__(self, origin, alpha=0, beta=0, gamma=0):
        """
        @param 3-tuple which is rotated about
        @param degree about x-axis
        @param degree about y-axis
        @param degree about z-axis
        """
        self.origin = origin
        self.alpha = alpha
        self.beta = beta
        self.gamma = gamma
        self.set_matrices()

    
    def set_matrices(self):
        self.away_from_origin_mx = projections.translations.TranslationMatrix3(self.origin)
        self.to_origin_mx = -self.away_from_origin_mx
        self.rot_x = projections.rotations.XRotationMatrix(self.alpha)
        self.rot_y = projections.rotations.YRotationMatrix(self.beta)
        self.rot_z = projections.rotations.XRotationMatrix(self.gamma)

    def update(self, origin=None, alpha=None, beta=None, gamma=None):
        """Update the matrices in this set.
            @param new origin for translation
            @param new angle for x rotation
            @param new angle for y rotation
            @param new angle for z rotation
        """
        self._update_translation_matrices(origin)
        self._update_rotation_matrices(alpha, beta, gamma)
    
    def _update_translation_matrices(self, origin):
        if origin is not None:
            self.origin = origin
            self.away_from_origin_mx = projections.translations.TranslationMatrix3(self.origin)
            self.to_origin_mx = -self.away_from_origin_mx
    
    def _update_rotation_matrices(self, alpha, beta, gamma):
        if alpha is not None:
            self.alpha = alpha
            self.rot_x = projections.rotations.XRotationMatrix(self.alpha)
        if beta is not None:
            self.beta = beta
            self.rot_y = projections.rotations.YRotationMatrix(self.beta)
        if gamma is not None:
            self.gamma = gamma
            self.rot_z = projections.rotations.XRotationMatrix(self.gamma)

    def _apply_rotations(self, point):
        """Apply xyz rotations.
            @param 3-tuple
            @return 3-tuple
        """
        x_rot = self.rot_x * point
        xy_rot = self.rot_y * x_rot
        xyz_rot = self.rot_z * xy_rot
        return xyz_rot

    def apply(self, point):
        """Apply a sequence of transformations to a given point.
            @param 3-tuple
            @return 3-tuple
        """
        at_origin = self.to_origin_mx * point
        xyz_rotated = self._apply_rotations(at_origin)
        translated_back = self.away_from_origin_mx * xyz_rotated
        return translated_back
