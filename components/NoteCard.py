from . import *


class NoteCard(ButtonBehavior, BoxLayout):
    def __init__(self, title, content, note_type="text", **kwargs):
        super(NoteCard, self).__init__(**kwargs)
        self.orientation = 'vertical'
        self.size_hint_y = None
        self.height = dp(120)
        self.padding = dp(15)
        self.spacing = dp(5)
        
        with self.canvas.before:
            Color(0.95, 0.95, 0.95, 1)  # Light gray background
            self.rect = RoundedRectangle(pos=self.pos, size=self.size, radius=[dp(15)])
            
        title_label = Label(
            text=title,
            font_size=dp(16),
            halign='left',
            valign='top',
            size_hint_y=0.4,
            text_size=(self.width, None)
        )
        
        content_label = Label(
            text=content,
            font_size=dp(14),
            halign='left',
            valign='top',
            size_hint_y=0.6,
            color=(0.5, 0.5, 0.5, 1),
            text_size=(self.width, None)
        )
        
        if note_type == "voice":
            # Add waveform visualization placeholder
            with self.canvas:
                Color(0.3, 0.8, 0.3, 1)  # Green color for waveform
                for i in range(10):
                    Rectangle(
                        pos=(self.x + i * dp(20), self.y + dp(40)),
                        size=(dp(4), dp(20 + (i % 3) * 10))
                    )
        
        self.add_widget(title_label)
        self.add_widget(content_label)
        
        self.bind(pos=self.update_rect, size=self.update_rect)
        
    def update_rect(self, *args):
        self.rect.pos = self.pos
        self.rect.size = self.size
