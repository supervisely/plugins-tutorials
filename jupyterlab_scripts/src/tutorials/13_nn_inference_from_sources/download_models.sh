# download and unpack YOLO model

wget -O ./data/model_yolo_coco/model.tar https://cloud.deepsystems.io/s/qBgkcIQUds0Fuws/download && \
tar -C ./data/model_yolo_coco/ -xvf ./data/model_yolo_coco/model.tar && \
rm ./data/model_yolo_coco/model.tar


# download and unpack UNet model

wget -O ./data/model_unet_lemon/model.tar https://cloud.deepsystems.io/s/pun79EulJls09M3/download && \
tar -C ./data/model_unet_lemon/ -xvf ./data/model_unet_lemon/model.tar && \
rm ./data/model_unet_lemon/model.tar


# download and unpack Mask-RCNN model

wget -O ./data/model_mask_rcnn_coco/model.tar https://cloud.deepsystems.io/s/F5VjtCoWwZtE7HP/download && \
tar -C ./data/model_mask_rcnn_coco/ -xvf ./data/model_mask_rcnn_coco/model.tar && \
rm ./data/model_mask_rcnn_coco/model.tar

