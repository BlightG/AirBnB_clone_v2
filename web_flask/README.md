# 0x04. AirBnB clone - Web framework

### Concepts

For this project, we expect you to look at this concept:

- [AirBnB clone](https://intranet.alxswe.com/concepts/74)

## Resources

**Read or Watch:**

- [What is a Web Framework?](https://intelegain-technologies.medium.com/what-are-web-frameworks-and-why-you-need-them-c4e8806bd0fb)
- [A Minimal Application](https://flask.palletsprojects.com/en/1.0.x/quickstart/#a-minimal-application)
- [Routing](https://flask.palletsprojects.com/en/1.0.x/quickstart/#routing) (except “HTTP Methods”)
- [Rendering Templates](https://flask.palletsprojects.com/en/1.0.x/quickstart/#rendering-templates)
- [Synopsis](https://jinja.palletsprojects.com/en/2.9.x/templates/#synopsis)
- [Variables](https://jinja.palletsprojects.com/en/2.9.x/templates/#variables)
- [Comments](https://jinja.palletsprojects.com/en/2.9.x/templates/#comments)
- [Whitespace Control](https://jinja.palletsprojects.com/en/2.9.x/templates/#whitespace-control)
- [List of Control Structures](https://jinja.palletsprojects.com/en/2.9.x/templates/#list-of-control-structures) (read up to “Call”)
- [Flask](https://palletsprojects.com/p/flask/)
- [Jinja](https://jinja.palletsprojects.com/en/2.9.x/templates/)

## Learning Objectives

At the end of this project, you are expected to be able to [explain to anyone](https://fs.blog/feynman-learning-technique/), **without the help of Google**:

### General

- What is a Web Framework
- How to build a web framework with Flask
- How to define routes in Flask
- What is a route
- How to handle variables in a route
- What is a template
- How to create a HTML response in Flask by using a template
- How to create a dynamic template (loops, conditions…)
- How to display in HTML data from a MySQL database

### Copyright - Plagiarism

- You are tasked to come up with solutions for the tasks below yourself to meet with the above learning objectives.
- You will not be able to meet the objectives of this or any following project by copying and pasting someone else’s work.
- You are not allowed to publish any content of this project.
- Any form of plagiarism is strictly forbidden and will result in removal from the program.

## Requirements

### Python Scripts

- Allowed editors: **vi**, **vim**, **emacs**
- All your files will be interpreted/compiled on Ubuntu 14.04 LTS using **python3** (version 3.4.3)
- All your files should end with a new line
- The first line of all your files should be exactly **#!/usr/bin/python3**
- A **README.md** file, at the root of the folder of the project, is mandatory
- Your code should use the **PEP 8** style (version 1.7)
- All your files must be executable
- The length of your files will be tested using **wc**
- All your modules should have documentation (**python3 -c 'print(__import__("my_module").__doc__)'**)
- All your classes should have documentation (**python3 -c 'print(__import__("my_module").MyClass.__doc__)'**)
- All your functions (inside and outside a class) should have documentation (**python3 -c 'print(__import__("my_module").my_function.__doc__)'** and **python3 -c 'print(__import__("my_module").MyClass.my_function.__doc__)'**)
- A documentation is not a simple word, it’s a real sentence explaining what’s the purpose of the module, class or method (the length of it will be verified)

### HTML/CSS Files

- Allowed editors: **vi**, **vim**, **emacs**
- All your files should end with a new line
- A **README.md** file at the root of the folder of the project is mandatory
- Your code should be W3C compliant and validate with **W3C-Validator** (except for jinja template)
- All your CSS files should be in the **styles** folder
- All your images should be in the **images** folder
- You are not allowed to use **!important** or **id** (**#**... in the CSS file)
- All tags must be in uppercase
- Current screenshots have been done on **Chrome 56.0.2924.87**.
- No cross browsers

## Tasks

### 0. Hello Flask!

Write a script that starts a Flask web application:

- Your web application must be listening on **0.0.0.0**, port **5000**
- Routes:
    - /: display “Hello HBNB!”
- You must use the option **strict_slashes=False** in your route definition
- File: **0-hello_route.py, __init__.py**

### 1. HBNB

Write a script that starts a Flask web application:

- Your web application must be listening on 0.0.0.0, port 5000
- Routes:
    - /: display “Hello HBNB!”
    - /hbnb: display “HBNB”
- You must use the option strict_slashes=False in your route definition
- File: **1-hbnb_route.py**

### 2. C is fun!

Write a script that starts a Flask web application:

- Your web application must be listening on 0.0.0.0, port 5000
- Routes:
    - **/**: display “Hello HBNB!”
    - **/hbnb**: display “HBNB”
    - **/c/<text>**: display “C ” followed by the value of the **text** variable (replace underscore _ symbols with a space )
- You must use the option **strict_slashes=False** in your route definition
- File: **2-c_route.py**

### 3. Python is cool!

Write a script that starts a Flask web application:

- Your web application must be listening on 0.0.0.0, port 5000
- Routes:
    - /: display “Hello HBNB!”
    - /hbnb: display “HBNB”
    - /c/<text>: display “C ”, followed by the value of the text variable (replace underscore _ symbols with a space )
    - /python/(<text>): display “Python ”, followed by the value of the text variable (replace underscore _ symbols with a space )
        - The default value of text is “is cool”
- You must use the option **strict_slashes=False** in your route definition
- File: **3-python_route.py**

### 4. Is it a number?

Write a script that starts a Flask web application:

- Your web application must be listening on 0.0.0.0, port 5000
- Routes:
    - /: display “Hello HBNB!”
    - /hbnb: display “HBNB”
    - /c/<text>: display “C ”, followed by the value of the text variable (replace underscore _ symbols with a space )
    - /python/(<text>): display “Python ”, followed by the value of the text variable (replace underscore _ symbols with a space )
        - The default value of text is “is cool”
    - /number/<n>: display “n is a number” only if n is an integer
- You must use the option **strict_slashes=False** in your route definition
- File: **4-number_route.py**

### 5. Number template

Write a script that starts a Flask web application:

- Your web application must be listening on 0.0.0.0, port 5000
- Routes:
    - **/**: display “Hello HBNB!”
    - **/hbnb**: display “HBNB”
    - **/c/<text>**: display “C ”, followed by the value of the **text** variable (replace underscore _ symbols with a space )
    - **/python/(<text>)**: display “Python ”, followed by the value of the **text** variable (replace underscore **_** symbols with a space )
        - The default value of **text** is “is cool”
    - **/number/<n>**display “n is a number” only if n is an integer
    - **/number_template/<n>**display a HTML page only if n is an integer:
       - **H1** tag: “Number: **n**” inside the tag **BODY**
- You must use the option **strict_slashes=False** in your route definition
- File: **5-number_template.py, templates/5-number.html**

### 6. Odd or even?

Write a script that starts a Flask web application:

- Your web application must be listening on 0.0.0.0, port 5000
- Routes:
    - **/**: display “Hello HBNB!”
    - **/hbnb**: display “HBNB”
    - **/c/<text>**: display “C ”, followed by the value of the **text** variable (replace underscore _ symbols with a space )
    - **/python/(<text>)**: display “Python ”, followed by the value of the text variable (replace underscore _ symbols with a space )
        - The default value of **text** is “is cool”
    - **/number/<n>**: display “n is a number” only if **n** is an integer
    - **/number_template/<n>**: display a HTML page only if **n** is an integer:
        - **H1** tag: “Number: **n**” inside the tag **BODY**
    - **/number_odd_or_even/<n>**: display a HTML page only if **n** is an integer:
        - **H1** tag: “Number: **n** is **even|odd**” inside the tag BODY
- You must use the option **strict_slashes=False** in your route definition
- File: **6-number_odd_or_even.py, templates/6-number_odd_or_even.html**
