""" Operations on dictionaries."""

def main():
    d = {'four': 400, 'three': 30, 'two': 2, 'one': 30}
    for key in d:
        print("the key is: ", key)
        print("The value is: ", d[key])

    print("d : ", d)
    print("Search for all keys assiciated with value: ", 30)
    for key in d:
        if d[key] == 30:
            print(key)

    print("Print dictionary values in order of sorted keys: ")
    L_sorted = sorted(d)
    L_sorted.reverse()
    for key in L_sorted:
        print(d[key])
    
main()