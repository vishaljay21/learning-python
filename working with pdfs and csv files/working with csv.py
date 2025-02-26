import csv

"""
data_file = open("F:\\learning python\\working with pdfs and csv files\\to_save_file.csv", "w", newline="")

csv_writer = csv.writer(data_file, delimiter=",")

csv_writer.writerow(["a", "b", "c"])

csv_writer.writerows((["1", "2", "3"], ["4", "5", "6"]))

data_file.close()

"""

file = open("F:\\learning python\\working with pdfs and csv files\\to_save_file.csv", "a", newline="")

new_csv_writer = csv.writer(file)

new_csv_writer.writerows((["new", "new", "new"], ["file", "file", "file"]))

file.close()
