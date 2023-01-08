import turtle

lsystem = turtle.Turtle()


print("Recursion State N0 i.e. Axiom")
lsystem.forward(50)

print("Recursion State N1")
lsystem.forward(50)
print(lsystem.pos())
lsystem.up()
lsystem.right(45)
lsystem.forward(50)
lsystem.goto(100.0, 0.0)
lsystem.left(45)
lsystem.pendown()
lsystem.forward(50)

print("Recursion State N2")
lsystem.forward(50)
print(lsystem.pos())
lsystem.up()
lsystem.right(45)
lsystem.forward(50)
lsystem.goto(200.0, 0.0)
lsystem.left(45)
lsystem.pendown()
lsystem.forward(50)
print(lsystem.pos())
lsystem.right(45)
lsystem.forward(50)
print(lsystem.pos())
lsystem.left(45)
lsystem.forward(50)
lsystem.penup()
lsystem.goto(250.0, 0.0)
lsystem.pendown()
# Repeat n1 logic with new position
lsystem.forward(50)
print(lsystem.pos())
lsystem.up()
lsystem.right(45)
lsystem.forward(50)
lsystem.goto(300.0, 0.0)
lsystem.left(45)
lsystem.pendown()
lsystem.forward(50)

print("Recursion State N3")
print(lsystem.pos())
# Repeat n1 logic with new position
lsystem.forward(50)
print(lsystem.pos())
lsystem.up()
lsystem.right(45)
lsystem.forward(50)
lsystem.goto(400.0, 0.0)
lsystem.left(45)
lsystem.pendown()
lsystem.forward(50)
print(lsystem.pos())

# Repeat n2 logic
lsystem.right(45)
lsystem.forward(50)
lsystem.left(45)
lsystem.forward(50)
lsystem.penup()
lsystem.goto(450.0, 0.0)
lsystem.pendown()
print(lsystem.pos())

# Repeat n1 logic
lsystem.forward(50)
print(lsystem.pos())
lsystem.up()
lsystem.right(45)
lsystem.forward(50)
lsystem.goto(500.0, 0.0)
lsystem.left(45)
lsystem.pendown()
lsystem.forward(50)
print(lsystem.pos())

lsystem.right(45)
lsystem.forward(50)
print(lsystem.pos())
lsystem.right(45)
lsystem.up()
lsystem.forward(50)
lsystem.goto(585.355339059, -35.3553390593)
lsystem.pendown()
lsystem.left(45)
lsystem.forward(50)
print(lsystem.pos())
lsystem.left(45)
lsystem.forward(50)
print(lsystem.pos())
lsystem.penup()
lsystem.right(45)
lsystem.forward(50)
lsystem.goto(670.71, -70.71)
lsystem.left(45)
lsystem.pendown()
lsystem.forward(50)
lsystem.penup()
lsystem.goto(550.00, 0.00)

# n1 logic
lsystem.pendown()
lsystem.forward(50)
print(lsystem.pos())
lsystem.up()
lsystem.right(45)
lsystem.forward(50)
lsystem.goto(600.0, 0.0)
lsystem.pendown()
lsystem.left(45)
lsystem.forward(50)
print(lsystem.pos())

lsystem.right(45)
lsystem.forward(50)
lsystem.left(45)
lsystem.forward(50)
lsystem.penup()
lsystem.goto(650.00, 0.00)
lsystem.pendown()
# n1 logic
lsystem.forward(50)
print(lsystem.pos())
lsystem.up()
lsystem.right(45)
lsystem.forward(50)
lsystem.goto(700.0, 0.0)
lsystem.pendown()
lsystem.left(45)
lsystem.forward(50)
print(lsystem.pos())


