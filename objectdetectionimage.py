# -*- coding: utf-8 -*-
"""objectdetectionimage.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1Edk90duE10XbFQz0zru1iXe5_jKrwF9d
"""

#Install the dependencies we need
!pip install -q numpy
!pip install -q scipy
!pip install -q numpy
!pip install -q opencv-python
!pip install -q pillow
!pip install -q matplotlib
!pip install -q h5py
!pip install -q keras
!pip install -q imageai-2.0.2-py3-none-any.whl

from imageai.Detection import ObjectDetection
import os

execution_path = os.getcwd()

detector = ObjectDetection()
detector.setModelTypeAsRetinaNet()
detector.setModelPath( os.path.join("resnet50_coco_best_v2.0.1.h5"))
detector.loadModel()
detections = detector.detectObjectsFromImage(input_image=os.path.join(execution_path , "soco.jpg"), output_image_path=os.path.join(execution_path , "soco2.jpg"))

for eachObject in detections:
    print(eachObject["name"] , " : " , eachObject["percentage_probability"] )