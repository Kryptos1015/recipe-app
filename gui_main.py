from libs import *
from import_button import *
from recipe_functions import specific_food_window
from specific_food_button import *

def main_window():
    # Main page, title, author and bg
    window.title('Recipe Scraper Tool')
    window.geometry('500x350')
    window.configure(bg='black')
    title = tk.Label(text='Recipe Scraper Tool', fg='white',bg='black', height=2, font='Courier 14')
    author = tk.Label(text='Made by Rahma', fg='white', bg='black',font='Courier 10')
    title.pack()
    author.pack()

    # Background image
    bg = (Image.open('bg.jpg')).resize((386,240), Image.ANTIALIAS)
    bg = ImageTk.PhotoImage(bg)
    panel = tk.Label(window, image=bg)
    panel.image = bg
    panel.pack()

    # Import fridge file button
    select_datafile = tk.Button(text='Import Fridge File', fg='black', bg='white', width=18, height=2, font='Courier 10', command= lambda: import_file(fridge))
    select_datafile.place(x=30, y=100)

    # Specific food based recipes button
    view_datafile = tk.Button(text='Specific Food Based Recipes', fg='black', bg='white', width=27, height=2, font='Courier 10', command= specific_food_window)
    view_datafile.place(x=30, y=160)




main_window()
window.mainloop()