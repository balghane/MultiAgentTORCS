import time
import pyxhook

up = False
down = False
left = False
right = False


def kbup(event):
    global up, down, left, right
    if event.Ascii == 81:
        left = True
    elif event.Ascii == 82:
        up = True
    elif event.Ascii == 83:
        right = True
    elif event.Ascii == 84:
        down = True


def kbdown(event):
    global up, down, left, right
    if event.Ascii == 81:
        left = False
    elif event.Ascii == 82:
        up = False
    elif event.Ascii == 83:
        right = False
    elif event.Ascii == 84:
        down = False


def main():
    hookman = pyxhook.HookManager()
    hookman.KeyDown = kbup
    hookman.KeyUp = kbdown
    hookman.HookKeyboard()
    hookman.start()

    hookman.cancel()

if __name__ == "__main__":
    main()