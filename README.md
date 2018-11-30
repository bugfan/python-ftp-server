# 功能
1. python上传文件夹(file uploader with gui) 通过socket发送数据 client是一个基于tk的gui程序，可以选择整个整个文件夹上传 主要目的（传文件和文件夹）
2. python 压缩文件夹
# 使用说明
1. 拉项目 `git clone https://github.com/bugfan/python-ftp-server.git`
2. 执行 `cd python-ftp-server`
3. 启动server `python server.py` ( 启动前配置server.py里面的host和端口以及存放地址路径)
4. 启动client `python pythonchoose.py` (启动前配置pythonchoose.py里面的端口ip等)
5. client启动之后可以看到一个gui程序(window,linux和mac都可以运行),点击选择按钮选择将要上传到服务器的文件或者文件夹，确定之后开始上传，上传完成会在gui打印出‘xxx 上传成功等字样’
6. 辅助功能:zip.py 可以单独压缩指定文件或者文件夹，可以单独做测试使用
