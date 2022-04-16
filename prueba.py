from manim import *

class VectorScene(Scene):
    def __init__(self, basis_vector_stroke_width=6, **kwargs):
        super().__init__(**kwargs)
        self.basis_vector_stroke_width = basis_vector_stroke_width
    def add_plane(self, animate=False, **kwargs):
        """
        Adds a NumberPlane object to the background.

        Parameters
        ----------
        animate : bool, optional
            Whether or not to animate the addition of the plane via Create.
        **kwargs
            Any valid keyword arguments accepted by NumberPlane.

        Returns
        -------
        NumberPlane
            The NumberPlane object.
        """
        plane = NumberPlane(**kwargs)
        if animate:
            self.play(Create(plane, lag_ratio=0.5))
        self.add(plane)
    