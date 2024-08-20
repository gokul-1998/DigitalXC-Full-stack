import unittest
from santa_assigner import SecretSantaAssigner


class TestSecretSantaAssigner(unittest.TestCase):

    def test_assign_santas_no_previous(self):
        employees = [
            {"name": "Alpha", "email": "Alpha@gmail.com"},
            {"name": "Beta", "email": "Beta@gmail.com"},
            {"name": "Charlie", "email": "Charlie@gmail.com"}
        ]
        assigner = SecretSantaAssigner(employees)
        assignments = assigner.assign_santas()
        
        self.assertEqual(len(assignments), 3)
        for employee in employees:
            self.assertNotEqual(assignments[employee['email']]['email'], employee['email'])

    def test_assign_santas_with_previous(self):
        employees = [
            {"name": "Alice", "email": "alice@gmail.com"},
            {"name": "Beta", "email": "Beta@gmail.com"},
            {"name": "Charlie", "email": "Charlie@gmail.com"}
        ]
        previous_assignments = {
            "alice@gmail.com": "Beta@gmail.com"
        }
        assigner = SecretSantaAssigner(employees, previous_assignments)
        assignments = assigner.assign_santas()

        self.assertEqual(len(assignments), 3)
        for employee in employees:
            self.assertNotEqual(assignments[employee['email']]['email'], employee['email'])
        self.assertNotEqual(assignments['alice@gmail.com']['email'], "Beta@gmail.com")


if __name__ == '__main__':
    unittest.main()
