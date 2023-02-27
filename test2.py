member_info = {"Joo":39, "Lee":35, "Kim": 20}

for name, age in member_info.items():
    print(f"{name} {age}")
    
member_name = member_info.keys()
member_values = member_info.values()
print(member_name)
print(member_values)

print(f"Average: {(sum(member_values)/len(member_values)):.3f}")
