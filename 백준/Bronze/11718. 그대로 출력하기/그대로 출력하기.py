while True:
    try:
        print(input())
    except EOFError:  # End of File Error
        break