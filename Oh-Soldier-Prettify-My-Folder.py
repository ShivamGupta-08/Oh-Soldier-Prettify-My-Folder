import os


def File_Reader(file_read):
    with open(file_read) as e:
        read = e.read()
        s = read.split("\n")
        return s


def Folder_Prettifer(path, file, format):
    """This function prettify your folder by -
    1 - Capitalizing the first letter of the files not folder expect the file names you have entered in the dictionary file.
    2 - Renaming the files by whole numbers of particular format you have entered. """
    os.chdir(path)
    s = File_Reader(file)
    list = os.listdir(path)
    list_of_files = [ele for ele in list if os.path.isfile(ele) if ele != file]
    for ele in s:
        list_of_files.remove(ele)
    for count, filename in enumerate(list_of_files):
        dst = filename.capitalize()
        src = path + "/" + filename
        dst = path + "/" + dst
        os.rename(src, dst)
    list_of_files_format = [ele for ele in list if os.path.isfile(ele) if ele != file if ele.endswith(format)]
    for count, filename in enumerate(list_of_files_format):
        dst = str(count)+"."+format
        src = path + "/" + filename
        dst = path + "/" + dst
        os.rename(src, dst)
    print("Your folder is now prettify")


if __name__ == '__main__':
    print("WELCOME TO "" Oh Soldier Prettify My Folder """)
    print("Enter the path of your folder:")
    folder = input()
    print("Enter the name of your dictionary file:")
    Dictionary_file = input()
    print("Enter the file format (without ""."") you want to name them in numerically order: ")
    exe = input()
    #input your folder path , Dictionary file and the format like this
    Folder_Prettifer(folder,Dictionary_file, exe)
