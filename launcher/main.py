# launcher/main.py
import sys
import subprocess
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QVBoxLayout

class Launcher(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Cura + Pronterface")
        self.init_ui()

    def init_ui(self):
        layout = QVBoxLayout()

        cura_btn = QPushButton("Launch Cura")
        cura_btn.clicked.connect(lambda: subprocess.Popen(["python3", "../cura_src/cura_app.py"]))

        pronterface_btn = QPushButton("Launch Pronterface")
        pronterface_btn.clicked.connect(lambda: subprocess.Popen(["python3", "../pronterface_src/pronterface.py"]))

        layout.addWidget(cura_btn)
        layout.addWidget(pronterface_btn)
        self.setLayout(layout)

app = QApplication(sys.argv)
window = Launcher()
window.show()
sys.exit(app.exec_())
