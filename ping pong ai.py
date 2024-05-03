import turtle

# Setup window
window = turtle.Screen()
window.title("Ping Pong Game By SabryHosny")
window.setup(width=800, height=600)
window.tracer(0)  # Set delay for updating drawings
window.bgcolor(0.1, 0.1, 0.1)

# Setup game objects
# Ball
ball = turtle.Turtle()
ball.speed(0)  # Drawing speed (fastest)
ball.shape("square")
ball.color("white")
ball.shapesize(stretch_len=1, stretch_wid=1)
ball.goto(x=0, y=0)  # Start position
ball.penup()  # Stop drawing lines when moving
ball_dx, ball_dy = 1, 1
ball_speed = 0.5

# Player 1
player1 = turtle.Turtle()
player1.speed(0)
player1.shape("square")
player1.shapesize(stretch_len=1, stretch_wid=5)
player1.color("blue")
player1.penup()
player1.goto(x=-350, y=0)

# Player 2 (computer)
player2 = turtle.Turtle()
player2.speed(0)
player2.shape("square")
player2.shapesize(stretch_len=1, stretch_wid=5)
player2.color("red")
player2.penup()
player2.goto(x=350, y=0)

# Score text
score = turtle.Turtle()
score.speed(0)
score.color("white")
score.penup()
score.goto(x=0, y=260)
score.write("Player1: 0 Computer: 0", align="center", font=("Courier", 14, "normal"))
score.hideturtle()

p1_score, p2_score = 0, 0  # Scores

# Players Movement
players_speed = 20

def p1_move_up():
    y = player1.ycor()
    if y < 250:
        player1.sety(y + players_speed)

def p1_move_down():
    y = player1.ycor()
    if y > -240:
        player1.sety(y - players_speed)

# Computer AI Movement using min and max algorithms
def computer_move():
    # Calculate the direction based on the sign of the difference between ball and player positions
    direction = (player2.ycor() < ball.ycor()) * 2 - 1  #هذا السطر يُحسب اتجاه حركة لاعب الكمبيوتر استنادًا إلى اختلاف مواقع الكرة واللاعب. إذا كانت موقع لاعب الكمبيوتر (player2) أقل من موقع الكرة (ball) على المحور الرأسي (ycor)، فسيتم تعيين direction إلى 1، وإلا فسيتم تعيينه إلى -1.
    new_y = player2.ycor() + direction * players_speed  #يُحسب هذا السطر موقع اللاعب الجديد بناءً على الموقع الحالي للاعب (player2) واتجاه الحركة الذي تم حسابه في الخطوة السابقة (direction) وسرعة اللاعب (players_speed). إذا كان الاتجاه إلى الأعلى، فسيتم إضافة السرعة، وإذا كان الاتجاه إلى الأسفل، فسيتم طرح السرعة.
    new_y = max(min(new_y, 250), -240)  # Ensure new_y is within bounds
    player2.sety(new_y)

# Get users inputs (Key Bindings)
window.listen()
window.onkeypress(p1_move_up, "Up")
window.onkeypress(p1_move_down, "Down")

# Game loop
while True:
    window.update()

    # Ball movement
    ball.setx(ball.xcor() + (ball_dx * ball_speed))
    ball.sety(ball.ycor() + (ball_dy * ball_speed))

    # Ball & borders collisions
    if ball.ycor() > 290:
        ball.sety(290)
        ball_dy *= -1

    if ball.ycor() < -290:
        ball.sety(-290)
        ball_dy *= -1

    # Ball & players collisions 
    if -350 < ball.xcor() < -340 and player1.ycor() - 60 < ball.ycor() < player1.ycor() + 60:
        ball.setx(-340)
        ball_dx *= -1

    if 340 < ball.xcor() < 350 and player2.ycor() - 60 < ball.ycor() < player2.ycor() + 60:
        ball.setx(340)
        ball_dx *= -1

    # Score handling
    if ball.xcor() > 390:
        ball.goto(0, 0)
        ball_dx *= -1
        p1_score += 1
        score.clear()
        score.write(f"Player1: {p1_score} Computer: {p2_score}", align="center", font=("Courier", 14, "normal"))

    if ball.xcor() < -390:
        ball.goto(0, 0)
        ball_dx *= -1
        p2_score += 1
        score.clear()
        score.write(f"Player1: {p1_score} Computer: {p2_score}", align="center", font=("Courier", 14, "normal"))

    # Computer AI movement call
    computer_move()
    