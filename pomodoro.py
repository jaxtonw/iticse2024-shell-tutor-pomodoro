from time import sleep


DELAY = 0.005


def cyan():
    print(end="\r\x1b[1;36m", flush=True)


def yellow():
    print(end="\r\x1b[1;33m", flush=True)


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
        try:
            cycle += 1
            cyan()
            press_enter("Back to work!")
            countdown(down)

            yellow()
            if cycle % 4 != 0:
                press_enter("It's time for a break!")
                countdown(up)
            else:
                press_enter("You've earned a nice, long break!")
                countdown(down)

        except KeyboardInterrupt:
            print()
            break


if __name__ == "__main__":
    pomodoro(5 * 60, 2 * 60)
