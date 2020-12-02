import os
import glob
import json
import subprocess

def GatherAllData(result_file):
    result_file.write('Function to gather data from all .json files started')

    dirPath = 'E:\\me\python\\year4\\last\\'
    files = glob.glob(os.path.join(dirPath, '*.json'))

    result_file.write('\nAll data files have same structure:')
    with open(files[0]) as data_file:
        one_file_data = json.load(data_file)
        result_file.write('\nMain info:')
        result_file.write(f'\nType of entire document: {type(one_file_data).__name__}')
        result_file.write(f'\nDocument has: {len(one_file_data)} elements')
        result_file.write(f'\nType of every element: {[type(one_file_data[elem]).__name__ for elem in one_file_data.keys()]}:')
        result_file.write(f"\nType of 'main' element: {type(one_file_data['main']).__name__}")
        result_file.write(f"\nValue of 'main':\n{one_file_data['main']}")
        result_file.write("\nSubelements of 'main':\n")
        result_file.write('\n'.join([ str(subvalue) for subvalue in one_file_data['main'].items() ]))
        
    data = []

    for file in files:
        with open(file) as data_file:
            filename = os.path.split(file)[1]
            temp = json.load(data_file)
            data.append({os.path.splitext(filename)[0] : temp})     

    result_file.write('\n\nAll data gathered')
    result_file.write('\nFirst data entry printed for example:\n')   
    json.dump(data[0], result_file, indent=4)
    
    return data
              
def GetValueByKey(result_file, data, key):
    result_file.write(f'\n\nPrint value by key: {key}:')
    for record in data: 
        key1 = list(record.keys())[0]
        key2 = record[key1].keys()
        for k in key2:  
            if k == key:
                result_file.write(f'\nValue of key: {key} is {record[key1][k]} on {key1}')

            elif isinstance(record[key1][k], list):
                for elem in record[key1][k]: 
                    key3 = elem.keys()
                    if key in key3:
                        result_file.write(f'\nValue of key: {key} is {elem[key]} on {key1}')

            elif isinstance(record[key1][k], dict):  
                key4 = record[key1][k].keys()
                if key in key4:
                    result_file.write(f'\nValue of key: {key} is {record[key1][k][key]} on {key1}')
    
              
def GetMaxValueByKey(result_file, data, key):
    result_file.write(f'\n\nPrint max value by key: {key}:')
    maxvalue = 0
    date = ''
    for record in data: 
        key1 = list(record.keys())[0]
        key2 = record[key1].keys()
        for k in key2:  
            if k == key:
                if record[key1][k] > maxvalue:
                    maxvalue = record[key1][k]
                    date = key1

            elif isinstance(record[key1][k], list):
                for elem in record[key1][k]: 
                    key3 = elem.keys()
                    if key in key3:
                        if elem[key] > maxvalue:
                            maxvalue = elem[key]
                            date = key1

            elif isinstance(record[key1][k], dict):  
                key4 = record[key1][k].keys()
                if key in key4:
                    if record[key1][k][key] > maxvalue:
                        maxvalue = record[key1][k][key]
                        date = key1    

    result_file.write(f'\nMax value of key: {key} is {maxvalue} on {key1}') 
              
def GetAvgValueByKey(result_file, data, key):
    result_file.write(f'\n\nPrint average value by key: {key}:')
    avg = 0
    for record in data: 
        key1 = list(record.keys())[0]
        key2 = record[key1].keys()
        for k in key2:  
            if k == key:
                avg += record[key1][k]

            elif isinstance(record[key1][k], list):
                for elem in record[key1][k]: 
                    key3 = elem.keys()
                    if key in key3:
                        avg += elem[key]

            elif isinstance(record[key1][k], dict):  
                key4 = record[key1][k].keys()
                if key in key4:
                    avg += record[key1][k][key]  

    result_file.write(f'\nAvg value of key: {key} is {avg / len(data)}') 
                
def GetDaysWithParticulatWeatherCondition(result_file, data, key, value):
    result_file.write(f'\n\nPrint dates with given value by key: {key}:')
    for record in data: 
        key1 = list(record.keys())[0]
        key2 = record[key1].keys()
        for k in key2:  
            if k == key:
                if record[key1][k] == value:
                    result_file.write(f'\nValue of key: {key} is {record[key1][k]} on {key1}')

            elif isinstance(record[key1][k], list):
                for elem in record[key1][k]: 
                    key3 = elem.keys()
                    if key in key3:
                        if elem[key] == value:
                            result_file.write(f'\nValue of key: {key} is {elem[key]} on {key1}')

            elif isinstance(record[key1][k], dict):  
                key4 = record[key1][k].keys()
                if key in key4:
                    if record[key1][k][key] == value:
                        result_file.write(f'\nValue of key: {key} is {record[key1][k][key]} on {key1}')       
              
def GetDaysWithValueMoreThan(result_file, data, key, diff):
    result_file.write(f'\n\nPrint dates with value bigger then given by key: {key}:')
    for record in data: 
        key1 = list(record.keys())[0]
        key2 = record[key1].keys()
        for k in key2:  
            if k == key:
                if record[key1][k] > diff:
                    result_file.write(f'\nValue of key: {key} is {record[key1][k]} and is more than {diff} on {key1}')

            elif isinstance(record[key1][k], list):
                for elem in record[key1][k]: 
                    key3 = elem.keys()
                    if key in key3:
                        if elem[key] > diff:
                            result_file.write(f'\nValue of key: {key} is {elem[key]} and is more than {diff} on {key1}')

            elif isinstance(record[key1][k], dict):  
                key4 = record[key1][k].keys()
                if key in key4:
                    if record[key1][k][key] > diff:
                        result_file.write(f'\nValue of key: {key} is {record[key1][k][key]} and is more than {diff} on {key1}')
    
def runSubprocess():
    print('Run subprocess')
    subprocess.run(['E:\\me\\python\\year4\\last\\script\\script\\bin\\Debug\\script.exe', ' empty'])  
    print('Subprocess ended')
              
def main():
    with open('E:\\me\\python\\year4\\last\\result.txt', 'w') as result_file:
        data = GatherAllData(result_file)
        GetValueByKey(result_file, data, 'temp_max')
        GetMaxValueByKey(result_file, data, 'temp')
        GetAvgValueByKey(result_file, data, 'humidity')
        GetDaysWithParticulatWeatherCondition(result_file, data, 'main', 'Clouds')
        GetDaysWithValueMoreThan(result_file, data, 'humidity', 98)
    runSubprocess()
    
main()