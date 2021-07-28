import asyncio

async def do_sync():
    print('here')

# 비동기 = 코루틴

async def main_async():
    print('there')
    await do_sync()


loop = asyncio.get_event_loop()
loop.run_until_complete(main_async())
loop.close()


#https://www.daleseo.com/python-asyncio/