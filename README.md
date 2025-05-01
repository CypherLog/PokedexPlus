# Pokedex Plus

*A RIC Software Engineering Senior Capstone Project*  
**⚠️ Requires an internet connection for API pulls (e.g., Pokémon images)**

---

## 📖 Overview

**Pokedex Plus** is a desktop application that allows you to explore Generation I Pokémon (001–151).  
View base stats, region maps, Pokémon locations by route, and detailed trainer teams from the Kanto region.

---

## 🛠️ Prerequisites

Most required libraries come built into Python. If something is missing, install it using the commands below.

### ✅ Built-in Python Modules
- `tkinter` – GUI Library
- `tkinter.ttk` – Themed Widgets
- `tkinter.font` / `tkFont` – Font Config
- `json` – JSON Parsing
- `io` – Byte stream handling (`BytesIO`)

---

## 🐍 Installing Python

### 🪟 **Windows**
1. Download Python: [python.org/downloads/windows](https://www.python.org/downloads/windows/)
2. Run the installer → **Check "Add Python to PATH"** → Install
3. Verify in Command Prompt:
   ```sh
   python --version
   ```

### 🍎 **macOS**
1. Install Homebrew:
   ```bash
   /bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
   ```
2. Add to shell:
   ```bash
   echo 'eval "$(/opt/homebrew/bin/brew shellenv)"' >> ~/.zprofile
   eval "$(/opt/homebrew/bin/brew shellenv)"
   ```
3. Install Python:
   ```bash
   brew install python
   ```
4. Verify install:
   ```bash
   python3 --version
   pip3 --version
   ```

---

## 📦 Installing Dependencies

### Mac:
```bash
pip3 install Pillow requests
```

### Windows:
```bash
pip install Pillow requests
```

---

## 🔤 Fonts

You can download fonts from:  
👉 [https://fonts.google.com/selection](https://fonts.google.com/selection)

---

## 💡 Features

- 🔍 Search any Gen 1 Pokémon (001–151) using a `.json` file
- 📊 View base stats and type data
- 🗺️ Explore the game world map with route-based Pokémon data
- 🎒 Access a glossary of trainer teams throughout the Kanto region

---

## 🚀 Running the Project

### macOS:
```bash
cd ~/Downloads/PokedexPlus
python3 pokemonVisual.py
```

### Windows:
```cmd
cd %USERPROFILE%\Downloads\PokedexPlus
python pokedexVisual.py
```
Or:
```cmd
python3 pokedexVisual.py
```

---


## 🧑‍💻 Author & Credits

Developed as a senior capstone project by students of Rhode Island College (RIC)  
Special thanks to [PokéAPI](https://pokeapi.co/) for providing free Pokémon data.

---

## 📄 License

This project is for educational use only.  

---
