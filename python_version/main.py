from PySide6.QtWidgets import QApplication, QWidget, QLabel, QVBoxLayout, QRadioButton
from PySide6.QtGui import QPixmap
from PySide6.QtCore import Qt
import sys, subprocess

class MainWindow(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("My Linux Essentials Installer")
        self.setGeometry(100, 100, 300, 300)

        layout = QVBoxLayout()

        image_label = QLabel(self)
        pixmap = QPixmap("img/tux.png") 
        if not pixmap.isNull():
            image_label.setPixmap(pixmap)
            image_label.setScaledContents(True)
            image_label.setFixedSize(150, 150)
        else:
            image_label.setText("Immagine non trovata")
        
        image_label.setAlignment(Qt.AlignCenter)

        title_label = QLabel("Tissy's Customization Script")
        title_label.setAlignment(Qt.AlignCenter)

        choose_label = QLabel("Scegli un'opzione:")

        self.rb_choose0 = QRadioButton('Aggiorna Repo e Sistema', self)
        self.rb_choose0.toggled.connect(self.pass_commands)

        self.rb_choose1 = QRadioButton('Installa i pacchetti dai repo Debian', self)
        self.rb_choose1.toggled.connect(self.pass_commands)

        self.rb_choose2 = QRadioButton('Installa i pacchetti esterni', self)
        self.rb_choose2.toggled.connect(self.pass_commands)

        layout.addWidget(image_label, alignment=Qt.AlignCenter)
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
            self.commands("sudo apt install chromium neofetch inxi gimp gparted simple-scan git gpaste-2 pluma virt-manager ghostwriter qbittorrent vlc vokoscreen-ng bleachbit zulucrypt-gui geany flatpak plasma-discover-backend-flatpak bash-completion")
        elif self.rb_choose2.isChecked():
            self.commands("echo 'Comando non abilitato'")

    def commands(self, command):
        if not command or not self.sender().isChecked():
            return

        terminal = f'xterm -e "{command}; echo Premere Invio per chiudere; read"'
        subprocess.Popen(terminal, shell=True)


if __name__ == "__main__":
    app = QApplication(sys.argv)

    main_window = MainWindow()
    main_window.show()

    sys.exit(app.exec())
