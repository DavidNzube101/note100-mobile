from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.boxlayout import BoxLayout
from kivy.graphics import Color, Rectangle, Line, Ellipse
from kivy.uix.anchorlayout import AnchorLayout
from kivy.metrics import dp
from kivy.uix.image import Image, AsyncImage
from kivy.uix.label import Label
from kivy.uix.checkbox import CheckBox
from kivy.uix.button import Button
from kivy.uix.gridlayout import GridLayout
from kivy.uix.scrollview import ScrollView
from kivy.clock import Clock

from components.UnderlineTextInput import UnderlineTextInput
from components.FolderButton import FolderButton
from components.NoteCard import NoteCard
from components.LoadingButton import LoadingButton

# Utilites
from dotenv import load_dotenv, find_dotenv
import requests
