# win_r
提供常用文件夹的命令行快捷创建和window_r快捷启动

(windows10系统专用)

## 使用方法

将主路径设置为名为"FileCMD"的环境变量

并在path中添加

"%FileCMD%\bin";"%FileCMD%\links"

## lmkdir 

destination: 必选参数，为要创建的文件夹类型

-m: 为所创建的文件夹增加shortcut，便于用win+r呼出

-p: 指定要创建文件夹的父目录，默认父目录可以在config.yml里设置

-s:选择要创建文件夹的父目录

## llink

-s:显示当前目录的所有shorcut

-m:为当前目录添加shortcut

-rm:删除当前目录的shortcut

## lcp

destination:必选参数,将shortcut对应的绝对路径复制到剪贴板中

# todo

用Electron重构，并添加托盘功能，可视化配置功能和导出映射表到输入法的选项