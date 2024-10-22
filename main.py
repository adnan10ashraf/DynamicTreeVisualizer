import pandas as pd

people = {}
parents = {}

def process_data():
    df = pd.read_csv("people.csv")
    for _, row in df.iterrows():
        name = f'{row['first_name']} {row['last_name']}'
        people[row['id']] = name
    df2 = pd.read_csv('parents.csv')
    for _, row in df2.iterrows():
        parents[row['child_id']] = (row['father_id'], row['mother_id'])



if __name__ == "__main__":
    process_data()
    print(people)
    print(parents)