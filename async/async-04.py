import time
import asyncio

async def find_users_async(n):
    for i in range(1, n+1):
        print(f'{n}명중 {i}')
        await asyncio.sleep(1)

    print('done: ',n)

async def process_async():
    start = time.time()

    await asyncio.wait([
        find_users_async(2),
        find_users_async(3),
        find_users_async(1),
    ])
    end = time.time()
    print(end-start)


if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    loop.run_until_complete(process_async())
    # process_async()


# https://www.daleseo.com/python-asyncio/