from tkinter import filedialog
import tkinter as tk
from tkinter import ttk
from tkinter import *
from PIL import ImageTk, Image
from bs4 import BeautifulSoup
from urllib.request import Request, urlopen
from io import BytesIO
from requests import *

fridge = []
possible_recipes = []
missing_ing_recipes = {}
specific_recipes = []
window = tk.Tk()