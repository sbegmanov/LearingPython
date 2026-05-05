import time, asyncio

def now():
    return time.strftime('[%H:%M:%S]') # Local time, as hour:minute:second

def producer(label):
    time.sleep(2) # Pause for two seconds: blocking
    return f'All done, {label}, {now()}' # And return a result

def main():
    print('Start =>', now())
    print(producer(f'serial task 1')) # Run three steps in sequence
    print(producer(f'serial task 2')) # Waiting for each one to finish
    print(producer(f'serial task 3')) # Before doing anything else
    print('Stop =>', now())

main()

# using await
async def producer1(label):              # await requires async
    await asyncio.sleep(2)               # Call nonblocking/awaitable sleep
    return f'All done, {label}, {now()}' # Result of await expression

async def main():
    print('Start =>', now())
    task1 = asyncio.create_task(producer1(f'async task 1'))
    task2 = asyncio.create_task(producer1(f'async task 2'))
    task3 = asyncio.create_task(producer1(f'async task 3'))
    print(await task1)
    print(await task2)
    print(await task3)  # Wait for tasks to finish
    print('Stop =>', now())

asyncio.run(main())  # Start event-loop schedule

# using loops
async def producer2(label):
    await asyncio.sleep(2)
    return f'All done, {label}, {now()}'

async def main():
    print('Start =>', now())
    tasks = []
    for i in range(3):
        tasks.append(asyncio.create_task(producer2(f'async task {i+1}')))
        for task in tasks:
            print(await task)
            print('Stop at', now())

asyncio.run(main())

# How not to use async functions
async def main():
    print(producer('xxx'))
main()
# Result
# …/all_async_blunders.py:12: RuntimeWarning: coroutine 'main' was never awaited

async def main():
    print(producer('xxx'))
asyncio.run(main())
# Result…
# <coroutine object producer at 0x10142e740>  …/all_async_blunders.py:22: RuntimeWarning: coroutine 'producer' was never awaited

async def main():
    print('Start =>', now())
    print(await producer('xxx'))
    print(await producer('yyy'))
    print('Stop =>', now())
asyncio.run(main())
# Result…
# Start => [18:41:56]
# All done, xxx, [18:41:58]
# All done, yyy, [18:42:00]
# Stop => [18:42:00]

async def main():
    print('Start =>', now())
    p1 = producer('xxx')
    p2 = producer('yyy')
    print('Await =>', now())
    print(await p1)
    print(await p2)
    print('Stop =>', now())
asyncio.run(main())
# Result…
# Start => [18:42:00]
# Await => [18:42:00]
# All done, xxx, [18:42:02]
# All done, yyy, [18:42:04]
# Stop => [18:42:04]
