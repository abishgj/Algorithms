import math
from collections import OrderedDict


def schedule_jobs(resource_dict: dict):
    new_dict = OrderedDict()
    min_res = min(resource_dict.values())
    for x, v in resource_dict.items():
        new_dict[x] = int(math.floor(resource_dict[x] / min_res))

    for k, v in new_dict.items():
        for _ in range(v):
            print(k)  # Serving the resource k
            resource_dict[k] -= 1
            if resource_dict[k] == 0:
                new_dict[k] = 0
                break
