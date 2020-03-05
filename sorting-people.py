from people_data import main as load_people_data
from pprint import pprint

def main():
    people_data =load_people_data()

    chosen_people = people_data[:40]

    default_sort = sorted(chosen_people)
    reversed_default = sorted(chosen_people, reverse=True)

    age_fc = lambda person: person.age
    # def age_fc(person):
    #     return person.age

    def age_worth_fc(person):
        return person.age * 1000 + person.net_worth

    # def networth_fc(person):
    #     return person.net_worth


    # networth_sort =sorted(chosen_people, key=networth_fc)
    #age_sort = sorted(chosen_people, key=age_fc)
    complex_sort = sorted(chosen_people, key=age_worth_fc)

    # pprint(reversed_default)
    pprint(complex_sort)

if __name__ == "__main__":
    main()