import sys
sys.path.append('app/util')
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QVBoxLayout, QHBoxLayout, QPushButton, QFileDialog, QWidget, QSpacerItem, QSizePolicy, QMessageBox, QDialog
from PyQt5.QtGui import QPixmap, QImage, QIcon
from PyQt5.QtCore import Qt
from PIL import Image, ImageOps
from split_rgb import split_rgb_with_dialog, RGBDialog
from binary import convert_to_binary
from mean import apply_mean_filter
from median import apply_median_filter

class ImageEditor(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle('Processamento de Imagens')
        self.setGeometry(100, 100, 600, 500)
        
        # ícone da janela
        self.setWindowIcon(QIcon('app/util/icon.png'))  
        
        # tema escuro
        self.setStyleSheet("""
            QMainWindow {
                background-color: #2E2E2E;
            }
            QLabel {
                color: #FFFFFF;
                background-color: #000000;
                border: 1px solid #4A4A4A;
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

        self.image_label = QLabel(self)
        self.image_label.setAlignment(Qt.AlignCenter)
        self.image_label.setStyleSheet("background-color: #2E2E2E;")  # Ajusta o fundo do QLabel

        self.load_button = QPushButton('Abrir imagem', self)
        self.load_button.clicked.connect(self.load_image)
        self.load_button.setFixedSize(100, 25)  

        self.save_button = QPushButton('Salvar imagem', self)
        self.save_button.clicked.connect(self.save_image)
        self.save_button.setFixedSize(100, 25) 
        
        self.revert_button = QPushButton('Reverter', self)
        self.revert_button.clicked.connect(self.revert_image)
        self.revert_button.setFixedSize(100, 25)

        self.rgb_button = QPushButton('Separar RGB', self)
        self.rgb_button.clicked.connect(self.split_rgb_dialog)
        
        self.gray_button = QPushButton('Grayscale', self)
        self.gray_button.clicked.connect(self.apply_grayscale)
        
        self.binary_button = QPushButton('Binário', self)
        self.binary_button.clicked.connect(self.convert_to_binary)
        
        self.mean_button = QPushButton('Média', self)
        self.mean_button.clicked.connect(self.apply_mean)
        
        self.median_button = QPushButton('Mediana', self)
        self.median_button.clicked.connect(self.apply_median)
        
        self.flip90_button = QPushButton('Girar em 90º', self)
        self.flip90_button.clicked.connect(self.rotate_90_degrees)
        
        self.fliph_button = QPushButton('Inverter imagem horizontalmente', self)
        self.fliph_button.clicked.connect(self.flip_horizontal)
        
        self.flipv_button = QPushButton('Inverter imagem verticalmente', self)
        self.flipv_button.clicked.connect(self.flip_vertical)
        
        # Layout horizontal para os botões Flip Horizontal e Flip Vertical
        flip_button_layout = QHBoxLayout()
        flip_button_layout.addWidget(self.fliph_button)
        flip_button_layout.addWidget(self.flipv_button)
        
        # Layout horizontal para os botões Load e Save
        top_button_layout = QHBoxLayout()
        top_spacer_left = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)
        top_spacer_right = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)
        top_button_layout.addItem(top_spacer_left)
        top_button_layout.addWidget(self.load_button)
        top_button_layout.addWidget(self.save_button)
        top_button_layout.addWidget(self.revert_button)
        top_button_layout.addItem(top_spacer_right)
          
        layout = QVBoxLayout()
        layout.addLayout(top_button_layout)
        layout.addWidget(self.image_label)
        layout.addWidget(self.gray_button)
        layout.addWidget(self.rgb_button)
        layout.addWidget(self.binary_button)
        layout.addWidget(self.mean_button)
        layout.addWidget(self.median_button)
        layout.addWidget(self.flip90_button)
        layout.addLayout(flip_button_layout)

        container = QWidget()
        container.setLayout(layout)
        self.setCentralWidget(container)

        self.image = None
        self.original_image = None

    def load_image(self):
        options = QFileDialog.Options()
        file_name, _ = QFileDialog.getOpenFileName(self, "Open Image File", "", "Images (*.png *.jpg *.jpeg *.bmp *.gif)", options=options)
        if file_name:
            try:
                self.image = Image.open(file_name).convert('RGBA')  # Converte para RGBA para garantir consistência
                self.original_image = self.image.copy()  # Salva uma cópia da imagem original
                self.display_image()
            except Exception as e:
                print(f"Erro ao abrir a imagem: {e}")
            
    def save_image(self):
        if self.image is not None:
            options = QFileDialog.Options()
            file_name, _ = QFileDialog.getSaveFileName(self, "Save Image File", "", "PNG Files (*.png);;JPEG Files (*.jpg *.jpeg);;BMP Files (*.bmp)", options=options)
            if file_name:
                try:
                    # Obtém a imagem atualmente exibida na tela
                    pixmap = self.image_label.pixmap()
                    if not pixmap.isNull():
                        # Converte o QPixmap para QImage
                        q_image = pixmap.toImage()

                        # Salva a imagem exibida na tela
                        q_image.save(file_name)
                except Exception as e:
                    print(f"Erro ao salvar a imagem: {e}")

    def display_image(self, img=None):
        if img is None:
            img = self.image

        if img is not None:
            label_width = self.image_label.width()
            label_height = self.image_label.height()
            
            img.thumbnail((label_width, label_height), Image.LANCZOS)

            q_image = self.convert_to_qimage(img)
            self.image_label.setPixmap(QPixmap.fromImage(q_image))
            self.image_label.setAlignment(Qt.AlignCenter)
            
    def revert_image(self):
        if self.original_image is not None:
            self.image = self.original_image.copy()  # Restaura a imagem original
            self.display_image()
            
    def rotate_90_degrees(self):
        if self.image is not None:
            self.image = self.image.transpose(Image.ROTATE_90)
            self.display_image()
            
    def flip_horizontal(self):
        if self.image is not None:
            self.image = self.image.transpose(Image.FLIP_LEFT_RIGHT)
            self.display_image()

    def flip_vertical(self):
        if self.image is not None:
            self.image = self.image.transpose(Image.FLIP_TOP_BOTTOM)
            self.display_image()
            
    def apply_grayscale(self):
        if self.image is not None:
            gray_image = ImageOps.grayscale(self.image)
            self.image = gray_image.convert("RGB")
            self.display_image()
            
    def split_rgb_dialog(self):
        dialog = RGBDialog(self)
        if dialog.exec_() == QDialog.Accepted:
            channel = dialog.channel
            if self.image is not None:
                red, green, blue = split_rgb_with_dialog(self.image, channel)
                if channel == 'red':
                    self.image = red
                elif channel == 'green':
                    self.image = green
                elif channel == 'blue':
                    self.image = blue
                self.display_image()
                
    def convert_to_binary(self):
        if self.image is not None:
            bin_image = convert_to_binary(self.image)
            self.display_image(bin_image)
            
    def apply_mean(self):
        if self.image is not None:
            mean_filtered_image = apply_mean_filter(self.image)
            self.display_image(mean_filtered_image)
            
    def apply_median(self):
        if self.image is not None:
            median_filtered_image = apply_median_filter(self.image)
            self.display_image(median_filtered_image)
        
    def convert_to_qimage(self, pil_image):
        try:
            if pil_image.mode != "RGBA":
                pil_image = pil_image.convert("RGBA")

            data = pil_image.tobytes("raw", "RGBA")
            q_image = QImage(data, pil_image.size[0], pil_image.size[1], QImage.Format_RGBA8888)
            return q_image
        except Exception as e:
            print(f"Erro ao converter imagem: {e}")
            return QImage()

    def resizeEvent(self, event):
        self.display_image()
        super().resizeEvent(event)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    editor = ImageEditor()
    editor.show()
    sys.exit(app.exec_())
