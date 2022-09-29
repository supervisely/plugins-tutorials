DOCKER_IMAGE='supervisely/nn-unet-v2:latest'

HOST_PATH_TO_SLY_REPO='/home/max/supervisely'
HOST_TUTORIAL_DIRECTORY=${HOST_PATH_TO_SLY_REPO}'/help/jupyterlab_scripts/src/tutorials/13_nn_inference_from_sources'
HOST_MODEL_DIR=${HOST_TUTORIAL_DIRECTORY}'/data/model_unet_lemon'  
HOST_PATH_INFERENCE_SCRIPT=${HOST_TUTORIAL_DIRECTORY}'/src/inference_unet.py'
HOST_PATH_TO_IMAGES=${HOST_TUTORIAL_DIRECTORY}/data/images



docker pull ${DOCKER_IMAGE} && \

nvidia-docker run --rm -it \
	-v ${HOST_PATH_TO_SLY_REPO}:/my_example/supervisely \
	-v ${HOST_MODEL_DIR}:/sly_task_data/model \
	-v ${HOST_PATH_TO_IMAGES}:/my_example/images \
	-v ${HOST_PATH_INFERENCE_SCRIPT}:/my_example/inference.py \
	-w "/my_example" \
	${DOCKER_IMAGE} python /my_example/inference.py