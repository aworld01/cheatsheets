words=["abc", "tuv", "xyz"]
print(words)

def reverse_element(l):
    element=[]
    for i in l:
        element.append(i[::-1])
    return element
print(reverse_element(words))