# AI-Use Note

## Audit trail

# AI prompt: Help me load the NHANES CSV in R.
# AI output:
```r
library(tidyverse)

nhanes <- read_csv(
  "examples/nhanes-equity/data/nhanes_equity_v6.csv",
  show_col_types = FALSE
)

tibble(
  raw_row_count = nrow(nhanes),
  raw_column_count = ncol(nhanes),
  missing_bmi_count = sum(is.na(nhanes$BMI))
)
```
# Verified:
- I clicked the Run Cell button and inspected the terminal output (105,626 rows).
- I checked the code to double-check that the equity data was imported.

# AI prompt: In R, help me produce a descriptive BMI summary by IncomeGroup and Gender. More specifically, I want to include adults ages 20 through 80, inclusive, with non-missing BMI, IncomeGroup, and Gender. The summary should report the number of observations, mean BMI, and sample standard deviation of BMI for each income and gender combination. Mean and standard deviation should be rounded to one decimal place.
# AI output:
```r
nhanes_filtered <- nhanes |>
  filter(
    !is.na(BMI),
    !is.na(IncomeGroup),
    !is.na(Gender),
    !is.na(Age),
    Age >= 20,
    Age <= 80
  )

bmi_summary_pipeline <- nhanes_filtered |>
  group_by(IncomeGroup, Gender) |>
  summarise(
    n = n(),
    mean_bmi = round(mean(BMI), 1),
    sd_bmi = round(sd(BMI), 1),
    .groups = "drop"
  ) |>
  arrange(IncomeGroup, Gender)
```
# Verified: I ran the R code and confirmed the presence of a table with the expected columns and values.

# AI prompt: Help me refactor the BMI summary code into a reusable R function that takes a data frame as input and returns the same summary. The function should apply the same filters and summary steps to the input data frame.
# AI output:
```r
summarize_bmi_by_income_gender <- function(data) {
  data |>
    filter(
      !is.na(BMI),
      !is.na(IncomeGroup),
      !is.na(Gender),
      !is.na(Age),
      Age >= 20,
      Age <= 80
    ) |>
    group_by(IncomeGroup, Gender) |>
    summarise(
      n = n(),
      mean_bmi = round(mean(BMI), 1),
      sd_bmi = round(sd(BMI), 1),
      .groups = "drop"
    ) |>
    arrange(IncomeGroup, Gender)
}

bmi_summary_function <- summarize_bmi_by_income_gender(nhanes)
stopifnot(isTRUE(all.equal(bmi_summary_pipeline, bmi_summary_function)))
bmi_summary_function
```
# Verified: I ran the R code and confirmed that the output of the function matched the output of the original pipeline.

# AI prompt: Please help me create `translation.ipynb`, which is a Jupyter notebook that contains the same analysis as the R code above. The notebook should include the same filters and summary steps, and should produce the same output as the R code, using pandas. The notebook should also include a reusable function that takes a DataFrame as input and returns the same summary.
# AI output: `translation.ipynb` file created.
# Verified:
- I selected Run All in the `translation.ipynb` document and selected the Python 3.11.16 kernel.
- My original note said that visual diagrams matched the R output; the notebook output is summary tables, which I compared with the R summary.

# AI prompt: Create `helpers.py` with at least one reusable Python helper called from the notebook.
# AI output: Created `helpers.py` with a `summarize_bmi_by_income_gender()` function that takes a DataFrame and applies the same filters and summary steps.
# Verified: In the notebook, I confirmed the helper is imported and called, then checked that its output matches the R summary.

# AI prompt: Complete a parity table comparing row counts, filtered row counts, grouping labels, and rounded summary values.
# AI output: Created `parity-table.csv`.
# Verified: I double-checked that the parity-table format matched the template in `parity-table-template.csv` and compared the R and Python values.

## What AI helped with
Copilot helped load and summarize the NHANES data in R, refactor the R summary into a function, translate the analysis to Python/pandas, create a reusable helper, and complete the parity table.

## What I changed
I kept the filters consistent in both languages: non-missing BMI, IncomeGroup, Gender, and Age, with ages 20 through 80 inclusive. I connected the notebook to `helpers.py` and recorded the grouped results and comparisons in the parity table.

## How I verified the result
I rendered the Quarto report and ran the notebook code with the helper. Both versions returned 105,626 raw rows, 50,851 filtered rows, and six groups. I compared all group labels, counts, rounded means, and sample SDs; they matched.
