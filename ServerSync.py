from ftplib import FTP
import sys, os
import os.path

print ("input clint folder: example: C:\\Users\\mdyas\\Desktop\\atiq vy\\ ")
root= input(); # such as "C:\\Users\\mdyas\\Desktop\\atiq vy\\"

print ("input server folder: example: /newfolder ")
destdir= input();# likely "/ssh"

print ("input hostname or ip: example: localhost or 127.0.0.1 ")
host = input(); # sample "127.0.0.1"

print ("input user name: example: name_given_from_the_server ")
user_name = input(); # sample "yasin";

print ("input passward: ")
password = input(); # exp "1234";

# ---------- Delete from clint to connected server --------------
ftps = FTP(host)
ftps.login(user_name, password)
files = list(ftps.nlst(destdir))
for f in files:
    ftps.delete(f)


#----------- Upload directory from clint to connected server -------------
for (dir, _, files) in os.walk(root):
       #newdir=destdir+dir[len(root):len(dir)].replace("\\","/")
       try:
               ftps.cwd(destdir)
       except Exception:
               ftps.mkd(destdir)
       for f in files:
               file = open(os.path.join(dir, f),'rb')
               ftps.storbinary('STOR '+f, file,blocksize=8192)
               file.close()
ftps.close()

try:
    print ("successful")
except:
    print ("failed")
