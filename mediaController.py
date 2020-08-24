from ctypes import windll
from pynput.keyboard import Listener, KeyCode, Key

user32 = windll.user32

KEY_SPACE = Key.space
KEY_LEFT = Key.left
KEY_UP = Key.up
KEY_RIGHT = Key.right
KEY_DOWN = Key.down
KEY_M = KeyCode(vk=0x4D)
KEY_FN = KeyCode(vk=0xFF)

VK_BACK = 0x08                  # Backspace
VK_VOLUME_MUTE = 0xAD           # "M"
VK_VOLUME_DOWN = 0xAE           # Down
VK_VOLUME_UP = 0xAF             # Up
VK_MEDIA_NEXT_TRACK = 0xB0      # Left
VK_MEDIA_PREV_TRACK = 0xB1      # Right
VK_MEDIA_PLAY_PAUSE = 0xB3      # Space


class MediaController(object):

    def __init__(self):
        super().__init__()
        self._fn_pressed = bool(user32.GetKeyState(0xFF))

    def on_press_key(self, key: KeyCode):
        if key == KEY_FN:
            self._fn_pressed = True
        elif self._fn_pressed:
            if key == KEY_SPACE:
                user32.keybd_event(VK_MEDIA_PLAY_PAUSE, 0, 0, 0)
                user32.keybd_event(VK_BACK, 0, 0, 0)
            elif key == KEY_LEFT:
                user32.keybd_event(VK_MEDIA_PREV_TRACK, 0, 0, 0)
            elif key == KEY_UP:
                user32.keybd_event(VK_VOLUME_UP, 0, 0, 0)
            elif key == KEY_RIGHT:
                user32.keybd_event(VK_MEDIA_NEXT_TRACK, 0, 0, 0)
            elif key == KEY_DOWN:
                user32.keybd_event(VK_VOLUME_DOWN, 0, 0, 0)
            elif key == KEY_M:
                user32.keybd_event(VK_VOLUME_MUTE, 0, 0, 0)
                user32.keybd_event(VK_BACK, 0, 0, 0)

    def on_release_key(self, key):
        if key == KEY_FN:
            self._fn_pressed = user32.GetAsyncKeyState(0xFF) > 1


model = MediaController()

with Listener(on_press=model.on_press_key, on_release=model.on_release_key) as l:
    l.join()
