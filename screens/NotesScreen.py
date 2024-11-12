from . import *

class NotesScreen(Screen):
    def __init__(self, **kwargs):
        super(NotesScreen, self).__init__(**kwargs)
        main_layout = BoxLayout(orientation='vertical', padding=dp(20), spacing=dp(20))
        
        # Header with profile
        header = BoxLayout(size_hint_y=0.1)
        profile_image = AsyncImage(
            source='https://placekitten.com/100/100',  # Placeholder profile image
            size_hint=(None, None),
            size=(dp(40), dp(40))
        )
        with profile_image.canvas.before:
            Color(1, 1, 1, 1)
            self.profile_circle = Ellipse(size=profile_image.size, pos=profile_image.pos)
        
        header.add_widget(profile_image)
        header.add_widget(Label(
            text="My Notes",
            font_size=dp(24),
            halign='left',
            valign='middle',
            text_size=(None, None)
        ))
        
        # Folders section
        folders_label = Label(
            text="My folders",
            font_size=dp(18),
            size_hint_y=None,
            height=dp(30),
            halign='left'
        )
        
        folders_grid = GridLayout(
            cols=3,
            spacing=dp(15),
            size_hint_y=None,
            height=dp(120)
        )
        folders = ["Homework", "Workout", "Sports"]
        for folder in folders:
            folders_grid.add_widget(FolderButton(folder))
            
        # Recent notes section
        recent_label = Label(
            text="Recent notes",
            font_size=dp(18),
            size_hint_y=None,
            height=dp(30),
            halign='left'
        )
        
        # Notes list in a scroll view
        notes_layout = BoxLayout(orientation='vertical', spacing=dp(15), size_hint_y=None)
        notes_layout.bind(minimum_height=notes_layout.setter('height'))
        
        notes = [
            {
                "title": "Voice note",
                "content": "0:15",
                "type": "voice"
            },
            {
                "title": "Grocery lists",
                "content": "🍎 Apple\n🥖 French croissant\n🌶️ Spicy clove",
                "type": "text"
            },
            {
                "title": "List plans for the next vacation",
                "content": "Explore hidden beaches, markets to browse in the old city...",
                "type": "text"
            }
        ]
        
        for note in notes:
            notes_layout.add_widget(
                NoteCard(note["title"], note["content"], note["type"])
            )
            
        notes_scroll = ScrollView(size_hint_y=0.6)
        notes_scroll.add_widget(notes_layout)
        
        # Bottom navigation bar
        nav_bar = BoxLayout(
            size_hint_y=None,
            height=dp(60),
            spacing=dp(20),
            padding=[dp(20), 0]
        )
        
        nav_buttons = ['🔍', '➕', '👤']
        for btn_text in nav_buttons:
            btn = Button(
                text=btn_text,
                font_size=dp(20),
                background_color=(0, 0, 0, 0),
                color=(0, 0, 0, 1)
            )
            nav_bar.add_widget(btn)
        
        # Add all sections to main layout
        main_layout.add_widget(header)
        main_layout.add_widget(folders_label)
        main_layout.add_widget(folders_grid)
        main_layout.add_widget(recent_label)
        main_layout.add_widget(notes_scroll)
        main_layout.add_widget(nav_bar)
        
        self.add_widget(main_layout)