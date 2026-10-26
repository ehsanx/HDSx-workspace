# Visual Audit Note

## Plot Question

Write the descriptive question the plot answers.

## Issues Checked

<!-- AI-EDIT(2026-06-11): SS-035 — worked example row added — needs review -->
The first row is a worked example of the expected shape — replace it with your own issue.

| Issue | Category | Why it matters | Correction |
| y axis is misleading | Correctness|because the plot actually use the unweighted mean to calculate the bmi, instead of just bmi, which can be misleading | in labs, instead of y = "BMI", use y = "MEAN BMI" |
| the missing values are filtered without caption | Silent missingness | since we silently filter out the missing value, without informing the readers that the dataset has missing values | add the caption : # BMI AND IncomeGroup column has missing values, which is filtered here near the line "filter(!is.na(BMI), !is.na(IncomeGroup)" |
| scales on y axis starts from 24 | design | The differences between groups will look smaller than they did on the 24–28 scale, because the viewer can see them relative to the full distance from zero. | replace " scale_y_continuous(limits = c(24, 28)) + " with " expand_limits(y = 0) +" | 
| the subtitle "drives" implies the causal effect | Interpretation | becasue observational study cannot imply causal effects | change " drives" to "associate" |


| *Example: y-axis starts at 22 instead of 0* | *Correctness* | *Exaggerates the BMI gap between groups, suggesting a larger difference than the data show* | *Start the y-axis at 0 (or show the full data range) and state the axis choice in the caption* |
|  | Correctness |  |  |
|  | Design |  |  |
|  | Interpretation |  |  |

## Final Caption

Write the final caption with data source, statistic, exclusions, and limitation.

## AI-Use Check

State what AI helped with and how the code, labels, and claims were verified.
