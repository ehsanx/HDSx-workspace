import pandas as pd


def summarize_bmi_by_income_gender(data: pd.DataFrame) -> pd.DataFrame:
    """Summarize BMI by income group and gender for adults ages 20 through 80."""
    analysis_columns = ["BMI", "IncomeGroup", "Gender", "Age"]
    filtered = data.dropna(subset=analysis_columns)
    filtered = filtered.loc[filtered["Age"].between(20, 80, inclusive="both")]

    summary = (
        filtered.groupby(["IncomeGroup", "Gender"])
        .agg(
            n=("BMI", "size"),
            mean_bmi=("BMI", "mean"),
            sd_bmi=("BMI", "std"),
        )
        .reset_index()
        .sort_values(["IncomeGroup", "Gender"])
        .reset_index(drop=True)
    )
    summary[["mean_bmi", "sd_bmi"]] = summary[["mean_bmi", "sd_bmi"]].round(1)
    return summary
