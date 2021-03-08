from tqdm import tqdm, tqdm_gui, trange
from time import sleep
"""
for i in tqdm(range(100)):
	sleep(0.01)

for i in tqdm(range(100), desc = "Tables", unit = " tables", unit_scale = 10):
	sleep(0.1)

for i in trange(100, desc = 'DataFrames', bar_format = '{desc} {percentage}%'):
	sleep(0.05)


for i in trange(100, leave = False, mininterval = 0.01, ncols= 150, dynamic_ncols = True):
	sleep(0.05)

for i in tqdm_gui(range(100), desc = 'ProgressBar'):
	sleep(.1)
"""
def ProgressBar	(function = 0):
	for i in tqdm(range(function), desc = "Test", unit = " speed", unit_scale = 10):
		sleep(0.001)

ProgressBar(1000)