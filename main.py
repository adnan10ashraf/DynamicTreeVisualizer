import pandas as pd

people = {}
parents = {}

def process_data():
    df = pd.read_csv("people.csv")
    for _, row in df.iterrows():
        name = f"{row['first_name']} {row['last_name']}"
        people[row['id']] = name
    df2 = pd.read_csv('parents.csv')
    for _, row in df2.iterrows():
        parents[row['child_id']] = (row['father_id'], row['mother_id'])

def find_ancestors(person_id):
    queue = [person_id]
    res = []
    while queue:
        id = queue.pop(0)
        if id in parents:
            queue.extend(parents[id])
        res.append(people[id])
    return res

def find_common_ancestors(p1, p2):
    ancestors1 = set(find_ancestors(p1))
    ancestors2 = set(find_ancestors(p2))
    ancestors1.intersection_update(ancestors2)
    return ancestors1


if __name__ == "__main__":
    process_data()
    print(people)
    print(parents)
    print(find_ancestors(0))
    print(find_common_ancestors(0,5))