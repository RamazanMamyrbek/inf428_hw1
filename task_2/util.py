import numpy as np


def generate_random_data(mean, variance, num_samples):
    return np.random.randint(max(mean - variance, 0), min(mean + variance + 1, 90), num_samples)


def generate_department(name, importance, mean, variance, num_samples):
    department = {
        "name": name,
        "importance": importance,
        "threat_scores": generate_random_data(mean, variance, num_samples)
    }
    return department

def calculate_threat_score(departments):
    importance_sum = 0
    total_score = 0
    for department in departments:
        importance_sum += department["importance"]
        total_score += (department["importance"] * np.mean(department["threat_scores"]))
    return total_score / importance_sum
