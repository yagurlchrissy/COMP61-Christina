class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.child = None

    def add_child(self, child):
        self.child = child

    def print_family_line(self):
        print(f"{self.name} ({self.age})")
        if self.child is not None:
            self.child.print_family_line()

    def count_large_age_gaps(self, gap_limit):
        if self.child is None:
            return 0
        gap = self.age - self.child.age
        count = 1 if gap > gap_limit else 0
        return count + self.child.count_large_age_gaps(gap_limit)


def build_family_line():
    name = input("Enter person's name: ")
    age = int(input(f"Enter {name}'s age: "))
    person = Person(name, age)
    has_child = input(f"Does {name} have a child? (yes/no): ").lower()
    if has_child == "yes":
        child = build_family_line()
        person.add_child(child)
    return person


def main():
    print("Welcome to the Generational Gap Checker!")
    root_person = build_family_line()
    print("\nHere is your family line:\n")
    root_person.print_family_line()
    gap_limit = int(input("\nEnter the minimum age gap to check between generations: "))
    gap_count = root_person.count_large_age_gaps(gap_limit)
    print(f"\nNumber of generations with an age gap greater than {gap_limit}: {gap_count}")


if __name__ == "__main__":
    main()
