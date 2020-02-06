from collections import namedtuple

processors = [
    str,
    str,
    float,
    int,
    str
]

def process_data(proccessors, data):
    for process, item in zip(processors, data):
        yield process(item)

def main():
    with open("Datasets/data_person_1000000.csv","r") as file:
        people_strings = file.read().splitlines()

        Person = namedtuple("Person", people_strings[0])
        # example_bob = Person("Bob", "TheBuilder", 24.5, 0.1, "black")

        people = []
        for string in people_strings[1:]:
            
            # first, last, age, worth, eye_colour = string.split(".")
            # people.append(Person(first, last, age, worth, eye_colour))
            people.append(Person(*process_data(processors, string.split(","))))

        # print(people[100:110])

        return people

if __name__ == "__main__":
    main()