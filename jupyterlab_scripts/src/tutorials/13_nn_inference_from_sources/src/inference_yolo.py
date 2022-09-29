import cv2
import json
import numpy as np

import supervisely.supervisely_lib as sly
from supervisely.plugins.nn.yolo_v3.src.inference import YOLOSingleImageApplier as model_applier

settings = {
    "gpu_device": 0,
}

input_img_path = '/my_example/images/00000220.png'
output_img_path = '/my_example/images/00000220_yolo_inference_visualization.jpeg'
output_ann_path = '/my_example/images/00000220_yolo_prediction.json'

applier = model_applier(settings)

# read input image and convert from BGR to RGB colorspace
image = cv2.imread(input_img_path)
image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

# create dummy annotation from image (necessary to know image resolution)
dummy_ann = sly.Annotation.from_img_path(input_img_path)

# methods return object of class sly.Annotation
prediction = applier.inference(image, dummy_ann)

# let's draw annotations on input image and save this visualization
visualization_image = np.zeros(prediction.img_size + (3,), dtype=np.uint8)
prediction.draw_contour(visualization_image, thickness=5)
res_image = cv2.addWeighted(image, 1, visualization_image, 0.95, 0)

res_image = cv2.cvtColor(res_image, cv2.COLOR_RGB2BGR)
cv2.imwrite(output_img_path, res_image)

# save predictions to json file in Supervisely Annotation Format (learn more here https://docs.supervise.ly/ann_format/)
with open(output_ann_path, 'w') as fout:
    json.dump(prediction.to_json(), fout, indent=4)

