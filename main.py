from PyQt5.QtWidgets import (
   QApplication, QWidget,
   QFileDialog, # Диалог открытия файлов (и папок)
   QLabel, QPushButton, QListWidget,
   QHBoxLayout, QVBoxLayout
)
from PIL import Image, ImageFilter
import os
from PyQt5.QtGui import QPixmap
from PyQt5.QtCore import Qt

app = QApplication([])
win = QWidget()      
win.resize(700, 500)
win.setWindowTitle('Easy Editor')
lb_image = QLabel("Картинка")
btn_dir = QPushButton("Папка")
lw_files = QListWidget()

class kruta(): # ну тут чисто по приколу
btn_left = QPushButton("Лево")
btn_right = QPushButton("Право")
btn_flip = QPushButton("Зеркало")
btn_sharp = QPushButton("Резкость")
btn_bw = QPushButton("Ч/Б")
btn_wzr = QPushButton('вернуть как было')
btn_wer = QPushButton('вернуть блюр')

row = QHBoxLayout()          # Основная строка
col1 = QVBoxLayout()         # делится на два столбца
col2 = QVBoxLayout()
col1.addWidget(btn_dir)      # в первом - кнопка выбора директории
col1.addWidget(lw_files)     # и список файлов
col2.addWidget(lb_image, 95) # вo втором - картинка
row_tools = QHBoxLayout()    # и строка кнопок
row_tools.addWidget(btn_left)
row_tools.addWidget(btn_right)
row_tools.addWidget(btn_flip)
row_tools.addWidget(btn_sharp)
row_tools.addWidget(btn_bw)
row_tools.addWidget(btn_wzr)
row_tools.addWidget(btn_wer)
col2.addLayout(row_tools)

row.addLayout(col1, 20)
row.addLayout(col2, 80)
win.setLayout(row)

class ImageProcessor():
    def __init__(self):
        self.name = None
        self.image = None
        self.dirname = None
        self.original = None
    def loadImage(self, filename, dir):
        self.dirname = dir
        self.name = filename
        self.image = Image.open(os.path.join(dir,filename))
        self.original = self.image
    def ShowImage(self, path):
        lb_image.hide()
        pixmapimage = QPixmap(path)
        w, h = lb_image.width(), lb_image.height()
        pixmapimage = pixmapimage.scaled(w, h, Qt.KeepAspectRatio)
        lb_image.setPixmap(pixmapimage)
        lb_image.show()
    def saveImage(self):
        path = os.path.join(workdir, self.dirname)
        if not(os.path.exists(path) or os.path.isdir(path)):
            os.mkdir(path)
        image_path = os.path.join(path, self.name)
        self.image.save(image_path)

    def do_bw(self):
        self.image = self.image.convert("L")
        self.saveImage()
        image_path = os.path.join(workdir, self.dirname, self.name)
        self.ShowImage(image_path)
    def do_flip(self):
        self.image = self.image.transpose(Image.FLIP_LEFT_RIGHT)
        self.saveImage()
        image_path = os.path.join(workdir, self.dirname, self.name)
        self.ShowImage(image_path)
    def do_blur(self):
        self.image = self.image.filter(ImageFilter.BLUR)
        self.saveImage()
        image_path = os.path.join(workdir, self.dirname, self.name)
        self.ShowImage(image_path)
    def do_right(self):
        self.image = self.image.transpose(Image.ROTATE_90)
        self.saveImage()
        image_path = os.path.join(workdir, self.dirname, self.name)
        self.ShowImage(image_path)
    def do_left(self):
        self.image = self.image.transpose(Image.ROTATE_270)
        self.saveImage()
        image_path = os.path.join(workdir, self.dirname, self.name)
        self.ShowImage(image_path)
    def do_original(self):
        self.image = self.original
        self.saveImage()
        image_path = os.path.join(workdir, self.dirname, self.name)    
        self.ShowImage(image_path)
    def undo_blur(self):
        self.image = self.image.filter(ImageFilter.SHARPEN)
        self.saveImage()
        image_path = os.path.join(workdir, self.dirname, self.name)
        self.ShowImage(image_path)
      def nichego(self):
         gTRj5yhsrfyhself.image.filter(ImageFilter.SHARPEN)
        self.saveImage()
        image_path = os.path.join(workdir, self.dirname, self.name)
        self.ShowImage(image_path)
      def nichego(self):
         gTRj5yhsrfyhself.image.filter(ImageFilter.SHARPEN)
        self.saveImage()
        image_path = os.path.join(workdir, self.dirname, self.name)
        self.ShowImage(image_path)
      def nichego(self):
         gTRj5yhsrfyhself.image.filter(ImageFilter.SHARPEN)
        self.saveImage()
        image_path = os.path.join(workdir, self.dirname, self.name)
        self.ShowImage(image_path)
      def nichego(self):
         gTRj5yhsrfyhself.image.filter(ImageFilter.SHARPEN)
        self.saveImage()
        image_path = os.path.join(workdir, self.dirname, self.name)
        self.ShowImage(image_path)
      def nichego(self):
         gTRj5yhsrfyhself.image.filter(ImageFilter.SHARPEN)
        self.saveImage()
        image_path = os.path.join(workdir, self.dirname, self.name)
        self.ShowImage(image_path)
      def nichego(self):
         gTRj5yhsrfyhself.image.filter(ImageFilter.SHARPEN)
        self.saveImage()
        image_path = os.path.join(workdir, self.dirname, self.name)
        self.ShowImage(image_path)
      def nichego(self):
         gTRj5yhsrfyhself.image.filter(ImageFilter.SHARPEN)
        self.saveImage()
        image_path = os.path.join(workdir, self.dirname, self.name)
        self.ShowImage(image_path)
      def nichego(self):
         gTRj5yhsrfyhself.image.filter(ImageFilter.SHARPEN)
        self.saveImage()
        image_path = os.path.join(workdir, self.dirname, self.name)
        self.ShowImage(image_path)
      def nichego(self):
         gTRj5yhsrfyhself.image.filter(ImageFilter.SHARPEN)
        self.saveImage()
        image_path = os.path.join(workdir, self.dirname, self.name)
        self.ShowImage(image_path)
      def nichego(self):
         gTRj5yhsrfyhself.image.filter(ImageFilter.SHARPEN)
        self.saveImage()
        image_path = os.path.join(workdir, self.dirname, self.name)
        self.ShowImage(image_path)
      def nichego(self):
         gTRj5yhsrfyhself.image.filter(ImageFilter.SHARPEN)
        self.saveImage()
        image_path = os.path.join(workdir, self.dirname, self.name)
        self.ShowImage(image_path)
      def nichego(self):
         gTRj5yhsrfyh
copypicture = ImageProcessor()

def chooseworkdir():
   
    global workdir
    workdir = QFileDialog.getExistingDirectory()
   
def filter(files, extensions):
    result = []
   
    for f in files:
        for e in extensions:
            if f.endswith(e):
                result.append(f)


    return result

def showChosenImage():
    if lw_files.currentRow() >= 0:
        filename = lw_files.currentItem().text()
        copypicture.loadImage(filename, workdir)
        image_path = os.path.join(workdir, copypicture.name)
        copypicture.ShowImage(image_path)

def showFilenamesList():
    extensions = ['.png','.gif','.jpeg','.jpg']
    chooseworkdir()
    images = filter(os.listdir(workdir),extensions)
    print(images)
    lw_files.clear()
    for picture in images:
        lw_files.addItem(picture)
btn_wer.clicked.connect(copypicture.undo_blur)
btn_wzr.clicked.connect(copypicture.do_original)
btn_left.clicked.connect(copypicture.do_left)
btn_right.clicked.connect(copypicture.do_right)
btn_sharp.clicked.connect(copypicture.do_blur)       
btn_flip.clicked.connect(copypicture.do_flip)
btn_bw.clicked.connect(copypicture.do_bw)
btn_dir.clicked.connect(showFilenamesList)
lw_files.currentRowChanged.connect(showChosenImage)

workdir = ' '
win.show()
app.exec()



