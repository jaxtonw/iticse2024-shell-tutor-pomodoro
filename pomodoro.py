from time import sleep


DELAY = 0.005

FIGLET = {
        "0": ["  ___  ",
              " / _ \\ ",
              "| | | |",
              "| |_| |",
              " \\___/ ",
              "       "],
        "1": [" _ ",
              "/ |",
              "| |",
              "| |",
              "|_|",
              "   "],
        "2": [" ____  ",
              "|___ \\ ",
              "  __) |",
              " / __/ ",
              "|_____|",
              "       "],
        "3": [" _____ ",
              "|___ / ",
              "  |_ \\ ",
              " ___) |",
              "|____/ ",
              "       "],
        "4": [" _  _   ",
              "| || |  ",
              "| || |_ ",
              "|__   _|",
              "   |_|  ",
              "        "],
        "5": [" ____  ",
              "| ___| ",
              "|___ \\ ",
              " ___) |",
              "|____/ ",
              "       "],
        "6": ["  __   ",
              " / /_  ",
              "| '_ \\ ",
              "| (_) |",
              " \\___/ ",
              "       " ],
        "7": [" _____ ",
              "|___  |",
              "   / / ",
              "  / /  ",
              " /_/   ",
              "       "],
        "8": ["  ___  ",
              " ( _ ) ",
              " / _ \\ ",
              "| (_) |",
              " \\___/ ",
              "       "],
        "9": ["  ___  ",
              " / _ \\ ",
              "| (_) |",
              " \\__, |",
              "   /_/ ",
              "       "],
        ":": ["   ",
              " _ ",
              "(_)",
              " _ ",
              "(_)",
              "   "],
        }

HOME = "\x1b[H"


def timestamp_to_figlet(timestr: str) -> str:
    digits = []
    for char in timestr:
        if char not in FIGLET:
            raise ValueError(f"{char} is neither a digit nor a colon")
        digits.append(FIGLET[char])

    if not digits:
        return "\n"

    output = []
    for i in range(len(digits[0])):
        row = []
        for d in digits:
            row.append(d[i])
        output.append("".join(row))
    return HOME + "\x1b[K\n".join(output)


def clear():
    """clear the screen and return cursor to home position"""
    print(end="\x1b[H\x1b[J", flush=True)


def press_enter(message):
    input(f"\a{message} Press [ENTER] to start cycle, Ctrl-C to quit")


def seconds_to_timestamp(seconds):
    minutes = seconds // 60
    seconds %= 60
    hours = minutes // 60
    minutes %= 60

    if hours > 0:
        return timestamp_to_figlet(f"{hours:02}:{minutes:02}:{seconds:02}")
    else:
        return timestamp_to_figlet(f"{minutes:02}:{seconds:02}")


def countdown(seconds):
    while seconds >= 0:
        print(seconds_to_timestamp(seconds), end="      \r")
        seconds -= 1
        sleep(DELAY)


def pomodoro(down, up):
    clear()
    cycle = 0
    while True:
        try:
            cycle += 1
            press_enter("Back to work!")
            countdown(down)

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
