"""practice with dictionaries"""

ice_cream: dict[str, int] = {"chocolate": 12, "vanilla": 8, "strawberry": 5}
ice_cream["mint"] = 3
print(ice_cream)

ice_cream.pop("mint")
print("after removing mint")
print(ice_cream)

print(f"Number of vanilla: {ice_cream['vanilla']}")

ice_cream["vanilla"] += 1
print(ice_cream)

print("mint" in ice_cream)
print("chocolate" in ice_cream)