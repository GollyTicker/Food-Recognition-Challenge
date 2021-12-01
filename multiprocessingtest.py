# multiprocessing test

#hide
from pathlib import Path
import os
import json
from multiprocessing import Pool
#from multiprocess import Pool # Attention: We use multiprocess instead of multiprocessing library.
# This works for parallelism on Windows in Jupyter

from tqdm.notebook import tqdm
from pycocotools.coco import COCO
from torch import tensor
import numpy as np
import cv2
import PIL
import platform
import skimage

data = np.random.random((30,10))

def func(xs):
  return xs[:3]

def doStuff(data):
  result = []

  with Pool() as p:
    total_images = len(data)

    with tqdm(total=total_images) as progress_bar:
      for funcres in p.imap(func, data):
        result.append(funcres)
        progress_bar.update(1)

  return result

if __name__ == "__main__":
  result = doStuff(data)
  print(result)
