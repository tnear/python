# asyncio — Asynchronous I/O
# asyncio allows writing concurrent code using async/await keywords
# async I/O is single-threaded and single-process
# asyncio, as its name implies, works better for i/o-bound tasks
# https://docs.python.org/3/library/asyncio.html

import asyncio

async def coroutine():
    # a coroutine in Python is a specialized generator function used in asyncio
    # coroutines are created with 'async'
    # note: @asyncio.coroutine is deprecated in favor of async/await
    pass

async def count():
    print('One')
    # do work (sleep is a placeholder)
    # asyncio.sleep is not a blocking call like time.sleep

    # 'await' passes control back to the event loop when used inside an 'async' function
    # the call to the right of 'await' must be awaitable
    await asyncio.sleep(.01)

    print('Two')

async def gather():
    # Output: One, One, Two, Two
    # the first call to count() suspends execution, allowing
    # the 2nd call to start before the first finishes.
    await asyncio.gather(count(), count())

def main():
    coroutine()
    asyncio.run(gather())

if __name__ == '__main__':
    main()
    print('Tests passed!')
