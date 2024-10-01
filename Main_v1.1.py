import os
import sys
import shutil
import colorama
import ctypes
from colorama import Fore, Back, Style
from colorama import just_fix_windows_console
from colorama import init
import subprocess
import datetime

just_fix_windows_console()
init(autoreset=True)
Os_UserName_Windows = os.getenv('USERNAME')


def is_admin():
    try:
        return ctypes.windll.shell32.IsUserAnAdmin()
    except:
        return False

def run_as_admin():
    try:
        ctypes.windll.shell32.ShellExecuteW(None, "runas", sys.executable, " ".join(sys.argv), None, 1)
        sys.exit()
    except Exception as e:
        print(f"PreLoader LC ERROR >> Ошибка: {e}")
        with open('file.txt', 'a') as file:
            file.write(f'PreLoader LC ERROR >> Ошибка: {e}\n')
        sys.exit(1)

if is_admin():
    print("PreLoader LC >> Программа был запущена от имени администратора.")
    with open('log.txt', 'a') as file:
        file.write(f'PreLoader LC >> Программа был запущена от имени администратора.\n')

else:
    print("PreLoader LC ERROR >> Программа не была запущен от имени администратора. Пожалуйста, разрешите выполнение от имени администратора.")
    with open('log.txt', 'a') as file:
        file.write(f'PreLoader LC >> Программа не была запущен от имени администратора. \n')
    run_as_admin()





def Main():
    print(f"\n-----> {Fore.YELLOW}Fire{Fore.LIGHTRED_EX}Soft")
    print(f"---->{Fore.CYAN} Light Cleaner V1.1\n")
    print(f"{Fore.LIGHTCYAN_EX}| 0. > Об программе{Fore.RESET}")
    print(f"{Fore.LIGHTCYAN_EX}| 1. > Полная очистка{Fore.RESET}")
    print(f"{Fore.LIGHTCYAN_EX}| 2. > Очистка папок Temp (User/Windows){Fore.RESET}")
    print(f"{Fore.CYAN}| e. > Выход из программы{Fore.RESET}")

    select_parametr = input(f"{Fore.YELLOW}| Введите номер пункта >> {Fore.CYAN}")
    print(f"{Fore.RESET}")

    if select_parametr == "0":
        About_Program()
    elif select_parametr == "1":
        Light_Clean_All()

    elif select_parametr == "2":
        Light_Clean_All_Temp_Folder()

    elif select_parametr in ["выйти", "в", "exit", "e"]:
        return 0
    else:
        Main()

def About_Program():
    print(f"\n-----> {Fore.LIGHTCYAN_EX}Light Cleaner{Fore.RESET}")
    print(f"|----> {Fore.CYAN}Автор: FireTIA")
    print(f"|----> {Fore.CYAN}Компания: {Fore.YELLOW}Fire{Fore.LIGHTRED_EX}Soft{Fore.RESET}")
    print(f"---> {Fore.CYAN}Версия: 1.1 Full {Fore.LIGHTGREEN_EX}>.py<{Fore.RESET}")
    print(f"--> {Fore.CYAN}О программе")
    print(f"{Fore.CYAN}|> Программа сделана в целях очистки временных файлов программ и файлов Windows.")
    print(f"{Fore.CYAN}|> За основу путей очистки файлов взято с Glary Utilites.")
    print(f"{Fore.CYAN}|> Программа не подлежит продаже.")

    print(f"{Fore.LIGHTCYAN_EX}| 0/1. > Назад{Fore.RESET}")
    select_parametr = input(f"{Fore.YELLOW}| Введите номер пункта >> {Fore.CYAN}")
    if select_parametr in ["0", "1"]:
        Main()
    else:
        About_Program()


def get_folder_size(folder_path):
    total_size = 0
    for dirpath, dirnames, filenames in os.walk(folder_path):
        for filename in filenames:
            file_path = os.path.join(dirpath, filename)
            total_size += os.path.getsize(file_path)
    return total_size

def get_time():
    current_datetime = datetime.datetime.now()
    formatted_datetime = current_datetime.strftime("%Y-%m-%d | %H:%M:%S")
    return formatted_datetime



    #--------------------------------------------------------------------
#--------------------------------------------------------------------
def Light_Clean_Folder_Temp_User():
    global initial_size_Temp_User, final_size_Temp_User

    folder_path_Temp = os.path.join(os.environ['LOCALAPPDATA'], 'Temp')

    print(f"{Fore.LIGHTBLUE_EX}\n \n \n|-")
    print(f"{Fore.LIGHTBLUE_EX}| LC Step 1 > Очистка Windows/Temp")
    print(f"{Fore.LIGHTBLUE_EX}|- \n \n \n")

    initial_size_Temp_User = get_folder_size(folder_path_Temp) / (1024 * 1024)

    if os.path.exists(folder_path_Temp) and os.path.isdir(folder_path_Temp):
        for filename in os.listdir(folder_path_Temp):
            file_path = os.path.join(folder_path_Temp, filename)
            try:
                if os.path.isfile(file_path) or os.path.islink(file_path):
                    os.unlink(file_path)  
                elif os.path.isdir(file_path):
                    shutil.rmtree(file_path)  
            except Exception as e:
                print(f'{Fore.LIGHTYELLOW_EX}| LC Warrning >{Fore.RESET} Не удалось удалить {file_path}. Причина: {Fore.LIGHTRED_EX}{e}{Fore.RESET}')
                
                time = get_time()
                with open('log_warning.txt', 'a') as file:
                    file.write(f'LC Warrning > {time} >  Не удалось удалить {file_path}. Причина: {e}  \n')
        print(f"{Fore.RESET} \n \n \n ")
        print(f'{Fore.LIGHTBLUE_EX}| LC Finish >{Fore.RESET} Содержимое папки {folder_path_Temp} удалено успешно.')

    else:
        print(f'{Fore.LIGHTRED_EX}| LC Error >{Fore.RESET} Папка {folder_path_Temp} не существует или не является директорией.')

    

    final_size_Temp_User = get_folder_size(folder_path_Temp) / (1024 * 1024)
    print(f"{Fore.LIGHTBLUE_EX}| LC Stat >{Fore.RESET} Вес папки {Os_UserName_Windows}/Temp до очистки: {Fore.YELLOW}{initial_size_Temp_User:.2f} МБ{Fore.LIGHTCYAN_EX} | {Fore.RESET} После: {Fore.GREEN}{final_size_Temp_User:.2f} МБ{Fore.RESET}")
    
    time = get_time()
    with open('log.txt', 'a') as file:
        file.write(f'LC Stat > {time} > > Вес папки ({Os_UserName_Windows}/Temp) до очистки: {initial_size_Temp_User:.2f} МБ | После: {final_size_Temp_User:.2f} МБ  \n')
#--------------------------------------------------------------------
    #--------------------------------------------------------------------





        #--------------------------------------------------------------------
#--------------------------------------------------------------------
def Light_Clean_Folder_Temp_Windows():

    global initial_size_Windows_Temp, final_size_Windows_Temp

    print(f"{Fore.LIGHTBLUE_EX}\n \n \n|-")
    print(f"{Fore.LIGHTBLUE_EX}| LC Step 2 > Очистка Windows/Temp")
    print(f"{Fore.LIGHTBLUE_EX}|- \n \n \n")


    folder_path_Windows_Temp = "C:/Windows/Temp"

    initial_size_Windows_Temp = get_folder_size(folder_path_Windows_Temp) / (1024 * 1024)

    if os.path.exists(folder_path_Windows_Temp) and os.path.isdir(folder_path_Windows_Temp):
        for filename in os.listdir(folder_path_Windows_Temp):
            file_path = os.path.join(folder_path_Windows_Temp, filename)
            try:
                if os.path.isfile(file_path) or os.path.islink(file_path):
                    os.unlink(file_path)  
                elif os.path.isdir(file_path):
                    shutil.rmtree(file_path)  # Удаляем подпапки
            except Exception as e:
                print(f'{Fore.LIGHTYELLOW_EX}| LC Warrning >{Fore.RESET} Не удалось удалить {file_path}. Причина: {Fore.LIGHTRED_EX}{e}{Fore.RESET}')
                
                time = get_time()
                with open('log_warning.txt', 'a') as file:
                    file.write(f'LC Warrning > {time} >  Не удалось удалить {file_path}. Причина: {e}  \n')
        print(f"{Fore.RESET} \n \n \n ")
        print(f'{Fore.LIGHTBLUE_EX}| LC Finish >{Fore.RESET} Содержимое папки {folder_path_Windows_Temp} удалено успешно.')

    else:
        print(f'{Fore.LIGHTRED_EX}| LC Error >{Fore.RESET} Папка {folder_path_Windows_Temp} не существует или не является директорией.')


    final_size_Windows_Temp = get_folder_size(folder_path_Windows_Temp) / (1024 * 1024)
    print(f"{Fore.LIGHTBLUE_EX}| LC Stat >{Fore.RESET} Вес папки {folder_path_Windows_Temp} до очистки: {Fore.YELLOW}{initial_size_Windows_Temp:.2f} МБ{Fore.LIGHTCYAN_EX} | {Fore.RESET} После: {Fore.GREEN}{final_size_Windows_Temp:.2f} МБ{Fore.RESET}")
    
    time = get_time()
    with open('log.txt', 'a') as file:
        file.write(f'LC Stat > {time} > > Вес папки ({folder_path_Windows_Temp}) до очистки: {initial_size_Windows_Temp:.2f} МБ | После: {final_size_Windows_Temp:.2f} МБ  \n')

#--------------------------------------------------------------------
    #--------------------------------------------------------------------        





    #--------------------------------------------------------------------
#--------------------------------------------------------------------
def Light_Clean_Folder_Cache_User():

    global initial_size_Cache_User, final_size_Cache_User

    print(f"{Fore.LIGHTBLUE_EX}\n \n \n|-")
    print(f"{Fore.LIGHTBLUE_EX}| LC Step 3 > Очистка {Os_UserName_Windows}/cache")
    print(f"{Fore.LIGHTBLUE_EX}|- \n \n \n")


    folder_path_User_Cache = os.path.join(os.environ['LOCALAPPDATA'], 'cache')
    initial_size_Cache_User = get_folder_size(folder_path_User_Cache) / (1024 * 1024)

    if os.path.exists(folder_path_User_Cache) and os.path.isdir(folder_path_User_Cache):
        for filename in os.listdir(folder_path_User_Cache):
            file_path = os.path.join(folder_path_User_Cache, filename)
            try:
                if os.path.isfile(file_path) or os.path.islink(file_path):
                    os.unlink(file_path)
                elif os.path.isdir(file_path):
                    shutil.rmtree(file_path)
            except Exception as e:
                print(f'{Fore.LIGHTYELLOW_EX}| LC Warrning >{Fore.RESET} Не удалось удалить {file_path}. Причина: {Fore.LIGHTRED_EX}{e}{Fore.RESET}')
                
                time = get_time()
                with open('log_warning.txt', 'a') as file:
                    file.write(f'LC Warrning > {time} >  Не удалось удалить {file_path}. Причина: {e}  \n')
        print(f"{Fore.RESET} \n \n \n ")
        print(f'{Fore.LIGHTBLUE_EX}| LC Finish >{Fore.RESET} Содержимое папки {folder_path_User_Cache} удалено успешно.')

    else:
        print(f'{Fore.LIGHTRED_EX}| LC Error >{Fore.RESET} Папка {folder_path_User_Cache} не существует или не является директорией.')

    

    final_size_Cache_User = get_folder_size(folder_path_User_Cache) / (1024 * 1024)
    print(f"{Fore.LIGHTBLUE_EX}| LC Stat >{Fore.RESET} Вес папки {Os_UserName_Windows}/cache до очистки: {Fore.YELLOW}{initial_size_Cache_User:.2f} МБ{Fore.LIGHTCYAN_EX} | {Fore.RESET} После: {Fore.GREEN}{final_size_Cache_User:.2f} МБ{Fore.RESET}")
    
    time = get_time()
    with open('log.txt', 'a') as file:
        file.write(f'LC Stat > {time} > > Вес папки ({Os_UserName_Windows}/cache) до очистки: {initial_size_Cache_User:.2f} МБ | После: {final_size_Cache_User:.2f} МБ  \n')
        
#--------------------------------------------------------------------
    #--------------------------------------------------------------------




        #--------------------------------------------------------------------
#--------------------------------------------------------------------
def Light_Clean_Folder_mbam_cache():

    global initial_size_User_Cache_mbam, final_size_User_Cache_mbam

    print(f"{Fore.LIGHTBLUE_EX}\n \n \n|-")
    print(f"{Fore.LIGHTBLUE_EX}| LC Step 4 > Очистка {Os_UserName_Windows}/mbam/cache/qmlcache")
    print(f"{Fore.LIGHTBLUE_EX}|- \n \n \n")


    folder_path_User_Cache_mbam = os.path.join(os.environ['LOCALAPPDATA'], 'mbam/cache/qmlcache')
    initial_size_User_Cache_mbam = get_folder_size(folder_path_User_Cache_mbam) / (1024 * 1024)

    if os.path.exists(folder_path_User_Cache_mbam) and os.path.isdir(folder_path_User_Cache_mbam):
        for filename in os.listdir(folder_path_User_Cache_mbam):
            file_path = os.path.join(folder_path_User_Cache_mbam, filename)
            try:
                if os.path.isfile(file_path) or os.path.islink(file_path):
                    os.unlink(file_path)
                elif os.path.isdir(file_path):
                    shutil.rmtree(file_path)
            except Exception as e:
                print(f'{Fore.LIGHTYELLOW_EX}| LC Warrning >{Fore.RESET} Не удалось удалить {file_path}. Причина: {Fore.LIGHTRED_EX}{e}{Fore.RESET}')
                
                time = get_time()
                with open('log_warning.txt', 'a') as file:
                    file.write(f'LC Warrning > {time} >  Не удалось удалить {file_path}. Причина: {e}  \n')
        print(f"{Fore.RESET} \n \n \n ")
        print(f'{Fore.LIGHTBLUE_EX}| LC Finish >{Fore.RESET} Содержимое папки {folder_path_User_Cache_mbam} удалено успешно.')

    else:
        print(f'{Fore.LIGHTRED_EX}| LC Warning >{Fore.RESET} Папка {folder_path_User_Cache_mbam} не существует или не является директорией.')
        time = get_time()
        with open('log_warning.txt', 'a') as file:
            file.write(f'LC Warrning > {time} >  Папка ({folder_path_User_Cache_mbam}) не существует или не является директорией.  \n')

    

    final_size_User_Cache_mbam = get_folder_size(folder_path_User_Cache_mbam) / (1024 * 1024)
    print(f"{Fore.LIGHTBLUE_EX}| LC Stat >{Fore.RESET} Вес папки {Os_UserName_Windows}/mbam/cache/qmlcache до очистки: {Fore.YELLOW}{initial_size_User_Cache_mbam:.2f} МБ{Fore.LIGHTCYAN_EX} | {Fore.RESET} После: {Fore.GREEN}{final_size_User_Cache_mbam:.2f} МБ{Fore.RESET}")
    
    time = get_time()
    with open('log.txt', 'a') as file:
        file.write(f'LC Stat > {time} > > Вес папки ({Os_UserName_Windows}/mbam/cache/qmlcache) до очистки: {initial_size_User_Cache_mbam:.2f} МБ | После: {final_size_User_Cache_mbam:.2f} МБ  \n')
        
#--------------------------------------------------------------------
    #--------------------------------------------------------------------



    #--------------------------------------------------------------------
#--------------------------------------------------------------------
def Light_Clean_Folder_CrushDumps():

    global initial_size_CrashDumps_User, final_size_CrashDumps_User, Confirm_Clean_1

    print(f"{Fore.LIGHTBLUE_EX}\n \n \n|-")
    print(f"{Fore.LIGHTBLUE_EX}| LC Step 5 > Очистка {Os_UserName_Windows}/CrashDumps")
    print(f"{Fore.LIGHTBLUE_EX}|- \n \n \n")


    Confirm_Clean_1 = input(f"{Fore.LIGHTBLUE_EX}| LC Step 5 > Удалять ли логи об сбоях системы? (y/n):{Fore.CYAN} ")

    if Confirm_Clean_1 in ["y", "Y", "yes", "Yes", "д", "Д", "да", "Да"]:

        folder_path_User_CrashDumps = os.path.join(os.environ['LOCALAPPDATA'], 'CrashDumps')
        initial_size_CrashDumps_User = get_folder_size(folder_path_User_CrashDumps) / (1024 * 1024)

        if os.path.exists(folder_path_User_CrashDumps) and os.path.isdir(folder_path_User_CrashDumps):
            for filename in os.listdir(folder_path_User_CrashDumps):
                file_path = os.path.join(folder_path_User_CrashDumps, filename)
                try:
                    if os.path.isfile(file_path) or os.path.islink(file_path):
                        os.unlink(file_path)
                    elif os.path.isdir(file_path):
                        shutil.rmtree(file_path)
                except Exception as e:
                    print(f'{Fore.LIGHTYELLOW_EX}| LC Warrning >{Fore.RESET} Не удалось удалить {file_path}. Причина: {Fore.LIGHTRED_EX}{e}{Fore.RESET}')
                
                    time = get_time()
                    with open('log_warning.txt', 'a') as file:
                        file.write(f'LC Warrning > {time} >  Не удалось удалить {file_path}. Причина: {e}  \n')
            print(f"{Fore.RESET} \n \n \n ")
            print(f'{Fore.LIGHTBLUE_EX}| LC Finish >{Fore.RESET} Содержимое папки {folder_path_User_CrashDumps} удалено успешно.')

        else:
            print(f'{Fore.LIGHTRED_EX}| LC Warning >{Fore.RESET} Папка {folder_path_User_CrashDumps} не существует или не является директорией.')
            time = get_time()
            with open('log_warning.txt', 'a') as file:
                file.write(f'LC Warrning > {time} >  Папка ({folder_path_User_CrashDumps}) не существует или не является директорией.  \n')

    

        final_size_CrashDumps_User = get_folder_size(folder_path_User_CrashDumps) / (1024 * 1024)
        print(f"{Fore.LIGHTBLUE_EX}| LC Stat >{Fore.RESET} Вес папки {Os_UserName_Windows}/CrashDumps до очистки: {Fore.YELLOW}{initial_size_CrashDumps_User:.2f} МБ{Fore.LIGHTCYAN_EX} | {Fore.RESET} После: {Fore.GREEN}{final_size_CrashDumps_User:.2f} МБ{Fore.RESET}")
    
        time = get_time()
        with open('log.txt', 'a') as file:
            file.write(f'LC Stat > {time} > > Вес папки ({Os_UserName_Windows}/CrashDumps) до очистки: {initial_size_CrashDumps_User:.2f} МБ | После: {final_size_CrashDumps_User:.2f} МБ  \n')
            
#--------------------------------------------------------------------
    #--------------------------------------------------------------------





    #--------------------------------------------------------------------
#--------------------------------------------------------------------   
def Light_Clean_Folder_SoftwareDistribution_Download():
    global initial_size_Windows_Update, final_size_Windows_Update
    print(f"{Fore.LIGHTBLUE_EX}\n \n \n|-")
    print(f"{Fore.LIGHTBLUE_EX}| LC Step 6 > Очистка C:/Win/SoftwareDistribution/Download")
    print(f"{Fore.LIGHTBLUE_EX}|- \n \n \n")


    
    folder_path_Windows_Update = "C:/Windows/SoftwareDistribution/Download"
    initial_size_Windows_Update = get_folder_size(folder_path_Windows_Update) / (1024 * 1024)

    if os.path.exists(folder_path_Windows_Update) and os.path.isdir(folder_path_Windows_Update):
        for filename in os.listdir(folder_path_Windows_Update):
            file_path = os.path.join(folder_path_Windows_Update, filename)
            try:
                if os.path.isfile(file_path) or os.path.islink(file_path):
                    os.unlink(file_path)
                elif os.path.isdir(file_path):
                    shutil.rmtree(file_path)
            except Exception as e:
                print(f'{Fore.LIGHTYELLOW_EX}| LC Warrning >{Fore.RESET} Не удалось удалить {file_path}. Причина: {Fore.LIGHTRED_EX}{e}{Fore.RESET}')
                
                time = get_time()
                with open('log_warning.txt', 'a') as file:
                    file.write(f'LC Warrning > {time} >  Не удалось удалить {file_path}. Причина: {e}  \n')
        print(f"{Fore.RESET} \n \n \n ")
        print(f'{Fore.LIGHTBLUE_EX}| LC Finish >{Fore.RESET} Содержимое папки {folder_path_Windows_Update} удалено успешно.')

    else:
        print(f'{Fore.LIGHTRED_EX}| LC Warning >{Fore.RESET} Папка {folder_path_Windows_Update} не существует или не является директорией.')
        time = get_time()
        with open('log_warning.txt', 'a') as file:
            file.write(f'LC Warrning > {time} >  Папка ({folder_path_Windows_Update}) не существует или не является директорией.  \n')

    

    final_size_Windows_Update = get_folder_size(folder_path_Windows_Update) / (1024 * 1024)
    print(f"{Fore.LIGHTBLUE_EX}| LC Stat >{Fore.RESET} Вес папки {folder_path_Windows_Update} до очистки: {Fore.YELLOW}{initial_size_Windows_Update:.2f} МБ{Fore.LIGHTCYAN_EX} | {Fore.RESET} После: {Fore.GREEN}{final_size_Windows_Update:.2f} МБ{Fore.RESET}")
    
    time = get_time()
    with open('log.txt', 'a') as file:
        file.write(f'LC Stat > {time} > > Вес папки ({folder_path_Windows_Update}) до очистки: {initial_size_Windows_Update:.2f} МБ | После: {final_size_Windows_Update:.2f} МБ  \n')
        
#--------------------------------------------------------------------
    #--------------------------------------------------------------------





    #--------------------------------------------------------------------
#--------------------------------------------------------------------
def Light_Clean_Folder_Nvidia_GLCache():
    global initial_size_Nividia_Cache, final_size_Nividia_Cache
    print(f"{Fore.LIGHTBLUE_EX}\n \n \n|-")
    print(f"{Fore.LIGHTBLUE_EX}| LC Step 7 > Очистка {Os_UserName_Windows}/NVIDIA/GLCache")
    print(f"{Fore.LIGHTBLUE_EX}|- \n \n \n")


    folder_path_User_Nividia_Cache = os.path.join(os.environ['LOCALAPPDATA'], 'NVIDIA/GLCache')
    initial_size_Nividia_Cache = get_folder_size(folder_path_User_Nividia_Cache) / (1024 * 1024)

    if os.path.exists(folder_path_User_Nividia_Cache) and os.path.isdir(folder_path_User_Nividia_Cache):
        for filename in os.listdir(folder_path_User_Nividia_Cache):
            file_path = os.path.join(folder_path_User_Nividia_Cache, filename)
            try:
                if os.path.isfile(file_path) or os.path.islink(file_path):
                    os.unlink(file_path)
                elif os.path.isdir(file_path):
                    shutil.rmtree(file_path)
            except Exception as e:
                print(f'{Fore.LIGHTYELLOW_EX}| LC Warrning >{Fore.RESET} Не удалось удалить {file_path}. Причина: {Fore.LIGHTRED_EX}{e}{Fore.RESET}')
                
                time = get_time()
                with open('log_warning.txt', 'a') as file:
                    file.write(f'LC Warrning > {time} >  Не удалось удалить {file_path}. Причина: {e}  \n')
        print(f"{Fore.RESET} \n \n \n ")
        print(f'{Fore.LIGHTBLUE_EX}| LC Finish >{Fore.RESET} Содержимое папки {folder_path_User_Nividia_Cache} удалено успешно.')

    else:
        time = get_time()
        print(f'{Fore.LIGHTRED_EX}| LC Warning >{Fore.RESET} Папка {folder_path_User_Nividia_Cache} не существует или не является директорией.')
        with open('log_warning.txt', 'a') as file:
            file.write(f'LC Warrning > {time} >  Папка ({folder_path_User_Nividia_Cache}) не существует или не является директорией.  \n')

    

    final_size_Nividia_Cache = get_folder_size(folder_path_User_Nividia_Cache) / (1024 * 1024)
    print(f"{Fore.LIGHTBLUE_EX}| LC Stat >{Fore.RESET} Вес папки {Os_UserName_Windows}/NVIDIA/GLCache до очистки: {Fore.YELLOW}{initial_size_Nividia_Cache:.2f} МБ{Fore.LIGHTCYAN_EX} | {Fore.RESET} После: {Fore.GREEN}{final_size_Nividia_Cache:.2f} МБ{Fore.RESET}")


    time = get_time()
    with open('log.txt', 'a') as file:
        file.write(f'LC Stat > {time} > > Вес папки ({folder_path_User_Nividia_Cache}) до очистки: {initial_size_Nividia_Cache:.2f} МБ | После: {final_size_Nividia_Cache:.2f} МБ  \n')


#--------------------------------------------------------------------
    #--------------------------------------------------------------------




def Light_Clean_All_Temp_Folder():
    time = get_time()
    with open('log.txt', 'a') as file:
        file.write(f'LC > {time} > Запуск "Windows/Temp | User/Temp" очистки. \n')

    Light_Clean_Folder_Temp_User()
    Light_Clean_Folder_Temp_Windows()

         #--------------------------------------------------------------------
#--------------------------------------------------------------------
    print(f"{Fore.LIGHTBLUE_EX}\n \n \n|-")
    print(f"{Fore.LIGHTBLUE_EX}| Light Cleaner > Окончание очистки")
    print(f"{Fore.LIGHTBLUE_EX}|- \n \n \n")
#--------------------------------------------------------------------
    #--------------------------------------------------------------------

    All_free_space_1 = initial_size_Temp_User - final_size_Temp_User
    All_free_space_2 = initial_size_Windows_Temp - final_size_Windows_Temp

    print(f"{Fore.LIGHTBLUE_EX}| LC Stat >{Fore.RESET} Вес папки {Os_UserName_Windows}/Temp до очистки: {Fore.YELLOW}{initial_size_Temp_User:.2f} МБ{Fore.RESET} | Очищено: {Fore.CYAN}{All_free_space_1:.2f}{Fore.RESET} | {Fore.RESET} После: {Fore.GREEN}{final_size_Temp_User:.2f} МБ{Fore.RESET}")
    print(f"{Fore.LIGHTBLUE_EX}| LC Stat >{Fore.RESET} Вес папки C:/Windows/Temp до очистки: {Fore.YELLOW}{initial_size_Windows_Temp:.2f} МБ{Fore.RESET} | Очищено: {Fore.CYAN}{All_free_space_2:.2f}{Fore.RESET} | {Fore.RESET} После: {Fore.GREEN}{final_size_Windows_Temp:.2f} МБ{Fore.RESET}")

    All_free_space_sum = All_free_space_1 + All_free_space_2

    print(f"{Fore.LIGHTBLUE_EX}| LC Stat >{Fore.RESET} Всего очищено: {Fore.LIGHTGREEN_EX}> {All_free_space_sum:.2f} МБ < ")
    input(f"{Fore.LIGHTBLUE_EX}| LC > {Fore.GREEN}Нажмите Enter что бы вернуться в главное меню: {Fore.RESET}")

    Main()

def Light_Clean_All():
    time = get_time()
    with open('log.txt', 'a') as file:
        file.write(f'LC > {time} > Запуск полной очистки. \n')
    
    Light_Clean_Folder_Temp_User()
    Light_Clean_Folder_Temp_Windows()
    Light_Clean_Folder_Cache_User()
    Light_Clean_Folder_mbam_cache()
    Light_Clean_Folder_CrushDumps()
    Light_Clean_Folder_SoftwareDistribution_Download()
    Light_Clean_Folder_Nvidia_GLCache()



     #--------------------------------------------------------------------
#--------------------------------------------------------------------
    print(f"{Fore.LIGHTBLUE_EX}\n \n \n|-")
    print(f"{Fore.LIGHTBLUE_EX}| Light Cleaner > Окончание очистки")
    print(f"{Fore.LIGHTBLUE_EX}|- \n \n \n")
#--------------------------------------------------------------------
    #--------------------------------------------------------------------

    All_free_space_1 = initial_size_Temp_User - final_size_Temp_User
    All_free_space_2 = initial_size_Windows_Temp - final_size_Windows_Temp
    All_free_space_3 = initial_size_Cache_User - final_size_Cache_User
    All_free_space_4 = initial_size_User_Cache_mbam - final_size_User_Cache_mbam
    All_free_space_5 = initial_size_CrashDumps_User - final_size_CrashDumps_User
    All_free_space_6 = initial_size_Windows_Update - final_size_Windows_Update
    All_free_space_7 = initial_size_Nividia_Cache - final_size_Nividia_Cache

    print(f"{Fore.LIGHTBLUE_EX}| LC Stat >{Fore.RESET} Вес папки {Os_UserName_Windows}/Temp до очистки: {Fore.YELLOW}{initial_size_Temp_User:.2f} МБ{Fore.RESET} | Очищено: {Fore.CYAN}{All_free_space_1:.2f}{Fore.RESET} | {Fore.RESET} После: {Fore.GREEN}{final_size_Temp_User:.2f} МБ{Fore.RESET}")
    print(f"{Fore.LIGHTBLUE_EX}| LC Stat >{Fore.RESET} Вес папки C:/Windows/Temp до очистки: {Fore.YELLOW}{initial_size_Windows_Temp:.2f} МБ{Fore.RESET} | Очищено: {Fore.CYAN}{All_free_space_2:.2f}{Fore.RESET} | {Fore.RESET} После: {Fore.GREEN}{final_size_Windows_Temp:.2f} МБ{Fore.RESET}")
    print(f"{Fore.LIGHTBLUE_EX}| LC Stat >{Fore.RESET} Вес папки {Os_UserName_Windows}/cache до очистки: {Fore.YELLOW}{initial_size_Cache_User:.2f} МБ{Fore.RESET} | Очищено: {Fore.CYAN}{All_free_space_3:.2f}{Fore.RESET} | {Fore.RESET} После: {Fore.GREEN}{final_size_Cache_User:.2f} МБ{Fore.RESET}")
    print(f"{Fore.LIGHTBLUE_EX}| LC Stat >{Fore.RESET} Вес папки {Os_UserName_Windows}/mbam/cache/qmlcache до очистки: {Fore.YELLOW}{initial_size_User_Cache_mbam:.2f} МБ{Fore.RESET} | Очищено: {Fore.CYAN}{All_free_space_4:.2f}{Fore.RESET} | {Fore.RESET} После: {Fore.GREEN}{final_size_User_Cache_mbam:.2f} МБ{Fore.RESET}")
    if Confirm_Clean_1 in ["y", "Y", "yes", "Yes", "д", "Д", "да", "Да"]:
        print(f"{Fore.LIGHTBLUE_EX}| LC Stat >{Fore.RESET} Вес папки {Os_UserName_Windows}/CrashDumps до очистки: {Fore.YELLOW}{initial_size_CrashDumps_User:.2f} МБ{Fore.RESET} | Очищено: {Fore.CYAN}{All_free_space_5:.2f}{Fore.RESET} | {Fore.RESET} После: {Fore.GREEN}{final_size_CrashDumps_User:.2f} МБ{Fore.RESET}")
    else:
        print(f"{Fore.LIGHTBLUE_EX}| LC Stat >{Fore.RESET} Вес папки {Os_UserName_Windows}/CrashDumps Не очищено!: {Fore.YELLOW}{initial_size_CrashDumps_User:.2f} МБ{Fore.RESET} {Fore.RESET}")
    print(f"{Fore.LIGHTBLUE_EX}| LC Stat >{Fore.RESET} Вес папки C:/Windows/SoftwareDistribution/Download до очистки: {Fore.YELLOW}{initial_size_Windows_Update:.2f} МБ{Fore.RESET} | Очищено: {Fore.CYAN}{All_free_space_6:.2f}{Fore.RESET} | {Fore.RESET} После: {Fore.GREEN}{final_size_Windows_Update:.2f} МБ{Fore.RESET}")
    print(f"{Fore.LIGHTBLUE_EX}| LC Stat >{Fore.RESET} Вес папки {Os_UserName_Windows}/NVIDIA/GLCache до очистки: {Fore.YELLOW}{initial_size_Nividia_Cache:.2f} МБ{Fore.RESET} | Очищено: {Fore.CYAN}{All_free_space_7:.2f}{Fore.RESET}  | {Fore.RESET} После: {Fore.GREEN}{final_size_Nividia_Cache:.2f} МБ{Fore.RESET}")
    
    
    All_free_space_sum = All_free_space_1 + All_free_space_2 + All_free_space_3 + All_free_space_4 + All_free_space_5 + All_free_space_6 + All_free_space_7
    print(f"{Fore.LIGHTBLUE_EX}| LC Stat >{Fore.RESET} Всего очищено: {Fore.LIGHTGREEN_EX}> {All_free_space_sum:.2f} МБ < ")
    input(f"{Fore.LIGHTBLUE_EX}| LC > {Fore.GREEN}Нажмите Enter что бы вернуться в главное меню: {Fore.RESET}")

    Main()



Main()