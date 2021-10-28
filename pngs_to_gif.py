import glob
from PIL import Image
import sys
from os import path

def run(folder):

    fp_in = f"{folder}/*.png"
    fp_out = f"{folder}/out.gif"

    if not path.exists(folder):
        sys.exit(f'Folder "{folder}" doesnt exist. please create folder first')

    if not len(glob.glob(fp_in)):
        sys.exit(f'Provided folder "{folder}" is empty')

    img, *imgs = [Image.open(f) for f in sorted(glob.glob(fp_in))]
    img.save(fp=fp_out, format='GIF', append_images=imgs,
             save_all=True, duration=200, loop=0)

if __name__ == '__main__':
    run('png_to_gif')
