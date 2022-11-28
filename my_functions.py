# Mark Faverzani
# Turned in late due to returning from a concussion

def total(lst):
    """
    This will return every even number in a list of integers
    """
    lst.sort()
    count = []
    for i in range(len(lst)):
        if lst[i] % 2 ==0:
            count.append(lst[i])
    return count


print(total([1,5,7,8,8,8,2,4,6,6,6,4,3,3,3]))
print(total([2]))
print(total([10,9,8,7,6,5,4,3,2,1]))

def charcount(str, let):
    """
    This will count the ammount of any given character in a string    
    """
    count = 0
    for i in range(len(str)):
        if str[i] == let:
            count = count + 1
    return count

print(charcount("ababa", 'a'))
print(charcount("mississippi", 's'))
print(charcount("magnanimous", 'm'))

def space(str):
    """
    Removes all of the spaces from any given string
    """
    str2 = ""
    for i in range(len(str)):
        if str[i] != ' ':
            str2 = str2 + str[i]
    return str2

print(space("a brak a da bra"))
print(space("s p e e d      y  "))
print(space("one on one"))
