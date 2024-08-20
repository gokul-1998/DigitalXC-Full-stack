import csv
import random


class SecretSantaAssigner:
    def __init__(self, employees, previous_assignments=None):
        self.employees = employees
        self.previous_assignments = previous_assignments or {}

    def assign_santas(self):
        remaining_employees = self.employees[:]
        assignments = {}
        
        for employee in self.employees:
            possible_choices = [
                e for e in remaining_employees
                if e['email'] != employee['email'] and e['email'] not in self.previous_assignments.get(employee['email'], [])
            ]
            if not possible_choices:
                raise ValueError("No valid Secret Santa assignment possible.")
            
            secret_child = random.choice(possible_choices)
            assignments[employee['email']] = secret_child
            remaining_employees.remove(secret_child)
        
        return assignments


def load_previous_assignments(filepath):
    previous_assignments = {}
    with open(filepath, mode='r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            previous_assignments[row['Employee_EmailID']] = row['Secret_Child_EmailID']
    return previous_assignments
