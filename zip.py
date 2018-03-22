#-*- coding: utf8 -*-
import os
import zipfile
# z = zipfile.ZipFile('my-archive.zip', 'w', zipfile.ZIP_DEFLATED)
startdir='/test/ggg'
fn='g1'
fstart=''
for dirpath, dirnames, filenames in os.walk(startdir):
#     print dirnames
   for dn in dirnames:
        fullpath=os.path.join(dirpath,dn)
        print fullpath
        if fullpath[fullpath.rindex('/')+1:]==fn:
                print 'yes'
                fstart=fullpath
                break
                
            
os .system('mv ' +fstart +' /home')         
            
def getlastdir(self):
         return self[self.rindex('/')+1:]
# (rid,str2)=commands.getstatusoutput('zip -qj '+alllogs+'/'+yests+'/'+newfn+' '+dir+'/'+fn)
#         fp=open(alllogs+'/alogs.txt','a')
#         if 0==rid:
#             print newfn
#             fp.write('\n'+newfn+'  ok')
#         else:
#             fp.write('\n'+str2)

#         z.write(os.path.join(dirpath, filename))
# z.close()