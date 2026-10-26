


def ft_count_harvest_iterative() -> None:
    days = int(input("Days until harvest: "))

    days_rg = range(1, days + 1)
    for x in days_rg:
        print(f"Day {x}")
    print("Harvest time!")

# >>> ft_count_harvest_iterative()
# Days until harvest: 5
# Day 1
# Day 2
# Day 3
# Day 4
# Day 5
# Harvest time!
