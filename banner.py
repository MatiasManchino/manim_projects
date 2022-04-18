from asyncore import write
from manim import *
import numpy as np
import itertools as it

class Texto(Scene):

    colores = ['#ff8c5c','#f5ff5c','#60ff5c','#ff5cf8','#5cd7ff']
    
    def construct(self):
        self.camera.background_color = '#500368'
        mi_text2 = Text('print(presentation(surname,names))', color='#ff5e5c')
        mi_texto = Text('Manchino, Matías Pablo', color='#5ce5ff').scale(1.8)
        self.play(Write(mi_text2))
        self.wait(1)
        self.play(Transform(mi_text2,mi_texto))
        self.wait(1)
        time=0
        while time<5:
            my_time=.15
            time+=my_time
            np.random.shuffle(self.colores)
            my_color=it.cycle(self.colores)
            for char in mi_texto.family_members_with_points():
                char.set_color(next(my_color))
            self.add(mi_texto)
            self.wait(my_time)
        self.play(FadeOut(mi_texto))
        self.play(FadeOut(mi_text2, scale=0.5))
        
            