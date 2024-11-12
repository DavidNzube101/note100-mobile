# App Essentials
from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.core.window import Window

# Components
from components.UnderlineTextInput import UnderlineTextInput

# Screens
from screens.LoginScreen import LoginScreen
from screens.ResultScreen import ResultScreen
from screens.NotesScreen import NotesScreen

class ModernLoginApp(App):
    def build(self):
        Window.clearcolor = (1, 1, 1, 1)  # White background
        sm = ScreenManager()
        sm.add_widget(LoginScreen(name='login'))
        sm.add_widget(ResultScreen(name='result'))
        sm.add_widget(NotesScreen(name='notes'))
        return sm

if __name__ == '__main__':
    ModernLoginApp().run()