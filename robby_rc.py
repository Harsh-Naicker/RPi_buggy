from bluedot import BlueDot
from gpiozero import Robot
bd=BlueDot()
robot=Robot(left=(8,7), right=(10,9))

def move(pos):
    if pos.top:
        robot.forward()
    elif pos.bottom:
        robot.backward()
    elif pos.right:
        robot.right()
    elif pos.left:
        robot.left()
def stop():
    robot.stop()
bd.when_pressed=move
bd.when_moved=move
bd.when_released=stop
