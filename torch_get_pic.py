"""
    convert CIFAR_10 RAW Data to CIFAR_10 img (png)
"""

import os
from sys import argv
from tqdm import tqdm
from torchvision.datasets import CIFAR10

class_names = ('airplane', 'automobile', 'bird', 'cat', 'deer', 'dog', 'frog', 'horse', 'ship', 'truck')

def CIFAR10Images(train, path, transform = None):
    download = (len(os.listdir(path)) == 0)
    return CIFAR10(path, train = train, download = download, transform = transform)

if __name__ == "__main__":
    extension = 'png'
    use_class_name = True
    path_to_dataset = argv[1]
    extension = argv[2]
    if len(argv) >= 4:
        use_class_name = False
    train_set = CIFAR10Images(True, path_to_dataset)
    test_set = CIFAR10Images(False, path_to_dataset)
    train_folder_cnt = [1 for _ in range(10)]
    test_folder_cnt = [1 for _ in range(10)]
    train_len, test_len = len(train_set), len(test_set)
    for i in tqdm(range(train_len), desc='Processing'):
        px, py = train_set[i]
        pic_cnt = train_folder_cnt[py]
        if use_class_name:
            save_path = "./%s/train/%s/%04d.%s"%(extension, class_names[py], pic_cnt, extension)
        else:
            save_path = "./%s/train/%d/%04d.%s"%(extension, py, pic_cnt, extension)
        px.save(save_path)
        train_folder_cnt[py] += 1
    for i in tqdm(range(test_len), desc='Processing'):
        px, py = test_set[i]
        pic_cnt = test_folder_cnt[py]
        if use_class_name:
            save_path = "./%s/test/%s/%04d.%s"%(extension, class_names[py], pic_cnt, extension)
        else:
            save_path = "./%s/test/%d/%04d.%s"%(extension, py, pic_cnt, extension)
        px.save(save_path)
        test_folder_cnt[py] += 1
    print("Train counter sum: %d, test counter sum: %d"%(sum(train_folder_cnt), sum(test_folder_cnt)))