import shutil
import os
from datetime import datetime,date
import os.path, time

def getit(filename):
    try:
        location_folder_=os.path.dirname(os.path.abspath(__file__))
        location_folder=location_folder_.replace('project','files')
        location_file = location_folder+"\\"+filename

        ''' 
        BASE_DIR = Path(__file__).resolve().parent
        print('BASE_DIR= ', BASE_DIR)
        print(os.path.abspath(os.curdir))
        print(os.path.dirname(os.path.abspath(__file__)))
        print(os.getcwd())
        '''


        print("location_folder=", location_folder)
        print("location_file=", location_file)

        filetime_=os.path.getmtime(location_file)
        filedatetime_=datetime.fromtimestamp(filetime_).strftime('%Y-%m-%d')

        print('filedate:', str(filedatetime_))
        today = date.today()

        print("Today is:", str(today))
        if str(filedatetime_)==str(today):
            print('file formed today')
        else:

            print('')
            print('ОШИБКА: EXCEL-ФАЙЛ СФОРМИРОВАН НЕ СЕГОДНЯ')
            print(' СФОРМИРУЙТЕ EXCEL-ФАЙЛ 1.XLSX И СОХРАНИТЕ ЕГО В КАТАЛОГЕ', location_folder)
            raise SystemExit

        return location_file

    except FileNotFoundError:
        print('')
        print('ОШИБКА - НЕТ НУЖНОГО EXCEL-ФАЙЛА В КАТАЛОГЕ ', location_folder)
        print('ИЗ LOTUS СФОРМИРУЙТЕ EXCEL-ФАЙЛ И СОХРАНИТЕ ЕГО В КАТАЛОГЕ', location_folder)
        raise SystemExit