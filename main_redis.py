import redis
from redis_lru import RedisLRU
import timeit

client = redis.StrictRedis(host="localhost", port=6379, password=None)
cache = RedisLRU(client)


def factor(m: int):
    if m == 1:
        return 1
    else:
        return m * factor(m - 1)


@cache
def factor_cache(m: int):
    if m == 1:
        return 1
    else:
        return m * factor_cache(m - 1)


if __name__ == '__main__':
    start_time = timeit.default_timer()
    #factor(50)
    print(factor(700))
    print(f'Duration: {timeit.default_timer() - start_time}')

    start_time = timeit.default_timer()
    print(factor_cache(700))
    print(f'Duration: {timeit.default_timer() - start_time}')
