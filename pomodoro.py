from time import sleep


def countdown(seconds):
    while seconds >= 0:
        print(seconds)
        seconds -= 1
        sleep(1.0)


def pomodoro(down, up):
    while True:
        print("Back to work! (Ctrl-C to quit)")
        countdown(down)
        print("It's time for a break! (Ctrl-C to quit)")
        countdown(up)


if __name__ == "__main__":
    pomodoro(10, 5)
