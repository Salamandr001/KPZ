# Zoo Management System

This project demonstrates the application of various programming principles through a Zoo Management System. Below are the principles followed and how they are implemented in the code.

## Principles Demonstrated

### 1. DRY (Don't Repeat Yourself)

The DRY principle is followed by abstracting common functionality into base classes. For instance, the `Animal` class is the base class for `Mammal` and `Bird`, avoiding repetition of common attributes and methods.

- **File**: [`animal.py`](./animal.py)
- **Lines**: 1-19

### 2. KISS (Keep It Simple, Stupid)

The code is kept simple and straightforward. Each class has a single responsibility, and methods are concise and to the point.

- **File**: [`main.py`](./main.py)
- **Lines**: Entire file

### 3. SOLID Principles

#### S - Single Responsibility Principle

Each class in the project has a single responsibility. For example, the `Animal` class deals only with attributes and methods related to animals, while the `Enclosure` class handles enclosure-specific details.

- **File**: [`animal.py`](./animal.py), [`enclosure.py`](./enclosure.py)
- **Lines**: 1-19, 1-15

#### O - Open/Closed Principle

The system is open for extension but closed for modification. New animal types can be added by extending the `Animal` class without altering existing code.

- **File**: [`animal.py`](./animal.py)
- **Lines**: 21-30, 32-41

#### L - Liskov Substitution Principle

Subtypes can replace their base types without altering the correctness of the program. For example, `Mammal` and `Bird` can be used wherever `Animal` is expected.

- **File**: [`main.py`](./main.py)
- **Lines**: 9-10, 12-13

#### I - Interface Segregation Principle

Interfaces are kept small and specific. Each class has methods relevant only to its role, avoiding large, monolithic interfaces.

- **File**: [`animal.py`](./animal.py), [`enclosure.py`](./enclosure.py), [`food.py`](./food.py), [`employee.py`](./employee.py)
- **Lines**: All lines

#### D - Dependency Inversion Principle

High-level modules do not depend on low-level modules. Both depend on abstractions. For example, `Inventory` class depends on abstract animal types, not on specific `Mammal` or `Bird` types.

- **File**: [`inventory.py`](./inventory.py)
- **Lines**: 1-13, 15-29

### 4. YAGNI (You Aren't Gonna Need It)

Only necessary features are implemented, avoiding over-engineering. The classes and methods are created to meet the current requirements of the zoo management system.

- **File**: [`main.py`](./main.py)
- **Lines**: Entire file

### 5. Composition Over Inheritance

Where appropriate, composition is used instead of inheritance. For example, the `Enclosure` class contains a list of `Animal` instances, demonstrating a "has-a" relationship.

- **File**: [`enclosure.py`](./enclosure.py)
- **Lines**: 5-8

### 6. Program to Interfaces, Not Implementations

The system is designed to depend on abstractions (e.g., `Animal` class) rather than concrete implementations (`Mammal`, `Bird`), allowing for greater flexibility and easier maintenance.

- **File**: [`inventory.py`](./inventory.py)
- **Lines**: 1-13, 15-29

### 7. Fail Fast

The constructors in the classes ensure that objects are initialized with valid data, causing the program to fail quickly if invalid data is provided.

- **File**: [`animal.py`](./animal.py)
- **Lines**: 2-8, 21-24, 32-35

## File Structure

- [`animal.py`](./animal.py): Contains the `Animal`, `Mammal`, and `Bird` classes.
- [`enclosure.py`](./enclosure.py): Contains the `Enclosure` class.
- [`food.py`](./food.py): Contains the `Food` class.
- [`employee.py`](./employee.py): Contains the `Employee` class.
- [`inventory.py`](./inventory.py): Contains the `Inventory` class.
- [`main.py`](./main.py): Main program to demonstrate the usage of all classes.

## How to Run

1. Ensure you have Python installed.
2. Clone this repository.
3. Run the `main.py` file using the command: `python main.py`.

