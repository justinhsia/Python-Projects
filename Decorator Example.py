def blah(func):
    def wrapper(*args, **kwargs):
        print(f'{func.__name__} Fuck Putin')
        results = func(*args, **kwargs)
        return results
    return wrapper

@blah
def squared_num(num_list):
    return [num*num for num in num_list]

if __name__ == '__main__':
    numbers = [1, 2, 3, 4, 5]
    print(f"Squares of {numbers} are {squared_num(numbers)}.")
