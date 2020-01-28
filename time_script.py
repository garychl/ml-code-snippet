import time

time_start = time.time()
time_model = time.time()
print('Used {} seconds to train/load the model'.format(round(time_model-time_start)))
