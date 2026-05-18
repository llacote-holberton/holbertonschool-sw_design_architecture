# Overview

This directory holds tasks tailored to learn about how to use design patterns

# General Rules
- Corrections will run on Ubuntu 20.04 LTS.
- Python version used for correction: Python 3.10.x or later.
- Every Python file must start exactly with:  
  `#!/usr/bin/env python3`
- Every Python file must:
  * End with a newline.
  * Be PEP8 compliant (pycodestyle 2.7.x).
  * All modules, classes, and functions should include
      clear and concise documentation strings.  
  * No external libraries are allowed unless explicitly requested.
  * All scripts must behave exactly as specified in the task instructions.

# Exercises

| Task name                               | Filename              |
|-----------------------------------------|-----------------------|
| 00. Factory — Extending a registry      | 0-factory.py          |
| 01. Observer - Adding a new subscriber  | 1-observer.py         |
| 02. Decorator - Adding a new wrapper    | 2-decorator.py        |
| 03. Design Patterns quizz               | (quizz)               |

## 00. Factory — Extending a registry
<details>
<summary>(Click for detailed information on Task 0 concept, goals and requirements)</b></summary>
### Design Problem

In many systems, object creation is spread across several parts of the code. This may start as something simple, but it becomes harder to maintain when new concrete types are added.

### Friendly scenario

Imagine a mobility platform that supports buses, trains, bikes, and scooters. If different parts of the application create these objects directly, adding a new vehicle type requires modifying several places. A factory centralizes that decision.

### Objective

Extend an existing factory registry to support a new vehicle type, without modifying the core creation logic inside create.
### Context

The Factory pattern is a creational pattern. Its role is to centralize object creation so the rest of the code does not need to know which concrete class to instantiate. Instead of scattering `Bus()`, `Train()`, and `Bike()` calls across the codebase, callers ask the factory for a vehicle by name.

A naive factory that grows with every new type looks like this:
```
  def create(self, kind: str):
    if kind == "bus":
      return Bus()
    elif kind == "train":
      return Train()
    elif kind == "scooter":    # must edit here every time
    return Scooter()
```

This violates the open/closed principle: the method is never closed for modification.
The registry approach solves this — new types are registered from outside, and `create` never changes:
  `factory.register_kind("scooter", Scooter)`

In the provided starter file, `VehicleFactory` already manages `Bus`, `Train`, and `Bike` via a `_registry` dictionary. `register_kind(name, cls)` maps a string key to a class; `create(kind)` looks up the key and calls the class with no arguments. The `Scooter` class is defined but not yet registered.
Instructions

1. Copy the starter code from here:  
  https://raw.githubusercontent.com/hbtn-edu/public_resources/refs/heads/main/3960-design_patterns/factory_starter.py

2. Read the existing `VehicleFactory` and `main()`.
3. In `main()`, call `factory.register_kind("scooter", Scooter)` to register the new type.
4. Add `print(factory.create("scooter").mode())` after the existing prints.

Running the code must print exactly:
```
  road
  rails
  lane
  scooter_lane
```

VehicleFactory.create must not contain a hardcoded `if kind == "scooter"` branch — the registry does the mapping.
Adding a new vehicle type required zero edits to existing factory logic.

</details>

## 01. Observer - Adding a new subscriber

<details>
<summary>(Click for detailed information on Task 1 concept, goals and requirements)</b></summary>

</details>

## 02. Decorator - Adding a new wrapper

<details>
<summary>(Click for detailed information on Task 2 concept, goals and requirements)</b></summary>

</details>

# Ressources

- https://refactoring.guru/design-patterns
- https://refactoring.guru/design-patterns/factory-method
- https://refactoring.guru/design-patterns/observer
- https://refactoring.guru/design-patterns/decorator
- https://www.geeksforgeeks.org/system-design/solid-principle-in-programming-understand-with-real-life-examples/
- https://en.wikipedia.org/wiki/Open%E2%80%93closed_principle
- https://en.wikipedia.org/wiki/Composition_over_inheritance
- https://intranet.hbtn.io/concepts/1527
- https://docs.python.org/3/library/typing.html#typing.Protocol
- https://docs.python.org/3/library/abc.html
