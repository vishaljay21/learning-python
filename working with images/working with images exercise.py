from PIL import Image

word_matrix = Image.open("D:\\programming\\learning python\\working with images\\word_matrix.png")
original_mask = Image.open("D:\\programming\\learning python\\working with images\\mask.png")

#print(word_matrix.size)
#print(original_mask.size)

resized_mask = original_mask.resize((1015,559))
#print(resized_mask.size)

resized_mask.putalpha(128)

word_matrix.paste(resized_mask, resized_mask)

#word_matrix.show()

word_matrix.save("D:\\programming\\learning python\\working with images\\solution.png")