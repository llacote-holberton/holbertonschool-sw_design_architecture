# Overview

This directory will hold the introductory exercises for learning how to create  
  data & controller architecture and sequence diagrams.

# General Rules

## UML projects
- Corrections will run on Ubuntu 20.04 LTS.
- Python version used for correction: Python 3.8.x.
- Mermaid compatible renderer must be used.
- Use Python-style data types (str, bool, etc.).
- Filenames must match exactly.
- Do not introduce elements not described in the problem.
- Do not rename classes, attributes, or methods.
- Diagram must be syntactically valid.
- Only include elements that can be justified from the problem statement.
- The project will be automatically corrected.
- Diagram must be designed and stored in Mermaid syntax.

# Exercises

## General context
A small library wants to manage its books and users.

The system must allow the library to...
- store information about books
- register users
- create loans when a user borrows a book

The system revolves around a Library that manages books, users, and loans.

The Library must be able to:
- add_book to its collection
- register_user
- create_loan when a user borrows a book

Each Book has:
- a title
- an author
- a state indicating whether it is available or not (true/false)

A Book must be able to:
- mark_as_unavailable
- mark_as_available

Each User has:
- a name
- an email

Each Loan contains:
- a start_date
- an end_date
A Loan must be able to:
- close_loan
When a user borrows a book, a Loan is created.
When a loan is created...
- the selected book must no longer be available
- the loan must reference the book and the user involved
When a loan is closed...
- the associated book becomes available again.

## 0. Class Diagram
Create a Mermaid class diagram that represents the system described above.

Your diagram must include:
- all relevant classes
- attributes for each class
- methods derived from the described behavior
- relationships between classes
- multiplicities

Expected file: uml_intro/0-class_diagram.mmd

## 1. Sequence Diagram

Create a Mermaid sequence diagram that represents this interaction.

Your diagram must...
- Include all relevant participants.
- Follow the behavior described in the problem.
- Reflect the correct order of interactions.
- Use method names exactly as described in the problem statement.

Your diagram must represent the following sequence...
- The User requests the Library to create a loan.
- The Library asks the Book to mark itself as unavailable.
- The Library creates a Loan.
- The Library returns confirmation to the User.

To ensure consistency and allow automatic correction, you must follow these rules exactly:

- Declare at the beginning only the participants that already exist before the interaction starts.
  * User
  * Library
  * Book
- Do not declare Loan at the beginning of the diagram
- The Loan must appear only at the moment it is created using: `create participant Loan`
- After creation, the Library must interact with the Loan
- Do not use aliases (as) or alternative naming
- Do not add extra participants
- Do not add extra messages beyond those required

The last interaction in the sequence diagram must be exactly:
`Library-->>User: loan created`

Use this message exactly as written:
```
  sender: Library
  arrow: -->>
  receiver: User
  label: loan created
```
Do not replace it with alternatives.

Expected file: uml_intro/1-sequence_diagram.mmd

# Resources

The following are recommended resources and tools

## Documentation

### UML Architecture Diagrams

- https://intranet.hbtn.io/concepts/1166
- https://intranet.hbtn.io/concepts/1167
- https://intranet.hbtn.io/concepts/1168
- https://intranet.hbtn.io/concepts/1169
- https://intranet.hbtn.io/concepts/1170
- https://intranet.hbtn.io/concepts/1171
- https://intranet.hbtn.io/concepts/1172
- https://www.youtube.com/watch?v=6XrL5jXmTwM
- https://www.youtube.com/watch?v=4emxjxonNRI
- https://intranet.hbtn.io/rltoken/aLTSzUCRwk3GrjqobV-jZA

### UML Sequence diagrams
- https://www.youtube.com/watch?v=pCK6prSq8aw

### Mermaid
- https://mermaid.js.org/syntax/classDiagram.html
- https://mermaid.js.org/syntax/sequenceDiagram.html

## Tools
- PlantUML: https://www.plantuml.com/plantuml/uml/SyfFKj2rKt3CoKnELR1Io4ZDoSa700001
- Mermaid (live): https://mermaid.live/edit
