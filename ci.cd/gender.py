def detect_gender(name):
    female_names = ["Alice", "Emma", "Olivia", "Lily"]
    male_names = ["James", "William", "Michael", "Henry"]

    if name in female_names:
        return "Female"
    elif name in male_names:
        return "Male"
    else:
        return "Unknown"