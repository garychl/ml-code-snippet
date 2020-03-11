import sys
import os

######################### Switching between local and colab #########################
if sys.platform == 'darwin':
    print('Using Mac locally')
    base_dir = os.getcwd()
    data_dir = './data'
    
elif sys.platform == 'linux' and os.getcwd() == '/content':
    print('Using colab')
    from google.colab import drive
    drive.mount('/content/gdrive', force_remount=True)
    root_dir = "/content/gdrive/My Drive/"
    base_dir = root_dir
    data_dir = './data'
else:
    raise "System platform is not recognized."

######################### prevent colab from disconnect######################### 
# function ClickConnect(){
# console.log("Working"); 
# document.querySelector("colab-toolbar-button#connect").click() 
# }
# setInterval(ClickConnect,60000)


######################### Using TPU ######################### 

############## Run below to install
# VERSION = "20200220"  #@param ["20200220","nightly", "xrt==1.15.0"]
# !curl https://raw.githubusercontent.com/pytorch/xla/master/contrib/scripts/env-setup.py -o pytorch-xla-env-setup.py
# !python pytorch-xla-env-setup.py --version $VERSION

