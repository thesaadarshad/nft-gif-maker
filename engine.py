import os
from random import randrange
from PIL import Image
import random
import os.path
from os import path
import sys
import urllib

MINIMUM_FOLDERS = 3
INPUT_DIRECTORY = 'input'
OUTPUT_DIRECTORY = 'output'


def make_url(base_url, *res):
    url = base_url
    for r in res:
        url = '{}/{}'.format(url, r)
    return url


def select_folders():
    selected_folders = []
    input_directory = INPUT_DIRECTORY

    if not path.exists(input_directory):
        sys.exit(f'Folder "{input_directory}" doesnt exist')

    sub_folders = [name for name in os.listdir(input_directory) if os.path.isdir(os.path.join(input_directory, name))]
    for folder in sub_folders:
        random_number = round(random.uniform(1, 100))
        if int(folder) >= random_number:
            selected_folders.append(folder)
    return selected_folders


def select_files(selected_folders):
    selected_files = []
    for listing in selected_folders:
        selected_folder_path = make_url(INPUT_DIRECTORY, listing)
        folder_contents = os.listdir(selected_folder_path)
        if len(folder_contents):
            random_index = randrange(len(folder_contents))
            selected_file_path = make_url(selected_folder_path, folder_contents[random_index])
            selected_files.append(selected_file_path)
    return selected_files


def run(no_of_nft=3):
    generated_hashes = []
    i = 0
    j = 0
    while len(generated_hashes) < no_of_nft:
        selected_folders = []
        i += 1

        while len(selected_folders) < MINIMUM_FOLDERS:
            selected_folders = select_folders()

        selected_files = select_files(selected_folders)
        new_hash = hash(str(selected_files))
        if new_hash not in generated_hashes:
            j += 1
            generated_hashes.append(new_hash)
            generate_gif(j, selected_files)
            print(f'NFTs created: {j} in {i} attempts')


def generate_gif(i, selected_files):
    random.shuffle(selected_files)
    img, *imgs = [Image.open(f) for f in selected_files]
    filename = make_url(OUTPUT_DIRECTORY, str(i) + '_output.gif')
    img.save(fp=filename, format='GIF', append_images=imgs, save_all=True, duration=20, loop=0)


if __name__ == '__main__':
    run(no_of_nft=10)
