from PySide6.QtWidgets import QApplication, QWidget, QLabel, QVBoxLayout, QRadioButton
from PySide6.QtGui import QPixmap
from PySide6.QtCore import Qt
import sys, subprocess

class HoverLabel(QLabel):
    def __init__(self, image_path_normal, image_path_hover, parent=None):
        super().__init__(parent)

        
        self.image_normal = QPixmap("img/tux.png")
        self.image_hover = QPixmap("img/computer.png")

        
        self.setPixmap(self.image_normal)
        self.setScaledContents(True)  
        self.setFixedSize(150, 150)  

    def enterEvent(self, event):
        
        if not self.image_hover.isNull():
            self.setPixmap(self.image_hover)

    def leaveEvent(self, event):
        
        if not self.image_normal.isNull():
            self.setPixmap(self.image_normal)


class MainWindow(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("My Linux Essentials Installer")
        self.setGeometry(100, 100, 300, 300)

        layout = QVBoxLayout()

       
        self.hover_label = HoverLabel("img/tux.png", "img/computer.png")
        self.hover_label.setAlignment(Qt.AlignCenter)

        title_label = QLabel("Tissy's Customization Script")
        title_label.setAlignment(Qt.AlignCenter)

        choose_label = QLabel("Scegli un'opzione:")
        
       
        self.rb_choose0 = QRadioButton('Aggiorna Repo e Sistema', self)
        self.rb_choose0.toggled.connect(self.pass_commands)

        self.rb_choose1 = QRadioButton('Installa i pacchetti dai repo Debian', self)
        self.rb_choose1.toggled.connect(self.pass_commands)

        self.rb_choose2 = QRadioButton('Installa i pacchetti non inclusi nei repo Debian', self)
        self.rb_choose2.toggled.connect(self.pass_commands)

        
        layout.addWidget(self.hover_label, alignment=Qt.AlignCenter)
        layout.addWidget(title_label)
        layout.addWidget(choose_label)

        layout.addWidget(self.rb_choose0)
        layout.addWidget(self.rb_choose1)
        layout.addWidget(self.rb_choose2)

        self.setLayout(layout)

    def pass_commands(self):
        if self.rb_choose0.isChecked():
            self.commands("sudo apt update")
        elif self.rb_choose1.isChecked():
            flatpak = "flatpak remote-add --if-not-exists flathub https://dl.flathub.org/repo/flathub.flatpakrepo"
            self.commands(f"sudo apt install chromium neofetch inxi gimp gparted simple-scan git gpaste-2 pluma virt-manager ghostwriter qbittorrent vlc vokoscreen-ng bleachbit zulucrypt-gui geany flatpak plasma-discover-backend-flatpak bash-completion && {flatpak}")
        elif self.rb_choose2.isChecked():
            tw="wget https://download.teamviewer.com/download/linux/teamviewer_amd64.deb && sudo dpkg -i teamviewer_amd64.deb"
            tg="flatpak install flathub org.telegram.desktop"
            disc="wget https://dl.discordapp.net/apps/linux/0.0.61/discord-0.0.61.deb && sudo dpkg -i discord-0.0.61.deb"
            opera="flatpak install flathub com.opera.Opera"
            spoty="flatpak install flathub com.spotify.Client"
            self.commands(f"{tw} && {tg} && {disc} && {opera} && {spoty}")

    def commands(self, command):
        if not command or not self.sender().isChecked():
            return

        terminal = f'xterm -title "Installing Packages..." -e "{command}; echo Premere Invio per chiudere; read"'
        subprocess.Popen(terminal, shell=True)


if __name__ == "__main__":
    app = QApplication(sys.argv)

    main_window = MainWindow()
    main_window.show()

    sys.exit(app.exec())