"""Changing to main dir"""

import os

def cd_prj_dir(show=False):
    sub_folder = ['experiments', 'data']
    cur_folder = os.path.basename(os.getcwd())

    if cur_folder in sub_folder:
        os.chdir("../")
        if show: 
            prj_dir = os.getcwd() 
        else:
            prj_dir = 'project dir.'
        print('Changed dir to {}'.format(prj_dir))

    assert 'README.md' in os.listdir(), "Cannot find REAME.md. Make sure current dir is the project dir."    
