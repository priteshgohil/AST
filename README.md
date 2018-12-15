# Continuous Integration With Travis CI

[![Build Status](https://travis-ci.com/priteshgohil/AST.svg?branch=developer_2)](https://travis-ci.com/priteshgohil/CI_travis)


## What is Continuous Integration?
* Continuous integration is a software development paradigm in which developers commit their code(s) to their respective branches (or master) recursi
vesly and each pushed commit is verified by an automated build which helps in a deep dive into the problem.

* When there is no CI, it gets hand to debug problems. In majority of cases the individual members are just a part of a bigger team and each team is
developing a sub-part of a bigger project. This causes a lot of problems if there is no validity check at the branch level or repository level.

* Whenever a sub-part of the project is build there are two tests which become essential to determine the functionality of the code:
    * Unit testing - Takes care of individual units (Chuncks of codes with some functionality)
    * Integration testing - Takes care of multiple units communicating with one another.

* In our case we have user travis for CI.

## Test components
* This given code test_area.py has a function that computers area of a rectangle and tests it using pytest.
* The repository is integrated with travisCI which monitors the correctness of the code.
* With each new code, we need to write unittest and pytest will continuously monitor for the changes.
