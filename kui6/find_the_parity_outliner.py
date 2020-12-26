# Done, need to refactoring"""

list_integers1 = [2, 4, 0, 100, 4, 11, 2602, 36]
list_integers2 = [2, 4, 6, 8, 10, 3]
list_integers3 = [160, 3, 1719, 19, 11, 13, -21]

def find_outlier(integers):
    odd_numbers = []
    even_numbers = []
    for integer in integers:
        if integer % 2 == 0:
            even_numbers.append(integer)
        else:
            odd_numbers.append(integer)
    if len(even_numbers) > len(odd_numbers):
        x = odd_numbers[0]
    else:
        x = even_numbers[0]
    return x



find_outlier(list_integers1)
find_outlier(list_integers2)
find_outlier(list_integers3)

def find_outlier2(int):
    odds = [x for x in int if x%2!=0]
    evens= [x for x in int if x%2==0]
    return odds[0] if len(odds)<len(evens) else evens[0]