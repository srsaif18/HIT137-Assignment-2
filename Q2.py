# Group Members:
# Mou Rani Biswas - 398778
# MD Saifur Rahman - 398921
# Nahid Hasan Sangram - 395231
# Mohammed Rifatul Alam - 399533
#
# HIT137 Assignment 2 - Question 2
# Temperature data analysis (Australia) across ALL stations and ALL years.
#
# Outputs:
#   1) average_temp.txt
#   2) largest_temp_range_station.txt
#   3) temperature_stability_stations.txt
#
# How to run (from this folder):
#   python Q2.py

from __future__ import annotations

import glob
import os
from typing import Dict, List, Tuple

import pandas as pd


MONTHS = [
    "January","February","March","April","May","June",
    "July","August","September","October","November","December"
]

SEASON_BY_MONTH = {
    "December": "Summer",
    "January": "Summer",
    "February": "Summer",
    "March": "Autumn",
    "April": "Autumn",
    "May": "Autumn",
    "June": "Winter",
    "July": "Winter",
    "August": "Winter",
    "September": "Spring",
    "October": "Spring",
    "November": "Spring",
}


def load_all_years(temps_dir: str) -> pd.DataFrame:
    """
    Loads ALL CSV files under temps_dir and returns one combined dataframe.

    Expected columns (based on the provided dataset):
      STATION_NAME, STN_ID, LAT, LON, January..December
    """
    pattern = os.path.join(temps_dir, "*.csv")
    files = sorted(glob.glob(pattern))
    if not files:
        raise FileNotFoundError(
            f"No CSV files found in '{temps_dir}'. "
            "Make sure the 'temperatures' folder exists next to this script."
        )

    frames: List[pd.DataFrame] = []
    for fp in files:
        df = pd.read_csv(fp)

        # Keep only the columns we need (safe even if extra columns exist)
        keep_cols = [c for c in ["STATION_NAME", "STN_ID"] + MONTHS if c in df.columns]
        missing = [c for c in ["STATION_NAME", "STN_ID"] + MONTHS if c not in df.columns]
        if missing:
            raise ValueError(f"File '{os.path.basename(fp)}' missing columns: {missing}")

        df = df[keep_cols].copy()

        # Ensure monthly columns are numeric (NaN remains NaN)
        for m in MONTHS:
            df[m] = pd.to_numeric(df[m], errors="coerce")

        frames.append(df)

    combined = pd.concat(frames, ignore_index=True)
    return combined


def seasonal_averages(combined: pd.DataFrame) -> Dict[str, float]:
    # Convert wide months -> long format
    long_df = combined.melt(
        id_vars=["STATION_NAME", "STN_ID"],
        value_vars=MONTHS,
        var_name="Month",
        value_name="Temp",
    )

    # Ignore missing values (NaN) automatically using mean(skipna=True)
    long_df["Season"] = long_df["Month"].map(SEASON_BY_MONTH)

    season_means = (
        long_df.dropna(subset=["Temp"])
              .groupby("Season", as_index=True)["Temp"]
              .mean()
              .to_dict()
    )

    # Ensure all seasons exist in output order
    ordered = {}
    for s in ["Summer", "Autumn", "Winter", "Spring"]:
        ordered[s] = float(season_means.get(s, float("nan")))
    return ordered


def station_ranges(combined: pd.DataFrame) -> pd.DataFrame:
    # Stack monthly values into one column per station across all years
    long_df = combined.melt(
        id_vars=["STATION_NAME", "STN_ID"],
        value_vars=MONTHS,
        var_name="Month",
        value_name="Temp",
    ).dropna(subset=["Temp"])

    grouped = long_df.groupby(["STATION_NAME", "STN_ID"], as_index=False)["Temp"].agg(["min", "max"])
    grouped = grouped.reset_index()
    grouped["range"] = grouped["max"] - grouped["min"]
    return grouped


def station_stability(combined: pd.DataFrame) -> pd.DataFrame:
    long_df = combined.melt(
        id_vars=["STATION_NAME", "STN_ID"],
        value_vars=MONTHS,
        var_name="Month",
        value_name="Temp",
    ).dropna(subset=["Temp"])

    # Use population standard deviation (ddof=0), common for full-dataset stability
    std_df = (
        long_df.groupby(["STATION_NAME", "STN_ID"], as_index=False)["Temp"]
              .std(ddof=0)
              .rename(columns={"Temp": "std"})
    )
    return std_df


def write_average_temp(path: str, season_means: Dict[str, float]) -> None:
    with open(path, "w", encoding="utf-8") as f:
        for season in ["Summer", "Autumn", "Winter", "Spring"]:
            val = season_means[season]
            # Format as one decimal place like the example
            f.write(f"{season}: {val:.1f}°C\n")


def write_largest_range(path: str, ranges_df: pd.DataFrame) -> None:
    max_range = ranges_df["range"].max()
    winners = ranges_df[ranges_df["range"] == max_range].copy()

    with open(path, "w", encoding="utf-8") as f:
        for _, row in winners.iterrows():
            name = row["STATION_NAME"]
            r = row["range"]
            mx = row["max"]
            mn = row["min"]
            f.write(f"{name}: Range {r:.1f}°C (Max: {mx:.1f}°C, Min: {mn:.1f}°C)\n")


def write_stability(path: str, std_df: pd.DataFrame) -> None:
    min_std = std_df["std"].min()
    max_std = std_df["std"].max()

    most_stable = std_df[std_df["std"] == min_std].copy()
    most_variable = std_df[std_df["std"] == max_std].copy()

    with open(path, "w", encoding="utf-8") as f:
        for _, row in most_stable.iterrows():
            f.write(f"Most Stable: {row['STATION_NAME']}: StdDev {row['std']:.1f}°C\n")
        for _, row in most_variable.iterrows():
            f.write(f"Most Variable: {row['STATION_NAME']}: StdDev {row['std']:.1f}°C\n")


def main() -> None:
    here = os.path.dirname(os.path.abspath(__file__))
    temps_dir = os.path.join(here, "temperatures")

    combined = load_all_years(temps_dir)

    season_means = seasonal_averages(combined)
    ranges_df = station_ranges(combined)
    std_df = station_stability(combined)

    write_average_temp(os.path.join(here, "average_temp.txt"), season_means)
    write_largest_range(os.path.join(here, "largest_temp_range_station.txt"), ranges_df)
    write_stability(os.path.join(here, "temperature_stability_stations.txt"), std_df)

    print("✅ Q2 complete: output files generated:")
    print(" - average_temp.txt")
    print(" - largest_temp_range_station.txt")
    print(" - temperature_stability_stations.txt")


if __name__ == "__main__":
    main()
