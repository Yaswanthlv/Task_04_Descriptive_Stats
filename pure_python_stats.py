import csv
import math
from collections import defaultdict, Counter

# --------- Utility Functions ----------

def is_float(value):
    try:
        float(value)
        return True
    except ValueError:
        return False

def mean(values):
    return sum(values) / len(values) if values else 0

def std_dev(values, mean_val):
    return math.sqrt(sum((x - mean_val) ** 2 for x in values) / len(values)) if values else 0

def get_column_stats(col_data):
    stats = {}
    numeric_values = [float(v) for v in col_data if is_float(v)]
    if numeric_values:
        stats["count"] = len(numeric_values)
        stats["mean"] = round(mean(numeric_values), 3)
        stats["min"] = min(numeric_values)
        stats["max"] = max(numeric_values)
        stats["std_dev"] = round(std_dev(numeric_values, stats["mean"]), 3)
    else:
        counter = Counter(col_data)
        stats["unique_count"] = len(counter)
        stats["most_common"] = counter.most_common(1)[0] if counter else ("N/A", 0)
    return stats

def guess_data_type(values):
    # Infer if a column is numeric or not
    sample = [v for v in values if v.strip() != ""]
    floats = [v for v in sample if is_float(v)]
    return "Numeric" if len(floats) >= 0.8 * len(sample) else "Categorical"

# --------- Main Analysis Code ----------

def analyze_dataset(file_path):
    with open(file_path, 'r', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        data = list(reader)

    print("============================================")
    print("Initial Exploratory Data Analysis (EDA)")
    print("============================================")

    num_rows = len(data)
    num_cols = len(data[0]) if data else 0
    print(f"Total Rows: {num_rows}")
    print(f"Total Columns: {num_cols}\n")

    column_data = defaultdict(list)
    missing_counts = {}

    for row in data:
        for col, val in row.items():
            column_data[col].append(val)

    for col, values in column_data.items():
        missing = sum(1 for v in values if v.strip() == "")
        dtype = guess_data_type(values)
        print(f"{col}: Type={dtype}, Missing={missing}")

    print("\n============================================")
    print("Overall Dataset Statistics")
    print("============================================")
    for col, values in column_data.items():
        print(f"\n--- Column: {col} ---")
        stats = get_column_stats(values)
        for k, v in stats.items():
            print(f"{k}: {v}")

    # -------- Grouped by prime_genre --------
    print("\n============================================")
    print("Grouped by 'prime_genre'")
    print("============================================")
    genre_group = defaultdict(lambda: defaultdict(list))
    for row in data:
        genre = row["prime_genre"]
        for col, val in row.items():
            genre_group[genre][col].append(val)

    for genre, cols in genre_group.items():
        print(f"\n--- Genre: {genre} ---")
        for col, values in cols.items():
            stats = get_column_stats(values)
            print(f"  > {col}:")
            for k, v in stats.items():
                print(f"    {k}: {v}")

    # -------- Grouped by prime_genre + track_name --------
    print("\n============================================")
    print("Grouped by 'prime_genre' + 'track_name'")
    print("============================================")
    combined_group = defaultdict(lambda: defaultdict(list))
    for row in data:
        key = (row["prime_genre"], row["track_name"])
        for col, val in row.items():
            combined_group[key][col].append(val)

    for (genre, track), cols in list(combined_group.items())[:5]:  # Limit output
        print(f"\n--- Genre: {genre}, App: {track} ---")
        for col, values in cols.items():
            stats = get_column_stats(values)
            print(f"  > {col}:")
            for k, v in stats.items():
                print(f"    {k}: {v}")

if __name__ == "__main__":
    # Replace with your actual dataset path
    analyze_dataset("data/AppleStore.csv")
