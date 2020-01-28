
ip = get_ipython()
if ip.has_trait('kernel'):
    !jupyter nbconvert --to script Doc2vec.ipynb

    