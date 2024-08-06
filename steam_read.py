#!/usr/bin/env python3
import os
import tkinter as tk
from tkinter import scrolledtext, messagebox
import platform

# Define custom quotes for specific games
quotes = {
    "Team Fortress 2": "A classic that got abandoned.",
    "SourceFilmmaker": "9 years without updates...",
    "Grand Theft Auto V": "Great if you want the simulation of robbing liquor stores.",
    "Half-Life": "OH MY GOD, WE'RE DOOOOMED!!!",
    "The Stanley Parable": "STOP MESSING WITH MY HEAD, NARRATOR!",
    "SourceSDK": "I only ever used this for Hammer.",
    "Source SDK Base 2013 Singleplayer": "Make a mod, you coward!",
    "Source SDK Base 2013 Multiplayer": "Make a multiplayer mod, you coward!",
    "Portal": "I feel sick after placing two portals above and below me...",
    "left 4 dead": "*YOU HAVE ALERTED THE HORDE*",
    "Overwatch": "Stop it... Get some help.",
    "Just Cause": "If you don't like this game, we're not friends.",
    "Krunker": "Basically a COD ripoff mixed with Minecraft graphics.",
    "Half-Life 2": "Sometimes... I dream about cheese.",
    "Five Nights at Freddy's": "Chica didn't serve me that cupcake.",
    "Half-Life 2 Deathmatch": "I threw a toilet at a russian.",
    "GarrysMod": "Love throwing kleiner.mdl around gm_contruct.",
    "Far Cry 3": "Did I ever tell you the definition of insanity?",
    "Among Us": "sus... Did I do the funny?",
    "Call of Duty Black Ops II": "You can't kill me...",
    "HenryStickmin": "HENRYYYYYYYYYYYYYY!!!",
    "OBS Studio": "Too many anime girl on the community hub.",
    "Blender": "I made a cube once then closed the program.",
    "Half-Life 2 Update": "Sometimes... I dream about cheese. - Updated",
    "Lego Star Wars Saga": "I wanna eat lego R2-D2.",
    "Hello Neighbor Pre-Alpha": "This is alright",
    "Hello Neighbor Alpha 1": "This is good.",
    "Hello Neighbor Alpha 2": "This is really good",
    "Hello Neighbor Alpha 3": "This is bad.",
    "Hello Neighbor Alpha 4": "This is terrible.",
    "Hello Neighbor": "This game sucks gods balls.",
    "counter-strike source": "I only got this for Garry's Mod only.",
    "BeamNG.drive": "I don't wanna drive a car anymore.",
    "Apex Legends": "Merry me, Pathfinder.",
    "Counter-Strike Global Offensive": "Can we go back to Source 1, please?",
    "sourcesdk_content": "IDK what this is.",
    "Half-Life MMod":  "HL2 but it has COD mechanics.",
    "Halo The Master Chief Collection": "We playin, Halo Reach with this one!",
    "Fallout 3 goty": "My dad left me.",
    "Fallout Shelter": "I only play this game on my Nintendo Switch.",
    "Battlefield 1": "This game aged quite quickly, but this is EA of course"
}

def list_steam_games(steam_directory):
    try:
        games = [name for name in os.listdir(steam_directory) if os.path.isdir(os.path.join(steam_directory, name))]
        return games
    except FileNotFoundError:
        return None

def get_game_quotes(games):
    game_quotes = {}
    for game in games:
        quote = quotes.get(game, "I didn't do this game or app yet.")
        game_quotes[game] = quote
    return game_quotes

def update_directory():
    global steam_directory
    new_directory = directory_entry.get()
    if os.path.isdir(new_directory):
        steam_directory = new_directory
        games = list_steam_games(steam_directory)
        if games is not None:
            game_quotes = get_game_quotes(games)
            text_area.delete(1.0, tk.END)  # Clear existing content
            for game, quote in game_quotes.items():
                text_area.insert(tk.END, f"{game}: {quote}\n")
        else:
            messagebox.showerror("Error", "Steam directory not found.")
    else:
        messagebox.showerror("Error", "Invalid directory path.")

def create_app():
    global text_area, directory_entry

    # Create main window
    window = tk.Tk()
    window.title("I try to review every steam game and app.")

    # Create a frame for the directory input
    input_frame = tk.Frame(window)
    input_frame.pack(padx=15, pady=5)

    # Directory entry
    tk.Label(input_frame, text="Steam Directory:").pack(side=tk.LEFT)
    directory_entry = tk.Entry(input_frame, width=50)
    directory_entry.pack(side=tk.LEFT, padx=5)
    directory_entry.insert(0, steam_directory)

    # Update button
    update_button = tk.Button(input_frame, text="Update", command=update_directory)
    update_button.pack(side=tk.LEFT, padx=5)

    # Create a scrolled text widget with adjusted size
    text_area = scrolledtext.ScrolledText(window, width=80, height=30, wrap=tk.WORD)
    text_area.pack(padx=15, pady=15)
    
    # Remove maximize and minimize buttons only on Windows
    window.resizable(False, False)
    if platform.system() == "Windows":
        window.wm_attributes('-toolwindow', True)  # This attribute will make the window a tool window, which does not include the minimize/maximize buttons
    
    # Populate the text area with game quotes
    games = list_steam_games(steam_directory)
    if games is not None:
        game_quotes = get_game_quotes(games)
        for game, quote in game_quotes.items():
            text_area.insert(tk.END, f"{game}: {quote}\n")
    else:
        messagebox.showerror("Error", "Steam directory not found.")

    # Start the GUI event loop
    window.mainloop()

# Set the default Steam directory based on the operating system
if platform.system() == "Windows":
    steam_directory = r"C:\Program Files (x86)\Steam\steamapps\common"
elif platform.system() == "Linux":
    steam_directory = os.path.expanduser("~/.local/share/Steam/steamapps/common")
else:
    steam_directory = ""  # Default to empty if OS is not recognized

create_app()

