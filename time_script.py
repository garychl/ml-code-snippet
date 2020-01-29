import time

time_start = time.time()
time_model = time.time()
print('Used {} seconds to train/load the model'.format(round(time_model-time_start)))


import timeit

# Example 1
params = {
    'stmt': '"-".join(str(n) for n in range(100))',
    'setup': 'pass',
    'number':10000,     # how many times to run stmt
    'repeat': 5,        # how many times to run timeit
    'globals': globals(),
}

run_times = timeit.repeat(**params)
print(run_times)


# Example 2
params = {
    'stmt': "train(model)",
    'setup': "import torchvision.models as models;" + \
        "model = models.resnet50(num_classes=num_classes).to('cuda:0')",
    'number':1,
    'repeat': 10,
    'globals': globals(),
}

rn_run_times = timeit.repeat(**params)
