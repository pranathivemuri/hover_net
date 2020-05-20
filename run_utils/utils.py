import os
import random
import shutil

import numpy as np
import torch
from imgaug import imgaug as ia
from termcolor import colored


####
def check_manual_seed(seed):
    """ 
    If manual seed is not specified, choose a 
    random one and communicate it to the user.

    Args:
        seed: seed to check
    """

    seed = seed or random.randint(1, 10000)
    random.seed(seed)
    np.random.seed(seed)
    torch.manual_seed(seed)
    torch.cuda.manual_seed(seed)
    # ia.random.seed(seed)

    print('Using manual seed: {seed}'.format(seed=seed))
    return


####
def check_log_dir(log_dir):
    """
    Check if log directory exists

    Args:
        log_dir: path to logs
    """

    if os.path.isdir(log_dir):
        colored_word = colored('WARNING', color='red', attrs=['bold', 'blink'])
        print('%s: %s exist!' %
              (colored_word, colored(log_dir, attrs=['underline'])))
        while (True):
            print('Select Action: d (delete) / q (quit)', end='')
            key = input()
            if key == 'd':
                shutil.rmtree(log_dir)
                break
            elif key == 'q':
                exit()
            else:
                color_word = colored('ERR', color='red')
                print('---[%s] Unrecognize Characters!' % colored_word)
    return
