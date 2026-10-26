
def ft_seed_inventory(seed_type: str, quantity: int, unit: str) -> None:   
    if unit == "packets":
        print(f"{seed_type.capitalize()} seeds: {quantity} {unit} available")
    elif unit == "grams":
        print(f"{seed_type.capitalize()} seeds: {quantity} {unit} total")
    elif unit == "area":
        print(f"{seed_type.capitalize()} seeds: covers {quantity} square meters")
    else: 
        print("Unknown unit type")



# >>> ft_seed_inventory("tomato", 15, "packets")
# Tomato seeds: 15 packets available
# >>> ft_seed_inventory("carrot", 8, "grams")
# Carrot seeds: 8 grams total
# >>> ft_seed_inventory("lettuce", 12, "area")
# Lettuce seeds: covers 12 square meters
