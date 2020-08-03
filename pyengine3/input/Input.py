from pyglet.window import key, mouse

__all__ = ["Input"]

class Input:
    def __init__(self, window):
        self.__key_handler = key.KeyStateHandler()
        self.__mouse_handler = mouse.MouseStateHandler()

        window.push_handlers(self.__key_handler)
        window.push_handlers(self.__mouse_handler)

    
    def is_key_down(self, key):
        return self.__key_handler[key]
    
    def is_key_up(self, key):
        return not self.is_key_down(key)

    def is_mousebutton_down(self, mousebutton):
        return self.__mouse_handler[mousebutton]
    
    def is_mousebutton_up(self, mousebutton):
        return not self.is_mousebutton_down(mousebutton)