import os
import shutil

def file_organizer():
    
    print("welcome to the file organizer")
    print("please enter the path of ther folder you want to organize")
    path = input()
    
    extensions = {
        'audio': ['mp3', 'wav', 'flac', 'm4a'],
        'video': ['mp4', 'mkv', 'flv', 'avi'],
        'documents': ['doc', 'pdf', 'txt', 'docx'],
        'images': ['jpg', 'jpeg', 'png', 'gif'],
        'compressed': ['zip', 'rar', '7z', 'tar'],
        'programs': ['exe', 'msi']
    }
    
    for directory in extensions.keys():
        if not os.path.exists(directory):
            os.mkdir(directory)
    
    for file in os.listdir(path):
        if os.path.isfile(file):
            for folder, extension in extensions:
                if file.split('.')[-1] in extension:
                    shutil.move(file, folder)
                    break
                else:
                    shutil.move(file, 'others')

if __name__ == '__main__':
    file_organizer()
    
        
        