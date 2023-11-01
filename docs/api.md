# ***API Documentation***



## Class: ZheJiang

A Class for the completion of Zhejiang Youth University Study.

### `__init__(self, nid, cardNo, openid, SendKey: str = None)`

Initializes the ZheJiang class.

**Parameters:**

- `nid`: The group organization number, in the form of N003************.
- `cardNo`: The card nickname, which may be a student number or a name.
- `openid`: WeChat openid.
- `SendKey`: Server's SendKey. This parameter is optional.

All parameters need to be captured from the network.

### `__call__(self, *args: Any, **kwds: Any) -> Any`

Calls the class.

**Parameters:**

- `args`: Arguments.
- `kwds`: Keyword arguments.

**Returns:**

- `True` if successful, `False` if failed.


## Function: push

A decorator function for sending notifications about the status of the job.

```python
def push(func):
```

**Parameters:**

- `func`: The function to be decorated. This function should return a tuple of objects, where each object has a `result` attribute indicating whether the job was successful, a `SendKey` attribute for the notification service, and a `msg` attribute containing a message about the job.

**Returns:**

- A wrapper function that calls `func` and sends a notification about the result. The notification includes a success or failure message and the `msg` from each object returned by `func`.

**Example:**

```python
@push
def my_job():
    # Do some work here...
    return (obj1, obj2, obj3)

my_job()
```

In this example, `my_job` is decorated with `push`, so when `my_job` is called, it will send a notification about the result of each object it returns.


## Function: job

A function that executes a list of jobs.

```python
def job(*jobs) -> None:
```

**Parameters:**

- `*jobs`: A variable number of job functions to be executed. Each job function should be a callable that takes no arguments.

**Returns:**

- None. The function executes each job in the order they were passed in, but does not return anything.

**Example:**

```python
job1 = ZheJiang(nid=..., cardNo=..., openid=...)
job2 = ZheJiang(nid=..., cardNo=..., openid=...)

job(job1, job2)
```

In this example, `job1` and `job2` are passed to the `job` function, which executes them in order. The output will be:

```
Job 1
Job 2
```

**Note:**

The function is decorated with the `@push` decorator, which means that a notification will be sent after each job is executed. The details of this notification depend on the implementation of the `push` decorator.