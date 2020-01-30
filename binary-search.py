def main(needle):
    with open("data_nums_1000000.txt", "r") as file:
        numbers = list(map(int, file.read().splitlines()))
        numbers.sort()

        left_index = 0
        right_index = len(numbers)
                
        while True:
            middle_index = (right_index - left_index) // 2 + left_index
            if numbers[middle_index] > needle:
                right_index = middle_index
            elif numbers[middle_index] < needle:
                left_index = middle_index
            elif middle_index == None:
                    print("Doesn't exist")
            else:
                return middle_index
                

print(main(6666666))