'''
@Author: your name
@Date: 2020-03-13 09:44:52
@LastEditTime: 2020-03-16 15:21:40
@LastEditors: Please set LastEditors
@Description: In User Settings Edit
@FilePath: \codeTransmit\mainwindow.py
'''
# This Python file uses the following encoding: utf-8
import sys, os
from PySide2.QtWidgets import QApplication, QMainWindow, QFileDialog, QCheckBox, QMessageBox, QTableWidgetItem
from PySide2.QtCore import Qt
from PySide2.QtCore import Signal, QObject,Slot #跨线程消息机制
from uiWindow import Ui_MainWindow

import codecs 
import chardet 
import threading

from charamel import Detector
#转换后的编码类型
UTF8_BOM = 0
UTF8 = 1
GB2312 = 2

FILE = 0
FOLDER = 1

class Communicate(QObject):
    speak_word = Signal(str)
    add_row = Signal(str,str,str,str)
class MainWindow(QMainWindow):

    @Slot(str)
    def say_something(self,stuff):
        # print(stuff)
        self.ui.textBrowser.append(stuff)
    @Slot(str,str,str)
    def slotTableWidgetAddRow(self,filename,source_encoding,decoding,result):
        # print(stuff)
        rouCount = self.ui.tableWidget.rowCount()
        self.ui.tableWidget.insertRow(rouCount)
        self.ui.tableWidget.setItem(rouCount, 0, QTableWidgetItem(filename))
        self.ui.tableWidget.setItem(rouCount, 1, QTableWidgetItem(source_encoding))
        self.ui.tableWidget.setItem(rouCount, 2, QTableWidgetItem(decoding))
        self.ui.tableWidget.setItem(rouCount, 3, QTableWidgetItem(result))
        self.ui.tableWidget.item(rouCount, 0).setTextAlignment(Qt.AlignCenter)
        self.ui.tableWidget.item(rouCount, 1).setTextAlignment(Qt.AlignCenter)
        self.ui.tableWidget.item(rouCount, 2).setTextAlignment(Qt.AlignCenter)
        self.ui.tableWidget.item(rouCount, 3).setTextAlignment(Qt.AlignCenter)
    signal = Communicate()
    def __init__(self):
        super(MainWindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.initForm()
        self.signal = Communicate()
        self.connectSlots()

        self.__path = None                                  #处理的文件/文件夹路径
        self.__fileSuffix = ['.c', '.h', '.cpp', '.hpp']    #内置可勾选的文件类型
        self.__customFileSuffix = []                        #自定义的文件类型

        self.usenewmethod = True
        if self.usenewmethod == False:
            self.__encodeType = 'UTF-8-SIG'                     #默认的编码类型
            self.__encodeTypeArr = ['UTF-8-SIG', 'utf-8', 'GB2312']
        else:
            self.__encodeType = 'utf_8_sig'                     #默认的编码类型
            self.__encodeTypeArr = ['utf_8_sig', 'utf_8', 'gb2312']
        
        self.__fileOrFolder = FOLDER                        #默认处理文件夹
        self.__mWorker = None                               #私有线程变量
        self.detector = Detector()
        # self.detector = Detector(min_confidence=0.5)        

    def initForm(self):
        self.ui.tableWidget.setColumnCount(4)
        self.ui.tableWidget.setHorizontalHeaderLabels(["文件名","识别类型","解码方法","结果"])
        # self.ui.tableWidget.horizontalHeader().setStretchLastSection(True)
        self.ui.tableWidget.setColumnWidth(0, 165)
        self.ui.tableWidget.setColumnWidth(1, 70)
        self.ui.tableWidget.setColumnWidth(2, 70)
        self.ui.tableWidget.setColumnWidth(3, 70)


    def setFilePath(self, path):
        self.__path = path

    def getFileSuffix(self):
        return self.__fileSuffix

    def addFileSuffix(self, item):
        self.__fileSuffix.append(item)

    def removeFileSuffix(self, item):
        self.__fileSuffix.remove(item)
    
    def clearFileSuffix(self):
        self.__fileSuffix.clear()

    def setEncodeType(self, type):
        self.__encodeType = type

    def connectSlots(self):
        self.ui.btnChooseFolder.clicked.connect(self.onOpenFolderClicked)
        self.ui.btnChooseFile.clicked.connect(self.onOpenFileClicked)
        self.ui.btnClear.clicked.connect(self.onBtnClearClicked)
        self.ui.comboBox.currentIndexChanged.connect(self.onCbEncodeIndexChanged)
        self.ui.btnCustomCheck.clicked.connect(self.onCustomEncodeCheck)
        fileTypeArr = self.ui.groupBox.findChildren(QCheckBox)
        for index, item in enumerate(fileTypeArr):
            item.stateChanged.connect(self.onFileTypeChanged)
        self.ui.btnTransmit.clicked.connect(self.onTransmitClicked)
        self.signal.speak_word.connect(self.say_something)
        self.signal.add_row.connect(self.slotTableWidgetAddRow)
        self.signal.speak_word.emit("started!")

    def onOpenFileClicked(self):
        fileName = QFileDialog.getOpenFileName(self, "", ".")
        if (fileName is None):
            self.signal.speak_word.emit("open file failed: fileName is None!")
            return

        self.setFilePath(fileName[0])
        self.__fileOrFolder = FILE
        self.ui.labelPath.setText(fileName[0])

    def onOpenFolderClicked(self):
        folderName = QFileDialog.getExistingDirectory(self, "", ".")
        if (folderName is None):
            self.signal.speak_word.emit("open folder failed:folderName is None!")
            return
        
        self.setFilePath(folderName)
        self.__fileOrFolder = FOLDER
        self.ui.labelPath.setText(folderName)

    def onBtnClearClicked(self):
        self.ui.textBrowser.clear()
        self.ui.tableWidget.clearContents()
        self.ui.tableWidget.setRowCount(0)

    def onCbEncodeIndexChanged(self, index):
        self.setEncodeType(self.__encodeTypeArr[index])
        self.signal.speak_word.emit("Set encodeType: %s" % self.__encodeTypeArr[index])
    
    def onCustomEncodeCheck(self):
        customStr = self.ui.leditCustomEncode.text()
        customArr = customStr.split(' ')

        for index, item in enumerate(customArr):
            if(len(item) < 2):
                QMessageBox.critical(self, "Error!", "自定义后缀无效:长度至少为2!")
                return
            if(item[0] != '.'):
                QMessageBox.critical(self, "Error!", "自定义后缀无效:必须以 '.' 打头!")
                return
            if(item.count('.',) > 1):
                QMessageBox.critical(self, "Error!", "自定义后缀无效:一种格式中不能出现多个 '.'!")
                return
            #移除后缀重复的元素
            if (item not in self.__fileSuffix) and (item not in self.__customFileSuffix):
                self.__customFileSuffix.append(item)
    
    def onFileTypeChanged(self, state):
        checkBox = QCheckBox.sender(self)
        itemText = checkBox.text()
        if(False == state):
            if itemText in self.__fileSuffix:
                self.removeFileSuffix(itemText)
        else:
            if itemText not in self.__fileSuffix:
                self.addFileSuffix(itemText)
            if itemText in self.__customFileSuffix:
                self.__customFileSuffix.remove(itemText)

    def enableWidgets(self, enabled):
        self.ui.groupBoxPath.setEnabled(enabled)
        self.ui.groupBoxEncode.setEnabled(enabled)
        self.ui.btnTransmit.setEnabled(enabled)
        self.ui.btnClear.setEnabled(enabled)

    def onTransmitClicked(self):
        if self.__path is None:
            QMessageBox.warning(self, "Warning!", "请先选择'文件'或'文件夹'路径!")
            return

        self.ui.tableWidget.clearContents()
        self.ui.tableWidget.setRowCount(0)

        if self.__fileOrFolder == FILE:
            self.convert(self.__path, self.__encodeType)
        elif self.__fileOrFolder == FOLDER:
            if 0 == len(self.__fileSuffix) and 0 == len(self.__customFileSuffix):
                QMessageBox.critical(self, "Error!", "请设置需要处理的文件后缀格式!")
                return
            self.enableWidgets(False)
            # self.explore(self.__path)
            self.__mWorker = threading.Thread(target=self.explore, args=(self.__path,))
            self.__mWorker.start()
        else:
            QMessageBox.critical(self, "Error!", "文件类型错误，无法转换!")
        QApplication.processEvents()

    def explore(self, dir):
        for root, dirs, files in os.walk(dir):
            for file in files:
                suffix = os.path.splitext(file)[1]
                # if suffix == '.h' or suffix == '.c' or suffix == '.cpp' or suffix == '.hpp' or suffix == '.bat': 
                #     path = os.path.join(root,file)
                #     self.convert(path)
                if self.__fileSuffix:
                    for item in self.__fileSuffix:
                        if(item == suffix):
                            path = os.path.join(root,file)
                            # print(path)
                            self.convert(path, self.__encodeType)
                if self.__customFileSuffix:
                    for item in self.__customFileSuffix:
                        if(item == suffix):
                            path = os.path.join(root,file)
                            self.convert(path, self.__encodeType)

        self.signal.speak_word.emit("explore over!")
        self.enableWidgets(True)

    def convert_true(self, content,filePath, source_encoding,decoding,out_enc):
        try: 
            self.signal.speak_word.emit("正在处理: %s" % filePath)
            content2 = content.decode(decoding).encode(out_enc)
            codecs.open(filePath,'wb').write(content2)
            self.signal.add_row.emit(filePath.split('\\')[-1],source_encoding,decoding,"成功")
            return True

        except Exception as err:
            self.signal.speak_word.emit("%s:%s"%(filePath, err))
            self.signal.add_row.emit(filePath.split('\\')[-1],source_encoding,decoding,"转换失败")
            return False
    def convert_chardet(self, filePath, out_enc): # chardet识别的编码容易出错，总是拿GB2312试一试
        try: 
            content = codecs.open(filePath,'rb').read()
            source_encoding = chardet.detect(content)['encoding']
            if source_encoding == out_enc:
                self.signal.speak_word.emit("此文件格式无需转换: %s" % filePath)
            elif source_encoding == "utf-8":
                self.convert_true(content,filePath,source_encoding,source_encoding,out_enc)
            elif source_encoding ==None:
                self.signal.speak_word.emit("此文件无法识别编码: %s" % filePath)
                self.signal.add_row.emit(filePath.split('\\')[-1],"无法识别","无法识别","无法识别")
                self.convert_true(content,filePath,source_encoding,"GB2312",out_enc) #无法识别的编码也用GB2312试一试
            else:
                if self.convert_true(content,filePath,source_encoding,"GB2312",out_enc)!=True :
                    self.convert_true(content,filePath,source_encoding,source_encoding,out_enc)


        except Exception as err: 
            self.signal.speak_word.emit("%s:%s"%(filePath, err))
            self.signal.add_row.emit(filePath.split('\\')[-1],source_encoding,out_enc,"转换失败")
    # charmel更准，更不容易编码识别出错，所以就不无脑先尝试GB2312了。
    # 在第一名可信度不高的时候，检查topk是否有gb2312
    # 但也有编码识别出错的问题。需要自己检查表格里的编码格式
    def convert_charamel(self, filePath, out_enc): 
        try: 
            content = codecs.open(filePath,'rb').read()                              
            source_encoding = None
            decode_encoding = None
            topk = 5            
            minTrustThreshold = 0.1
            source_encoding_probes = self.detector.probe(content, top=topk)
            if len(source_encoding_probes)==0:
                source_encoding = None
            else:
                source_encoding = source_encoding_probes[0][0]
                decode_encoding = source_encoding            
            if source_encoding_probes[0][1]<minTrustThreshold: #如果第一名的可信度不够高，则找一找topk有没有gb2312，有则设为gb2312
                for i in range(len(source_encoding_probes)):
                    if source_encoding_probes[i][0]=='gb2312':
                        decode_encoding='gb2312'
                        break

            if source_encoding == out_enc:
                self.signal.speak_word.emit("此文件格式无需转换: %s" % filePath)                
            elif source_encoding == None:
                self.signal.speak_word.emit("此文件无法识别编码: %s" % filePath)
                self.signal.add_row.emit(filePath.split('\\')[-1],"无法识别","无法识别","无法识别")                
            else:
                self.convert_true(content,filePath,source_encoding,decode_encoding,out_enc)

        except Exception as err: 
            self.signal.speak_word.emit("%s:%s"%(filePath, err))
            self.signal.add_row.emit(filePath.split('\\')[-1],source_encoding,decode_encoding,"转换失败")

    def convert(self, filePath, out_enc):        
        if self.usenewmethod == True:
            self.convert_charamel(filePath,out_enc)
        else:
            self.convert_chardet(filePath,out_enc)

if __name__ == "__main__":
    app = QApplication(sys.argv)

    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
