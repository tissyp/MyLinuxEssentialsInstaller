from PySide6.QtWidgets import QApplication, QWidget, QLabel, QVBoxLayout, QRadioButton
from PySide6.QtGui import QPixmap
from PySide6.QtCore import Qt
import sys

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

        rb_choose0 = QRadioButton('Aggiorna Repo e Sistema', self)
        rb_choose0.toggled.connect(self.update)

        rb_choose1 = QRadioButton('Installa i pacchetti dai repo Debian', self)
        rb_choose1.toggled.connect(self.update)

        rb_choose2 = QRadioButton('Installa i pacchetti esterni')
        rb_choose2.toggled.connect(self.update)

        def update(self):
            rb = self.sender()
            if rb.isChecked():
                self.result_label.setText(f'You selected {rb.text()}')

        layout.addWidget(image_label, alignment=Qt.AlignCenter)
        layout.addWidget(title_label)
        layout.addWidget(choose_label)
        layout.addWidget(rb_choose0)
        layout.addWidget(rb_choose1)
        layout.addWidget(rb_choose2)


        self.setLayout(layout)

if __name__ == "__main__":
    app = QApplication(sys.argv)

    main_window = MainWindow()
    main_window.show()

    sys.exit(app.exec())
