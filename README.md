# Illumination using WGIF

This repository features an implementation of the algorithm proposed in ["Low and non-uniform illumination color image enhancement using weighted guided image filtering" by Mu, Q., Wang, X., Wei, Y. et al. (2021)](https://doi.org/10.1007/s41095-021-0232-x)

## Usage

```python
from PIL import Image
import numpy as np
from scipy import ndimage
from math import floor
import math
import os

from illumination_using_wgif import illuminate

image = Image.open("./<YOUR_IMAGE_HERE>")

rgb_image_data = np.reshape(image.getdata(), (image.size[1], image.size[0], 3))
greyscale_image_data = np.reshape(image.convert('L').getdata(), (image.size[1], image.size[0]))

illuminated_image_data_greyscale = illuminate(rgb_image_data)
# or: illuminated_image_data_greyscale = illuminate(greyscale_image_data)
illuminated_image_greyscale = Image.fromarray(illuminated_image_data_greyscale)

illuminated_image_data_color = illuminate(rgb_image_data, True)
illuminated_image_color = Image.fromarray(illuminated_image_data_color)
```

## Results
Illuminated images from the [DARK FACE: Face Detection in Low Light Condition](https://flyywh.github.io/CVPRW2019LowLight/) dataset
![Illuminated images from the DARK FACE dataset](/assets/Illumination-result.png)

## Notes
The color restoration is terribly slow as of now, could be optimized