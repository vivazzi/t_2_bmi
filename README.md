# Calculation of Body Mass Index (BMI) - test app #2

This is a test application using real bmi calculation.

You can find a task description in this repo:

- [docs/task.md](docs/task.md) in English
- [docs/task_ru.md](docs/task_ru.md) in Russian


## Run project

### Requirements

- python 3.10
- pipenv

### Running

1. Clone this repo
2. Create virtual environment: `pipenv sync`

This task was decided with two ways, so you can run:

- `pipenv run python manage.py funcs_bmi` for an app running using only functions (see: [funcs](funcs))
- `pipenv run python manage.py class_bmi` for an app running using class (see: [classes](classes))


## Run project with Docker

```
docker pull vivazzi/t_2_bmi:latest
docker run -it vivazzi/t_2_bmi:latest /bin/sh
```

You will enter to container. Run:

- `pipenv run python manage.py funcs_bmi`
- `pipenv run python manage.py class_bmi`

See difference of the running in previous section (`Run Project / Running`)


## Tests

Run:

```
pipenv run python tests.py
```


## Additional tasks

Below are the tasks that I decided to do additionally outside the main task for more
demonstrations:

### 1. Task formalization

Initially, the task was given in a less formalization form (look [docs/raw_task.txt](docs/raw_task.txt), task was given in Russian only, the errors in the text are preserved). 
The result of task formalization is in [docs/task.md](docs/task.md) (in English) and [docs/task_ru.md](docs/task_ru.md) (in Russian).

### 2. Different aspects of programming

#### 2.1. Loading modules

Since I added two options for solving the task (using functions and classes), 
I added a control mechanism for starting code execution in a file [manage.py](manage.py).
This way decides problem with python path loading module. 

> For example, we cannot run `classes.main` through `if __name__ == '__main__'`, sense
module `classes.main` contains `utils` import, that is in parent folder.  
> For reproduce this bug you can replace `def run():` to
> `if __name__ == '__main__'` in file `classes.main` and try to run `pipenv run python classes/main.py`.

#### 2.2. Programming methodologies, OOP, SOLID

The program itself follows the principle of IPO - Input-Process-Output. This is one of the principles of creating flexible and extensible systems.

```python
# classes/main.py
...

def run():
    # Input
    mass = _input('mass (kg) = ')
    height = _input('height (cm) = ')
    
    # Process
    result = BMI(mass, height).result()
    
    # Output
    print(result)
```

> Since the program is simple, so Process and Output can be written in one line (see: [classes/main.py](classes/main.py))


`classes.bmi` module demonstrate minimal parts of OOP and SOLID (one of principles: the Single Responsibility Principle): 
in this module it is declared class BMI. This class contains only functions related to the calculation of the BMI, 
as well as a function for presenting the result for human beings. The class does not and should not know how the input is given 
(this could be interactive input, as in this example, or reading data from a file, or calling some API function, etc.). 
Also, the class does not care what happens to the result data next (printing data on the screen or sending it over the network).

### 3. Containerization with Docker

Docker has become the standard in today's programming world which simplifies testing and deployment of applications. You don't need to install all project requirements 
(python, DBMS, specific libraries and so on). You need install only docker to your OS.

### 4. Adding tests

When solving the task, it was used Test-Driven Development (TDD) methodology.