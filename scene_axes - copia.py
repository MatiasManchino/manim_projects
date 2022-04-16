from manim import *

class EjesCartesianos(Scene):
    def construct(self):

        color_line = "#D3AF37" #color de lienas

        plano = NumberPlane(

            #x_length=14, #ancho de la pantalla donde aparecera el plano
           # y_length=8, #alto de la pantalla donde aparecera el plano

            x_range=[0 , 4, 1], #rango menor, mayor, en intervalos de.
            y_range=[-10, 10, 1],
            
            axis_config={ #ejes principales 
                "stroke_color": color_line, #color de los ejes
                "stroke_width": 5, #grosor
                "include_tip": True, #agregar flechas de direccion
                "include_ticks": True,
                },
            background_line_style={ 
                "stroke_color": color_line,
                "stroke_width": 1,
                "stroke_opacity": 0.2,
                },
        )
        plano.add_coordinates() 
        text1 = MathTex("y").set_color(YELLOW).to_edge(UP/2).to_edge(RIGHT*15) #"y", color, posición respecto a altura, posicion respecto a laterales
        text2 = MathTex("x").set_color(YELLOW).to_edge(DOWN*6.5).to_edge(RIGHT) #"x", color, posición respecto a altura, posicion respecto a laterales

        self.play(Write(plano), rum_time=10)
        self.play(Write(text1))
        self.play(Write(text2))
        self.wait(7)       