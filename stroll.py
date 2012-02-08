import os
import sys

import IPython
from wand.image import METRIC_TYPES
from wand.image import Image

DATA_DIR = 'data'

def get_image_paths():
    return [os.path.join(DATA_DIR, f) for f in os.listdir(DATA_DIR)]


def main():
    image_paths = get_image_paths()
    for i, image_path in enumerate(image_paths):
        if i + 1 == len(image_paths):
            next_image_path = None
        else:
            next_image_path = image_paths[i + 1]

        with Image(filename=image_path) as img:
            if next_image_path:
                with Image(filename=next_image_path) as next_img:
                    comp_img = img.compare(next_img, 'undefined')[0]
                    comp_img.save(filename='compared/%s.jpg' % i)
                    for metric in METRIC_TYPES:
                        distortion = img.compare(next_img, metric)[1]
                        print "%s %s: %s" % (i, metric, distortion)


if __name__ == '__main__':
    main()
