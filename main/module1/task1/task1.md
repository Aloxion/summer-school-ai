task1
================
Anton Sandbye
2025-08-04

``` r
mydata <- read.csv("DATASET1.csv")
```

``` r
names(mydata)
```

    ## [1] "ID"            "civil_status"  "cancer_family" "prostdtfirst" 
    ## [5] "metastasis"    "date_met"      "birthdate"

``` r
summary(mydata)
```

    ##        ID          civil_status   cancer_family    prostdtfirst      
    ##  Min.   :   1.0   Min.   :1.000   Min.   :0.0000   Length:1159       
    ##  1st Qu.: 290.5   1st Qu.:1.000   1st Qu.:0.0000   Class :character  
    ##  Median : 580.0   Median :1.000   Median :1.0000   Mode  :character  
    ##  Mean   : 580.0   Mean   :1.303   Mean   :0.5375                     
    ##  3rd Qu.: 869.5   3rd Qu.:2.000   3rd Qu.:1.0000                     
    ##  Max.   :1159.0   Max.   :2.000   Max.   :1.0000                     
    ##    metastasis       date_met          birthdate        
    ##  Min.   :0.0000   Length:1159        Length:1159       
    ##  1st Qu.:0.0000   Class :character   Class :character  
    ##  Median :0.0000   Mode  :character   Mode  :character  
    ##  Mean   :0.3632                                        
    ##  3rd Qu.:1.0000                                        
    ##  Max.   :1.0000

``` r
str(mydata)
```

    ## 'data.frame':    1159 obs. of  7 variables:
    ##  $ ID           : int  1 2 3 4 5 6 7 8 9 10 ...
    ##  $ civil_status : int  1 2 2 2 2 2 1 1 1 1 ...
    ##  $ cancer_family: int  1 0 0 0 0 0 1 1 1 0 ...
    ##  $ prostdtfirst : chr  "2017-03-16" "2005-03-31" "2017-08-08" "2008-01-02" ...
    ##  $ metastasis   : int  0 0 0 0 0 0 0 0 0 0 ...
    ##  $ date_met     : chr  NA NA NA NA ...
    ##  $ birthdate    : chr  "1935-01-01" "1942-01-01" "1959-01-01" "1934-02-01" ...

## Are the variables correctly recognized by the software (e.g. are categorical variables recognized as categorical, and numerical variables recognized as numerical)?

No, they are not set correctly dates are in chr type and not correct
data type

``` r
data = mydata %>% mutate(
  prostdtfirst = ymd(prostdtfirst),
  date_met = ymd(date_met),
  birthdate = ymd(birthdate)
)
```

- Do we have any missing data?

Yes, there is missing data for date_met in several rows.

``` r
data %>% summarise_all(funs(sum(is.na(.))))
```

    ## Warning: `funs()` was deprecated in dplyr 0.8.0.
    ## ℹ Please use a list of either functions or lambdas:
    ## 
    ## # Simple named list: list(mean = mean, median = median)
    ## 
    ## # Auto named with `tibble::lst()`: tibble::lst(mean, median)
    ## 
    ## # Using lambdas list(~ mean(., trim = .2), ~ median(., na.rm = TRUE))
    ## Call `lifecycle::last_lifecycle_warnings()` to see where this warning was
    ## generated.

    ##   ID civil_status cancer_family prostdtfirst metastasis date_met birthdate
    ## 1  0            0             0            0          0      738         0

## With information available in DATASET 1, make a summary table describing the study population, e.g.:

First, we create two neew environemnt variables, to calculate the age of
the patient with that diagnosis.

``` r
data <- data %>%
  mutate(
    age_at_prostate_cancer_diagnosis = (prostdtfirst - birthdate) / dyears(1),
    age_at_metastasis_diagnosis = (date_met - birthdate) / dyears(1)
  )
```

- Age of patients at diagnosis of prostate cancer (mean and standard
  deviation)

``` r
age_prostate_cancer <- data %>%
  summarise(
    Mean = mean(age_at_prostate_cancer_diagnosis, na.rm = TRUE),
    SD = sd(age_at_prostate_cancer_diagnosis, na.rm = TRUE)
  )

print_table(age_prostate_cancer, "Age Prostate Cancer")
```

|     Mean |       SD |
|---------:|---------:|
| 74.29092 | 8.747814 |

Age Prostate Cancer

- Age of patients at diagnosis of metastasis (for those that metastasis
  = 1)

``` r
age_metastasis <- data %>%
  filter(metastasis == 1) %>%
  summarise(
    Mean = mean(age_at_metastasis_diagnosis),
    SD = sd(age_at_metastasis_diagnosis)
  )

print_table(age_metastasis, "Age Metastatis diagnosed")
```

|       Mean |                                          SD |
|-----------:|--------------------------------------------:|
|     78.854 |                                    8.461654 |
| \* Percent | age of patients with and without metastasis |

Age Metastatis diagnosed

``` r
metastasis_percentage <- mydata %>%
  # Use na.rm = FALSE to count NA values as well
  count(metastasis, .drop = FALSE) %>%
  mutate(
    percentage = n / sum(n) * 100,
    status = case_when(
      metastasis == 1 ~ "With metastasis",
      metastasis == 0 ~ "Without metastasis",
      is.na(metastasis) ~ "Missing",
      TRUE ~ "Other" # Catches any other value
    )
  )

print_table(metastasis_percentage, "Metastasis Percentages")
```

| metastasis | n | percentage | status |
|---:|---:|---:|:---|
| 0 | 738 | 63.67558 | Without metastasis |
| 1 | 421 | 36.32442 | With metastasis |
| \* Previous ca | ncer i | n the family |  |
| 0 being no ag | gressi | ve cancer in | family |
| 1 being that | patien | t reported at | least on case of aggressive cancer in family |

Metastasis Percentages

``` r
  cancer_family_percentage <- data %>%
    count(cancer_family) %>%
    mutate(
      percentage = n / sum(n) * 100,
      status = case_when(
        cancer_family == 1 ~ "Aggressive cancer in family",
        cancer_family == 0 ~ "No aggressive cancer in family",
        TRUE ~ "Other"
      )
    )
print_table(cancer_family_percentage, "Cancer Family Percentage")
```

|   cancer_family |   n | percentage | status                         |
|----------------:|----:|-----------:|:-------------------------------|
|               0 | 536 |   46.24676 | No aggressive cancer in family |
|               1 | 623 |   53.75324 | Aggressive cancer in family    |
| \* Civil status |     |            |                                |

Cancer Family Percentage

Civil status 1 meaning married/cohabiting Civil status 2 meaning
single/divorced/widow

``` r
  civil_status_percentage <- data %>%
    count(civil_status) %>%
    mutate(
      percentage = n / sum(n) * 100,
      status = case_when(
        civil_status == 1 ~ "Married/cohabiting",
        civil_status == 2 ~ "Single/divorced/widow",
        TRUE ~ paste("Civil Status:", civil_status)
      )
    )
print_table(civil_status_percentage, "Civil Status Percentage")
```

| civil_status |   n | percentage | status                |
|-------------:|----:|-----------:|:----------------------|
|            1 | 808 |   69.71527 | Married/cohabiting    |
|            2 | 351 |   30.28473 | Single/divorced/widow |

Civil Status Percentage

``` r
# This helper function safely gets a percentage, returning "-" if the category is not found.
safe_get_value <- function(df, status_string) {
  if (status_string %in% df$status) {
    return(paste0(round(df$percentage[df$status == status_string], 2), "%"))
  } else {
    return("-") 
  }
}

summary_df <- data.frame(
  Characteristic = c(
    "Age at Prostate Cancer Diagnosis (years)",
    "Age at Metastasis Diagnosis (years)",
    "Patients with Metastasis (%)",
    "Patients without Metastasis (%)",
    "Aggressive Cancer in Family (%)",
    "No Aggressive Cancer in Family (%)",
    "Married/Cohabiting (%)",
    "Single/Divorced/Widow (%)"
  ),
  Value = c(
    # These two are safe because they always return a single value
    paste0(round(age_prostate_cancer$Mean, 2), " (SD: ", round(age_prostate_cancer$SD, 2), ")"),
    paste0(round(age_metastasis$Mean, 2), " (SD: ", round(age_metastasis$SD, 2), ")"),
    # Now use the helper function for all the percentages
    safe_get_value(metastasis_percentage, "With metastasis"),
    safe_get_value(metastasis_percentage, "Without metastasis"),
    safe_get_value(cancer_family_percentage, "Aggressive cancer in family"),
    safe_get_value(cancer_family_percentage, "No aggressive cancer in family"),
    safe_get_value(civil_status_percentage, "Married/cohabiting"),
    safe_get_value(civil_status_percentage, "Single/divorced/widow")
  )
)
print_table(summary_df, "Final Results")
```

| Characteristic                           | Value            |
|:-----------------------------------------|:-----------------|
| Age at Prostate Cancer Diagnosis (years) | 74.29 (SD: 8.75) |
| Age at Metastasis Diagnosis (years)      | 78.85 (SD: 8.46) |
| Patients with Metastasis (%)             | 36.32%           |
| Patients without Metastasis (%)          | 63.68%           |
| Aggressive Cancer in Family (%)          | 53.75%           |
| No Aggressive Cancer in Family (%)       | 46.25%           |
| Married/Cohabiting (%)                   | 69.72%           |
| Single/Divorced/Widow (%)                | 30.28%           |

Final Results
