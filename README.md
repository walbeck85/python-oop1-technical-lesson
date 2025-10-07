# Dog Model OOP Technical Lesson

This project guides you through building a Dog class in Python, demonstrating core Object Oriented Programming (OOP) concepts such as instance attributes, methods, and properties. The Dog model simulates a veterinary clinic’s database tool to manage client information.

## Overview

In this lesson, you will create a Dog class that models the essential attributes and behaviors of a dog in a veterinary setting. You will learn how to:

- Define a class and initialize instance properties
- Implement instance methods to modify object state
- Use Python properties to add validation logic to attributes
- Create and interact with class instances

This exercise provides a practical introduction to OOP fundamentals in Python.

## Learning Objectives

By the end of this lesson, you will be able to:

- Define a Python class with appropriate attributes and methods
- Initialize class instances with default and required parameters
- Create instance methods that modify object state
- Implement getter and setter methods using Python properties
- Validate attribute values within setters to enforce data integrity
- Understand the use of `self` and instance-specific data
- Work with feature branches and Git workflow for collaborative development

## Technologies Used

- Python 3.x
- pipenv for dependency management and virtual environment

## Project Setup

Follow these steps to set up your environment:

1. **Fork and Clone the Repository**

   - Navigate to the [GitHub Repo](https://github.com/learn-co-curriculum/python-oop1-technical-lesson).
   - Fork the repository to your GitHub account.
   - Clone your fork locally:
     ```bash
     git clone <your-forked-repo-url>
     cd python-oop1-technical-lesson
     ```

2. **Install Dependencies**

   - Run the following commands to install dependencies and activate the virtual environment:
     ```bash
     pipenv install
     pipenv shell
     ```

3. **Open the Project**

   - Open the project folder in your preferred code editor (e.g., VSCode).

## Usage Instructions

To run the Dog class demonstration:

```bash
python lib/dog.py
```

This will execute the script that creates Dog instances, invokes methods, and demonstrates property validation.

## Expected Output

When running the script, you should see the following output in your terminal:

```
3
Fido is turning 4
4
None
Checking up with Clifford on 03/02/2024
03/02/2024
Not valid age
Not valid age
```

## Code Structure

The `Dog` class includes:

- **Attributes:**
  - `name` (string): Dog’s name
  - `breed` (string): Dog’s breed
  - `age` (int): Dog’s age, validated to be a non-negative integer
  - `last_checkup` (string or None): Date of last checkup

- **Methods:**
  - `checkup(date)`: Updates the `last_checkup` date and prints a message
  - `birthday_celebration()`: Increments the dog’s age by 1 and prints a celebratory message

- **Property:**
  - `age`: Uses getter and setter to enforce that age is an integer ≥ 0. Invalid assignments print an error message.

## Git Workflow

Follow this workflow for development:

1. Create a feature branch:
   ```bash
   git checkout -b dog_class
   ```

2. Make your changes and commit with a descriptive message:
   ```bash
   git commit -am "Finish Dog model"
   ```

3. Push the branch to GitHub:
   ```bash
   git push origin dog_class
   ```

4. Open a Pull Request (PR) on GitHub, review, and merge into the main branch.

5. Pull the latest main branch and delete the feature branch locally:
   ```bash
   git checkout main
   git pull origin main
   git branch -d dog_class
   ```

   If deletion fails because Git doesn’t recognize the branch as merged, force delete with:
   ```bash
   git branch -D dog_class
   ```

## Reflection / Best Practices

- **Code Comments:** Add comments to clarify code intent and improve maintainability.
- **Understanding Instances and `self`:** Each instance has its own `self` context; this is fundamental to OOP.
- **Property Underscores:** Use an underscore prefix (e.g., `_age`) in getter/setter to avoid recursive calls.
- **Validation:** Use property setters to enforce data integrity and prevent invalid attribute values.

---

# Detailed Code Walkthrough

## Step 1: Create a Feature Branch

Create a new branch for your work:

```bash
git checkout -b dog_class
```

## Step 2: Build the Class

Define a basic Dog class:

```python
class Dog:
    pass
```

Classes in Python start with the `class` keyword, followed by the class name capitalized and a colon.

## Step 3: Initialize Instance Properties

Add the `__init__` method to initialize attributes when creating an instance:

```python
class Dog:
    def __init__(self, name, breed, age, last_checkup=None):
        self.name = name
        self.breed = breed
        self.age = age
        self.last_checkup = last_checkup
```

- `self` refers to the instance being created.
- `last_checkup` defaults to `None` if no value is provided.

## Step 4: Create Instance Methods

Add methods to perform actions on instances:

```python
class Dog:
    def __init__(self, name, breed, age, last_checkup=None):
        self.name = name
        self.breed = breed
        self.age = age
        self.last_checkup = last_checkup
    
    def checkup(self, date):
        print(f"Checking up with {self.name} on {date}")
        self.last_checkup = date
    
    def birthday_celebration(self):
        self.age += 1
        print(f"{self.name} is turning {self.age}")
```

- `checkup` updates `last_checkup` and prints a message.
- `birthday_celebration` increments age and prints a celebratory message.

## Step 5: Create and Use Instances of the Class

Instantiate Dog objects and interact with them:

```python
fido = Dog("Fido", "Golden Retriever", 3, "05/22/2022")
clifford = Dog(
    name="Clifford",
    age=2, 
    breed="Big Red"
)

print(fido.age)
fido.birthday_celebration()
print(fido.age)
print(clifford.last_checkup)
clifford.checkup("03/02/2024")
print(clifford.last_checkup)
```

- `fido` uses positional arguments.
- `clifford` uses keyword arguments for clarity and flexibility.

## Step 6: Modify and Access Instance Properties with Validation

Add getter and setter for `age` to validate input:

```python
class Dog:
    def __init__(self, name, breed, age, last_checkup=None):
        self.name = name
        self.breed = breed
        self.age = age
        self.last_checkup = last_checkup
    
    def checkup(self, date):
        print(f"Checking up with {self.name} on {date}")
        self.last_checkup = date
    
    def birthday_celebration(self):
        self.age += 1
        print(f"{self.name} is turning {self.age}")
    
    def get_age(self):
        return self._age
    
    def set_age(self, value):
        if type(value) is int and 0 <= value:
            self._age = value
        else:
            print("Not valid age")
    
    age = property(get_age, set_age)
```

- The setter checks that `age` is a non-negative integer.
- The underscore prefix `_age` prevents recursive setter/getter calls.

## Step 7: Test Instance Properties

Test the validation by creating instances with invalid ages:

```python
fido = Dog("Fido", "Golden Retriever", 3, "05/22/2022")
clifford = Dog(
    name="Clifford",
    age=2, 
    breed="Big Red"
)

print(fido.age)
fido.birthday_celebration()
print(fido.age)
print(clifford.last_checkup)
clifford.checkup("03/02/2024")
print(clifford.last_checkup)

balto = Dog("Balto", "Husky", "Not an age")
steele = Dog("Steele", "Husky", -10)
```

You should see the following output including error messages for invalid ages:

```
3
Fido is turning 4
4
None
Checking up with Clifford on 03/02/2024
03/02/2024
Not valid age
Not valid age
```

---

This concludes the technical lesson on creating a Dog class using Python OOP principles. Make sure to commit your changes and push to your GitHub repository following the Git workflow outlined above.
