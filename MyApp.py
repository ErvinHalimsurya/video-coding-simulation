from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtMultimedia import QMediaPlayer, QMediaContent
from PyQt5.QtCore import QObject, pyqtSlot, QUrl
from PyQt5.QtWidgets import QStyle,QDialog,QApplication
import os
import cv2
import sys
import threading
import numpy as np
from utility.mainwindow import Ui_MainWindow
from utility.model import Model
from utility.encodelib import encode
from utility.decodelib import decode, getDimension


class MainWindow(QtWidgets.QMainWindow,Ui_MainWindow):
    def __init__(self,parent=None):
        super(MainWindow, self).__init__(parent)
        self.setupUi(self)
        self.model = Model()

        self.huffButton.clicked.connect(self.displayHuff)
        
        self.browseButton1.clicked.connect(self.browseSourceSlot)
        self.browseButton2.clicked.connect(self.browseDestSlot)
        # self.sourceInput.returnPressed.connect(self.returnSourceSlot)
        # self.DestInput.returnPressed.connect(self.returnDestSlot)
        self.outputName.returnPressed.connect(self.returnNameSlot)
        self.playButton1.clicked.connect(self.playVidSource)
        self.playButton2.clicked.connect(self.playVidRes)
        # self.decodedPathInput.returnPressed.connect(self.returnDecFolderSlot)
        self.browseButton3.clicked.connect(self.browseDecFolderSlot)
        self.decodedName.returnPressed.connect(self.returnDecNameSlot)
        
        self.dispButton.clicked.connect(self.displayFile)
        self.customButton.clicked.connect(self.dialogbox)


        self.mediaPlayer1 =  QMediaPlayer(None, QMediaPlayer.VideoSurface)
        self.mediaPlayer1.stateChanged.connect(self.mediaStateChanged1)
        self.mediaPlayer2 =  QMediaPlayer(None, QMediaPlayer.VideoSurface)
        self.mediaPlayer2.stateChanged.connect(self.mediaStateChanged2)
        self.mediaPlayer1.setVideoOutput(self.videoScreen1)
        self.mediaPlayer2.setVideoOutput(self.videoScreen2)

        self.encodeButton.clicked.connect(lambda: self.launchThread(1))
        self.decodeButton.clicked.connect(lambda: self.launchThread(2))

        self.customButton.clicked.connect(self.dialogbox) 
        self.codeLength = []

    @QtCore.pyqtSlot()
    def launchThread(self,option):
        if option ==1:
            if self.decodeButton.isEnabled():
                thread = threading.Thread(target=self.Encode)
                thread.start()
            else:
                self.debugPrint("Please wait until the other process is finished")
        else:
            if self.encodeButton.isEnabled():
                thread = threading.Thread(target=self.Decode)
                thread.start()
            else:
                self.debugPrint("Please wait until the other process is finished")

    @QtCore.pyqtSlot()
    def Encode(self):
        fileName = self.model.getFileName()
        outputFolder = self.model.getDestFolder()
        name = self.outputName.text()
        outputPath = self.model.getDestPath()
        if self.model.isValid(fileName):
            if outputFolder==None:
                self.debugPrint("Determine the output folder first")
            elif name=="":
                self.debugPrint("Determine the output name first")
            else:
                try:
                    self.encodeButton.setEnabled(False)
                    
                    # Kode encoding
                    cap = cv2.VideoCapture(fileName) #Read the video File
                    frames,frame_num,fps = self.readVideo(cap)
                    self.debugPrint("Encoding..........")

                    counter=1
                    tablePath = self.model.getHuffPath()
                    encodePath = self.model.getDestPath()
                    f = open(encodePath, 'wb')
                    f.close()

                    for frame in frames :
                        self.codeLength.append(encode(frame,frame_num,fps,tablePath,encodePath))
                        self.debugPrint('Progress = '+str(counter)+' out of '+str(frame_num))
                        counter=counter+1
                    self.encodeButton.setEnabled(True)
                    self.debugPrint("Done Encoding")
                except:
                    self.debugPrint("An error happened")
                    self.encodeButton.setEnabled(True)
        
        else:
            self.debugPrint("Source file invalid!")

    @QtCore.pyqtSlot()
    def Decode(self):
        if self.model.getDestPath() ==None or self.model.getHuffPath == None:
            self.debugPrint("Determine Source to be Decoded")
            return
        sourceFile = self.model.getDestPath()
        tablePath = self.model.getHuffPath()
        outputFolder = self.model.getDecodedFolder()
        name = self.decodedName.text()
        outputPath = self.model.getDecodedPath()
        
        if self.model.isValid(sourceFile) or self.model.isValid(tablePath):
            if outputFolder==None:
                self.debugPrint("Determine the output video folder first")
            elif name=="":
                self.debugPrint("Determine the output video name first")
            else:
                try:
                    self.decodeButton.setEnabled(False)
                    counter=1
                    frames = []
                    width,height,frame_num,fps = getDimension(tablePath)
                    width = int(width)
                    height = int(height)
                    self.debugPrint("Width : %d" % (width))
                    self.debugPrint("Height : %d" % (height))
                    
                    self.debugPrint("Decoding..........")
                    i = 0
                    with open(sourceFile,'rb') as file, open(tablePath,'r') as table:
                        while(i<int(frame_num)):
                            frame=decode(file.read(self.codeLength[i]),table)                        
                            frames.append(frame)
                            self.debugPrint('Progress = '+str(counter)+' out of '+str(frame_num))
                            counter = counter+1
                            i +=1
                    
                    codec_id = "mp4v"
                    fourcc = cv2.VideoWriter_fourcc(*codec_id)
                    out = cv2.VideoWriter(outputPath, fourcc, int(fps), (width, height)) # bikin fungsi ambil row, cols
                    # video = np.array(frames)
                    # video = np.stack(video, axis=0) # dimensions (T, H, W, C)
                    video=frames
                    # np.split(video, frame_num, axis=0)

                    for frame in video: #Jumlah frame?
                        frame_bgr = cv2.cvtColor(frame, cv2.COLOR_YCR_CB2BGR)
                        #frame = frame[0, :, :]
                        out.write(frame_bgr)
                    
                    self.decodeButton.setEnabled(True)
                    self.debugPrint("Done Decoding")
                    size = os.path.getsize(outputPath)
                    size = round((size/1024),2)
                    self.decodedSize.setText('File Size: '+ str(size) + ' KB')
                    
                except:
                    self.debugPrint("An error happened")
                    self.decodeButton.setEnabled(True)
        else:
            self.debugPrint("Compressed file or table that is about to be decoded is invalid!")
    
        

    def debugPrint( self, msg ):
        '''Print the message in the text edit at the bottom of the
        horizontal splitter.
        '''
        self.textBrowser.append( msg )
    
    def mediaStateChanged1(self, state):
        if self.mediaPlayer1.state() == QMediaPlayer.PlayingState:
            self.playButton1.setIcon(
                    self.style().standardIcon(QStyle.SP_MediaPause))
        else:
            self.playButton1.setIcon(
                    self.style().standardIcon(QStyle.SP_MediaPlay))
    
    def mediaStateChanged2(self, state):
        if self.mediaPlayer2.state() == QMediaPlayer.PlayingState:
            self.playButton2.setIcon(
                    self.style().standardIcon(QStyle.SP_MediaPause))
        else:
            self.playButton2.setIcon(
                    self.style().standardIcon(QStyle.SP_MediaPlay))
    
    def readVideo(self,cap):
        frames = []
        while(cap.isOpened()):
            ret,frame = cap.read() #akan dibaca frame per frame, var frame akan menyimpan nilai pembacaanya 
            if not ret:
                frame_num = cap.get(cv2.CAP_PROP_FRAME_COUNT)
                fps = cap.get(cv2.CAP_PROP_FPS)
                width =int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
                height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
                self.debugPrint("Reading Video Done. Total Frame : %d" % (frame_num))
                self.debugPrint("Width : %d" % (width))
                self.debugPrint("Height : %d" % (height))
                break
            frame_ycbcr = cv2.cvtColor(frame, cv2.COLOR_BGR2YCR_CB)
            #frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
            frames.append(frame_ycbcr)
        return frames,frame_num,fps

    

    @QtCore.pyqtSlot()
    def playVidSource(self):
        if self.mediaPlayer1.state() == QMediaPlayer.PlayingState:
            self.mediaPlayer1.pause()
        else:
            self.mediaPlayer1.play()

    @QtCore.pyqtSlot()
    def playVidRes(self):
        filename = self.model.getDecodedPath()
        if (self.model.isValid(filename)):
            self.mediaPlayer2.setMedia(QMediaContent(QUrl.fromLocalFile(filename)))

            if self.mediaPlayer2.state() == QMediaPlayer.PlayingState:
                self.mediaPlayer2.pause()
            else:
                self.mediaPlayer2.play()
        else:
            self.debugPrint("Video not yet created")
    

    # @QtCore.pyqtSlot()
    # def returnSourceSlot(self):
    #     pass

    # @QtCore.pyqtSlot()
    # def returnDestSlot(self):
    #     pass

    # @QtCore.pyqtSlot()
    # def returnDecFolderSlot(self):
    #     pass


    @QtCore.pyqtSlot()
    def displayFile(self):
        filename = self.model.getDestPath()
        if (self.model.isValid(filename)):
            self.textBrowser_2.setText(str(self.model.getDestContents()))
        else:
            self.debugPrint("File has not been made yet!")
    
    @QtCore.pyqtSlot()
    def displayHuff(self):
        filename = self.model.getHuffPath()
        if (self.model.isValid(filename)):
            with open(filename) as fin:
                fin.seek(0)
                contents = fin.read(2000-0)
            self.textBrowser_2.setText(contents)
        else:
            self.debugPrint("File has not been made yet!")

    @QtCore.pyqtSlot()
    def browseSourceSlot(self):
        options = QtWidgets.QFileDialog.Options()
        fileName, _ = QtWidgets.QFileDialog.getOpenFileName(
                        None,
                        "QFileDialog.getOpenFileName()",
                        "",
                        "Video Files (*.mp4 *.flv *.ts *.mts *.avi);;All Files (*)",
                        options=options)
        if fileName:
            self.debugPrint( "setting source file name: " + fileName )
            self.model.setFileName( fileName )
            self.mediaPlayer1.setMedia(QMediaContent(QUrl.fromLocalFile(fileName)))
            self.playButton1.setEnabled(True)
            self.sourceInput.setText(fileName)
            size = os.path.getsize(self.model.getFileName())
            size = round((size/1024),2)
            self.SourceSize.setText('File Size: '+ str(size) + ' KB')
            
        
    # Buat nyari folder yang mau di bikinin hasil encodednya. Penamaan variabel agak ngaco
    @QtCore.pyqtSlot()
    def browseDestSlot(self):
        options = QtWidgets.QFileDialog.Options()
        foldName = QtWidgets.QFileDialog.getExistingDirectory(self, "Select Directory")
        if foldName:
            self.debugPrint( "setting Encoding Folder : " + foldName )
            self.model.setDestFolder( foldName ) #Bikin folder + outputname
            self.DestInput.setText( self.model.getDestFolder())
            # self.sourceSize.setText()

    # Return nama output encoded. Penamaan variabel agak ngaco biarin lah ahahahaha
    @QtCore.pyqtSlot()
    def returnNameSlot(self):
        name =  self.outputName.text()
        self.model.setDestPath(name)
        fileName = self.model.getDestPath()
        self.outputName.setText( fileName )
        self.dispButton.setEnabled(True)
        self.debugPrint("Entered Encoded File Name !")
        
    
    # Pilih folder video decoded mau dibikin dimana
    @QtCore.pyqtSlot()
    def browseDecFolderSlot(self):
        options = QtWidgets.QFileDialog.Options()
        foldName = QtWidgets.QFileDialog.getExistingDirectory(self, "Select Directory")
        if foldName:
            self.debugPrint( "setting Destination Folder : " + foldName )
            self.model.setDecodedFolder( foldName ) #Bikin folder + outputname
            self.decodedPathInput.setText( self.model.getDecodedFolder())
            
    
    @QtCore.pyqtSlot()
    def returnDecNameSlot(self):
        self.debugPrint("Entered Output Video File Name !")
        name =  self.decodedName.text()
        self.model.setDecodedPath(name)
        fileName = self.model.getDecodedPath()
        self.playButton2.setEnabled(True)
        self.decodedName.setText(fileName)
        if self.model.isValid(fileName):
            size = os.path.getsize(fileName)
            size = round((size/1024),2)
            self.decodedSize.setText('File Size: '+ str(size) + ' KB')
        else:
            self.decodedSize.setText('File Size: Not yet created')

    def dialogbox(self):
        self.myDialog = MyDialog()
        self.myDialog.show()


class MyDialog(QDialog):
    def __init__(self):
        super().__init__()
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
        self.ui.dialogButton.clicked.connect(self.returnTable)
 
    def returnTable(self):
        pass

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(780, 780)
    
        self.dialogButton = QtWidgets.QPushButton(Dialog)
        self.dialogButton.setGeometry(QtCore.QRect(700,700,40,30))
        self.dialogButton.setObjectName("OkButton")
        self.table = QtWidgets.QTableWidget(Dialog)
        self.table.setGeometry(QtCore.QRect(70,70,400,300))

        
        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle("Quantization Table")
        self.dialogButton.setText("OK")
        

def main():
    app = QtWidgets.QApplication(sys.argv)
    w = MainWindow()
    w.show()
    sys.exit(app.exec_())

main()