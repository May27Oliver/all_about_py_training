
import time
from typing import Callable


def timer(func: Callable[[int], None]) -> Callable[[int], None]:
    def wrap(sleep_time):
        time_start = time.time()
        func(sleep_time)
        time_end = time.time()
        total_time = time_end - time_start
        print("花費：", total_time)
    return wrap


@timer
def do_something(sleep_time: int):
    print("do something")
    time.sleep(sleep_time)


# foo = timer(do_something)
# foo(3)
do_something(3)
