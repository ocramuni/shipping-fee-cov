# Coverage Lab: Line Coverage vs Branch Coverage

## Goal

In this lab, your task is to extend the provided test suite to achieve full coverage of the production code.

You will learn the difference between:

- **line coverage**: whether a line of code was executed
- **branch coverage**: whether every decision outcome was exercised

## Project Structure

```text
.
├── src/
│   └── shipping.py
├── tests/
│   └── test_shipping.py
└── pytest.ini
```

You must:
* run the existing tests
* inspect the coverage report
* add new tests to improve coverage
* reach 100% line coverage
* reach 100% branch coverage

## Rules
* You may edit only the test file(s)
* Do not modify the production code in src/
* Use pytest to run the tests
* Use pytest-cov to measure coverage

## Suggested Workflow
1. Run the provided tests
2. Read the coverage report carefully
3. Identify missing lines and missing branches
4. Add one test at a time
5. Re-run coverage after each change
6. Continue until coverage reaches 100%

## Deliverable
Submit the completed test suite with:

* all tests passing
* 100% line coverage
* 100% branch coverage