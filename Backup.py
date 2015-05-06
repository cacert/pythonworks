'''
Created on Jul 19, 2014

@author: kasimsert
'''

import os
import time

source=['/Users/kasimsert/Documents/python']
target='/Users/kasimsert/Documents/pythonBackup'

target = target+os.sep+time.strftime('%Y%m%d%H%M%S')+'.zip'

if not os.path.exists(target):
    os.mkdir(target)
    print('target dir %s created' % target)
    
zip_command = 'zip -r {0} -b {1}'.format(target, ' '.join(source))

print('zip command is %s ' % zip_command)

print('zip started..')

if os.system(zip_command) == 0:
    print('zip succedded')
else:
    print('error')
