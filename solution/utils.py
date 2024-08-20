import csv


def load_employees(filepath):
    employees = []
    with open(filepath, mode='r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            employees.append({
                "name": row['Employee_Name'],
                "email": row['Employee_EmailID']
            })
    return employees


def save_assignments(assignments, filepath):
    with open(filepath, mode='w', newline='') as file:
        fieldnames = ['Employee_Name', 'Employee_EmailID', 'Secret_Child_Name', 'Secret_Child_EmailID']
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writeheader()

        for employee_email, secret_child in assignments.items():
            # Here, `employee_email` is a string (the key), and `secret_child` is a dictionary (the value).
            writer.writerow({
                'Employee_Name': secret_child['name'],
                'Employee_EmailID': secret_child['email'],
                'Secret_Child_Name': secret_child['name'],
                'Secret_Child_EmailID': secret_child['email']
            })
