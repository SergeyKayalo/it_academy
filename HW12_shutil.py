import shutil
import os
import stat

print("Создание файла settings.ini")
with open('settings.ini', 'w', encoding='utf-8') as f:
    f.write('[settings]\ntest=1')

#1
print("1. Копирование файла settings.ini -> settings_backup.ini")
shutil.copy("settings.ini","settings_backup.ini")


#2
dir0 = "logs_backup"
print("2. Копирование файла settings.ini -> " + dir0 + "\\")
if not os.path.exists(dir0):
    os.mkdir(dir0)
    shutil.copy("settings.ini", dir0 + "\\")

#3
dir0 = "project_backup"
print ("3. Рекурсивное копирование проекта ..\\it_academy в ", dir0)
shutil.copytree("..\\it_academy", dir0, dirs_exist_ok=True)

#4
print("4. Переименование settings.ini -> settings_old.ini")
shutil.move("settings.ini", "settings_old.ini")

#5
source = "project_backup"
dest = source + "\\archive"
print(f"5. Перемещение {source} в {dest}")
if not os.path.exists(dest):
    os.makedirs(dest)
for name in os.listdir(source):
    src_path = source + "\\" + name
    dst_path = dest + "\\" + name
    print(f"{name}: {src_path} -> {dst_path}")
    if name != "archive": shutil.move(src_path, dst_path)

#6
def _remove_readonly(func, path, exc_info):
    """Снимает флаг 'только для чтения' и повторяет операцию."""
    os.chmod(path, stat.S_IWRITE)
    func(path)

def clean_build(rem_dir):
    if os.path.exists(rem_dir):
        shutil.rmtree(rem_dir, onexc=_remove_readonly)

dir0 = "project_backup"
print ("6.Удаление директории ", dir0)
clean_build(dir0)

#7
print("7. Создание архива logs_backup")
shutil.make_archive("logs_backup", "zip", "logs_backup")

#8
print("8. Распаковка архива logs_backup -> logs_backup_unziped")
shutil.unpack_archive("logs_backup.zip", "logs_backup_unziped")







