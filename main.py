def main():
    #Non compliant method
    values = [1, 2, 3, 4, 5]
    list_numbers = []
    for val in values:
        numbers.insert(0, val)


    #Compliant method
    deque_numbers = deque()
    for val in values:
        deque_numbers.appendleft(val)
    

if __name__ == "__main__":
    main()
