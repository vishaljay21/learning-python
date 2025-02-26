import shutil

shutil.unpack_archive("F:\\learning python\\advance module exercise\\unzip_me_for_instructions.zip", "F:\\learning python\\advance module exercise", "zip")

f1 = open("F:\\learning python\\advance module exercise\\extracted_content\\Instructions.txt", "r+")
print(f1.read())
f1.close()