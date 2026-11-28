scores = {
    "Amina": {"python": 82, "statistics": 76, "calculus": 88},
    "Maya": {"python": 58, "statistics": 64, "calculus": 61},
    "Disha": {"python": 91, "statistics": 89, "calculus": 94},
    "Nora": {"python": 45, "statistics": 52, "calculus": 56}
}

results = {}
best_student = None
best_avg = -1

for name, subjects in scores.items():
    total = 0
    for mark in subjects.values():
        total += mark
    avg = total / len(subjects)

    status = "Pass" if avg >= 60 else "Fail"
    results[name] = {"average": round(avg, 2), "status": status}

    if avg > best_avg:
        best_avg = avg
        best_student = name

print("Results:", results)
print(f"Highest average: {best_student} ({best_avg:.2f})")