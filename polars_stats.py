import polars as pl

def analyze_with_polars(file_path):
    # Load dataset with Polars
    df = pl.read_csv(file_path)

    print("\n============================================")
    print("Overall Dataset Statistics (Polars)")
    print("============================================")
    # Describe numeric columns
    print(df.describe())

    # Categorical columns: unique counts and most frequent
    print("\n=== Unique Counts and Most Frequent Values (Categorical Columns) ===")
    for col in df.columns:
        if df[col].dtype == pl.Utf8:
            unique_count = df[col].n_unique()
            most_common = df.group_by(col).count().sort("count", descending=True).select(col).first()
            print(f"\n--- Column: {col} ---")
            print(f"Unique values: {unique_count}")
            print(f"Most frequent: {most_common[0]}")

    # -------- Grouped by prime_genre --------
    print("\n============================================")
    print("Grouped by 'prime_genre'")
    print("============================================")
    genre_grouped = df.group_by("prime_genre").agg([
        *[pl.col(c).mean().alias(f"{c}_mean") for c in df.columns if df[c].dtype in [pl.Float64, pl.Int64]],
        *[pl.col(c).min().alias(f"{c}_min") for c in df.columns if df[c].dtype in [pl.Float64, pl.Int64]],
        *[pl.col(c).max().alias(f"{c}_max") for c in df.columns if df[c].dtype in [pl.Float64, pl.Int64]],
        *[pl.col(c).std().alias(f"{c}_std") for c in df.columns if df[c].dtype in [pl.Float64, pl.Int64]]
    ])
    print(genre_grouped)

    # -------- Grouped by prime_genre + track_name --------
    print("\n============================================")
    print("Grouped by 'prime_genre' + 'track_name'")
    print("============================================")
    combo_grouped = df.group_by(["prime_genre", "track_name"]).agg([
        *[pl.col(c).mean().alias(f"{c}_mean") for c in df.columns if df[c].dtype in [pl.Float64, pl.Int64]],
        *[pl.col(c).min().alias(f"{c}_min") for c in df.columns if df[c].dtype in [pl.Float64, pl.Int64]],
        *[pl.col(c).max().alias(f"{c}_max") for c in df.columns if df[c].dtype in [pl.Float64, pl.Int64]],
        *[pl.col(c).std().alias(f"{c}_std") for c in df.columns if df[c].dtype in [pl.Float64, pl.Int64]]
    ])
    print(combo_grouped.head(5))  # limit to first 5 groups

if __name__ == "__main__":
    # Replace with your actual dataset path
    analyze_with_polars("data/AppleStore.csv")
