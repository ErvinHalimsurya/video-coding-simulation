from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtMultimedia import QMediaPlayer, QMediaContent
from PyQt5.QtCore import QObject, pyqtSlot, QUrl
from utility.mainwindow import Ui_MainWindow
from PyQt5.QtWidgets import QStyle
import cv2
import sys
import threading
import numpy as np
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


        self.mediaPlayer1 =  QMediaPlayer(None, QMediaPlayer.VideoSurface)
        self.mediaPlayer1.stateChanged.connect(self.mediaStateChanged1)
        self.mediaPlayer2 =  QMediaPlayer(None, QMediaPlayer.VideoSurface)
        self.mediaPlayer2.stateChanged.connect(self.mediaStateChanged2)
        self.mediaPlayer1.setVideoOutput(self.videoScreen1)
        self.mediaPlayer2.setVideoOutput(self.videoScreen2)

        self.encodeButton.clicked.connect(lambda: self.launchThread(1))
        self.decodeButton.clicked.connect(lambda: self.launchThread(2))

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
                self.encodeButton.setEnabled(False)
                self.debugPrint("Encoding..........")
                # Kode encoding
                cap = cv2.VideoCapture(fileName) #Read the video File
                frames,frame_num = self.readVideo(cap)

                counter=1
                tablePath = self.model.getHuffPath()
                encodePath = self.model.getDestPath()
                f = open(encodePath, 'wb')
                f.close()

                for frame in frames :
                    encode(frame,frame_num,tablePath,encodePath)
                    self.debugPrint('Progress = '+str(counter)+' out of '+str(frame_num))
                    counter=counter+1
                self.encodeButton.setEnabled(True)
        else:
            self.debugPrint("Source file invalid!")

    @QtCore.pyqtSlot()
    def Decode(self):
        filename = self.model.getDestPath()
        outputFolder = self.model.getDecodedFolder()
        name = self.decodedName.text()
        outputPath = self.model.getDecodedPath()
        tablePath = self.model.getHuffPath()
        if self.model.isValid(filename) or self.model.isValid(tablePath):
            if outputFolder==None:
                self.debugPrint("Determine the output video folder first")
            elif name=="":
                self.debugPrint("Determine the output video name first")
            else:
                self.decodeButton.setEnabled(False)
                self.debugPrint("Decoding..........")
                #Lanjut kode encode gan
                counter=1
                frames = []
                idx=0
                height,width,frame_num = getDimension(filename,tablePath,idx)
                self.debugPrint(height+" "+width+" "+frame_num)
                idx=0
                for i in range (int(frame_num)):
                    frame,idx=decode(filename,tablePath,idx)
                    self.debugPrint(str(idx))
                    self.debugPrint(frame_num)
                    frames.append(frame)
                    self.debugPrint('Progress = '+str(counter)+' out of '+str(frame_num))
                    counter = counter+1
                
                codec_id = "mp4v"
                fourcc = cv2.VideoWriter_fourcc(*codec_id)
                out = cv2.VideoWriter(outputPath, fourcc, 20, (width, height)) # bikin fungsi ambil row, cols
                video = np.stack(frames, axis=0) # dimensions (T, H, W, C)
                for frame in np.split(video, frame_num, axis=0): #Jumlah frame?
                    frame = frame[0, :, :]
                    out.write(frame)
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
                self.debugPrint("Reading Video Done. Total Frame : %d" % (frame_num))
                break
            frame_ycbcr = cv2.cvtColor(frame, cv2.COLOR_BGR2YCR_CB)
            #frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
            frames.append(frame_ycbcr)
        return frames,frame_num

    

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
        
    # Buat nyari folder yang mau di bikinin hasil encodednya. Penamaan variabel agak ngaco
    @QtCore.pyqtSlot()
    def browseDestSlot(self):
        options = QtWidgets.QFileDialog.Options()
        foldName = QtWidgets.QFileDialog.getExistingDirectory(self, "Select Directory")
        if foldName:
            self.debugPrint( "setting Encoding Folder : " + foldName )
            self.model.setDestFolder( foldName ) #Bikin folder + outputname
            self.DestInput.setText( self.model.getDestFolder())

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
            #self.sourceInput.setText( self.model.getFileName())
    
    @QtCore.pyqtSlot()
    def returnDecNameSlot(self):
        self.debugPrint("Entered Output Video File Name !")
        name =  self.decodedName.text()
        self.model.setDecodedPath(name)
        fileName = self.model.getDecodedPath()
        self.playButton2.setEnabled(True)
        self.decodedName.setText( fileName )

def main():
    app = QtWidgets.QApplication(sys.argv)
    w = MainWindow()
    w.show()
    sys.exit(app.exec_())

main()