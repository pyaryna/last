import os
import json
import glob
import urllib.request
from datetime import date
from pprint import pprint

def GetDataFromServer():   
    print('Checking if file with data for this day already exist')

    dirPath = 'E:\\me\python\\year4\\last\\'
    files = glob.glob(os.path.join(dirPath, '*.json'))

    today = date.today().strftime('%d-%m-%Y')
    filename = dirPath + f'{today}.json'

    if filename in files:
        print('File with data for this day already exist')
        return

    print('Connecting to server...')

    remoteaddr = 'http://api.openweathermap.org/data/2.5/weather?q=Lviv&appid=MYAPI'
    remotefile = urllib.request.urlopen(remoteaddr)  

    print('Get file')

    with open(filename, 'wb') as fsave:     
        fsave.write(remotefile.read())  
        print('File was saved')

    remotefile.close()
    print('Remote file closed')

    print('\nPrint file to python window: ')
    with open(filename) as data_file:
        data = json.load(data_file)
    pprint(data)

    print('\nPrinting finished')
    
def main():
    GetDataFromServer()
    
main()