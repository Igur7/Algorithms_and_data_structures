import mixing_list

def test1(size, c1=1, c2=0):
    print("=== TEST 1 ===")

    ht = mixing_list.HashTable(size, c1, c2)

    # klucze
    keys = list(range(1, 16))
    keys[5] = 18
    keys[6] = 31

    # wartości A, B, C...
    values = [chr(ord('A') + i) for i in range(15)]

    # insert
    for k, v in zip(keys, values):
        ht.insert(k, v)

    print("Tablica:")
    print(ht)

    print("Search 5:", ht.search(5))
    print("Search 14:", ht.search(14))

    ht.insert(5, 'Z')
    print("Search 5 po nadpisaniu:", ht.search(5))

    ht.remove(5)

    print("Tablica po usunięciu 5:")
    print(ht)

    print("Search 31:", ht.search(31))

    # dodatkowy test po naprawie
    ht.insert("test", "W")
    print("Po dodaniu ('test','W'):")
    print(ht)

def test2(size, c1=1, c2=0):
    print("=== TEST 2 ===")

    ht = mixing_list.HashTable(size, c1, c2)

    keys = [13 * (i + 1) for i in range(15)]
    values = [chr(ord('A') + i) for i in range(15)]

    for k, v in zip(keys, values):
        ht.insert(k, v)

    print("Tablica:")
    print(ht)

if __name__ == "__main__":
    test1(size = 13)

    print("\n----------------------\n")
    test2(size = 13)

    print("\n----------------------\n")
    test2(13, 0, 1)

    print("\n----------------------\n")
    test1(13, 0, 1)