# CIFAR-10-images

---

CIFAR-10 images

You can just clone this repository to use dataset. (like for [timm (pytorch-image-models)](https://github.com/rwightman/pytorch-image-models))

[issue #2](https://github.com/YoongiKim/CIFAR-10-images/issues/2) mentioned the artifacts by jpeg compression, therefore we present a way for generating different image file extensions.

Or you prefer to generate your own image dataset, feel free to modify `torch_get_pic.py`. For example, if you want to generate resized images, you can add `transform` to CIFAR10 dataset with torchvision.

To generate images with `get_pic.sh`, dependencies like `torch` `torchvision` `tqdm` should be satisfied.

---

### Usage

```shell
sudo chmod +x ./get_pic.sh
./get_pic.sh <1> <2> <optional: 3>
```

- <1>: path to your cifar-10 dataset
- <2>: image file extension: like `png` (no dot)
- <3>: optional: if you prefer to generate class labels in digits, then set 1 here

The script will make folders if no available output directory found.
