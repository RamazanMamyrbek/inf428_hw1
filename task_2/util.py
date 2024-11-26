import numpy as np
import os
import pandas as pd


def generate_random_data(mean, variance, num_samples):
    return np.random.randint(max(mean - variance, 0), min(mean + variance + 1, 90), num_samples)


def read_or_generate_csv(parameters, output_file):
    if os.path.exists(output_file):
        return pd.read_csv(output_file)
    departments = ["Engineering", "Marketing", "Finance", "HR", "Science"]
    department_data = []
    for department_id, (mean_score, score_variance, sample_count) in enumerate(parameters, start=1):
        scores = generate_random_data(mean_score, score_variance, sample_count)
        department_frame = pd.DataFrame({
            "Department": [departments[department_id-1]] * len(scores),
            "ThreatScore": scores
        })
        department_data.append(department_frame)
    final_data = pd.concat(department_data, ignore_index=True)
    final_data.to_csv(output_file, index=False)
    return final_data


def convert_threat_scores_to_array(data_frame):
    department_scores = data_frame.groupby("Department")["ThreatScore"].apply(list)
    return department_scores.tolist()


def calculate_threat_score(data):
    return max(calculate_single_threat_score(np.array(scores)) for scores in data)


def calculate_single_threat_score(scores):
    mean_score = np.mean(scores)
    variance = np.var(scores)
    if variance > 150:
        return np.mean([score for score in scores if (score - mean_score) ** 2 >= variance])
    return mean_score
