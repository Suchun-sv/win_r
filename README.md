# win_r
缩短文件夹从需要到打开的速度

(windows10系统专用)

## 安装方法

将主路径设置为名为"FileCMD"的环境变量

并在path中添加

"%FileCMD%\bin";"%FileCMD%\links"

## 使用方法

### 1.创建文件夹

假设工作父目录是C:/foo/:.

foo/

├─00 计算机网络
├─01 计算机体系结构
└─02 算法

在任意地方使用lmkdir "bar" -p "C:/foo/"

会自动在foo文件夹下创建 “03 bar”的文件夹:.

foo/

├─00 计算机网络
├─01 计算机体系结构
├─02 算法
└─03 bar

默认保存上一次创建所用的父目录，可以用-s 参数选择已用过的父目录，也可以在config.yml里修改

### 2. shortcut

对常用的文件夹创建以文件夹名缩写或者其他助记符为名的windows快捷方式,可以在win+r窗口一键呼出。

#### 2.1 创建方式

1. 在利用lmkdir创建文件夹时利用-m参数指定助记符

   > lmkdir "foo" -m abc ff ss asd kjk 命令可以创建foo文件夹并且创建快捷方式(shortcut),在win+r中输入abc或者其他助记符来快速打开foo文件夹

2. 在资源管理器地址栏打开cmd,输入

   > llink -m bar 

   可以为当前文件夹创建名为bar的shortcut

### 2.2 删除方式

	1. 在当前文件夹的cmd窗口中输入

>  llink -rm 

​	可以删除当前文件夹的所有shortcut

### 2.3 查看方式

​      在当前文件夹的cmd窗口中输入

>  llink -s 或者直接输入llink 

​	会展示当前文件夹对应的所有shortcut

### 2.4 查看shortcut对应的文件夹路径 

在任意窗口输入

> lcp [缩写]

即可查看缩写对应的文件夹绝对路径，并且会把路径复制到剪贴板，便于使用。

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