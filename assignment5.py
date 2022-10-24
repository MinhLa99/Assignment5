import re

def quicksort(numbers_in_a_list):
    '''
    Reference: 
        (https://stackoverflow.com/questions/20175380/quick-sort-python-recursion) 
    '''
    if len(numbers_in_a_list) <= 1:
        return numbers_in_a_list
    else:
        pivot = numbers_in_a_list[0]
        small = []
        big = []
        for i in range(1,len(numbers_in_a_list)):
            if numbers_in_a_list[i] < pivot:
                small.append(numbers_in_a_list[i])
            if numbers_in_a_list[i] > pivot:
                big.append(numbers_in_a_list[i])
        return quicksort(small) + [pivot] + quicksort(big)


    
def read(fileinput):
    list_number = []
    with open(fileinput) as file_object:
        line = file_object.readline()
        number = re.findall("[0-9]+", line)
        for x in number:
            x = int(x)
            list_number.append(x)
    return list_number



def write(fileoutput, number):
    with open(fileoutput, "w") as sorted_output:
        for x in quicksort(number):
            x = str(x)
            sorted_output.write(f"{x}\n")
            
            
def main():
    number = read("numbers.txt")
    return write("sorted.txt", number)


if __name__ == "__main__":
    main()
