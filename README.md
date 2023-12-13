# CodeTransmit
## 简介
基于python开发的编码转换工具，图形化界面基于pyside2（也就是qt5）开发。 

    支持批量转换任意格式的文件编码；
  
    可将文件编码转为UTF-8 BOM 、UTF-8、GB2312中的任意一种格式；
  
  src文件夹下是源码  
  
## 编译
使用 [charamel](https://github.com/chomechome/charamel) 做解码器，编译时需要包含其资源
pyinstaller --onefile --windowed --collect-data "charamel" mainwindow.py

打包好可直接在windows下运行的exe程序在release里

## 已知的问题：

charamel也会有编码识别出错的问题，需要自行检查

转换结果里的显示
   
![微信截图_20231213085704](https://github.com/niunuinui/CodeTransmit/assets/5020840/37893979-817b-4098-a8f5-4cd6f79ddfc3)

实际编码转换的效果
   
![微信截图_20231213085640](https://github.com/niunuinui/CodeTransmit/assets/5020840/c7b5202d-554c-4eb4-8347-faafd603756c)
