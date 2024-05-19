from PyQt5.QtWidgets import QDialog, QVBoxLayout, QPushButton
from PyQt5.QtCore import Qt
from PIL import Image


class RGBDialog(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        
        self.setWindowTitle('Selecionar Canal')
        self.setWindowFlags(Qt.Dialog | Qt.WindowCloseButtonHint)
        self.setStyleSheet("""
            QDialog {
                background-color: #2E2E2E;
            }
            QPushButton {
                background-color: #4A4A4A;
                color: #FFFFFF;
                border: none;
                padding: 5px;
            }
            QPushButton:hover {
                background-color: #555555;
            }
            QPushButton:pressed {
                background-color: #3A3A3A;
            }
        """)
        
        layout = QVBoxLayout()
        
        self.red_button = QPushButton('Canal Vermelho', self)
        self.red_button.clicked.connect(self.show_red_channel)
        layout.addWidget(self.red_button)
        
        self.green_button = QPushButton('Canal Verde', self)
        self.green_button.clicked.connect(self.show_green_channel)
        layout.addWidget(self.green_button)
        
        self.blue_button = QPushButton('Canal Azul', self)
        self.blue_button.clicked.connect(self.show_blue_channel)
        layout.addWidget(self.blue_button)
        
        self.setLayout(layout)
        
        self.setFixedSize(150, 100)
    
    def show_red_channel(self):
        self.accept_with_channel('red')
    
    def show_green_channel(self):
        self.accept_with_channel('green')
    
    def show_blue_channel(self):
        self.accept_with_channel('blue')
    
    def accept_with_channel(self, channel):
        self.channel = channel
        self.accept()

def convert_to_rgb(img):
    if img.mode != 'RGB':
        img = img.convert('RGB')
    return img

def split_rgb_with_dialog(img, channel):
    img = convert_to_rgb(img)
    
    width, height = img.size
    
    img_r = Image.new("RGB", (width, height))
    img_g = Image.new("RGB", (width, height))
    img_b = Image.new("RGB", (width, height))

    for x in range(width):
        for y in range(height):        
            r, g, b = img.getpixel((x, y))
            if channel == 'red':
                img_r.putpixel((x, y), (r, r, r))
            elif channel == 'green':
                img_g.putpixel((x, y), (g, g, g))
            elif channel == 'blue':
                img_b.putpixel((x, y), (b, b, b))

    return img_r, img_g, img_b