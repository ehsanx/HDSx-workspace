# AI-Use Note

## Audit trail

### 1. Load and inspect the NHANES data

**AI prompt:** Help me load the NHANES CSV in R.

**AI output:**

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

**Verified:**

- Ran the code and inspected the terminal output; it showed 105,626 rows.
- Checked the code to confirm that it imported the NHANES equity data.

### 2. Create the R BMI summary

**AI prompt:** In R, produce a descriptive BMI summary by `IncomeGroup` and
`Gender`. Include adults ages 20 through 80, inclusive, with non-missing BMI,
`IncomeGroup`, and `Gender`. Report the number of observations, mean BMI, and
sample standard deviation by group, rounded to one decimal place.

**AI output:**

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

**Verified:** Ran the R code and confirmed the table had the expected columns
and values.

### 3. Refactor the R summary into a function

**AI prompt:** Refactor the BMI summary into a reusable R function that takes a
data frame and applies the same filters and summary steps.

**AI output:**

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

**Verified:** Ran the function and confirmed its output matched the original
pipeline.

### 4. Translate the analysis to Python

**AI prompt:** Create `translation.ipynb` with the same analysis as the R code,
using pandas, the same filters, and the same summary steps. Include a reusable
function that takes a DataFrame and returns the same summary.

**AI output:** Created `translation.ipynb` to load the CSV, filter the records,
and summarize BMI by income group and gender in Python.

**Verified:**

- Selected **Run All** and the Python 3.11.16 kernel.
- Compared the notebook's summary tables with the R results. My original note
  called these “visual diagrams”; they are summary tables.

### 5. Create and use a Python helper

**AI prompt:** Create `helpers.py` with at least one reusable Python helper
called from the notebook.

**AI output:** Created `summarize_bmi_by_income_gender()` in `helpers.py` to
apply the same filters and summary steps to a DataFrame.

**Verified:** Checked that the notebook imports and calls the helper, then ran
the notebook and confirmed the grouped results.

### 6. Complete the parity table

**AI prompt:** Complete a parity table comparing row counts, filtered row
counts, grouping labels, and rounded summary values.

**AI output:** Created `parity-table.csv`.

**Verified:** Compared the R and Python values and checked the table against the
provided template.

## What AI helped with

Copilot helped load and summarize the NHANES data in R, refactor the R summary
into a function, translate the analysis to Python/pandas, create a reusable
helper, and complete the parity table.

## What I changed

I kept the filters consistent in both languages: non-missing BMI,
`IncomeGroup`, `Gender`, and `Age`, with ages 20 through 80 inclusive. I
connected the notebook to `helpers.py` and recorded the grouped results and
comparisons in the parity table.

## How I verified the result

I rendered the Quarto report and ran the notebook code with the helper. Both
versions returned 105,626 raw rows, 50,851 filtered rows, and six groups. I
compared all group labels, counts, rounded means, and sample standard
deviations; they matched.
