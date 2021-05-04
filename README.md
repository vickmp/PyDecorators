# PyDecorators

Set of custom Python decorators with useful functions for development.

Currently, this package includes three different decorators:

- **@debug**: print the init and the end of the wrapped function in the logs. Optionally, the attributes of the function can be shown.
- **@repeat**: try repeat the function a certain num of times until success.
- **@sleep**: sleep the program a certain time before calling the function.

## Examples of use

### @debug
Input
````python
from decorators.debug import debug

@debug(params=True)
def say_hello_to (name: str) -> None:
    print(f'Hello {name}!')

say_hello_to(name='vick')
````
Log output
````sh
Init: say_hello_to(name='vick')
Hello vick!
End: 'say_hello_to' returned None
````

### @repeat
Input
````python
from decorators.repeat import repeat

@repeat(num_times=2, time_sleep=5)
def error_func():
    empty_list = list()
    print(empty_list[2])

print('Doing something')
error_func()
print('Finish somethiing')
````
output
````sh
Doing something
Error in error_func. Trying again in 5second(s). Traceback: Traceback (most recent call last):
  File "/Users/vick/Documents/desarrollos/decorators/repeat.py", line 39, in wrapper_repeat
    value = func(*args, **kwargs)
  File "test.py", line 20, in error_func
    print(empty_list[2])
IndexError: list index out of range

Error in error_func. Trying again in 5second(s). Traceback: Traceback (most recent call last):
  File "/Users/vick/Documents/desarrollos/decorators/repeat.py", line 39, in wrapper_repeat
    value = func(*args, **kwargs)
  File "test.py", line 20, in error_func
    print(empty_list[2])
IndexError: list index out of range
Finish something
````

### @sleep
Input
````python
from decorators.sleep import sleep

@sleep(seconds=5)
def init_db() -> None:
    print('Connection with DB stablished')

print('Doing something')
init_db()
````
output
````sh
Doing something
# After 5 seconds...
Connection with DB stablished
````


