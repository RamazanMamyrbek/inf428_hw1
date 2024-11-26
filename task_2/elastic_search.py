import numpy as np
import pandas as pd
from elasticsearch import Elasticsearch, helpers

es = Elasticsearch("http://localhost:9200")


def generate_random_data(mean, variance, num_samples):
    return np.random.randint(max(mean - variance, 0), min(mean + variance + 1, 90), num_samples)


def get_doc_for_testcase(index_name, test_case_id):
    df = pd.read_csv(f"test_case_{test_case_id}.csv")
    return {
        "_index": index_name,
        "_id": test_case_id,
        "_source": {
            "Department": df["Department"],
            "ThreatScore": df["ThreatScore"]
        }
    }


def populate_elastic_search(index_name, max_test_cases):
    data = []
    for test_case in range(1, max_test_cases + 1):
        document = get_doc_for_testcase(index_name, test_case)
        data.append(document)
    helpers.bulk(es, data)

if __name__ == '__main__':
    int count = 4
    populate_elastic_search('threat_scores', count)