def average():
    """Calculate the average of numbers entered by the user."""
    try:
        lst = list(map(int, input("Please input numbers separated by commas: ").split(',')))
    except ValueError as v:
        print(f'Value Error: {v}')
        return
    if not lst:
        print("Error: No numbers entered")
        return

    try:
        len_lst = len(lst)
        sum_lst = sum(lst)
        avarage_lst = sum_lst/len_lst
    except (ValueError, ZeroDivisionError) as e:
        print(f"Error: {e}")
    print(f"Avarage number is: {avarage_lst}")
    print(f"Your list: {lst}, has {len_lst} numbers, and sum of numbers: {sum_lst}")


average()


