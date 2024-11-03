import unittest
from util import generate_department
from util import calculate_threat_score

ENGINEERING = "Engineering"
MARKETING = "Marketing"
FINANCE = "Finance"
HR = "HR"
SCIENCE = "Science"


class TestThreatScores(unittest.TestCase):

    # Case 1:
    # - each department has no outliers (no really high threat scores)
    # - each department mean threat score are NOT far from each other
    # - similiar number of users.
    # - all departments has the same importance
    def test1(self):
        departments = [
            generate_department(name=ENGINEERING, importance=3, mean=10, variance=5, num_samples=100),
            generate_department(name=MARKETING, importance=3, mean=9, variance=5, num_samples=100),
            generate_department(name=FINANCE, importance=3, mean=11, variance=5, num_samples=100),
            generate_department(name=HR, importance=3, mean=12, variance=5, num_samples=100),
            generate_department(name=SCIENCE, importance=3, mean=10, variance=5, num_samples=100)
        ]

        result = calculate_threat_score(departments)

        self.assertTrue(0 <= result <= 90)

# Case 2:
    # - All departments have the same importance
    # - Departments with varied mean threat scores
    def test2(self):
        departments = [
            generate_department(name=ENGINEERING, importance=3, mean=20, variance=10, num_samples=100),
            generate_department(name=MARKETING, importance=3, mean=40, variance=10, num_samples=100),
            generate_department(name=FINANCE, importance=3, mean=60, variance=10, num_samples=100),
            generate_department(name=HR, importance=3, mean=80, variance=10, num_samples=100),
            generate_department(name=SCIENCE, importance=3, mean=90, variance=10, num_samples=100)
        ]

        result = calculate_threat_score(departments)
        self.assertTrue(0 <= result <= 90)

    # Case 3:
    # - Different importance scores across departments
    def test3(self):
        departments = [
            generate_department(name=ENGINEERING, importance=5, mean=20, variance=10, num_samples=100),
            generate_department(name=MARKETING, importance=3, mean=40, variance=10, num_samples=100),
            generate_department(name=FINANCE, importance=2, mean=60, variance=10, num_samples=100),
            generate_department(name=HR, importance=4, mean=30, variance=10, num_samples=100),
            generate_department(name=SCIENCE, importance=1, mean=10, variance=10, num_samples=100)
        ]

        result = calculate_threat_score(departments)
        self.assertTrue(0 <= result <= 90)

    # Case 4:
    # - One department with extremely high mean
    def test4(self):
        departments = [
            generate_department(name=ENGINEERING, importance=3, mean=10, variance=5, num_samples=100),
            generate_department(name=MARKETING, importance=3, mean=15, variance=5, num_samples=100),
            generate_department(name=FINANCE, importance=3, mean=90, variance=5, num_samples=100),  # Extremely high
            generate_department(name=HR, importance=3, mean=12, variance=5, num_samples=100),
            generate_department(name=SCIENCE, importance=3, mean=10, variance=5, num_samples=100)
        ]

        result = calculate_threat_score(departments)
        self.assertTrue(0 <= result <= 90)

    # Case 5:
    # - All departments have very low mean threat scores
    def test5(self):
        departments = [
            generate_department(name=ENGINEERING, importance=3, mean=1, variance=1, num_samples=100),
            generate_department(name=MARKETING, importance=3, mean=2, variance=1, num_samples=100),
            generate_department(name=FINANCE, importance=3, mean=3, variance=1, num_samples=100),
            generate_department(name=HR, importance=3, mean=1, variance=1, num_samples=100),
            generate_department(name=SCIENCE, importance=3, mean=0, variance=1, num_samples=100)
        ]

        result = calculate_threat_score(departments)
        self.assertTrue(0 <= result <= 90)

    # Case 6:
    # - Mixed importance and threat levels
    def test6(self):
        departments = [
            generate_department(name=ENGINEERING, importance=1, mean=30, variance=10, num_samples=100),
            generate_department(name=MARKETING, importance=4, mean=50, variance=10, num_samples=100),
            generate_department(name=FINANCE, importance=2, mean=70, variance=10, num_samples=100),
            generate_department(name=HR, importance=5, mean=90, variance=10, num_samples=100),
            generate_department(name=SCIENCE, importance=3, mean=60, variance=10, num_samples=100)
        ]

        result = calculate_threat_score(departments)
        self.assertTrue(0 <= result <= 90)

    # Case 7:
    # - One department has no threat scores (all zeros)
    def test7(self):
        departments = [
            generate_department(name=ENGINEERING, importance=3, mean=0, variance=0, num_samples=100),  # All zero
            generate_department(name=MARKETING, importance=3, mean=30, variance=10, num_samples=100),
            generate_department(name=FINANCE, importance=3, mean=40, variance=10, num_samples=100),
            generate_department(name=HR, importance=3, mean=50, variance=10, num_samples=100),
            generate_department(name=SCIENCE, importance=3, mean=60, variance=10, num_samples=100)
        ]

        result = calculate_threat_score(departments)
        self.assertTrue(0 <= result <= 90)

    # Case 8:
    # - Extreme variance with all departments having high threat scores
    def test8(self):
        departments = [
            generate_department(name=ENGINEERING, importance=3, mean=80, variance=20, num_samples=100),
            generate_department(name=MARKETING, importance=3, mean=70, variance=20, num_samples=100),
            generate_department(name=FINANCE, importance=3, mean=90, variance=20, num_samples=100),
            generate_department(name=HR, importance=3, mean=85, variance=20, num_samples=100),
            generate_department(name=SCIENCE, importance=3, mean=75, variance=20, num_samples=100)
        ]

        result = calculate_threat_score(departments)
        self.assertTrue(0 <= result <= 90)

    # Case 9:
    # - All departments have a high degree of importance but varied scores
    def test9(self):
        departments = [
            generate_department(name=ENGINEERING, importance=5, mean=30, variance=15, num_samples=100),
            generate_department(name=MARKETING, importance=4, mean=60, variance=15, num_samples=100),
            generate_department(name=FINANCE, importance=5, mean=45, variance=15, num_samples=100),
            generate_department(name=HR, importance=4, mean=50, variance=15, num_samples=100),
            generate_department(name=SCIENCE, importance=5, mean=55, variance=15, num_samples=100)
        ]

        result = calculate_threat_score(departments)
        self.assertTrue(0 <= result <= 90)

    # Case 10:
    # - Each department has a different number of users
    def test10(self):
        departments = [
            generate_department(name=ENGINEERING, importance=3, mean=30, variance=10, num_samples=50),  # 50 users
            generate_department(name=MARKETING, importance=3, mean=40, variance=10, num_samples=150),  # 150 users
            generate_department(name=FINANCE, importance=3, mean=60, variance=10, num_samples=30),  # 30 users
            generate_department(name=HR, importance=3, mean=20, variance=10, num_samples=100),  # 100 users
            generate_department(name=SCIENCE, importance=3, mean=10, variance=10, num_samples=200)  # 200 users
        ]

        result = calculate_threat_score(departments)
        self.assertTrue(0 <= result <= 90)