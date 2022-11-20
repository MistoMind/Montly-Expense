import pandas as pd
from person import Person
import private_data

ITEM_COL = 0
COST_COL = 1
PERSON_COL = 2
NON_CONTRIBUTOR_COL = 3
persons_name = private_data.people


# Creating Person's
def create_people():
    persons = []

    for p in persons_name:
        person = Person(p)
        persons.append(person)

    return persons


# Calculating Spending
def calculate_spending_all(persons, data):
    for p in persons:
        p_spending = list(pd.to_numeric((data[data[PERSON_COL] == p.name][COST_COL])))
        p.calculate_spend(p_spending)


# Calculate Give/Take
def calculate_give_take(persons, data):
    non_contributors = list(data[NON_CONTRIBUTOR_COL].unique())

    for person in non_contributors:
        if person is not None:
            no_con_this = [x.strip() for x in person.split(',')]
            part_total = sum(pd.to_numeric(data[data[NON_CONTRIBUTOR_COL] == person][COST_COL]))
            contributors = [i for i in persons_name if i not in no_con_this]
            per_person_cost = part_total / (len(contributors))
            # print("They do not contribute:", no_con_this)
        else:
            contributors = persons_name
            part_total = sum(pd.to_numeric(data[data[NON_CONTRIBUTOR_COL].isnull()][COST_COL]))
            per_person_cost = part_total / len(persons)

        # print("Total sum consumed:", part_total)
        # print("They will contribute:", contributors)
        # print("Each person contribution:", per_person_cost)

        for p in persons:
            if p.name in contributors:
                p.give += per_person_cost
