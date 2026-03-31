from skip_list import SkipList

import random
import string

if __name__ == "__main__":
    random.seed(42)

    sl = SkipList(5)

    for i, letter in enumerate(string.ascii_uppercase[:15], start=1):
        sl.insert(i, letter)

    print("Lista po wstawieniu 1..15:")
    sl.displayList_()

    print("\nWyszukaj klucz 2:", sl.search(2))

    sl.insert(2, 'Z')
    print("Po nadpisaniu klucza 2 literą 'Z':", sl.search(2))

    sl.remove(5)
    sl.remove(6)
    sl.remove(7)

    print("\nLista po usunięciu kluczy 5,6,7:")
    print(sl)

    sl.insert(6, 'W')

    print("\nLista po wstawieniu klucza 6 z wartością 'W':")
    print(sl)


    print("\n\n=== TEST 2: WSTAWIANIE 15 → 1 ===")

    random.seed(42)  # żeby był ten sam rozkład poziomów

    sl2 = SkipList(5)

    letters = string.ascii_uppercase[:15]

    for i, letter in zip(range(15, 0, -1), letters):
        sl2.insert(i, letter)

    print("Lista po wstawieniu 15..1:")
    sl2.displayList_()

    print("\nWyszukaj klucz 2:", sl2.search(2))

    sl2.insert(2, 'Z')
    print("Po nadpisaniu klucza 2:", sl2.search(2))

    sl2.remove(5)
    sl2.remove(6)
    sl2.remove(7)

    print("\nLista po usunięciu 5,6,7:")
    print(sl2)

    sl2.insert(6, 'W')

    print("\nLista po ponownym wstawieniu 6:")
    print(sl2)