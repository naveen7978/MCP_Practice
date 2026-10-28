import asyncio

async def greet():
    print("Hello")

async def main():
    await greet()

asyncio.run(main())