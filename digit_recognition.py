import cv2
import numpy as np 
import pandas as pd 
import seaborn as sns
import matplotlib.pylot as plt 
from sklearn.datasets import fetch_openml 
from sklearn.model_selection import train_test_split
from sklearn.liner_model import LogisticRegression 
from sklearn.metrics import accuracy_score
from PIL import Image
import PIL.ImageOps
import os,ssl,time

if(not os.environ.get("PYTHONHTTPSVERIFY",'')and 
   getattr(ssl,'_create_unverified_context',None)):
   ssl._create_default_https_context = ssl._create_unverified_contex


X,y = fetch_openml('mnist_784',version= 1,return_X_y = True)
print (pd.Series(y).value_counts())
classes = {'0','1','2','3','4','5','6','7','8','9'}
nclasses = len(classes)