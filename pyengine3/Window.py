import pyglet

from pyengine3.utils import WindowStyle, MouseCursors
from pyengine3.input.Input import Input

class Window:
    def __init__(self, title: str = "PyEngine3 Window", width: int = 640, height: int = 480, resizable: bool = False, style: WindowStyle = WindowStyle.DEFAULT,
        fullscreen: bool = False, visible: bool = True, vsync: bool = True, debug: bool = False, ups: int = 60):
        self.__window = pyglet.window.Window(width, height, title, resizable, style, fullscreen, visible, vsync)
        self.__debug = debug
        self.__fps_label = pyglet.text.Label("FPS : {}".format(int(pyglet.clock.get_fps())), x = 10, y = 10)
        self.__fps_timer = 0
        self.__ups = ups
        self.__input = Input(self.__window)

        pyglet.clock.schedule_interval(self.update, 1.0/ups)

        @self.__window.event
        def on_draw():
            pyglet.clock.tick()
            self.__window.clear()
            if self.__debug:
                self.__fps_label.draw()

    def update(self, dt):
        if self.__debug:
            if self.__fps_timer <= 0:
                self.__fps_label.text = "FPS : {}".format(int(pyglet.clock.get_fps()))
                self.__fps_timer = self.__ups / 2
            self.__fps_timer -= 1

    def run(self):
        pyglet.app.run()

    def get_input(self) -> Input:
        return self.__input

    def set_mouse_visible(self, visible: bool):
        self.__window.set_mouse_visible(visible)
    
    def set_cursor(self, cursor: MouseCursors):
        cursor = self.__window.get_system_mouse_cursor(cursor)
        self.__window.set_mouse_cursor(cursor)

    def set_cursor_image(self, cursor: str):
        cursor = pyglet.window.ImageMouseCursor(pyglet.image.load(cursor), 16, 8)
        self.__window.set_mouse_cursor(cursor)

    def set_exclusive_mouse(self, exclusive: bool):
        self.__window.set_exclusive_mouse(exclusive)
        
    def set_ups(self, ups: int = 60):
        self.__ups = ups
        pyglet.clock.unschedule(self.update)
        pyglet.clock.schedule_interval(self.update, 1.0/ups)
    
    def get_ups(self) -> int:
        return self.__ups