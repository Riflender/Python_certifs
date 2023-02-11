from os import cpu_count

MAX_CPU = cpu_count()


@property
def MAX_THREAD():
    return 2 * MAX_CPU


del cpu_count
