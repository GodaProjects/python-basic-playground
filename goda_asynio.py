import asyncio


async def find_divisibles(inrange, div_by):
    print("finding nums in range {} divisible by {}".format(inrange, div_by))
    located = []
    for i in range(inrange):
        if i % div_by == 0:
            located.append(i)
        if i % 50000 == 0:
            await asyncio.sleep(0.0001)
    print("Done w/ nums in range {} divisible by {}".format(inrange, div_by))
    return located


async def main():
    divs1 = loop.create_task(find_divisibles(5080000000, 34113))
    divs2 = loop.create_task(find_divisibles(5080000000, 34113))
    divs3 = loop.create_task(find_divisibles(5080000000, 34113))
    divs4 = loop.create_task(find_divisibles(5080000000, 34113))
    divs5 = loop.create_task(find_divisibles(5080000000, 34113))
    divs6 = loop.create_task(find_divisibles(5080000000, 34113))

    # divs2 = loop.create_task(find_divisibles(1000520, 3210))
    # divs3 = loop.create_task(find_divisibles(500000, 3))
    await asyncio.wait([divs1, divs2, divs3])


if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main())
    loop.close()
