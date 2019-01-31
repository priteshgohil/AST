# Why do we need a software design pattern?

It was widely observed by Robert C Martin (AKA Uncle Bob) that object oriented codes followed a fixed pattern of errors and in general couble be boiled down to the following components:

* RIGIDITY: Every change affects many other parts.
* FRAGILITY: Things break at unrelated palces.
* IMMOBILITY: Cannot reuse the code.

# How can we solve the problem?

* S- Single Responsibility Principle
* O- Open-Closed Principle
* L- Liskov Substituition Principle
* I- Interface Segregation Principle
* D- Dependency Inversion Principle

## Single Responsibility Principle

- A class should have only one reason to change. If the class has to adjust with too many parameters everytime you should consider refactoring your code.

## Open-Closed Principle
- You should be able to extend the class without modifying it.

## Liskov Substituition Principle
- Derieved classes must be substituited for their base classes.

## Interface Segregation Principle

- Make fine grained interfaces with specific methods.

## Dependency Inversion Principle

- Depend on abstraction and not on concretions.


# Design pattern used in the code

In the demo codes, DIP and ISP are highly used. Check out the codes for detained flow.


# Types of design patterns

Design patterns can be:
1. Behavioral
2. Creational
3. Dft
4. Fundamental
5. Structural 
