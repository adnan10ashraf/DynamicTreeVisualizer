import pandas as pd

people = {}
parents = {}

def process_data():
    df = pd.read_csv("people.csv")
    for _, row in df.iterrows():
        name = f'{row['first_name']} {row['last_name']}'
        people[name] = row['id'] 



if __name__ == "__main__":
    process_data()
    print(people)