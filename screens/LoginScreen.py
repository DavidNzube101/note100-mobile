import os
from . import *

load_dotenv(find_dotenv())

NOTE100_LOCAL_ADDRESS = os.getenv('NOTE100_LOCAL_ADDRESS')
NOTE100_API_ROUTE = os.getenv('NOTE100_API_ROUTE')

class LoginScreen(Screen):
    def __init__(self, **kwargs):
        super(LoginScreen, self).__init__(**kwargs)
        main_layout = BoxLayout(orientation='vertical', padding=[dp(40), dp(20)], spacing=dp(20))
        
        # White background
        with main_layout.canvas.before:
            Color(1, 1, 1, 1)  # White
            self.rect = Rectangle(size=main_layout.size, pos=main_layout.pos)
        main_layout.bind(size=self._update_rect, pos=self._update_rect)

        # Logo
        logo_layout = AnchorLayout(size_hint_y=0.2)
        logo = Image(source='logo.png', size_hint=(None, None), size=(dp(50), dp(50)))
        logo_layout.add_widget(logo)
        
        # Welcome text
        welcome_label = Label(
            text='Welcome back!',
            color=(0, 0, 0, 1),
            font_size=dp(24),
            size_hint_y=None,
            height=dp(40),
            halign='left'
        )
        subtitle_label = Label(
            text='Please enter your details',
            color=(0, 0, 0, 0.5),
            font_size=dp(14),
            size_hint_y=None,
            height=dp(30),
            halign='left'
        )

        # Input fields
        email_label = Label(
            text='Email',
            color=(0, 0, 0, 0.8),
            size_hint_y=None,
            height=dp(30),
            halign='left'
        )
        self.email = UnderlineTextInput(
            multiline=False,
            size_hint_y=None,
            height=dp(40)
        )
        
        password_label = Label(
            text='Password',
            color=(0, 0, 0, 0.8),
            size_hint_y=None,
            height=dp(30),
            halign='left'
        )
        self.password = UnderlineTextInput(
            multiline=False,
            password=True,
            size_hint_y=None,
            height=dp(40)
        )

        # Remember me and Forgot password row
        remember_forgot_layout = BoxLayout(size_hint_y=None, height=dp(40))
        remember_layout = BoxLayout(size_hint_x=0.5)
        self.remember = CheckBox(color=(0, 0, 0, 1), size_hint_x=None, width=dp(30))
        remember_text = Label(
            text='Remember for 30 days',
            color=(0, 0, 0, 0.8),
            font_size=dp(12)
        )
        forgot_button = Button(
            text='Forgot password?',
            color=(0, 0, 0, 0.5),
            size_hint_x=0.5,
            background_color=(0, 0, 0, 0),
            font_size=dp(12)
        )
        
        remember_layout.add_widget(self.remember)
        remember_layout.add_widget(remember_text)
        remember_forgot_layout.add_widget(remember_layout)
        remember_forgot_layout.add_widget(forgot_button)

        # Login buttons
        login_button = Button(
            text='Log in',
            size_hint_y=None,
            height=dp(50),
            background_color=(0, 0, 0, 1),
            background_normal=''
        )
        google_button = Button(
            text='Log in with Google',
            size_hint_y=None,
            height=dp(50),
            background_color=(0.95, 0.95, 0.95, 1),
            color=(0, 0, 0, 1),
            background_normal=''
        )
        
        # Sign up text
        signup_layout = BoxLayout(size_hint_y=None, height=dp(40))
        signup_text = Label(
            text="Don't have an account?",
            color=(0, 0, 0, 0.5),
            font_size=dp(12)
        )
        signup_button = Button(
            text='Sign Up',
            color=(0, 0, 0, 1),
            size_hint_x=None,
            width=dp(60),
            background_color=(0, 0, 0, 0),
            font_size=dp(12)
        )
        
        signup_layout.add_widget(signup_text)
        signup_layout.add_widget(signup_button)

        # Add all widgets to main layout
        main_layout.add_widget(logo_layout)
        main_layout.add_widget(welcome_label)
        main_layout.add_widget(subtitle_label)
        main_layout.add_widget(email_label)
        main_layout.add_widget(self.email)
        main_layout.add_widget(password_label)
        main_layout.add_widget(self.password)
        main_layout.add_widget(remember_forgot_layout)
        main_layout.add_widget(login_button)
        main_layout.add_widget(google_button)
        main_layout.add_widget(signup_layout)

        login_button.bind(on_press=self.login)
        self.add_widget(main_layout)

    def _update_rect(self, instance, value):
        self.rect.pos = instance.pos
        self.rect.size = instance.size

    def login(self, instance):
        username = self.email.text
        password = self.password.text
        remember = self.remember.active
        
        try:
            print(NOTE100_LOCAL_ADDRESS, NOTE100_API_ROUTE)
            response = requests.post(
                f'{NOTE100_LOCAL_ADDRESS}{NOTE100_API_ROUTE}login',
                data={
                    'username': username,
                    'password': password,
                    'remember': remember
                }
            )
            result = response.text
        except requests.RequestException as e:
            result = f"Error: {str(e)}"

        result_screen = self.manager.get_screen('result')
        result_screen.update_result(result)
        self.manager.current = 'result'
        
        
        