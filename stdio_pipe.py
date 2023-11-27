import os
import subprocess
import sys

JAVA_HOME_SECURITY = os.getenv('JAVA_HOME') + '/lib/security'
os.chdir(JAVA_HOME_SECURITY)
print(os.getcwd())
pwd = subprocess.Popen(['changeit'], stdout=subprocess.PIPE ,shell=True)
res = subprocess.Popen('keytool -list -v -keystore cacerts | findstr /c:"Alias name"', stdin=pwd.stdout, stdout=subprocess.PIPE ,shell=True, encoding='MS949')

#for linux python 2.7
#res = subprocess.Popen(['keytool', '-list', '-v', '-keystore', 'cacerts'], stdin=pwd.stdout, stdout=subprocess.PIPE)

response = res.communicate()
try:
    for iter in response:
        for character in iter.split('\n'):
            print(character)
except Exception as e:
    _, _, tb = sys.exc_info()
    print('error msg : ' + str(e))
    print ('err line no = {}'.format(tb.tb_lineno))
    pass
