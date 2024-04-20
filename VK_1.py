import os
import winreg
import urllib.request

def find_goose():
    try:
        key = winreg.OpenKey(winreg.HKEY_CURRENT_USER, r"Software\Valve\Steam")

        steam_folder_path, _ = winreg.QueryValueEx(key, "SteamPath")
       
        goose_folder = os.path.join(steam_folder_path, r"steamapps\common\Goose Goose Duck")

        return goose_folder
    except FileNotFoundError:
        print("Game not found")
        return None

def registry_changes(reg_file_path):
     os.system('regedit.exe /s "{}"'.format(reg_file_path))

def download_file(url, game_directory):
    try:
        destination = os.path.join(game_directory, "settings.reg")
        
        with urllib.request.urlopen(url) as response:
                with open(destination, 'wb') as out_file:
                    out_file.write(response.read())
        registry_changes(destination)
    except Exception as e:
        print("An error occurred while applying changes to the registry:", e) 
    
    
goose_path = find_goose()
url = "https://drive.usercontent.google.com/download?id=1IGENwFzLm8bBEboISadYSNEdxbnjz1fH&export=download&authuser=0&confirm=t&uuid=ce65747d-9b29-444d-883c-39964c0f0a39&at=APZUnTXFi0RHtt2aQeB4KbQykYFk%3A1713626715056"
download_file(url, goose_path)


