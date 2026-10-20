# AI-Use Note

## Audit trail
# AI prompt: Create a dplyr function to categorize adult BMI and summarize by gender.
# Verified: Checked the NHANES column names and ran the function; it returned 8 groups.

# AI prompt: Create a reusable function that returns n, mean, and SD for a numeric vector.
# Verified: Ran it on nhanes$Age; it returned n = 105626, mean = 31.7, and SD = 24.9.

## What AI helped with
Copilot helped draft the `bmi_categories_by_gender()` dplyr function and the reusable `mean_sd()` function, and helped troubleshoot missing setup in the R Interactive session.

## What I changed
I used `nhanes$Age` as the example input for `mean_sd()` so the function demonstrates that it works with a variable other than BMI. I also placed the BMI function under the analysis-ready-table task heading.

## How I verified the result
I checked the requested columns against the NHANES CSV and ran both functions on the local data after loading tidyverse. The BMI function returned eight gender and BMI-category groups; `mean_sd(nhanes$Age)` returned 105,626 non-missing values, a mean of 31.7, and a standard deviation of 24.9. These are descriptive summaries, not survey-weighted population estimates.
