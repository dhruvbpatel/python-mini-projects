import os

# function to create folder if it already doesn't exists
def createIfNotExists(folder):
    if not os.path.exists(folder):
        os.mkdir(folder)

# function to move files in respective folders
def moveFiles(folder_name, files):
    count = 0
    for file in files:
        os.replace(file, f"{folder_name}/{file}") # place file in /folder_name
        count+=1
    return count

if __name__ == "__main__":

    files = os.listdir()  # lists all files in current folder
    

    # Add folder names here that are to be created
    dir_names = ['Images', 'Docs', 'Media', "Others"]

    # create folders if it already doesn't exists
    for dir in dir_names:
        createIfNotExists(dir)

    # extensions for classification
    img_exts = [".png", ".jpg", ".jpeg"]
    docs_exts = [".txt", ".xlxs", ".docx", ".pdf", ".doc", ".md"]
    media_exts = [".mkv", ".mp4", ".avi", ".mp3",".MP4"]

    # get list of files for each category by extension name
    # add new category here if you have added folder
    images = [file for file in files if os.path.splitext(file)[1].lower() in img_exts]
    docs = [file for file in files if os.path.splitext(file)[1].lower() in docs_exts]
    medias = [file for file in files if os.path.splitext(file)[1].lower() in media_exts]
    others = []

    # dictionary for key_value pair of folder_name and files
    # If you add new folder then add value here
    folder_file_dict = {
        "Images":images,
        "Docs":docs,
        "Media":medias,
        "Others":others
    }


    
    ## for other files which doesn't fall into any of the above categories
    for file in files:
        ext = os.path.splitext(file)[1].lower()
        if (ext not in media_exts) and (ext not in docs_exts) and (ext not in img_exts) and os.path.isfile(file):
            
            if file == "main.py":
                continue
            else:
                others.append(file)



    # move files to corresponding folders
    move_count = 0
    for index,key in enumerate(folder_file_dict):
        move_count += moveFiles(key, folder_file_dict[key])

    print("====================")
    print(f'successfully moved {move_count} files into {len(folder_file_dict)} folders')
    print("====================")

    
