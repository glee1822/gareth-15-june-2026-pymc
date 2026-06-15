# AT THE END OF LESSON, COPY YOUR CODE FROM MINECRAFT HERE.
# THIS IS SO THAT YOU HAVE A RECORD OF YOUR CODE FROM MINECRAFT CODE BUILDER
################# Function Section #############################


################## On Chat Commands Section #####################
def come():
    agent.teleport_to_player()
player.on_chat("come", come)

def left():
    agent.turn_left()
def on_chat4():
    left()
player.on_chat("left", on_chat4)

def right():
    agent.turn_right()
def on_chat5():
    right()
player.on_chat("right", on_chat5)

def turn():
    agent.turn_right()
    agent.turn_right()
player.on_chat("turn", turn)

def up(num):
    agent.move(UP, num)
def on_chat3(steps):
    up(steps)
player.on_chat("up", on_chat3)

def down(num):
    agent.move(DOWN, num)
def on_chat2(steps):
     down(steps)
player.on_chat("down", on_chat2)

def front(steps):
    agent.move(FORWARD, steps)

def on_chat(steps):
    front(steps)
player.on_chat("front", on_chat)


def back(num):
    agent.move(BACK, num)
player.on_chat("back", back)

def mine(direction):
    agent.destroy(direction)


def minefront(length):
    for i in range(length):
        mine(FORWARD)
        agent.move(FORWARD, 1)
player.on_chat("minefront", minefront)

def mineup(length):
    for i in range(length):
        mine(UP)
        agent.move(UP, 1)
player.on_chat("mineup", mineup)

def minedown(length):
    for i in range(length):
        mine(DOWN)
        agent.move(DOWN, 1)
player.on_chat("minedown", minedown)
        
def ch1():
    front(4)
    left()
    front(4)
    right()
    front(2)
    for i in range(3):
        up(1)
        front(1)
    front(2)
    for i in range(3):
        down(1)
        front(1)
    down(1)
player.on_chat("ch1", ch1)

