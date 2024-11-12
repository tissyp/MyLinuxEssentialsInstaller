from PySide6.QtWidgets import QApplication, QWidget, QLabel, QVBoxLayout
from PySide6.QtGui import QPixmap
from PySide6.QtCore import Qt

import sys

class MainWindow(QWidget):
    def __init__(self):
        super().__init__()

        # Imposta il titolo e le dimensioni della finestra
        self.setWindowTitle("My Linux Essentials Installer")
        self.setGeometry(100, 100, 300, 300)

        # Creazione del layout principale
        layout = QVBoxLayout()

        # Aggiunta dell'immagine
        image_label = QLabel(self)
        pixmap = QPixmap("img/tux.png")  # Sostituisci con il percorso della tua immagine
        if not pixmap.isNull():  # Verifica se l'immagine è stata caricata correttamente
            image_label.setPixmap(pixmap)
            image_label.setScaledContents(True)  # Adatta l'immagine alla label
            image_label.setFixedSize(150, 150)  # Dimensioni fisse per l'immagine
        else:
            image_label.setText("Immagine non trovata")  # Messaggio alternativo se l'immagine non si carica
        
        image_label.setAlignment(Qt.AlignCenter)

        # Aggiunta del testo
        text_label = QLabel("Tissy's Customization Script")
        text_label.setAlignment(Qt.AlignCenter)  # Centra il testo

        # Aggiungi i widget al layout
        layout.addWidget(image_label, alignment=Qt.AlignCenter)
        layout.addWidget(text_label)



        # Imposta il layout della finestra
        self.setLayout(layout)

if __name__ == "__main__":
    app = QApplication(sys.argv)

    # Creazione e visualizzazione della finestra principale
    main_window = MainWindow()
    main_window.show()

    # Esecuzione dell'applicazione
    sys.exit(app.exec())
