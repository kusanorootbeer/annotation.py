import pandas as pd
import numpy as np
import os
from glob import glob
from PIL import Image
import matplotlib.pyplot as plt

import pdb


def main():
    # ここは各自でよしなにやってください
    data_dir_path = "{}/Desktop/N2C2_DataSet/*.jpg".format(
        os.environ['HOME'])

    # ここも各自でよしなに
    csv_path = "{}/Desktop/N2C2_DataSet/emo_received.csv".format(
        os.environ['HOME'])

    data_path_list = np.array(sorted(glob(data_dir_path)))
    if os.path.exists(csv_path):
        df = pd.read_csv(csv_path)
    else:
        labels = np.array(["None"]*len(data_path_list))
        arr = np.vstack([data_path_list, labels]).T
        df = pd.DataFrame(arr, columns=["x:image", "y:label"])
        df.to_csv(csv_path, index=False)

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
