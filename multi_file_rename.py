import os

def rename_file():

    save_file = os.listdir(r"C:\Users\MD. Nobin\Downloads\prank")
    directory = os.getcwd()
    print(directory)
    os.chdir(r"C:\Users\MD. Nobin\Downloads\prank")

    for img in save_file:
        update = str.maketrans("0123456789","          ")
        os.rename(img, img.translate(update))
    os.chdir(directory)

rename_file()
