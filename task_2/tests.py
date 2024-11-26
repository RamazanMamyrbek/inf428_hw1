import unittest
from util import *


class TestThreatScores(unittest.TestCase):

    # Case 1:
    # All departments has quite same high scores.
    def test_case1(self):
        parameters = [(85, 2, 100), (84, 3, 100), (86, 2, 100), (83, 3, 100), (87, 2, 100)]
        output_file = 'test_case_1.csv'
        df = read_or_generate_csv(parameters, output_file)
        data = convert_threat_scores_to_array(df)

        actual = calculate_threat_score(data=data)

        self.assertTrue(78 <= actual <= 90)

    # Case 2:
    # One department has high mean threat score, other low
    def test_case2(self):
        parameters = [(80, 4, 100), (30, 4, 100), (23, 3, 100), (10, 5, 100), (15, 3, 100)]
        output_file = 'test_case_2.csv'

        df = read_or_generate_csv(parameters, output_file)
        data = convert_threat_scores_to_array(df)

        actual = calculate_threat_score(data)

        self.assertTrue(75 <= actual <= 85)

    # Case 3: All departments have the same mean threat scores,
    # but in one department there are really high threat
    # score users.
    def test_case3(self):
        parameters = [(80, 40, 100), (25, 3, 100), (30, 10, 100), (20, 4, 100), (15, 2, 100)]
        output_file = 'test_case_3.csv'

        df = read_or_generate_csv(parameters, output_file)
        data = convert_threat_scores_to_array(df)

        actual = calculate_threat_score(data)
        print(actual)

        self.assertTrue(60 <= actual <= 85)

    # Case 4:
    # All departments has a different number of users and quite high mean threat scores
    def test_case4(self):
        parameters = [(80, 4, 50), (74, 3, 10), (69, 2, 100), (85, 4, 83), (78, 2, 5)]
        output_file = 'test_case_4.csv'

        df = read_or_generate_csv(parameters, output_file)
        data = convert_threat_scores_to_array(df)

        actual = calculate_threat_score(data)
        print(actual)

        self.assertTrue(75 <= actual <= 90)
