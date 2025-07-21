import pandas as pd

# Load original dataset
df = pd.read_csv("spreadspoke_scores.csv")

# Filter: 2020–2023 games only
df = df[df["schedule_season"] >= 2020]

# Drop games with missing scores
df = df.dropna(subset=["score_home", "score_away"])

# Create a new binary column: home team wins
df["home_win"] = (df["score_home"] > df["score_away"]).astype(int)

# Select relevant columns
df_model = df[[
    "schedule_date", "team_home", "team_away",
    "score_home", "score_away",
    "spread_favorite", "over_under_line",
    "stadium_neutral", "home_win"
]]

# Save cleaned file
df_model.to_csv("nfl_games_2020_2023_clean.csv", index=False)
print("✅ Cleaned file saved as nfl_games_2020_2023_clean.csv")
