import turtle as t #from turtle import*
#turtle.setup(500,500)

t.shape("turtle")        # Le damos la forma de una tortuga 
t.color("green") 


#**********  1  *******
#print("Origen", t.pos())
#t.forward(250)
#t.left(90)
#t.forward(250)
#print("Esquina superior #derecha", t.pos())
#t.left(90)
#t.forward(500)
#print("Esquina superior izquierda", t.pos())
#t.left(90)
#t.forward(500)
#*********   1   *********

#*************     2  ****

input_recorrido = input ("Enter your recorrido: ")
input_angulo = input ("Enter your angulo: ")

recorrido = int(input_recorrido)
angulo = int(input_angulo)
t.forward(recorrido)
t.left(angulo)
t.forward(recorrido)
t.left(angulo)
t.forward(recorrido)
t.left(angulo)
t.forward(recorrido)
t.left(angulo)
#**********  2   ************
