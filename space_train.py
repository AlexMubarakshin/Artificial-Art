import argparse

import numpy as np
import tensorflow as tf
import matplotlib.pyplot as plt

from dcgan import DCGAN, create_dataset

def parse_args():
    parser = argparse.ArgumentParser()
    help_ = "Load h5 model trained weights"
    parser.add_argument("-w", "--weights", help=help_) # TODO

    help_ = "Number of training epochs"
    parser.add_argument("-e", "--epochs", help=help_, default=101, type=int)

    return parser.parse_args()

if __name__ == '__main__':

    # parse arguments
    args = parse_args()
    if args is None:
      exit()

    x_train, y_train = create_dataset(128, 128, nSlices=1000, resize=0.5, directory='Space/Galaxy/') # 3 channels = RGB
    assert(x_train.shape[0]>0)

    x_train /= 255 

    # plot results to make sure data looks good!
    fig, axs = plt.subplots(4, 4)
    for i in range(4):
        for j in range(4):
            axs[i,j].imshow( x_train[ np.random.randint(x_train.shape[0]) ] )
            axs[i,j].axis('off')
    plt.show()
  
    dcgan = DCGAN(img_rows = x_train[0].shape[0],
                    img_cols = x_train[0].shape[1],
                    channels = x_train[0].shape[2], 
                    latent_dim=128,
                    name='space_128_128')
    
    dcgan.load_weights(generator_file="generator (space_128_128).h5", discriminator_file="discriminator (space_128_128).h5")
                    
    dcgan.train(x_train, epochs=args.epochs, batch_size=32, save_interval=100)