from . import *

class FolderButton(ButtonBehavior, BoxLayout):
    def __init__(self, title, **kwargs):
        super(FolderButton, self).__init__(**kwargs)
        self.orientation = 'vertical'
        self.size_hint_y = None
        self.height = dp(100)
        self.padding = dp(10)
        
        with self.canvas.before:
            Color(0.4, 0.6, 1, 1)  # Light blue color for folder
            self.rect = RoundedRectangle(pos=self.pos, size=self.size, radius=[dp(15)])
            
        folder_icon = Label(
            text="📁",
            font_size=dp(32),
            size_hint_y=0.7
        )
        folder_name = Label(
            text=title,
            font_size=dp(14),
            size_hint_y=0.3
        )
        
        self.add_widget(folder_icon)
        self.add_widget(folder_name)
        
        self.bind(pos=self.update_rect, size=self.update_rect)
        
    def update_rect(self, *args):
        self.rect.pos = self.pos
        self.rect.size = self.size