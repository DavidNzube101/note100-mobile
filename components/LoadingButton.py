from . import *
from .RoundedButton import RoundedButton

class LoadingButton(RoundedButton):
    def __init__(self, **kwargs):
        super(LoadingButton, self).__init__(**kwargs)
        self.original_text = self.text
        self.loading = False
        self.dots = 0
        
    def start_loading(self):
        self.loading = True
        self.disabled = True
        Clock.schedule_interval(self.update_loading_text, 0.5)
        
    def stop_loading(self):
        self.loading = False
        self.disabled = False
        self.text = self.original_text
        Clock.unschedule(self.update_loading_text)
        
    def update_loading_text(self, dt):
        if self.loading:
            self.dots = (self.dots + 1) % 4
            self.text = "Loading" + "." * self.dots
            return True
        return False