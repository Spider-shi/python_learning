#-*-coding:utf-8-*-

#简明python教程 第十章 脚本

print '01'
print '-' * 15
#脚本的第一个版本

import os
import time
'''
#1.The files and directories to be backed up are specified in a list
source = ['/home/bob/unix', '/home/bob/code']

#2. The back up must be stored in a main backup directory
target_dir = '/mnt/backup/'

#3. The files are backed up into a zip file
#4. The name of the zip archive is the current data and time
target = target_dir + time.strftime('%Y%m%d%H%M%S') + '.zip'

#5. We use the zip command(in Unix/Linux) to put the files in a zip archive
zip_command = "zip -qr '%s' %s" % (target, ' '.join(source))

# Run the backup
if os.system(zip_command) == 0:
	print 'Successful backup to', target
else:
	print 'Backup FAILED'
'''

print '02'
print'-' * 15
# 脚本的第二个版本
'''
#1. The files and directories to be backed up are specified in a list
source = ['/home/bob/unix', '/home/bob/code']

#2. The back up must be stored in a main backup directory
target_dir = '/mnt/backup/'

#3. The files are backed up into a zip file
#4. The current day is the name of the subdirectory in the main directory 
today = target_dir + time.strftime('%Y%m%d')

# The current time is the name of the zip archive
now = time.strftime('%H%M%S')

# Run the backup
# Create the subdirectory if it isn't already there
if not os.path.exists(today):
	os.mkdir(today)
	print 'Successfully created directory', today

# The name of the zip file
target = today + os.sep + now + '.zip'

#5. We use the zip command (in Unix/Linux) to put the files in a zip archive
zip_command = "zip -qr %s %s" % (target, ' '.join(source))

# Run the backup
if os.system(zip_command) == 0:
	print "Successfully backed to", target
else:
	print "Backedup FAILED"
'''

print '03'
print '-' * 15

# 第三个脚本

source = ['/home/bob/unix', '/home/bob/code']

target_dir = '/mnt/backup/'

today = target_dir + time.strftime('%Y%m%d')

if not os.path.exists(today):
	os.mkdir(today)
	print "Successfully created dir", today

now = time.strftime("%H%M%S")

comment = raw_input("-->")

if len(comment) == 0:
	target = today + os.sep + now + '.zip'
else:
	target = today + os.sep + now + '_' + comment.replace(' ', '_') + '.zip'

zip_command = "zip -qr %s %s" % (target, ' '.join(source))

if os.system(zip_command) == 0:
	print "Successfully backup to", target
else:
	print "Backed FAILED"
