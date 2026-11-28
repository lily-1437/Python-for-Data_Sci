students = [
    {"name": "Amina", "major": "AMDS"},
    {"name": "Maya", "major": "Economics"},
    {"name": "Disha", "major": "AMDS"},
    {"name": "Nora", "major": "Public Health"},
    {"name": "Lina", "major": "Economics"}
]

groups = {}
for s in students:
    major = s["major"]
    if major not in groups:
        groups[major] = []         # create empty list first time
    groups[major].append(s["name"])

counts = {}
for major, names in groups.items():
    counts[major] = len(names)

print("Groups:", groups)
print("Counts:", counts)