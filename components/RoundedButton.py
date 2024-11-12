from . import *

class RoundedButton(ButtonBehavior, Label):
    def __init__(self, **kwargs):
        super(RoundedButton, self).__init__(**kwargs)
        self.background_color = kwargs.get('background_color', (0, 0, 0, 1))
        
    def on_size(self, *args):
        self.canvas.before.clear()
        with self.canvas.before:
            Color(*self.background_color)
            Rectangle(pos=self.pos, size=self.size)
            Color(1, 1, 1, 1)  # Reset color to white for potential border
            Line(rounded_rectangle=(self.x, self.y, self.width, self.height, 10), width=1.2)