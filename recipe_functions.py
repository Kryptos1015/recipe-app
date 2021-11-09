
from libs import *

def specific_food_window():

    # Window configs
    recipe_finder_window = tk.Toplevel(window)
    recipe_finder_window.configure(bg='black')
    recipe_finder_window.title('Specific Recipe Finder')
    recipe_finder_window.geometry('500x400')

    # Entry box
    canvas_entry = tk.Canvas(recipe_finder_window, width = 400, height = 100, bg= 'black')
    canvas_entry.pack()
    entry1 = tk.Entry(recipe_finder_window) 
    canvas_entry.create_window(200, 30, window=entry1)

    # results window and scrollbar
    container = ttk.Frame(recipe_finder_window)
    canvas = tk.Canvas(container)
    scrollbar = ttk.Scrollbar(container, orient="vertical", command=canvas.yview)
    scrollable_frame = ttk.Frame(canvas)

    scrollable_frame.bind(
        "<Configure>",
        lambda e: canvas.configure(
            scrollregion=canvas.bbox("all")
        )
    )

    canvas.create_window((0, 0), window=scrollable_frame, anchor='center')
    canvas.configure(yscrollcommand=scrollbar.set)
    container.pack()
    canvas.pack(side="left", fill="both", expand=True)
    scrollbar.pack(side="right", fill="y")

    def show_recipe_info(name, url):
        display_info_window = tk.Toplevel(recipe_finder_window)
        display_info_window.configure(bg='black')
        display_info_window.title(name)
        display_info_window.geometry('800x500')

        # Scraping all recipe info
        bs = BeautifulSoup(urlopen(url), "html.parser")
        img_url = bs.find('img', {'alt': name+' '})['src']

        ingredients = []
        ings = bs.findAll(attrs= {'ingredients-item-name'}) # ingredients
        for i in ings:
            ingredients.append(i.get_text().strip())

        # directions
        paragraphs = bs.findAll('p')
        description = paragraphs[0].get_text()
        directions = []

        for i in paragraphs[1:]:
            directions.append(i.get_text())

        blue = '#407294'

        # displaying image
        img_label = Label(display_info_window, text='Image link:', fg=blue, bg='black', font='Courier 14')
        img_label.pack(anchor='n', padx=(10, 0))

        imgl = Label(display_info_window, text=img_url, fg='white', bg='black', font='Courier 10')
        imgl.pack(anchor='n')

        #display description
        desc_label = Label(display_info_window, text='Description:\n', fg=blue, bg='black', font='Courier 14')
        desc_label.pack(anchor='n', padx=(10, 0))

        desc = Label(display_info_window, text=description, fg='white', bg='black', font='Courier 10')
        desc.pack(anchor='n')

        # display ings
        ings_label = Label(display_info_window, text='Ingredients:\n', fg=blue, bg='black', font='Courier 14')
        ings_label.pack(anchor='n', padx=(10, 0))

        for ing in ingredients:
            ing_label = Label(display_info_window, text=ing, fg='white', bg='black', font='Courier 10')
            ing_label.pack(anchor='n')

        # display directions
        dir_label = Label(display_info_window, text='Directions:\n', fg=blue, bg='black', font='Courier 14')
        dir_label.pack(anchor='n', padx=(10, 0))

        for direction in directions:
            dirl = Label(display_info_window, text=direction, fg='white', bg='black', font='Courier 10')
            dirl.pack(anchor='n')




    def get_food():
        food = entry1.get()
        find_recipes_for(food)

    def find_recipes_for(food):
        
        link = 'https://www.allrecipes.com/search/results/?search=' + food.replace(' ','+')
        bs = BeautifulSoup(urlopen(link), "html.parser")

        for recipe in bs.find_all('h3', {'class': 'card__title'}):
            specific_recipes.append(recipe.get_text().strip())
        
        def callback(event):
            recipe_name = event.widget.cget("text")
            urlSlug = '-'.join(recipe_name.split(' '))
            url = 'https://www.allrecipes.com/recipe/'+ urlSlug +'/'
            show_recipe_info(recipe_name, url)

        for recipe in specific_recipes:
            recipe = Label(scrollable_frame, text=recipe, fg="#407294", cursor="hand2")
            recipe.pack(pady = 4, padx = (70, 0))
            recipe.bind("<Button-1>", callback)

    # Button
    enter_button = tk.Button(canvas_entry, text='Find me Recipes', command= get_food)
    canvas_entry.create_window(200, 60, window=enter_button)


# Unfortunately didn't have time to use this function        
def find_recipes_from_personal(recipes):
    for recipe, ings in recipes.items():
        missing_ings = list(set(ings).difference(fridge))

        if set(ings).issubset(fridge): # if ingredients in fridge
            possible_recipes.append(recipe)
        
        elif len(missing_ings) < 5:
            missing_ing_recipes[recipe] = missing_ings

