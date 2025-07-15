import pandas as pd

def analyze_with_pandas(file_path):
    # Load dataset
    df = pd.read_csv(file_path)

    print("\n============================================")
    print("Overall Dataset Statistics (Pandas)")
    print("============================================")
    print(df.describe(include='all'))

    # Categorical columns: unique counts and most frequent
    print("\n=== Unique Counts and Most Frequent Values (Categorical Columns) ===")
    cat_cols = df.select_dtypes(include='object').columns
    for col in cat_cols:
        print(f"\n--- Column: {col} ---")
        print(f"Unique values: {df[col].nunique()}")
        print(f"Most frequent: {df[col].mode().iloc[0]} ({df[col].value_counts().iloc[0]} occurrences)")

    # -------- Grouped by prime_genre --------
    print("\n============================================")
    print("Grouped by 'prime_genre'")
    print("============================================")
    genre_group = df.groupby('prime_genre')

    # Numeric stats for each group
    grouped_numeric = genre_group.describe().transpose()
    print(grouped_numeric)

    # Most frequent non-numeric per group
    print("\n=== Most Frequent Values per Genre (for Categorical Columns) ===")
    for genre, group_df in genre_group:
        print(f"\n--- Genre: {genre} ---")
        for col in cat_cols:
            most_common = group_df[col].mode()
            if not most_common.empty:
                print(f"{col}: {most_common.iloc[0]}")

    # -------- Grouped by prime_genre + track_name --------
    print("\n============================================")
    print("Grouped by 'prime_genre' + 'track_name'")
    print("============================================")
    combo_group = df.groupby(['prime_genre', 'track_name'])
    combo_stats = combo_group.describe().transpose()
    print(combo_stats.head(30))  # Limit output for readability

if __name__ == "__main__":
    # Replace with your dataset path
    analyze_with_pandas("data/AppleStore.csv")
