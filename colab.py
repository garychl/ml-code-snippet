import sys
import os

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