from time import sleep


def press_enter(message):
    input(f"\a{message} Press [ENTER] to start cycle, Ctrl-C to quit")


def countdown(seconds):
    while seconds >= 0:
        print(seconds, end="\r")
        seconds -= 1
        sleep(1.0)


def pomodoro(down, up):
    while True:
        press_enter("Back to work!")
        countdown(down)
        press_enter("It's time for a break!")
        countdown(up)


if __name__ == "__main__":
    pomodoro(10, 5)
