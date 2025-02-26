import os
import re

final_list = []                         # list to capture the phone number
number_file_path = ""

def search(file, pattern = r"\d{3}-\d{3}-\d{4}"):
    
    f = open(file, "r")
    text = f.read()
    
    if re.search(pattern, text):
        global number_file_path
        number_file_path = file
        a = re.search(pattern, text)
        return a.group()
    else:
        return ""


for folder, sub_folders, files in os.walk("F:\\learning python\\advance module exercise\\extracted_content"):
    for f1 in files:
        full_path = folder + "\\" + f1
        final_list.append(search(full_path))

print(final_list)
for x in final_list:
    if x:
        print(x)
        print("Found in file: ", number_file_path)
    else:
        pass