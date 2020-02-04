from pprint import pprint

import yaml
from neo4j import GraphDatabase


#################### Drop all constraints ####################
#     for constraint in session.run("CALL db.constraints"):
#             session.run("DROP " + constraint[0])


if __name__ == "__main__":
    with open('config.yaml', 'r', newline='') as f:
        config = yaml.safe_load(f)

    uri = "bolt://localhost:7687"
    driver = GraphDatabase.driver(uri, auth=(config['database']['auth']['name'], config['database']['auth']['password']))

    with driver.session() as session:
        result = session.run(return_all())
        pprint((result.data()))