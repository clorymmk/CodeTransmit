# CodeTransmit
基于python开发的编码转换工具，图形化界面基于pyside2（也就是qt5）开发。 

    支持批量转换任意格式的文件编码；
  
    可将文件编码转为UTF-8 BOM 、UTF-8、GB2312中的任意一种格式；
  
  src文件夹下是源码  

使用 [charamel](https://github.com/chomechome/charamel) 做解码器，编译时需要包含其资源
pyinstaller --onefile --windowed --collect-data "charamel" mainwindow.py

打包好可直接在windows下运行的exe程序在release里