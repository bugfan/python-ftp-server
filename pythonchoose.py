#!/usr/bin/python
#-*- coding: utf8 -*-
import Tkinter, Tkconstants, tkFileDialog
import os
import zipfile
import socket,shutil
#str='无'
#fpath=''
class TkFileDialogExample(Tkinter.Frame):

    def __init__(self, root):

        Tkinter.Frame.__init__(self, root)

        # options for buttons
        button_opt = {'fill': Tkconstants.BOTH,'side':Tkinter.TOP,'padx': 5, 'pady': 5}
        #
        # define buttons
#         Tkinter.Button(self,  command=self.askopenfile,text='打开文件').pack(**button_opt)
#         Tkinter.Button(self, text='打开文件名', command=self.askopenfilename).pack(**button_opt)
#         Tkinter.Button(self, text='保存文件', command=self.asksaveasfile).pack(**button_opt)
#         Tkinter.Button(self, text='另存为文件',bg='orange' ,fg='blue',command=self.asksaveasfilename).pack(**button_opt)
        #Tkinter.Button(self, text='上传文件', command=send).pack(**button_opt)
        Tkinter.Button(self, text='选择上传目录', command=self.askdirectoryandroid).pack(**button_opt)
#         Tkinter.Button(self, text='选择ios目录', command=self.askdirectoryios).pack(**button_opt)
#         Tkinter.Button(self, text='选择banner目录', command=self.askdirectorybanner).pack(**button_opt)
        Tkinter.Label(self,text='结果显示:').pack()

        # define options for opening or saving a file
        self.file_opt = options = {}
        options['defaultextension'] = '.txt'
        options['filetypes'] = [('all files', '.*'), ('text files', '.txt')]
        options['initialdir'] = 'C:\\'
        options['initialfile'] = 'myfile.txt'
        options['parent'] = root
        options['title'] = 'This is a title'

        # This is only available on the Macintosh, and only when Navigation Services are installed.
        #options['message'] = 'message'

        # if you use the multiple file version of the module functions this option is set automatically.
        #options['multiple'] = 1

        # defining options for opening a directory
        self.dir_opt = options = {}
        options['initialdir'] = 'C:\\'
        options['mustexist'] = False
        options['parent'] = root
        options['title'] = 'This is a title'

    def askopenfile(self):
        
        """Returns an opened file in read mode."""
		
        f=tkFileDialog.askopenfile(mode='rb', **self.file_opt)
        print(f.read())
        f.close()
        return None

    def askopenfilename(self):

        """Returns an opened file in read mode.
        This time the dialog just returns a filename and the file is opened by your own code.
        """

        # get filename
        filename = tkFileDialog.askopenfilename(**self.file_opt)

        # open file on your own
        if filename:
            return open(filename, 'r')

    def asksaveasfile(self):

        """Returns an opened file in write mode."""
        
        return tkFileDialog.asksaveasfile(mode='w', **self.file_opt)

    def asksaveasfilename(self):

        """Returns an opened file in write mode.
        This time the dialog just returns a filename and the file is opened by your own code.
        """

        # get filename
        filename = tkFileDialog.asksaveasfilename(**self.file_opt)
        # open file on your own
        if filename:
            print 'ff'
            f=open(filename, 'rb')
            print(f.read())
            f.close()
            return None

    def askdirectoryandroid(self):

        """Returns a selected directoryname."""
        send( tkFileDialog.askdirectory(**self.dir_opt) ,self) 
        return None
    def askdirectoryios(self):
        
        """Returns a selected directoryname."""
        send( tkFileDialog.askdirectory(**self.dir_opt),self)
        return None
    def askdirectorybanner(self):

        """Returns a selected directoryname."""
        send(tkFileDialog.askdirectory(**self.dir_opt),self)
        return None
    
    
#发送与压缩
def send(fpath,self):
    if fpath!='':
            h=fpath
            print h
            print '目录操纵'
            fname=getlastdir(h)+'.zip'
            z = zipfile.ZipFile(fname, 'w', zipfile.ZIP_DEFLATED)
            for dirpath, dirnames, filenames in os.walk(h):
              for filename in filenames:
                  print os.path.join(dirpath, filename) #将来输出到ｌabel
                  z.write(os.path.join(dirpath, filename))
            z.close()
#             os.system('chmod 777 '+fname)
            print '压缩成功'
            SIZE = 2048
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            HOST='meiyue2.mm419.com'
            PORT=9999
            ADDR=(HOST,PORT)
            # 建立连接:
            try:
                s.connect(ADDR)
                # 接收欢迎消息:
                print s.recv(SIZE)
                sp=getlastdir(fpath)
                if not sp:
                    s.send('88file')
                else:
                    s.send(sp)
                print 'sending, please wait for a second ...'
                try:
                    with open(fname, 'rb') as f:
                        for data in f:  #他妈的竟然自己就知道发送多少，比c强多了
                            s.send(data)
                except IOError:
                    print '文件打开失败或者发送失败'
                print 'sended !'
                Tkinter.Label(self,text=getlastdir(h)+'~OK!').pack()
                s.close()
                print 'connection closed'
            except IOError:
                print '连接异常'
                Tkinter.Label(self,text='上传失败，连接异常').pack()
            os.remove(fname)
            print '删除压缩文件成功'
    else:
        fpath=''
        Tkinter.Label(self,text='目录不对').pack()
    return None     
    
def getlastdir(self):
         return self[self.rindex('/')+1:]
     
if __name__ == '__main__':
    os.system('apt-get install python-tk')
    root = Tkinter.Tk()
    root.title('美约')
    TkFileDialogExample(root).pack()
    root.mainloop()
