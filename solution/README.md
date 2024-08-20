# Secret Santa Assigner

## Overview

This project automates the Secret Santa assignment process for a company. It reads employee data from a CSV file and assigns each employee a "secret child" to whom they will anonymously give a gift. The assignment follows specific rules to ensure fairness and avoid repeating the same pairings as in the previous year.

## Features

- Modular, extensible code following OOP principles
- Avoids assigning an employee to themselves or repeating last year's assignments
- Generates a CSV output file with the Secret Santa assignments
- Error handling for invalid input and file issues
- Unit tests to ensure code quality and correctness

## How to Use

1. **Install dependencies**: 
    - No requirements in this case


2. **Run the program**:
    - `python main.py`


3. **Test the code**:
    - `python tests.py`


## Input Files

- `Employee-List.csv`: A CSV file containing employee information.
- `Secret-Santa-Game-Result-2023.csv`: A CSV file containing last year's Secret Santa assignments.

## Output Files

- `current_assignments.csv`: The output CSV file with the current Secret Santa assignments.

## Error Handling

- If no valid assignment is possible (e.g., due to constraints), the program will raise an error.

## How to Run
1. Prepare your input files:

    - data/Employee-List.csv: Add the employee details.
    - data/Secret-Santa-Game-Result-2023.csv: Add the previous assignments, if applicable.

## Run the program:

    - `python main.py`

## Check the output:

    - The new assignments will be saved in `data/current_assignments.csv`.

## Testing
    - Run `tests.py` to ensure that all components work correctly.

