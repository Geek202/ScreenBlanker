print("Loading ScreenBlank v1.0...")

import pyglet
import os

display = pyglet.canvas.get_display()
screens = display.get_screens()

class Win(pyglet.window.Window):
    def __init__(self, sc):
        super().__init__(self, fullscreen=True, screen=sc)

    def on_draw(self):
        self.clear()

    def on_key_press(self, sym, mods):
        if sym == pygame.window.key.ESCAPE:
            os._exit()

print("Found", len(screens), "displays to blank!")
windows = []
for i, screen in enumerate(screens):
    print("Blanking display:", i)
    w=pyglet.window.Window(fullscreen=True, screen=screen)
    windows.append(w)

windows[0].set_exclusive_mouse()
pyglet.app.run()

input("Thanks for using ScreenBlank v1.0!")
