lst = [2,5,3,1,4,7,6]
lst.sort(reverse=True)
print(lst)
def average_of_evens(lst):
    evens = []
    for num in lst:
        if num % 2 == 0:
            evens.append(num)
    if len(evens) == 0:
        return 0
    return sum(evens) / len(evens)
print("Average of even numbers is: ", average_of_evens(lst))