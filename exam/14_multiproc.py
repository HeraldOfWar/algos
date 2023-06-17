'''
Модуль asyncio доступен для предоставления базовой реализации цикла событий
'''
import multiprocessing
import timeit


def if_prime(x):
    if x <= 1:
        return 0
    elif x <= 3:
        return x
    elif x % 2 == 0 or x % 3 == 0:
        return 0
    i = 5
    while i**2 <= x:
        if x % i == 0 or x % (i + 2) == 0:
            return 0
        i += 6
    return x


def worker(x):
    name_proc = multiprocessing.current_process().name
    res = x*x
    print(name_proc, res)
    return res


def f(x):
    return x*x


data = range(3, 7)


if __name__ == '__main__':

    with multiprocessing.Pool(5) as p:
        print(p.map(f, [1, 2, 3]))

    with multiprocessing.Pool(5) as pool:
        print('Результаты:')
        print(pool.map(worker, data))

    start = timeit.default_timer()
    with multiprocessing.Pool(2) as p:
        answer = sum(p.map(if_prime, list(range(1000000))))
    end = timeit.default_timer()
    print(end - start)
    print(answer)