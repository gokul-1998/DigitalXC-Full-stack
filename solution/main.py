from santa_assigner import SecretSantaAssigner, load_previous_assignments
from utils import load_employees, save_assignments


def main():
    employees = load_employees('data/Employee-List.csv')
    try:
        previous_assignments = load_previous_assignments('data/Secret-Santa-Game-Result-2023.csv')
    except FileNotFoundError:
        previous_assignments = {}

    assigner = SecretSantaAssigner(employees, previous_assignments)

    try:
        assignments = assigner.assign_santas()
    except ValueError as e:
        print(f"Error: {e}")
        return

    # Save the assignments
    save_assignments(assignments, 'data/current_assignments.csv')
    print("Secret Santa assignments saved successfully!")


if __name__ == '__main__':
    main()
