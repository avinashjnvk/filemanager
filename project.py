import os, shutil
dict_extension={
    'audio_extension': ('.mp3','.wav','.m4a'),
    'document_extension':('.doc','.pdf','.txt'),
    'video_extension':('.mp4','.MKV','.mkv','.flv','.mpeg')

}

filepath=input('enter r path: ')

def searcher(file_path,extension):
    files=[]
    for file in os.listdir(file_path):
        for name in extension:
            if file.endswith(name):
                files.append(file)
    return files

for key,value in dict_extension.items():
    filename=key.split('_')[0] + ' files'
    folder_path=os.path.join(filepath,filename)
    os.mkdir(folder_path)
    for item in (searcher(filepath,value)):
        item_path = os.path.join(filepath,item)
        item_newpath=os.path.join(folder_path,item)
        shutil.move(item_path,item_newpath)


