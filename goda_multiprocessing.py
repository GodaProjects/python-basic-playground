import multiprocessing


def find_divisibles():
    inrange = 5080000000
    div_by = 3411
    print("finding nums in range {} divisible by {}".format(inrange, div_by))
    located = []
    for i in range(inrange):
        if i % div_by == 0:
            located.append(i)
    print("Done w/ nums in range {} divisible by {}".format(inrange, div_by))
#    print(located)


def main():
    divs1 = multiprocessing.Process(target=find_divisibles)
    divs2 = multiprocessing.Process(target=find_divisibles)
    divs3 = multiprocessing.Process(target=find_divisibles)
    divs4 = multiprocessing.Process(target=find_divisibles)
    divs5 = multiprocessing.Process(target=find_divisibles)
    divs6 = multiprocessing.Process(target=find_divisibles)
    divs1.start()
    divs2.start()
    divs3.start()
    divs4.start()
    divs5.start()
    divs6.start()
    divs1.join()
    divs2.join()
    divs3.join()
    divs4.join()
    divs5.join()
    divs6.join()
    # divs1 = target = find_divisibles()
    # divs2 = target = find_divisibles()
    # divs3 = target = find_divisibles()
    # divs3 = target = find_divisibles()
    # divs3 = target = find_divisibles()
    # divs3 = target = find_divisibles()


if __name__ == '__main__':
    main()
