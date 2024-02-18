from tqdm import tqdm

# 1.
# import time
# for i in tqdm(range(100)):
#     time.sleep(1)

# 2.
# for i in tqdm(range(int(9e6))):
#     pass

# 3.
from tqdm import trange
for i in trange(100, desc='info about waiting:', unit='my_unit'):
    pass
