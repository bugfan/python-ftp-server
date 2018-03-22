# -*- coding: UTF-8 -*-

# 导入库
import socket, threading, os,commands

SIZE = 2048
RECVPATH='/test2'
fp='/test/abc.zip'
startdir='/test/temdir'

def checkFile():
    list = os.listdir('.')
    for iterm in list:
        if iterm == fp:
            os.remove(iterm)
            print 'remove'
        else:
            pass
		

# 接受数据线程
def tcplink(sock, addr):
    print 'Accept new connection from %s:%s...' % addr
    sock.send('Welcome from server!')
    print 'receiving, please wait for a second ...'
    while True:
        data = sock.recv(SIZE)
        if not data :
            print 'reach the end of file'
            break
        elif data == 'android':
            print data
            fn='android'
            checkFile()
            with open(fp, 'wb') as f:
                pass
        elif data == 'ios':
            print data
            fn='ios'
            checkFile()
            with open(fp, 'wb') as f:
                pass
        elif data == 'banner':
            print data
            fn='banner'
            checkFile()
            with open(fp, 'wb') as f:
                pass
        elif data == '88dir':
            print 'create dir'
        else:
            with open(fp, 'ab') as f:
                f.write(data)
    sock.close()
    print 'receive finished'
	
    (id,str)=commands.getstatusoutput('unzip  -d' +startdir+' '+fp)
    if id==0:
        print 'unzip ok!'
    else:
        print str
    os.remove(fp)
    print 'remove zip ok!'
    for dirpath, dirnames, filenames in os.walk(startdir):
        for dn in dirnames:
            fullpath=os.path.join(dirpath,dn)
            print fullpath
            if fullpath[fullpath.rindex('/')+1:]==fn:
				print 'path: mv -f ' +fullpath +' '+RECVPATH
				os.system('mv -f ' +fullpath +' ' +RECVPATH)   
				isExists= os.path.exists(RECVPATH)
				if  not  isExists:
    			    (rid,str)=commands.getstatusoutput('mkdir '+RECVPATH)
					pass
					

      
    #os.system('rm '+startdir +' -rf')
	

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

s.bind(('172.16.207.174', 9999))

s.listen(1)
print 'Waiting for connection...'
while True:
    sock, addr = s.accept()
   
    t = threading.Thread(target = tcplink, args = (sock, addr))
    t.start()
