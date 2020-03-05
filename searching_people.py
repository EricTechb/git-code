from people_data import main as load_people_data
from binary_search import binary_search

def main():
    print("Starting process...")
    people_data = load_people_data()
    print("Loaded data")
    age_key = lambda person: person.age
    age_sorted  = sorted(people_data, key=age_key)
    print("Sorted data")
    age_result = binary_search(age_sorted, 66.6, key= age_key)


    def complex_key(person):
        if person.first.startswith("A") and person.eye_colour == "blue" and person.age == 66.6:
            if person.net_worth < 30000:
                return -1
            elif person.net_worth > 40000:
                return 1
            else:
                return 0
        else:
            return -1

    complex_sorted = sorted(people_data, key=complex_key)
    complex_result = binary_search(complex_sorted, 0, key=complex_key)

    print(f"Found index: {complex_result}")
    print(f"Person found: {complex_sorted[complex_result]}")

if __name__ == "__main__":
    main()