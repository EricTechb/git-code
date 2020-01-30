def main(needle):
    with open("data_nums_1000000.txt", "r") as file:
        numbers = map(int, file.read().splitlines())
        #for i in range(len(numbers)):
        #   numbers[i] = int(numbers[i])

        for idex,n in enumerate(numbers):
            if n == needle:
                return idex
                
print(main(12345))