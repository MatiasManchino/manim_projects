from manim import *
import numpy as np

class EjesCartesianos(Scene):
    def construct(self):

        color_line = "#D3AF37" #color de lienas

        plano = NumberPlane(

            x_length=14, #ancho de la pantalla donde aparecera el plano
            y_length=8, #alto de la pantalla donde aparecera el plano

            x_range=[-10 , 10, 1], #rango menor, mayor, en intervalos de.
            y_range=[-10, 10, 1],
            
            axis_config={ #ejes principales 
                "stroke_color": color_line, #color de los ejes
                "stroke_width": 5, #grosor
                "include_tip": True, #agregar flechas de direccion
                "include_ticks": True,
                },
            background_line_style={ 
                "stroke_color": WHITE,
                "stroke_width": 1,
                "stroke_opacity": 0.2,
                },
        )

        colorX=plano[2]
        colorX[1].set_color(RED).scale(0.6).set_opacity(0.5).stretch_to_fit_width(0.5)
        colorY=plano[3]
        colorY[1].set_color(RED).scale(0.8).set_opacity(0.5).stretch_to_fit_height(0.5)

        plano.add(plano.get_axis_labels().set_color(color_line))
        plano.add_coordinates()
       
        self.play(Write(plano))
        self.wait(7)       