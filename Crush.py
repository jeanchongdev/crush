import turtle

# Crear una ventana de graficos
window = turtle.Screen()
window.bgcolor("white")

# Crear un objeto para dibujar
t = turtle.Turtle()
t.speed(1)

# Dibujar el corazón
t.fillcolor("red")
t.begin_fill()
t.left(45)
t.forward(100)
t.circle(50, 180)
t.right(90)
t.circle(50, 180)
t.forward(100)
t.end_fill()

# Mover el objeto fuera de la pantalla
t.penup()
t.goto(0, -100)
t.pendown()

# Mantener la ventana abierta
turtle.done()