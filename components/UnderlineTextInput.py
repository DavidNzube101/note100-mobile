from . import *

class UnderlineTextInput(TextInput):
    def __init__(self, **kwargs):
        super(UnderlineTextInput, self).__init__(**kwargs)
        self.background_color = (0, 0, 0, 0)  # Transparent background
        self.cursor_color = (0, 0, 0, 1)
        self.foreground_color = (0, 0, 0, 1)
        self.padding = [0, dp(10), 0, dp(10)]
        
        with self.canvas.after:
            Color(0, 0, 0, 0.1)  # Light gray line
            self.underline = Line(points=[self.x, self.y, self.x + self.width, self.y], width=1)
        
        self.bind(pos=self.update_underline, size=self.update_underline)

    def update_underline(self, instance, value):
        self.underline.points = [self.x, self.y, self.x + self.width, self.y]