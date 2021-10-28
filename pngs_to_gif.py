import glob
from PIL import Image

def run():
    fp_in = "png_to_gif/*.png"
    fp_out = "png_to_gif/out.gif"

    img, *imgs = [Image.open(f) for f in sorted(glob.glob(fp_in))]
    img.save(fp=fp_out, format='GIF', append_images=imgs,
             save_all=True, duration=200, loop=0)

if __name__ == '__main__':
    run()
