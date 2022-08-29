import os
from time import strftime, localtime
from functools import wraps
from old_homework import flat_generator

def logger(old_function):
    @wraps(old_function)
    def new_function(*args, **kwars):
        result = old_function(*args, **kwars)
        with open(os.path.join("logs", "logs.txt"), 'a', encoding='utf-8') as f:
            f.write(f'{strftime("%Y-%m-%d %H:%M:%S", localtime())}: вызов функции - {old_function.__name__} с аргументами {args, kwars}, и полученным результатом {result}.\n')
        return result
    return new_function

def logger_with_path(old_function, path_logs):
    @wraps(old_function, path_logs)
    def new_function(*args, **kwars):
        result = old_function(*args, **kwars)
        with open(os.path.join("logs", "logs.txt"), 'r', encoding='utf-8') as f:
            ind = 0
            for line in f:
                if line.find(old_function.__name__):
                    ind += 1
                    func_time = line[0:19]
            print(f'Фукция {old_function.__name__} вызывалась {ind} раз, последний вызов - {func_time}')
        return result
    return new_function

@logger
def summator(n, m):
	return n + m

print(summator(1, 2))

summator = logger_with_path(summator,  os.path.abspath("logs.txt"))

print(summator(1, 2,))

flat_generator = logger(flat_generator)

print(flat_generator([1, 2, ["1", 3]]))

flat_generator = logger_with_path(flat_generator,  os.path.abspath("logs.txt"))

print(flat_generator([1, 2, ["1", 3]]))
