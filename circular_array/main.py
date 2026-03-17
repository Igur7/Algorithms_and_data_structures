from cirrcular_array import CircularQueue


def main():
    queue = CircularQueue()

    # wstaw 0 i 1
    queue.enqueue(0)
    queue.enqueue(1)

    # odczyt pierwszego elementu
    print(queue.dequeue())

    # podgląd kolejnego
    print(queue.peek())

    # wstaw 2, 3, 4
    for value in range(2, 5):
        queue.enqueue(value)

    # kolejny odczyt
    print(queue.dequeue())

    # stan kolejki (od odczytu do zapisu)
    print(queue)

    # wstaw 5..8 (spowoduje realokację)
    for value in range(5, 9):
        queue.enqueue(value)

    # stan wewnętrznej tablicy
    print(queue.table_state())

    # opróżnij kolejkę
    while not queue.is_empty():
        print(queue.dequeue())

    # powinna być pusta
    print(queue)


if __name__ == "__main__":
    main()
