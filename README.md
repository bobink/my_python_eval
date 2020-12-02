# my_python_eval

my_python_eval is a small project that aims to teach me Python

A basic arithmetic evaluator is a good project because it is not too small nor big 

### What did I learn ?
- python language
- how bad is python:
  - name collision between token.py of the standard library and my token.py because the standard library is not in a package
    So there is hidden reserved word in this language
  - --i and ++i will not do what you expect
  - no overload, no error if you use it
  - standard test assertions accessible by inheritance. Bad example for developers    
  - in test assertions, actual is first
  - file with "-" cannot be imported but can be directly interpreted  


### Usage

#### Tools
- IntelliJ IDEA 2020.2.3
- Python 3.9

#### How to test

```
python -m unittest
```

#### How to run

```
python -m org.bobink.my_eval "2 + 3 * 4"
=> 14
```