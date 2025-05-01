import tkinter as tk
from PIL import Image, ImageTk
import json
from tkinter import ttk
from tkinter import font as tkFont
import requests
from io import BytesIO
from tkinter import Label, Button, Frame
from tkinter import Scrollbar
#Pokemon Locations File
with open("pokemonLocations.json", "r") as loc_file:
    location_info = json.load(loc_file)

#Pokedex File
with open("pokedex.json", "r") as file:
    pokemon_info = json.load(file)
#Trainer Information File
with open("pokemon_trainers.json", "r") as file:
    trainer_info = json.load(file)
# Create the main window
root = tk.Tk()
root.title("Pokédex+")

press_start_font = tkFont.Font(family="Press Start 2P", size=10)

# Gets the image of the Pokemon from the API and grabs the exact sprite (Logans coding)
def get_image(pokemon_name):
    url = f"https://pokeapi.co/api/v2/pokemon/{pokemon_name.lower()}"
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        image_url = data["sprites"]["front_default"]
        image_response = requests.get(image_url, stream=True)
        if image_response.status_code == 200:
            image = Image.open(image_response.raw)
            image = image.resize((150, 150), Image.LANCZOS)
            return ImageTk.PhotoImage(image)
    return None
#In the case of the user wanting to use their own json, this checks to see if the file is in the right format.
    if response.status_code == 200:
        pokemon_data = response.json()
        image_url = pokemon_data["sprites"]["versions"]["generation-v"]["black-white"]["front_default"]
        
        image_response = requests.get(image_url)
        img = Image.open(BytesIO(image_response.content))
        return ImageTk.PhotoImage(img)
    else:
        return None


# Load paths to Pokédex and button images(Abbies Coding)
closed_pokedex_path = "Images/pokedex.png"
open_pokedex_path = "Images/openpokedex.png"
open_button_path = "Images/open_button.png"
left_button_path = "Images/left_button.png"
background_image_path = "Images/background5.jpeg"
map_button_path = "Images/map_mode.png"
pokedex_button_path = "Images/pokedex_mode.png"
trainer_button_path = "Images/trainer_mode.png"
map_image_path = "Images/Kanto_Map.png"
location_button_path = "Images/Kanto_Map_Buttons.png"

# Load and resize images(Abbies Coding)
closed_pokedex = Image.open(closed_pokedex_path)
open_pokedex = Image.open(open_pokedex_path)
open_button_img = Image.open(open_button_path).resize((50, 50), Image.NEAREST)
left_button_img = Image.open(left_button_path).resize((30, 30), Image.NEAREST)
map_button_img = Image.open(map_button_path).resize((50, 40), Image.NEAREST)
trainer_button_img = Image.open(trainer_button_path).resize((50, 40), Image.NEAREST)
pokedex_button_img = Image.open(pokedex_button_path).resize((50, 40), Image.NEAREST)
background_img = Image.open(background_image_path).resize((267, 267), Image.NEAREST)
map_img = Image.open(map_image_path).resize((275, 275), Image.NEAREST)
location_button_img = Image.open(location_button_path).resize((30, 30), Image.NEAREST)

# Resize open Pokédex to match closed one (Abbies Coding)
open_pokedex = open_pokedex.resize((int(open_pokedex.width * closed_pokedex.height / open_pokedex.height), closed_pokedex.height))

# Convert images to work for tkinter (Abbies Coding)
open_pokedex = ImageTk.PhotoImage(open_pokedex)
closed_pokedex = ImageTk.PhotoImage(closed_pokedex)
open_button_photo = ImageTk.PhotoImage(open_button_img)
left_button_photo = ImageTk.PhotoImage(left_button_img)
map_button_photo = ImageTk.PhotoImage(map_button_img)
trainer_button_photo = ImageTk.PhotoImage(trainer_button_img)
pokedex_button_photo = ImageTk.PhotoImage(pokedex_button_img)
background_photo = ImageTk.PhotoImage(background_img)
map_photo = ImageTk.PhotoImage(map_img)
location_button = ImageTk.PhotoImage(location_button_img)

# Create a canvas to display the open and closed pokedex images(Abbies Coding)
canvas = tk.Canvas(root, width=closed_pokedex.width(), height=closed_pokedex.height(), highlightthickness=0)
canvas.pack(fill=tk.BOTH, expand=True)

# Display the closed Pokédex image(Abbies Coding)
image_container = canvas.create_image(0, 0, anchor=tk.NW, image=closed_pokedex)

# Edit sizing of canvases where info and image of pokemon will be displayed(matching sizes with the built in screens on pokedex image)
pokemon_image_canvas_x, pokemon_image_canvas_y = 22, 122
pokemon_image_canvas_width, pokemon_image_canvas_height = 267, 267

pokemon_info_canvas_x, pokemon_info_canvas_y = 375, 125
pokemon_info_canvas_width, pokemon_info_canvas_height = 220, 290

# Create canvases for the open Pokédex screens where info and image of pokemon will be displayed
pokemon_image_canvas = tk.Canvas(root, width=pokemon_image_canvas_width, height=pokemon_image_canvas_height, 
                                 bg="#ECF0F1", highlightbackground="red", bd=2)

pokemon_info_canvas = tk.Canvas(root, width=pokemon_info_canvas_width, height=pokemon_info_canvas_height, 
                                bg="#2C3E50", highlightbackground="blue", bd=2)

# Set image as background of image canvas
pokemon_image_canvas.create_image(0, 0, image=background_photo, anchor="nw")


# Start off pokedex state as closed(Abbies coding)
pokedex_state = "closed"
mode = "pokedex"
# Function to toggle Pokédex open/closed
def toggle_pokedex():
    global pokedex_state
    if pokedex_state == "closed":
        # Open Pokédex
        canvas.config(width=open_pokedex.width(), height=open_pokedex.height())
        canvas.itemconfig(image_container, image=open_pokedex)
        pokemon_image_canvas.place(x=pokemon_image_canvas_x, y=pokemon_image_canvas_y)
        pokemon_info_canvas.place(x=pokemon_info_canvas_x, y=pokemon_info_canvas_y)
        switch_to_pokedex_mode()
        show_open_button()  
        show_left_button()  
        show_map_button()
        show_trainer_button()  
        show_pokedex_button()    
        hide_search_bar()  
        hide_open_button()
        show_search_bar()
        pokedex_state = "open" 
    elif pokedex_state == "open":
        # Close Pokédex
        canvas.config(width=closed_pokedex.width(), height=closed_pokedex.height())
        canvas.itemconfig(image_container, image=closed_pokedex)
        pokemon_image_canvas.place_forget()
        pokemon_info_canvas.place_forget()
        hide_search_bar()  
        show_open_button()  
        hide_left_button()
        hide_map_button()
        hide_trainer_button()
        hide_pokedex_button()
        hide_map_location_buttons()
        pokemon_info_canvas.delete("all")
        pokedex_state = "closed"

#This shows the scroll bar for the canvas(Logans coding)
def show_info_scroll_canvas():
    info_scroll_canvas.place(x=pokemon_info_canvas_x, y=pokemon_info_canvas_y)
    info_scrollbar.place(x=pokemon_info_canvas_x + pokemon_info_canvas_width - 10, y=pokemon_info_canvas_y, height=pokemon_info_canvas_height)
#This hides the scroll bar
def hide_info_scroll_canvas():
    info_scroll_canvas.place_forget()
    info_scrollbar.place_forget()

#Function to switch into Pokedex mode(Abbies coding)
def switch_to_pokedex_mode():
    global mode
    mode = "pokedex"
    show_search_bar()
    pokemon_image_canvas.place(x=pokemon_image_canvas_x, y=pokemon_image_canvas_y)
    pokemon_info_canvas.place(x=pokemon_info_canvas_x, y=pokemon_info_canvas_y)
    pokemon_image_canvas.delete("all")
    pokemon_image_canvas.create_image(0, 0, image=background_photo, anchor="nw")
    pokemon_info_canvas.delete("all")
    hide_map_location_buttons()
    hide_info_scroll_canvas()
#Definition to switch to map mode
def switch_to_map_mode():
    global mode
    mode = "map"
    hide_search_bar()
    pokemon_info_canvas.delete("all")
    pokemon_image_canvas.delete("all") 
    pokemon_image_canvas.create_image(0, 0, image=map_photo, anchor="nw") 
    create_map_city_buttons()  
    show_map_location_buttons()
#Definition to switch to trainer mode
def switch_to_trainer_mode():
    global mode
    mode = "trainer"
    hide_search_bar()
    pokemon_info_canvas.delete("all")
    pokemon_image_canvas.delete("all")
    hide_map_location_buttons()
    hide_info_scroll_canvas()
    pokemon_image_canvas.create_image(0, 0, image=map_photo, anchor="nw")
    pokemon_image_canvas.place(x=pokemon_image_canvas_x, y=pokemon_image_canvas_y)
    pokemon_info_canvas.place_forget()
    # Open Trainer Glossary window
    open_trainer_glossary()

#Definition for Pokemon search(Abbie and Logans coding)
def pokemon_search():
    user_input = entry.get().strip()
    pokemon_result = None
    # Check if the input is a digit (number)
    if user_input.isdigit():
        # Find the Pokémon by Pokedex number
        pokedex_number = int(user_input)  # Normalize number format
        
        # Search for the Pokémon in the Info Sheet
        for pokemon in pokemon_info["Info Sheet"]:
            if pokemon["Pokedex Entry"] == pokedex_number:
                pokemon_result = pokemon
                break
        
        if pokemon_result:
            pokemon_stats = (f"#{pokemon_result['Pokedex Entry']}: {pokemon_result['Name']}\n"
                       f"Type: {pokemon_result['Type'].strip()}\n"
                       f"Height: {pokemon_result['Height (Meters)'].strip()}\n"
                       f"Weight: {pokemon_result['Weight (Kg)'].strip()}\n"
                       f"Abilities: {pokemon_result['Abilities '].strip()}\n"
                       f"Base HP: {pokemon_result['Base HP']}\n"
                       f"Base Attack: {pokemon_result['Base Attack']}\n"
                       f"Base Defense: {pokemon_result['Base Defense']}\n"
                       f"Sp. Atk: {pokemon_result['Sp. Atk']}\n"
                       f"Sp. Def: {pokemon_result['Sp. Def']}\n"
                       f"Speed: {pokemon_result['Speed']}\n"
                       f"Total: {pokemon_result['Total']}")
        else:
            pokemon_stats = "Pokémon not found."
    else:
        pokemon_stats = "Enter valid Pokedex+ ID Number."

    #Gets and displays the image of the Pokemon
    image = get_image(pokemon_result['Name'])
    if image:
            pokemon_image_canvas.delete("pokemon_img")  # Clear previous image
            pokemon_image_canvas.create_image(130, 160, anchor=tk.CENTER, image=image)
            pokemon_image_canvas.image = image  # Prevent garbage collection
    else:
        pokemon_stats = "Pokémon not found."
    
    pokemon_info_canvas.delete("all")
    entry.delete(0, tk.END)

    

    
    # Display result text in the info canvas
    pokemon_info_canvas.create_text(
        15,    
        45, 
        anchor="nw", 
        text=pokemon_stats,  
        font=(press_start_font),  
        fill="white",  
        width=pokemon_info_canvas_width - 20  
    )


# Create the Entry widget for search bar(Abbie and Logans code for search bar)
entry = tk.Entry(root, bd=0, relief="flat", font=("Arial", 14)) 
entry.place_forget()  
entry.bind("<Return>", lambda event: pokemon_search())

# Placeholder tracking flag
placeholder_active = True

# Function when entry is clicked/focused in
def when_focus_in(event):
    global placeholder_active
    if placeholder_active:
        entry.delete(0, tk.END)
        entry.config(fg='black')
        placeholder_active = False


# Bind focus events
entry.bind("<FocusIn>", when_focus_in)


# Function to show the search bar
def show_search_bar():
    global placeholder_active
    entry.place(x=60, y=440, width=215, height=30)
    if not entry.get():  # If nothing typed in
        entry.insert(0, "Enter Pokémons number")
        entry.config(fg='gray')
        placeholder_active = True

# Function to hide the search bar
def hide_search_bar():
    entry.place_forget()



# Function to show the open button(Abbies code for hiding and showing all buttons)
def show_open_button():
    global open_button_container
    open_button_container = canvas.create_window(225, closed_pokedex.height() - 80, anchor=tk.NW, window=open_button)

# Function to hide the open button
def hide_open_button():
    canvas.delete(open_button_container)  

# Function to show the left button
def show_left_button():
    global left_button_container, left_button
    left_button = tk.Button(root, image=left_button_photo, command=toggle_pokedex, 
                            borderwidth=0, highlightthickness=0, bg="#D32F2F")
    left_button.image = left_button_photo  
    left_button_container = canvas.create_window(8, open_pokedex.height() - 40, anchor=tk.NW, window=left_button)

# Function to hide the left button
def hide_left_button():
    canvas.delete(left_button_container)

# Functions to show mode switching buttons
def show_map_button():
    global map_button_container, map_button
    map_button = tk.Button(root, image=map_button_photo, command=switch_to_map_mode, borderwidth=0, highlightthickness=0, bg="#D32F2F")
    map_button.image = map_button_photo  
    map_button_container = canvas.create_window(530, open_pokedex.height() - 50, anchor=tk.NW, window=map_button)
#Hides the map button when it isnt needed
def hide_map_button():
    canvas.delete(map_button_container)
#Shows the trainer button only when needed
def show_trainer_button():
    global trainer_button_container, trainer_button
    trainer_button = tk.Button(root, image=trainer_button_photo, command=switch_to_trainer_mode, borderwidth=0, highlightthickness=0, bg="#D32F2F")
    trainer_button.image = trainer_button_photo 
    trainer_button_container = canvas.create_window(470, open_pokedex.height() - 50, anchor=tk.NW, window=trainer_button)


#Hides the trainer button when not needed
def hide_trainer_button():
    canvas.delete(trainer_button_container)

#Shows the Pokedex Button when needed
def show_pokedex_button():
    global pokedex_button_container, pokedex_button
    pokedex_button = tk.Button(root, image=pokedex_button_photo, command=switch_to_pokedex_mode, borderwidth=0, highlightthickness=0, bg="#D32F2F")
    pokedex_button.image = pokedex_button_photo  
    pokedex_button_container = canvas.create_window(410, open_pokedex.height() - 50, anchor=tk.NW, window=pokedex_button)


#Hides the Pokedex button when it is not needed(Abbies coding)
def hide_pokedex_button():
    canvas.delete(pokedex_button_container)

# locations for map buttons(Abbies coding)
map_locations = [
    {"x": 23, "y": 40, "town": "Pallet Town"},
    {"x": 56, "y": 56, "town": "Viridian City"},
    {"x": 137, "y": 88, "town": "Cerulean City"},
    {"x": 185, "y": 88, "town": "Lavender Town"},
    {"x": 185, "y": 40, "town": "Rock Tunnel Area"},
    {"x": 250, "y": 88, "town": "Power Plant Area"},
    {"x": 185, "y": 153, "town": "Fuchsia City"},
    {"x": 56, "y": 250, "town": "Cinnabar Islands"},
    {"x": 153, "y": 217, "town": "Seafoam Islands"},
    {"x": 56, "y": 185, "town": "Vermilion City"},
    {"x": 56, "y": 137, "town": "Saffron City"},
]

#Definition to show the town name(Logans coding)
def display_town_name(town_name):
    pokemon_info_canvas.delete("all")
    pokemon_info_canvas.create_text(
        15,
        45,
        anchor="nw",
        text=town_name,
        font=(press_start_font),
        fill="white",
        width=pokemon_info_canvas_width - 20
    )

#Definition to show the location Pokemon info(Logans coding)
def show_location_info(town_name):
    # Clear previous info
    for widget in info_frame.winfo_children():
        widget.destroy()
    # Find all keys matching the town name
    for key in location_info:
        if town_name.lower() in key.lower():
            tk.Label(info_frame, text=key, bg="#2C3E50", fg="white", font=(press_start_font, 8, "bold"), anchor="w", justify="left").pack(anchor="w", pady=(0, 2))
            for entry in location_info[key]:
                text = (
                    f"Pokémon: {entry.get('Pokemon', '')}\n"
                    f"Games: {entry.get('Games', '')}\n"
                    f"How To Gain: {entry.get('How To Gain', '')}\n"
                    f"Levels: {entry.get('Levels', '')}\n"
                    f"Rate: {entry.get('Rate', '')}\n"
                )
                tk.Label(info_frame, text=text, bg="#2C3E50", fg="white", font=(press_start_font, 7), anchor="w", justify="left").pack(anchor="w", padx=5, pady=(0, 10))
location_buttons = []



#Creates the buttons for the map(Abbies code)
def create_map_city_buttons():
    global location_buttons
    for location in map_locations:
        town_name = location["town"]
        locationbtn = tk.Button(root, image=location_button, width=2, height=1,
                        bg="black", activebackground="gray",
                        command=lambda town=town_name: on_town_button_click(town))
        location_btn_container = canvas.create_window(
            pokemon_image_canvas_x + location["x"],
            pokemon_image_canvas_y + location["y"],
            anchor=tk.CENTER,
            window=locationbtn
        )
        location_buttons.append((locationbtn, location_btn_container))

#Shows the map buttons (Abbies coding)
def show_map_location_buttons():
    for locationbtn, container in location_buttons:
        canvas.itemconfigure(container, state='normal')

#Hides map button when the map is not used
def hide_map_location_buttons():
    for locationbtn, container in location_buttons:
        canvas.itemconfigure(container, state='hidden')



def on_town_button_click(town_name):
    # Hide the normal info canvas, show the scrollable one (Logans coding)
    pokemon_info_canvas.place_forget()
    show_info_scroll_canvas()
    show_location_info(town_name)

# Logans coding for scroll bar
info_scroll_canvas = tk.Canvas(root, width=pokemon_info_canvas_width, height=pokemon_info_canvas_height, 
                               bg="#2C3E50", highlightbackground="blue", bd=2)
info_scrollbar = Scrollbar(root, orient="vertical", command=info_scroll_canvas.yview)
info_frame = tk.Frame(info_scroll_canvas, bg="#2C3E50")

info_frame_id = info_scroll_canvas.create_window((0, 0), window=info_frame, anchor="nw")
info_scroll_canvas.configure(yscrollcommand=info_scrollbar.set)

def on_frame_configure(event):
    info_scroll_canvas.configure(scrollregion=info_scroll_canvas.bbox("all"))

info_frame.bind("<Configure>", on_frame_configure)



#Definition to open the glossary for the trainers(Whole trainer section is Kevin and Logans coding)
def open_trainer_glossary():
    glossary_win = tk.Toplevel(root)
    glossary_win.title("Pokémon Trainer Glossary")
    glossary_win.geometry("600x300")
    glossary_win.configure(bg="white")

    # Use your existing font detection from TrainerGlossary.py
    def get_custom_font():
        try:
            import tkinter.font as tkFont
            families = tkFont.families()
            if "Press Start 2P" in families:
                return "Press Start 2P"
        except Exception as e:
            print("Font check failed:", e)
        return "Courier"

    custom_font = get_custom_font()

    # Helper functions from TrainerGlossary.py:
    def get_pokemon_image(name):
        try:
            url = f"https://pokeapi.co/api/v2/pokemon/{name.lower()}"
            res = requests.get(url)
            if res.status_code == 200:
                data = res.json()
                sprite_url = data['sprites']['front_default']
                if sprite_url:
                    img_data = requests.get(sprite_url, stream=True).raw
                    image = Image.open(img_data).resize((96, 96), Image.NEAREST)
                    return ImageTk.PhotoImage(image)
        except Exception as e:
            print(f"Error loading sprite for {name}: {e}")
        return None
#Parses the trainer entry from the json file
    def extract_pokemon_list(entry):
        result = []
        levels_raw = str(entry.get("Levels", ""))
        levels = [l.strip() for l in levels_raw.split(",")] if levels_raw else []
        for i in range(1, 7):
            name = entry.get(f"Pokemon {i}")
            if name and name != "N/A":
                level = levels[i-1] if i - 1 < len(levels) else "?"
                result.append((name, level))
        return result
#Displays the popup window with the trainer information
    def show_popup(title, entries):
        popup = tk.Toplevel(glossary_win)
        popup.title(title)
        popup.geometry("800x600")
        popup.configure(bg="white")

        canvas = tk.Canvas(popup, bg="white", borderwidth=0)
        frame = tk.Frame(canvas, bg="white")
        scrollbar = tk.Scrollbar(popup, orient="vertical", command=canvas.yview)
        canvas.configure(yscrollcommand=scrollbar.set)

        scrollbar.pack(side="right", fill="y")
        canvas.pack(side="left", fill="both", expand=True)
        canvas.create_window((0, 0), window=frame, anchor="nw")
#Adjusts the scroll region in the canvas
        def on_configure(event):
            canvas.configure(scrollregion=canvas.bbox("all"))

        frame.bind("<Configure>", on_configure)
#Goes through the entries for the trainers and displays their information
        for entry in entries:
            entry_frame = tk.Frame(frame, bg="white", pady=10)
            entry_frame.pack(fill="x", padx=10)

            trainer_name = entry.get("Trainers", "Unknown Trainer")
            how_to_fight = entry.get("How To Fight", "Unknown Method")
            item_uses = entry.get("Item Uses", "None")
#Displays the trainer name and strategy
            trainer_label = tk.Label(
                entry_frame,
                text=f"{trainer_name} — How to Fight: {how_to_fight} | Items: {item_uses}",
                font=(custom_font, 10),
                fg="black",
                bg="white",
                wraplength=750,
                justify="left"
            )
            trainer_label.pack(anchor="w")
#Displays Pokemon image and the levels side by side
            pokemon_info = extract_pokemon_list(entry)
            poke_frame = tk.Frame(entry_frame, bg="white")
            poke_frame.pack(anchor="w", pady=5)

            for pkmn_name, level in pokemon_info:
                poke_img = get_pokemon_image(pkmn_name)
                if poke_img:
                    img_label = tk.Label(poke_frame, image=poke_img, bg="white")
                    img_label.image = poke_img
                    img_label.pack(side="left", padx=5)
#Label for the name and level of the Pokemon
                label = tk.Label(
                    poke_frame,
                    text=f"{pkmn_name}, Lv {level}",
                    font=(custom_font, 8),
                    fg="black",
                    bg="white"
                )
                label.pack(side="left", padx=(0, 20))
#Dropdown for selecting the location

    label = tk.Label(glossary_win, text="Select A Location:", font=(custom_font, 10), fg="black", bg="white")
    label.pack(pady=15)
#Dropdown menu with all locations
    options = list(trainer_info.keys())
    dropdown_var = tk.StringVar()
    dropdown = ttk.Combobox(glossary_win, textvariable=dropdown_var, values=options, width=60)
    dropdown.pack(pady=5)
#Displays the information when th submit button is selected
    def on_submit():
        selected = dropdown_var.get()
        if selected in trainer_info:
            show_popup(selected, trainer_info[selected])
        else:
            show_popup("Error", [{"Trainers": "No data found."}])

    submit_button = ttk.Button(glossary_win, text="Submit", command=on_submit)
    submit_button.pack(pady=20)



# Create Open button(Abbies coding)
open_button = tk.Button(root, image=open_button_photo, command=toggle_pokedex, 
                        borderwidth=0, highlightthickness=0, bg="#D32F2F")
open_button.image = open_button_photo  

# Initially place open button
show_open_button()

# Run the application
root.mainloop()
