from time import sleep


DELAY = 0.02

def press_enter(message):
    input(f"\a{message} Press [ENTER] to start cycle, Ctrl-C to quit")


def seconds_to_timestamp(seconds):
    minutes = seconds // 60
    seconds %= 60
    hours = minutes // 60
    minutes %= 60

    if hours > 0:
        return f"{hours:02}:{minutes:02}:{seconds:02}"
    else:
        return f"{minutes:02}:{seconds:02}"


def countdown(seconds):
    while seconds >= 0:
        print(seconds_to_timestamp(seconds), end="      \r")
        seconds -= 1
        sleep(DELAY)


def pomodoro(down, up):
    cycle = 0
    while True:
        cycle += 1
        press_enter("Back to work!")
        countdown(down)

        if cycle % 4 != 0:
            press_enter("It's time for a break!")
            countdown(up)
        else:
            press_enter("You've earned a nice, long break!")
            countdown(down)


if __name__ == "__main__":
    pomodoro(5 * 60, 2 * 60)
