# Code built from
# https://www.stefaanlippens.net/python_inspect/#:~:text=does%20it%20work%3F-,inspect.,of%20the%20frame%20record%20(%20inspect.
import inspect
def whoami():
    return inspect.stack()[1][3]
def whosdaddy():
    return inspect.stack()[2][3]
def whatsmyvariable():
    stack = inspect.stack()
    for frame_info in stack[1:]:
        frame = frame_info[0]
        for var_name, var_value in frame.f_locals.items():
            return var_name, var_value
def factorial(n: int) -> int:
    var_name, var_value = whatsmyvariable()
    print(f"I'm {whoami()}. My variable {var_name} has value {var_value}. My parent is {whosdaddy()}")
    if n > 1:
        return n * factorial(n-1)
    else: 
        return 1
print(factorial(4))