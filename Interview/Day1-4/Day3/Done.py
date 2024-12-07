import asyncio

async def square_number(number):
    await asyncio.sleep(2)
    print(f"Square of Number {number} == {number*number} \n")

async def main(number):
    numbers = range(number)
    tasks = [ square_number(number) for number in numbers]
    await  asyncio.gather(*tasks)


if __name__ == "__main__":
    asyncio.run(main(10))






