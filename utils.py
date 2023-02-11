from os import cpu_count

MAX_CPU = cpu_count()


def MAX_THREAD():
    return 2 * MAX_CPU

