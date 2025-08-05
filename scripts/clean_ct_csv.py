# clean_ct_stimulant_analysis.py

import pandas as pd

def clean_ct_stimulant_data(input_path, output_path):
    df = pd.read_csv(input_path)

    df_filtered = df[[
        "Date",
        "Patient Residence",
        "Stimulant Prescription Count",
        "Stimulant Rate per 1,000 Residents"
    ]].copy()

    df_filtered.columns = [
        "report_period",
        "town",
        "prescription_count",
        "rate_per_1000"
    ]

    df_filtered = df_filtered.sort_values(by=["report_period", "town"])

    # Save cleaned CSV
    df_filtered.to_csv(output_path, index=False)
    print(f"Cleaned data saved to: {output_path}")

if __name__ == "__main__":
    input_csv = "data/raw/ct_stimulant_reports.csv"      
    output_csv = "data/clean/cleaned_ct_stimulant_reports.csv"
    clean_ct_stimulant_data(input_csv, output_csv)
