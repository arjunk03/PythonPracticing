from concurrent.futures import ThreadPoolExecutor

import time


def ret_aftr_n_secs(n, message):
    time.sleep(n)
    return message


pool = ThreadPoolExecutor(3)
submitted_job = pool.submit(ret_aftr_n_secs, 1, "Hello")
print(submitted_job.done())
print(submitted_job.result())


num_list = [1, 2, 3, 4]


def cal_square(n):
    return n * n


def executor_func():
    with ThreadPoolExecutor(max_workers=3) as exec:
        results = exec.map(cal_square, num_list)

        return results


square_data = executor_func()
print(list(square_data))
