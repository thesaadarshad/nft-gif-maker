
import os
from random import randrange
from PIL import Image
import random
import uuid

def select_folders():

    selected_folders = []
    folderName = 'input'
    sub_folders = [name for name in os.listdir(folderName) if os.path.isdir(os.path.join(folderName, name))]
    for folder in sub_folders:

        random_number = round(random.uniform(1, 100))
        if int(folder) >= random_number:
            selected_folders.append(folder)
    return selected_folders

def select_files(selected_folders):
    selected_files = []
    for listing in selected_folders:
        selected_folder_path = f'input/{listing}/'
        folder_contents = os.listdir(selected_folder_path)
        if len(folder_contents):
            random_index = randrange(len(folder_contents))
            file_name_complete = selected_folder_path+ folder_contents[random_index]
            selected_files.append(file_name_complete)
    return selected_files

def run(no_of_nft=3):

    generated_hashes = []
    i = 0
    while len(generated_hashes) < no_of_nft:
        i += 1
        ensure_minimum = 3
        selected_folders = []

        while len(selected_folders) < ensure_minimum:
            selected_folders = select_folders()

        selected_files = select_files(selected_folders)
        new_hash = hash(str(selected_files))
        if new_hash not in generated_hashes:
            generated_hashes.append(new_hash)
            generate_gif(i, selected_files)
            print(f'NFTs created: {i}')

def generate_filename(filename):

    return uuid.uuid4()


def generate_gif(i, selected_files):
    random.shuffle(selected_files)
    img, *imgs = [Image.open(f) for f in selected_files]
    filename = 'output/' + str(i) + 'output.gif'
    img.save(fp=filename, format='GIF', append_images=imgs, save_all=True, duration=20, loop=0)


if __name__ == '__main__':
    run(no_of_nft=10)