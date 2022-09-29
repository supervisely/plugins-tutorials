# coding: utf-8

import supervisely_lib as sly

from supervisely_lib.nn.hosted.pytorch.trainer import PytorchSegmentationTrainer

from model import model_factory_fn

from torch.nn.modules.loss import CrossEntropyLoss


def main():
    trainer = PytorchSegmentationTrainer(
        model_factory_fn=model_factory_fn,
        optimization_loss_fn=CrossEntropyLoss()
    )
    trainer.train()


if __name__ == '__main__':
    sly.main_wrapper('UNET_V2_TRAIN', main)
