from time import sleep


def countdown(seconds):
    while seconds >= 0:
        print(seconds)
        seconds -= 1
        sleep(1.0)


if __name__ == "__main__":
    countdown(100)
