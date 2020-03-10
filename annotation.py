import pdb
import pandas as pd
import numpy as np
import os
from glob import glob
from PIL import Image
import matplotlib.pyplot as plt
import cv2

'''

'''


def main():
    # ここは各自でよしなにやってください
    data_dir_path = "{}/Desktop/N2C2_DataSet/*.jpg".format(
        os.environ['HOME'])

    # ここも各自でよしなに
    csv_path = "{}/Desktop/N2C2_DataSet/f_test.csv".format(
        os.environ['HOME'])

    face_cascade_path = '/usr/local/opt/opencv/share/OpenCV/haarcascades/haarcascade_frontalface_alt.xml'
    face_cascade = cv2.CascadeClassifier(face_cascade_path)

    data_path_list = np.array(sorted(glob(data_dir_path)))
    if os.path.exists(csv_path):
        df = pd.read_csv(csv_path)
    else:
        labels = np.array(["None"]*len(data_path_list))
        arr = np.vstack([data_path_list, labels]).T
        df = pd.DataFrame(arr, columns=["x:image", "y:label"])
        df.to_csv(csv_path, index=False)

        for index, row in df.iterrows():
            img = cv2.imread(row['x:image'])
            im_gray = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)
            faces = face_cascade.detectMultiScale(im_gray)
            if len(faces) > 0:
                pass
            else:
                df.at[index, 'y:label'] = 0
            df.to_csv(csv_path, index=False)
    pdb.set_trace()

    # labelがついてない状態ではNoneラベルがついています
    for index, row in df.iterrows():
        if row['y:label'] != "None":
            continue
        else:
            while True:
                im = Image.open(row['x:image'])
                plt.imshow(np.asarray(im))
                plt.axis('off')
                plt.pause(.1)
                inp = input('This image is labeled as : ')
                if inp != None:
                    df.at[index, 'y:label'] = inp
                    df.to_csv(csv_path, index=False)
                    break


if __name__ == "__main__":
    main()
