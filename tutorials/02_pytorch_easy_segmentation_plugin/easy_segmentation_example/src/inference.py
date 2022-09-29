# coding: utf-8

# Supervisely imports.
import supervisely_lib as sly
from supervisely_lib.nn.hosted.inference_batch import BatchInferenceApplier
from supervisely_lib.nn.hosted.inference_modes import InfModeFullImage
from supervisely_lib.nn.hosted.pytorch.inference_applier import PytorchSegmentationApplier

# Local imports.
from model import model_factory_fn


def main():
    # Bring up the model for inference (process class mapping configs; load model weights to the GPU).
    single_image_applier = PytorchSegmentationApplier(model_factory_fn=model_factory_fn)
    # By default simply use the full image as model input. Other inference modes are possible, see
    # supervisely_lib/nn/hosted/inference_modes.py
    default_inference_mode_config = InfModeFullImage.make_default_config(
        model_result_suffix='_pytorch_segm_example')
    # IO wrapper to read inputs and save results in supervisely format within the context of a supervisely
    # agent task.
    dataset_applier = BatchInferenceApplier(single_image_inference=single_image_applier,
                                            default_inference_mode_config=default_inference_mode_config)
    # Process the input images and write out results.
    dataset_applier.run_inference()


if __name__ == '__main__':
    sly.main_wrapper('PYTORCH_SEGMENTATION_INFERENCE', main)
