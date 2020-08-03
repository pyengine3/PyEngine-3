import pyglet

from pyengine3.utils import WindowStyle

class Window(pyglet.window.Window):
    def __init__(self, title: str = "PyEngine3 Window", width: int = 640, height: int = 480, resizable: bool = False, style: WindowStyle = WindowStyle.DEFAULT,
        fullscreen: bool = False, visible: bool = True, vsync: bool = True, debug: bool = False, ups: int = 60):
        if style == WindowStyle.DEFAULT:
            style = None
        elif style == WindowStyle.DIALOG:
            style = pyglet.window.Window.WINDOW_STYLE_DIALOG
        elif style == WindowStyle.TOOL:
            style = pyglet.window.Window.WINDOW_STYLE_TOOL
        elif style == WindowStyle.BORDERLESS:
            style = pyglet.window.Window.WINDOW_STYLE_BORDERLESS
        else:
            raise ValueError("Style must be a WindowStyle")

        super(Window, self).__init__(width, height, title, resizable, style, fullscreen, visible, vsync)
        self.debug = debug
        self.fps_label = pyglet.text.Label("FPS : {}".format(int(pyglet.clock.get_fps())), x = 10, y = 10)
        self.fps_timer = 0
        self.ups = ups
        pyglet.clock.schedule_interval(self.update, 1.0/ups)

    def update(self, dt):
        if self.debug:
            if self.fps_timer <= 0:
                self.fps_label.text = "FPS : {}".format(int(pyglet.clock.get_fps()))
                self.fps_timer = self.ups / 2
            self.fps_timer -= 1
        
    def on_draw(self):
        pyglet.clock.tick()
        self.clear()
        if self.debug:
            self.fps_label.draw()

    def run(self):
        pyglet.app.run()