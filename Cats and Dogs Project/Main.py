import os
import random
import io
from PIL import Image

'''
Eduardo Herrera
CS2303
Professor Aguirre
Date: 09/12/2018
Going to make a folder for the dogs and another folder for the cats pictures. Then
we are going to traverse the directories through recusion and get all the dog and cat pictures. Finally,
all the pictures are going to be moved to the corresponding folder.
'''

#Going to get the files and directories names of all the files
def get_dirs_and_files(path):
    dir_list = [directory for directory in os.listdir(path) if os.path.isdir(path + '/' + directory)]
    file_list = [directory for directory in os.listdir(path) if not os.path.isdir(path + '/' + directory)]

    return dir_list, file_list

#Going to classify the picture is they are a cat or a dog
def classify_pic(path):
    # To be implemented by Diego: Replace with ML model
    if "dog" in path:
        return 0.5 + random.random() / 2

    return random.random() / 2

#Going to go trough the directories and move the pics to the corresponding folder
def process_dir(path):

    dir_list, file_list = get_dirs_and_files(path)
    
    cat_list = []
    dog_list = []

    #Base case is going to be when there is no more directories to go into.
    if not dir_list:
        #Iterate through the pictures
        for pic in file_list:
            if "jpg" in pic:
                #print("Last run, pic: ", pic)
                pic_path = os.path.abspath(pic)
                num = classify_pic(pic_path)

                #Investigate if the picture is a Dog or a Cat
                if num < .5:
                    cat_list.append((os.rename(pic_path, os.path.join(cat_folder, pic))), os.path.getmtime(pic_path))
                else:
                     dog_list.append((os.rename(pic_path, os.path.join(dog_folder, pic))), os.path.getmtime(pic_path))

        #We are going to return to the previous directory.
        parent_path = os.path.dirname(os.getcwd())
        os.chdir(parent_path)
        
        return cat_list, dog_list
    else:
        #Iterate through the pictures
        for pic in file_list:
            if "jpg" in pic:
                pic_path = os.path.abspath(pic)
                num = classify_pic(pic_path)
                #Investigate if the picture is a Dog or a Cat
                if num < .5:
                    cat_list.append((os.rename(pic_path, os.path.join(cat_folder, pic))), os.path.getmtime(pic_path))
                else:
                     dog_list.append((os.rename(pic_path, os.path.join(dog_folder, pic))), os.path.getmtime(pic_path))
        
        #Iterate through the Directories through recursion
        for dir in dir_list:
            next_path = os.path.abspath(dir)
            os.chdir(next_path)
            temp0, temp1 = process_dir(next_path)
            cat_list.extend(temp0)
            dog_list.extend(temp1)
        
        #We are going to return to the previous directory
        os.chdir(os.path.dirname(os.getcwd()))
    return cat_list, dog_list

def main():
    global main_path
    global dog_folder
    global cat_folder

    main_path = os.getcwd()
    path = os.path.join(os.getcwd(), "Pictures")
    
    dog_folder = os.path.join(os.getcwd(), "Dog")
    cat_folder = os.path.join(os.getcwd(), "Cat")
    
    if not os.path.exists(dog_folder) and not os.path.exists(cat_folder):
        os.makedirs(dog_folder)
        os.makedirs(cat_folder)
    
    os.chdir(path)
    
    print(path)
    cats, dogs = process_dir(path)

main()
