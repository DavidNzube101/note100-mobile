from . import *

class ResultScreen(Screen):
    def __init__(self, **kwargs):
        super(ResultScreen, self).__init__(**kwargs)
        self.layout = BoxLayout(orientation='vertical', padding=50, spacing=20)
        
        with self.layout.canvas.before:
            Color(1, 1, 1, 1)  # White background
            self.rect = Rectangle(size=self.layout.size, pos=self.layout.pos)
        self.layout.bind(size=self._update_rect, pos=self._update_rect)

        self.result_label = Label(text='', font_size=18, color=(0, 0, 0, 1))
        
        go_to_notes = Button(
            text='Proceed',
            size_hint_y=None,
            height=50,
            background_color=(0, 0, 0, 1),
            background_normal=''
        )
        go_to_notes.bind(on_press=self.go_to_notes_screen)
        
        back_button = Button(
            text='Back to Login',
            size_hint_y=None,
            height=50,
            background_color=(0.95, 0.95, 0.95, 1),
            color=(0, 0, 0, 1),
            background_normal=''
        )
        back_button.bind(on_press=self.go_back)
        
        

        self.layout.add_widget(self.result_label)
        self.layout.add_widget(go_to_notes)
        self.layout.add_widget(back_button)
        self.add_widget(self.layout)

    def _update_rect(self, instance, value):
        self.rect.pos = instance.pos
        self.rect.size = instance.size

    def update_result(self, result):
        self.result_label.text = result

    def go_back(self, instance):
        self.manager.current = 'login'
    
    def go_to_notes_screen(self, instance):
        self.manager.current = 'notes'
