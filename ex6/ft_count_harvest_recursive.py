
def ft_count_harvest_recursive() -> None:
    days = int(input("Days until harvest: "))

    def loop_harvest(d: int = 1) -> None:
        if d <= days:
            print(f"Day {d}")
            loop_harvest(d + 1)

    loop_harvest()
    print("Harvest time!")




# >>> ft_count_harvest_recursive()
# Days until harvest: 5
# Day 1
# Day 2
# Day 3
# Day 4
# Day 5
# Harvest time!