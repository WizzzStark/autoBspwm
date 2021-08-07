import os, time
from sys import stdout

def red():
    RED = "\033[1;31m"
    stdout.write(RED)

def green():
    GREEN = "\033[0;32m"
    stdout.write(GREEN)

def blue():
    BLUE = "\033[1;34m"
    stdout.write(BLUE)

def yellow():
    YELLOW = "\033[1;33m"
    stdout.write(YELLOW)

def purple():
    PURPLE = "\033[1;35m"
    stdout.write(PURPLE)

def white():
    WHITE = "\033[1;37m"
    stdout.write(WHITE)

banner = """
 █████╗ ██╗   ██╗████████╗ ██████╗ ██████╗ ███████╗██████╗ ██╗    ██╗███╗   ███╗
██╔══██╗██║   ██║╚══██╔══╝██╔═══██╗██╔══██╗██╔════╝██╔══██╗██║    ██║████╗ ████║
███████║██║   ██║   ██║   ██║   ██║██████╔╝███████╗██████╔╝██║ █╗ ██║██╔████╔██║
██╔══██║██║   ██║   ██║   ██║   ██║██╔══██╗╚════██║██╔═══╝ ██║███╗██║██║╚██╔╝██║  (by Yorkox)
██║  ██║╚██████╔╝   ██║   ╚██████╔╝██████╔╝███████║██║     ╚███╔███╔╝██║ ╚═╝ ██║
╚═╝  ╚═╝ ╚═════╝    ╚═╝    ╚═════╝ ╚═════╝ ╚══════╝╚═╝      ╚══╝╚══╝ ╚═╝     ╚═╝
"""

def menu():
    red()
    print(banner)
    blue()
    time.sleep(1)
    print("1 -> Instalar Requerimientos necesarios\n")
    print("2 -> Instalar bspwm\n")
    print("3 -> Instalar Polybar\n")
    print("4 -> Instalar p10k\n")
    print("5 -> All In One\n")
    print("6 -> Salir\n")
    time.sleep(1)

    usuario = input("Introduce el nombre de tu usuario de bajos privilegios(Ej: kali): ")
    time.sleep(1)
    option = input("\n-->> ")

    if option == "1":
        req()
    if option == "2":
        bspwm()
    if option == "3":
        polybar()
    if option == "4":
        p10k()
    if option == "5":
        req()
        bspwm()
        polybar()
        p10k()
    if option == "6":
        exit()

def req():
    green()
    print("[+] Instalando requerimientos...\n")

    # Instalando Requerimientos
    os.system("sudo apt install build-essential git vim xcb libxcb-util0-dev libxcb-ewmh-dev libxcb-randr0-dev libxcb-icccm4-dev libxcb-keysyms1-dev libxcb-xinerama0-dev libasound2-dev libxcb-xtest0-dev libxcb-shape0-dev -y")
    os.system("sudo apt install cmake cmake-data pkg-config python3-sphinx libcairo2-dev libxcb1-dev libxcb-util0-dev libxcb-randr0-dev libxcb-composite0-dev python3-xcbgen xcb-proto libxcb-image0-dev libxcb-ewmh-dev libxcb-icccm4-dev libxcb-xkb-dev libxcb-xrm-dev libxcb-cursor-dev libasound2-dev libpulse-dev libjsoncpp-dev libmpdclient-dev libcurl4-openssl-dev libnl-genl-3-dev -y")
    os.system("sudo apt install meson libxext-dev libxcb1-dev libxcb-damage0-dev libxcb-xfixes0-dev libxcb-shape0-dev libxcb-render-util0-dev libxcb-render0-dev libxcb-randr0-dev libxcb-composite0-dev libxcb-image0-dev libxcb-present-dev libxcb-xinerama0-dev libpixman-1-dev libdbus-1-dev libconfig-dev libgl1-mesa-dev libpcre2-dev libevdev-dev uthash-dev libev-dev libx11-xcb-dev libxcb-glx0-dev -y")
    os.system("sudo apt install bspwm rofi caja feh gnome-terminal -y")
    os.system("apt install firejail")

    time.sleep(2)
    print("[+] Requetimientos instalados correctamente")

def bspwm():
    green()

    # Clona la repo de bspwm
    os.system("git clone https://github.com/baskerville/bspwm.git")
    os.system("mv bspwm/* .")
    os.system("sudo rm -r bspwm/")
    os.system("make")

    # Crea directorio para fondo de pantalla
    os.system("mkdir ~/Desktop/Images")
    os.system("cp tools/fondo.jpg ~/Desktop/Images")

    # Acava del build
    os.system("sudo make install")

    # Elimina los archivos de bspwm
    os.system("sudo rm -r artworks/ contrib/ doc/ src/ tests/ bspc bspc.o bspwm bspwm.o desktop.o events.o ewmh.o geometry.o helpers.o history.o jsmn.o LICENSE Makefile messages.o monitor.o parse.o pointer.o query.o README.md restore.o rule.o settings.o Sourcedeps stack.o subscribe.o tree.o VERSION window.o")

    # Clona la repo de sxhkd
    os.system("git clone https://github.com/baskerville/sxhkd.git")
    os.system("mv sxhkd/* .")
    os.system("sudo rm -r sxhkd/")
    os.system("cd ../sxhkd")
    os.system("make")

    # Acaba el build
    os.system("sudo make install")

    # Crea las carpetas de bspwm y sxhkd en ~/.config
    os.system("mkdir ~/.config/bspwm")
    os.system("mkdir ~/.config/sxhkd")
    os.system("cp examples/bspwmrc ~/.config/bspwm/")

    # Les da permisos de ejecucion a bspwmrc
    os.system("rm ~/.config/bspwm/bspwmrc")
    os.system("cp tools/bspwmrc ~/.config/bspwm/bspwmrc")
    os.system("chmod +x ~/.config/bspwm/bspwmrc")
    os.system("cp examples/sxhkdrc ~/.config/sxhkd/")

    # Elimina los archivos de sxhkd
    os.system("sudo rm -r contrib/ doc/ examples/ src/ grab.o helpers.o LICENSE Makefile parse.o README.md Sourcedeps sxhkd sxhkd.o types.o VERSION")
    os.system("cp tools/sxhkdrc ~/.config/sxhkd")
    print("\n[+] Bspwm instalado correctamente!")

def polybar():
    green()

    # Clona el repo de polybar
    os.system("git clone --recursive https://github.com/polybar/polybar")
    os.system("mv polybar/* .")
    os.system("sudo rm -r polybar/")
    os.system("cmake .")
    os.system("make -j$(nproc)")

    # Acaba el build
    os.system("sudo make install")

    # Elimina los archivos de polybar
    os.system("sudo rm -r bin/ cmake/ CMakeFiles/ common/ config/ contrib/ doc/ generated-sources/ include/ lib/ libs/ polybar/ src/ tests/ banner.png build.sh CHANGELOG.md CMajeCache.txt cmake_install.cmake CMakeLists.txt compile_commands.json CONTRIBUTING.md install_manifest LICENSE Makefile README.md SUPPORT.md version.txt")

    # Clona el repo de picom
    os.system("git clone https://github.com/ibhagwan/picom.git")
    os.system("mv picom/* .")
    os.system("sudo rm -r picom/")
    os.system("git submodule update --init --recursive")
    os.system("meson --buildtype=release . build")
    os.system("ninja -C build")

    # Hace el build de picom
    os.system("sudo ninja -C build install")

    # Elimina los archivos de picom
    os.system("sudo rm -r *.md *.conf *.desktop *.txt *.build *.spdx *.glsl COPYING Doxyfile CONTRIBUTORS bin/ build/ dbus-examples/ LICENSES/ man/ media/ meson/ src/ subprojects/ tests/")

    # Añade el wallpaper
    os.system("mkdir ~/.wallpapers")
    os.system("mv tools/wallpaper.jpg ~/.wallpapers")
    os.system("echo 'feh --bg-fill ~/.wallpapers/wallpaper.jpg' >> ~/.config/bspwm/bspwmrc")

    # Clona el tema de blue-sky
    os.system("git clone https://github.com/VaughnValle/blue-sky.git")
    os.system("mkdir ~/.config/polybar")

    # Copia el tema de blue-sky a la config de polybar
    os.system("cp -r blue-sky/polybar/* ~/.config/polybar")
    os.system("echo '~/.config/polybar/./launch.sh' >> ~/.config/bspwm/bspwmrc")
    os.system("sudo cp blue-sky/polybar/fonts/* /usr/share/fonts/truetype")
    os.system("fc-cache -v")

    # Copia la config de picom
    os.system("mkdir ~/.config/picom")
    os.system("cp tools/picom.conf ~/.config/picom")
    os.system("echo 'bspc config focus_follows_pointer true' >> ~/.config/bspwm/bspwmrc")
    os.system("echo 'picom --experimental-backends &' >> ~/.config/bspwm/bspwmrc")
    os.system("echo 'bspc config border_width 0' >> ~/.config/bspwm/bspwmrc")
    os.system("mkdir ~/.config/bin")

    # Mete el ethernet_status.sh, hackthebox_status.sh, target_to_hack.sh y target en ~/.config/bin
    os.system("wget https://raw.githubusercontent.com/yorkox0/exaple01/main/ethernet_status.sh")
    os.system("chmod +x ethernet_status.sh 2>/dev/null")
    os.system("mv ethernet_status.sh ~/.config/bin")
    os.system("wget https://raw.githubusercontent.com/yorkox0/exaple01/main/hackthebox.sh")
    os.system("chmod +x hackthebox.sh")
    os.system("mv hackthebox.sh ~/.config/bin")
    os.system("cp tools/target_to_hack.sh .")
    os.system("chmod +x target_to_hack.sh")
    os.system("mv target_to_hack.sh ~/.config/bin")
    os.system("echo '' > ~/.config/bin/target")

    # Copia la config de polybar personalizada
    os.system("cp tools/launch.sh ~/.config/polybar")
    os.system("cp tools/current.ini ~/.config/polybar")

    # Copia la config de rofi personalizada
    os.system("mkdir ~/.config/rofi")
    os.system("mkdir ~/.config/rofi/themes")
    os.system("cp blue-sky/nord.rasi ~/.config/rofi/themes")

    # Mueve los comandos settarget y cleartarget a /bin
    os.system("sudo cp tools/settarget /bin")
    os.system("sudo cp tools/cleartarget /bin")
    os.system("sudo chmod +x /bin/settarget")
    os.system("sudo chmod +x /bin/cleartarget")


    # Añadiendo scripts personaliados de s4vitar. extractPorts, whichSystem...
    os.system("sudo cp tools/wichSystem.py /bin")
    os.system("echo '' >> ~/.bashrc")
    os.system("cat tools/mkt.txt >> ~/.zshrc")
    os.system("echo '' >> ~/.zshrc")
    os.system("cat tools/extractPorts.txt >> ~/.zshrc")
    os.system("echo '' >> ~/.bashrc")
    os.system("cat tools/mkt.txt >> ~/.bashrc")
    os.system("echo '' >> ~/.bashrc")
    os.system("cat tools/extractPorts.txt >> ~/.bashrc")
    os.system("chmod +x tools/wichSystem.py")
    os.system("sudo cp tools/wichSystem.py /bin")
    
    # Instalando Hack Nerd Fonts
    os.system("cp tools/Hack.zip .")
    os.system("unzip Hack.zip")
    os.system("sudo mv *.ttf /usr/share/fonts")
    os.system("rm *.zip")

    print("\n[+] POLYBAR INSTALADO!!!")


def p10k():
    green()

    # Clona la repo de powerlvl10k
    os.system("git clone --depth=1 https://github.com/romkatv/powerlevel10k.git ~/powerlevel10k")
    os.system("echo 'source ~/powerlevel10k/powerlevel10k.zsh-theme' >>~/.zshrc")

    # Spawnear menu de configuracion de powerlvl10k
    os.system("zsh")

    #Actualizar la informacion de powerlvl10k
    os.system("rm ~/.p10k.zsh")
    os.system("cp tools/p10k.zsh ~/.p10k.zsh")
    os.system("cp tools/sudo/p10k.zsh /root/.p10k.zsh")

    #Asignamos la zsh a tu usuario principal y root
    os.system(f"usermod --shell /usr/bin/zsh {usuario}")
    os.system("usermod --shell /usr/bin/zsh root")

    print("\n[+] P10K INSTALADO!!!")


if __name__ == '__main__':
    menu()
