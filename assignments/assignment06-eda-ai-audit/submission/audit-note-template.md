# Table 1 Audit Note

## Cohort

The intended cohort includes adults aged 20 to 80 (inclusive). In the code, the filter excludes those exactly 20 and 80, contradicting the intended stated cohort. This matters since not correcting this would mean misrepresenting the cohort through missing data on those aged 20 and 80. They would not be included in the analysis. 

The appropriate corrections would be to change the code to also include those age 20 and 80 as follows:
```{r}
#| label: planted-cohort
analysis_df <- nhanes |>
  filter(Age > 20, Age < 80, Age==20, Age==80) |>
  na.omit()
```

An alternate correction would be to redefine the cohort to be adults aged 20 to 80 exclusive. 


## Missingness

Before summarizing, check Age, BMI, and IncomeGroup for missing values. The starter has code na.omit() which drops rows for missingness in unused columns. 

## Planted Issues

| Issue | Category | Why it matters | Corrected approach |

|var() was reported under the label "SD" for BMI and Age|Correctness|Variance is SD squared, but not SD itself. The value in the table is not SD, but variance.|Use sd() instead of var() and keep the column labels OR change the label to say variance instead of SD.|

|Fallback path list resolved against the current working directory, which loads whichever file is found first. This changes with where the document is rendered from.| Reproducibility |Two people can run the same script and produce different Table 1 values.|Use 1 project-anchored path, so that differing values from the same code is avoided.|

|"Income determines BMI" and "statistically significant" with no statistical test done| Interpretation |There were no statistical tests done to concretely interpret that income determines BMI. This shows causality which is not tested for. Statistical significance is also not tested for.|Use more appropriate, descriptive language rather than implying an association between income and BMI OR run statistical tests to establish an association betweent income and BMI to describe using associaion language.|

|"Downloaded fresh from the NHANES website last week"| Stewardship |Date, URL, file version are not stated explicitly. Additionally the filename (nhanes_equity_v6.csv) implies that the original csv file was either renamed or derived for the class, running the risk of misstating the source.|Writing a provenance statement that names the source, access date, URL, etc. would address this.|

|IncomeGroup variable is grouped with no checks of levels/order after omitting with na.omit()| Correctness |If IncomeGroup is stored as text, rows are in alphabetical order and not in a meaningful order (i.e. low to high).|Convert to an ordered factor so the table order and group counts are correct.|

## AI-Use Check

Copilot helped with the more technical aspects of appropriate "why this matters" and corrections for the planted issues. 
