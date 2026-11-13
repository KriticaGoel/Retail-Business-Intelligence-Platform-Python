

# Retail Business Intelligence Platform
## 24-Day Project Plan

**Project:** Retail Business Intelligence Platform  
**Duration:** 24 working days  
**Team:** 2 Developers  
**Language:** Python  
**Primary Libraries:** NumPy, Pandas, Matplotlib, Seaborn, Streamlit, Pytest  
**Version:** 1.0

---

# 1. Project Overview

## 1.1 Objective

Build a complete Retail Business Intelligence Platform using Python.

The project will transform raw retail datasets into validated, cleaned, analyzed data and present useful business insights through an interactive dashboard.

The project is designed to develop practical Python development skills while implementing a realistic data analytics application.

Both developers will learn the full project lifecycle, including:

- Python fundamentals and object-oriented programming.
- File handling and CSV processing.
- Data structures and algorithms.
- Exception handling and logging.
- NumPy and Pandas.
- Data cleaning and validation.
- Data analysis and business metrics.
- Data visualization.
- Software architecture.
- Unit and integration testing.
- Git and collaborative development.
- Streamlit dashboard development.
- Documentation and deployment preparation.

## 1.2 Final Project Outcome

At the end of 24 working days, the team should deliver a working application that:

1. Reads multiple raw retail datasets.
2. Profiles and validates incoming data.
3. Identifies data quality problems.
4. Cleans data without modifying the original raw files.
5. Maintains rejected or problematic records for investigation.
6. Integrates related datasets safely.
7. Calculates retail business metrics.
8. Analyzes sales, products, customers, stores, inventory, and suppliers.
9. Presents results through an interactive dashboard.
10. Includes automated tests and technical documentation.

---

# 2. Team Responsibilities

The project has two developers.

The ownership split is intended to divide implementation work, not learning. Both developers must understand the complete application and be able to explain and execute each module.

## Developer A

Primary ownership:

- Transactions and sales analytics.
- Stores.
- Inventory.
- Sales-related metrics.
- Sales dashboard.

## Developer B

Primary ownership:

- Products.
- Customers.
- Suppliers.
- Product and customer analytics.
- Product and customer dashboard pages.

## Shared Responsibilities

Both developers will work together on:

- Project architecture.
- Python fundamentals.
- Data dictionary.
- Validation framework.
- Calendar data.
- Data cleaning standards.
- Integration.
- Testing.
- Git workflow.
- Dashboard shell.
- Final quality assurance.
- Documentation and demonstration.

## Collaboration Rules

1. Each developer completes their individual assignment.
2. Developers review each other's implementation.
3. Shared tasks are completed together.
4. Code must be tested before integration.
5. Every significant change must be committed to Git.
6. No developer should merge code without reviewing its impact on shared modules.
7. Both developers must be able to run the complete application independently.

---

# 3. Dataset Inventory

The project uses a synthetic retail dataset containing seven primary CSV files.

| Dataset | Approximate rows | Purpose |
|---|---:|---|
| transactions.csv | 20,000 | Retail transaction lines |
| products.csv | 49 | Product catalog |
| customers.csv | 2,501 | Customer master data |
| stores.csv | 12 | Store information |
| calendar.csv | 731 | Date dimension |
| inventory.csv | 2,304 | Quarterly inventory snapshots |
| suppliers.csv | 15 | Supplier information |

The row counts include intentionally introduced quality issues, including duplicate records in some files.

## 3.1 Dataset Relationships

Expected relationships:

- Transactions reference products.
- Transactions reference customers.
- Transactions reference stores.
- Transactions reference calendar dates.
- Inventory references products and stores.
- Products may reference suppliers.
- Calendar provides date attributes for analytical reporting.

The team must verify these relationships using the actual dataset rather than assuming that every reference is valid.

## 3.2 Important Dataset Limitations

- Inventory data represents quarterly snapshots, not live stock.
- Supplier lead time is an attribute, not evidence of actual delivery performance.
- Historical transaction prices may differ from current product catalog prices.
- A transaction line is not necessarily equivalent to a distinct order.
- A valid average order value requires a validated order identifier.
- Estimated gross profit is not the same as net profit.

---

# 4. Business Rules and Data Quality Standards

These rules must guide implementation, validation, cleaning, and analysis.

## 4.1 Raw Data Preservation

- Never overwrite raw source files.
- Store cleaned outputs separately.
- Preserve source information needed for auditing.
- Record rejected records in quarantine outputs.

## 4.2 Duplicate Records

- Identify exact duplicate rows.
- Identify duplicate business identifiers.
- Do not automatically delete every duplicate.
- Investigate conflicting records before deciding which record to retain.
- Record duplicate counts and decisions.

## 4.3 Missing Values

- Identify missing values by column.
- Do not replace missing values with arbitrary defaults.
- Apply a documented strategy for each field.
- Reject records when required information is unavailable and cannot safely be recovered.

## 4.4 Quantity and Returns

- Negative transaction quantities can represent returns.
- Do not automatically discard negative quantities.
- Preserve signed quantities.
- Investigate invalid nonnumeric quantities separately.

## 4.5 Prices and Discounts

- Historical transaction unit prices must be preserved.
- Do not replace historical prices with current catalog prices.
- Discounts must be validated against the agreed business range.
- Invalid numeric values must be identified and handled explicitly.

## 4.6 Identifier Normalization

- Normalize identifiers before joining datasets.
- Handle values that contain unwanted trailing decimal notation, such as `1001.0`.
- Trim unnecessary whitespace.
- Preserve original source values when needed for auditability.

## 4.7 Referential Integrity

Validate that:

- Every transaction product reference maps to a valid product.
- Every transaction customer reference maps to a valid customer, where customer identification is required.
- Every transaction store reference maps to a valid store.
- Inventory product and store references are valid.
- Supplier references are valid where required.

Do not silently remove orphan records.

## 4.8 Financial Metric Definitions

**Net sales**

`quantity × transaction_unit_price × (1 - discount_pct / 100)`

**Estimated gross profit**

`net_sales - (quantity × product_unit_cost)`

This is an estimate based on available cost data. It excludes operating expenses, taxes, shipping, and other costs.

**Average Order Value**

`net sales / distinct valid orders`

Only calculate AOV after validating order identifiers and ensuring that the calculation uses distinct orders rather than transaction lines.

**Returns**

Negative quantities must remain signed in calculations. Report returns separately when that improves business interpretation.

## 4.9 Inventory Limitations

Inventory records are quarterly snapshots.

The project can analyze:

- Snapshot stock levels.
- Differences between snapshots.
- Products with low recorded stock.
- Store-level stock distribution.

The project must not claim to show live stock availability.

## 4.10 Supplier Limitations

Supplier lead time can be analyzed as a stated supplier attribute.

Without actual purchase order and delivery event data, the project cannot calculate a true on-time delivery rate.

---

# 5. Project Timeline: 24 Working Days

# Phase 1 — Python Foundations

## Day 1 — Python Fundamentals and CSV Processing

**Objective:** Understand Python basics and read CSV data.

### Developer A — Transactions

- Read `transactions.csv`.
- Inspect column names.
- Count total rows.
- Calculate total valid transaction quantities.
- Identify missing quantities.
- Identify invalid numeric quantities.
- Preserve negative quantities for returns.

### Developer B — Products

- Read `products.csv`.
- Inspect column names.
- Count total rows.
- Calculate average valid catalog price.
- Count products by category.
- Identify missing and invalid prices.

### Shared Task

- Discuss missing values.
- Discuss invalid numeric values.
- Define initial validation rules.
- Record assumptions.

**Expected output:**

Two independent Python scripts that read their respective CSV files and produce correct summaries.

**Acceptance criteria:**

- Both scripts run successfully.
- CSV files are read without manual row-by-row editing.
- Invalid values are identified rather than silently ignored.
- Negative quantities are retained.
- Results are understandable and reproducible.

---

## Day 2 — Python Collections and Data Structures

**Objective:** Understand lists, tuples, sets, and dictionaries.

### Developer A

- Store transaction summaries using dictionaries.
- Count transactions by store.
- Identify duplicate transaction identifiers.
- Group quantities by product identifier.

### Developer B

- Store product information using dictionaries.
- Count products by category.
- Identify duplicate product identifiers.
- Find minimum, maximum, and average prices.

### Shared Task

Create an initial data dictionary documenting:

- Dataset name.
- Column name.
- Expected meaning.
- Expected data type.
- Whether null values are allowed.
- Basic business constraints.

**Expected output:**

Python scripts using collections effectively, plus an initial data dictionary.

**Acceptance criteria:**

- Grouping logic is correct.
- Duplicate identification is demonstrated.
- Appropriate data structures are used.
- Both developers can explain why each structure was selected.

---

## Day 3 — Functions, Modules, and File Handling

**Objective:** Write reusable and maintainable Python code.

### Developer A

Create reusable functions for:

- Reading transaction data.
- Counting rows.
- Summarizing quantities.
- Identifying missing values.

### Developer B

Create reusable functions for:

- Reading product data.
- Calculating average prices.
- Counting categories.
- Identifying invalid prices.

### Shared Task

Create the initial project package structure.

Introduce:

- Functions.
- Imports.
- Modules.
- `pathlib`.
- Relative and absolute paths.
- Main entry points.

**Expected output:**

Reusable Python modules rather than large scripts containing all logic.

**Acceptance criteria:**

- Functions have clear responsibilities.
- File paths are not unnecessarily hardcoded.
- Scripts can be executed from the project root.
- Common logic is not duplicated unnecessarily.

---

## Day 4 — Object-Oriented Programming

**Objective:** Understand and apply Python OOP.

### Both Developers

Study and implement:

- Classes and objects.
- Constructors.
- Instance attributes.
- Methods.
- Encapsulation.
- Inheritance.
- Polymorphism.
- Abstraction.
- Abstract base classes.
- Duck typing.
- Composition.

### Practical Task

Design simple classes for:

- Dataset reader.
- Data validator.
- Data summary.

Discuss how Python OOP differs from Java OOP, especially:

- Dynamic typing.
- Access conventions.
- Duck typing.
- Multiple inheritance.
- Abstract base classes.

**Expected output:**

A small OOP prototype demonstrating appropriate use of classes and composition.

**Acceptance criteria:**

- Both developers can explain class and object behavior.
- Inheritance is used only where appropriate.
- Composition is considered before introducing unnecessary inheritance.
- The prototype has clear responsibilities.

---

# Phase 2 — Reliability and NumPy

## Day 5 — Exception Handling and Custom Exceptions

**Objective:** Handle failures safely.

### Developer A

Implement error handling for transaction processing.

Consider:

- Missing input file.
- Malformed CSV.
- Invalid quantity.
- Invalid transaction date.
- Invalid price.

### Developer B

Implement error handling for product processing.

Consider:

- Missing input file.
- Invalid product price.
- Missing product identifier.
- Invalid unit cost.

### Shared Task

Define exception categories:

- File-level errors.
- Configuration errors.
- Row-level data errors.
- Validation failures.

Create custom exceptions where they improve clarity.

**Expected output:**

Reliable scripts that distinguish recoverable row problems from fatal processing failures.

**Acceptance criteria:**

- Errors are not silently swallowed.
- A bad row does not unnecessarily terminate the entire pipeline.
- Missing input files are handled clearly.
- Fatal errors produce meaningful messages.

---

## Day 6 — Logging, Configuration, and Code Quality

**Objective:** Make processing observable and maintainable.

### Developer A

Add logging to transaction processing.

Log:

- File loading.
- Row counts.
- Invalid transaction counts.
- Processing failures.

### Developer B

Add logging to product processing.

Log:

- File loading.
- Product counts.
- Invalid price counts.
- Duplicate identifiers.

### Shared Task

Introduce:

- Python `logging`.
- Configuration files.
- Type hints.
- Docstrings.
- Basic formatting and code quality standards.

**Expected output:**

Scripts with consistent logging and configurable file paths.

**Acceptance criteria:**

- Processing events are recorded.
- Errors include useful context.
- Configuration is separated from business logic.
- Function signatures use meaningful type hints where practical.

---

## Day 7 — NumPy Fundamentals

**Objective:** Understand numerical computation with NumPy.

### Both Developers

Study:

- NumPy arrays.
- Array creation.
- Dimensions and shape.
- Data types.
- Indexing and slicing.
- Boolean masks.
- Vectorized operations.
- Aggregations.
- Missing and invalid numerical values.

### Developer A

Apply NumPy to transaction quantity and price summaries.

### Developer B

Apply NumPy to product price and cost summaries.

**Expected output:**

Small numerical analysis modules using NumPy.

**Acceptance criteria:**

- Both developers understand array shape and dtype.
- Vectorized operations are demonstrated.
- Results are compared against simple Python calculations.

---

## Day 8 — Applied NumPy and Numerical Validation

**Objective:** Apply NumPy to realistic data problems.

### Developer A

- Investigate unusual transaction quantities.
- Calculate numerical summaries.
- Identify suspicious extreme values.
- Compare Python and NumPy calculations.

### Developer B

- Investigate unusual product prices and costs.
- Calculate numerical summaries.
- Identify invalid numerical values.
- Compare Python and NumPy calculations.

### Shared Task

Discuss:

- Outliers versus invalid data.
- Why an extreme value is not automatically wrong.
- How numerical validation should be documented.

**Expected output:**

Numerical investigation reports and reusable NumPy functions.

**Acceptance criteria:**

- Outliers are investigated rather than automatically deleted.
- Numerical assumptions are documented.
- Calculations are reproducible.

---

# Phase 3 — Pandas and Data Engineering

## Day 9 — Pandas Ingestion and Profiling

**Objective:** Load and inspect all datasets with Pandas.

### Developer A

Profile:

- Transactions.
- Stores.
- Inventory.

### Developer B

Profile:

- Products.
- Customers.
- Suppliers.

### Shared Task

Profile:

- Calendar.

For every dataset, inspect:

- Shape.
- Column names.
- Data types.
- Missing values.
- Duplicate rows.
- Unique values.
- Basic descriptive statistics.

**Expected output:**

Initial dataset profiling report covering all seven datasets.

**Acceptance criteria:**

- Every dataset is loaded.
- Row counts and column counts are recorded.
- Missing values are quantified.
- Duplicate records are investigated.
- Unexpected data types are documented.

---

## Day 10 — Data Cleaning

**Objective:** Clean datasets while preserving source data.

### Developer A

Clean:

- Transactions.
- Stores.
- Inventory.

### Developer B

Clean:

- Products.
- Customers.
- Suppliers.

### Shared Task

Clean calendar data and agree on common standards for:

- Date parsing.
- Numeric parsing.
- Identifier normalization.
- String trimming.
- Category standardization.
- Missing values.
- Quarantine handling.

**Expected output:**

Cleaned datasets saved separately from raw datasets.

**Acceptance criteria:**

- Raw files remain unchanged.
- Invalid records are not silently lost.
- Cleaning decisions are documented.
- Original and cleaned row counts can be reconciled.

---

## Day 11 — Data Validation Framework

**Objective:** Build reusable validation rules.

### Developer A

Implement validation rules for:

- Transactions.
- Stores.
- Inventory.

### Developer B

Implement validation rules for:

- Products.
- Customers.
- Suppliers.

### Shared Task

Implement reusable validation capabilities for:

- Required fields.
- Data types.
- Uniqueness.
- Nullability.
- Numeric ranges.
- Date validity.
- Referential integrity.
- Duplicate detection.

**Expected output:**

Reusable validation framework and dataset-specific validation rules.

**Acceptance criteria:**

- Rules are separated from cleaning logic.
- Validation results identify the affected dataset and field.
- Invalid rows can be traced.
- Validation results are reproducible.

---

## Day 12 — Data Integration and Joins

**Objective:** Integrate datasets safely.

### Developer A

- Join transactions with stores.
- Join transactions with calendar.
- Investigate inventory-to-store relationships.

### Developer B

- Join transactions with products.
- Join transactions with customers.
- Investigate product-to-supplier relationships.

### Shared Task

Validate:

- Join keys.
- Key normalization.
- One-to-one relationships.
- One-to-many relationships.
- Many-to-many risks.
- Orphan records.
- Row counts before and after joins.

**Expected output:**

Integrated analytical datasets with documented join behavior.

**Acceptance criteria:**

- No accidental many-to-many multiplication.
- Join cardinality is checked.
- Orphan records are reported.
- Joined row counts are explained.

---

# Phase 4 — Retail Business Analytics

## Day 13 — Sales and Business Metrics

**Objective:** Calculate core retail metrics.

### Developer A

Implement:

- Total transaction line count.
- Distinct order count.
- Total signed quantity.
- Gross sales before discount.
- Net sales after discount.
- Return quantities and values.
- Sales by store.
- Sales over time.

### Developer B

Support:

- Sales by product.
- Sales by category.
- Product performance.
- Customer purchase summaries.

### Shared Task

Create a metric dictionary containing:

- Metric name.
- Business definition.
- Formula.
- Required columns.
- Assumptions.
- Known limitations.

**Expected output:**

Sales analytics module and metric dictionary.

**Acceptance criteria:**

- Formulas are documented.
- Distinct orders are not confused with transaction lines.
- Returns are handled consistently.
- AOV is calculated only when order identifiers are validated.

---

## Day 14 — Profitability and Customer Analytics

**Objective:** Analyze estimated profitability and customer behavior.

### Developer A

Calculate:

- Estimated gross profit.
- Estimated gross margin.
- Store-level profitability.
- Product-level profitability.

### Developer B

Analyze:

- Customer purchase frequency.
- Customer net sales.
- Customer segmentation.
- Customer contribution to sales.

### Shared Task

Review metric definitions and assumptions.

**Expected output:**

Profitability and customer analytics modules.

**Acceptance criteria:**

- Cost calculations use the appropriate historical transaction quantity and available product cost.
- Estimated gross profit is clearly labelled.
- Unsupported customer lifetime value claims are avoided.
- Customer segmentation rules are documented.

---

## Day 15 — Inventory and Supplier Analytics

**Objective:** Analyze inventory snapshots and supplier attributes.

### Developer A

Analyze:

- Inventory by store.
- Inventory by product.
- Quarterly stock changes.
- Negative or invalid stock records.
- Products with low recorded stock.

### Developer B

Analyze:

- Supplier lead time.
- Products by supplier.
- Supplier catalog coverage.
- Missing supplier attributes.

### Shared Task

Document data limitations.

**Expected output:**

Inventory and supplier analytics modules.

**Acceptance criteria:**

- Inventory is described as quarterly snapshot data.
- Stock comparisons use comparable snapshots.
- Supplier lead time is not presented as actual delivery performance.
- Invalid records are accounted for.

---

# Phase 5 — Data Visualization

## Day 16 — Matplotlib

**Objective:** Create meaningful static visualizations.

### Developer A

Create:

- Sales trend chart.
- Store sales comparison.
- Return analysis.
- Sales distribution.

### Developer B

Create:

- Product category comparison.
- Top products.
- Customer contribution.
- Product price distribution.

### Shared Task

Agree on chart naming, units, labels, titles, and reusable visualization conventions.

**Expected output:**

A collection of Matplotlib charts saved under the reports directory.

**Acceptance criteria:**

- Every chart has a meaningful title.
- Axes are labelled.
- Units are clear.
- Charts use the correct aggregation level.

---

## Day 17 — Seaborn and Insight Development

**Objective:** Develop more advanced visualizations and communicate findings.

### Developer A

Create store and sales visualizations.

### Developer B

Create product and customer visualizations.

### Shared Task

Use Seaborn for appropriate:

- Distributions.
- Category comparisons.
- Correlation heatmaps.
- Analytical plots.

Write business observations for each major chart.

**Expected output:**

Visualization report containing charts and written observations.

**Acceptance criteria:**

- Visualizations answer defined business questions.
- Correlation is not described as causation.
- Observations are supported by calculated data.
- Charts are readable.

---

# Phase 6 — Testing and Git Collaboration

## Day 18 — Unit and Integration Testing

**Objective:** Test the application systematically.

### Developer A

Write tests for:

- Transaction ingestion.
- Transaction validation.
- Sales calculations.
- Inventory analytics.

### Developer B

Write tests for:

- Product ingestion.
- Product validation.
- Customer analytics.
- Supplier analytics.

### Shared Task

Use Pytest for:

- Fixtures.
- Parameterized tests.
- Edge cases.
- Integration tests.
- Error handling tests.

**Expected output:**

Automated test suite.

**Acceptance criteria:**

- Core business calculations have tests.
- Invalid inputs are tested.
- Expected exceptions are tested.
- Tests can run from the project root.

---

## Day 19 — Git and Team Integration

**Objective:** Establish a professional collaboration workflow.

### Both Developers

Practice:

- Branch creation.
- Meaningful commits.
- Pull requests.
- Code reviews.
- Merging.
- Conflict resolution.
- Reverting changes.

### Shared Task

Integrate all completed modules.

**Expected output:**

Integrated codebase with reviewed changes.

**Acceptance criteria:**

- Both developers use separate working branches.
- Changes are reviewed before merging.
- Main branch remains runnable.
- Integration issues are recorded and resolved.

---

# Phase 7 — Application Architecture and Dashboard

## Day 20 — Application Architecture

**Objective:** Organize the project into maintainable layers.

### Developer A

Prepare sales and inventory services.

### Developer B

Prepare product, customer, and supplier services.

### Shared Task

Define:

- Ingestion layer.
- Validation layer.
- Cleaning layer.
- Model layer.
- Analytics layer.
- Service layer.
- Visualization layer.
- Application layer.

**Expected output:**

Integrated application architecture with clear module responsibilities.

**Acceptance criteria:**

- Business logic is separate from UI logic.
- Modules have clear responsibilities.
- Dependencies are understandable.
- Application services can be called independently of Streamlit.

---

## Day 21 — Streamlit Dashboard Foundation

**Objective:** Build the interactive dashboard.

### Developer A

Build the Sales page.

### Developer B

Build the Product and Customer pages.

### Shared Task

Build:

- Application entry point.
- Sidebar navigation.
- Dashboard layout.
- Shared filters.
- Common KPI components.
- Executive Overview.
- Data Quality page.

**Expected output:**

A working Streamlit dashboard with the first core pages.

**Acceptance criteria:**

- Application starts successfully.
- Navigation works.
- Filters affect relevant charts and metrics.
- UI does not contain duplicated business logic.

---

## Day 22 — Complete Dashboard and Export Features

**Objective:** Complete dashboard functionality.

### Developer A

Build:

- Store page.
- Inventory page.

### Developer B

Build:

- Supplier analytics.
- Product and customer drill-downs.

### Shared Task

Implement:

- Date filters.
- Store filters.
- Product/category filters where appropriate.
- Data exports.
- Data quality summary.
- Inventory snapshot freshness labels.

**Expected output:**

Complete dashboard with all agreed pages.

**Acceptance criteria:**

- All seven dashboard pages are accessible.
- Filters behave consistently.
- Exported data matches the selected filters.
- Inventory dates are clearly displayed.
- Unsupported metrics are not presented.

---

# Phase 8 — Quality Assurance and Delivery

## Day 23 — End-to-End QA

**Objective:** Validate the entire system.

### Developer A

Validate:

- Transactions.
- Sales metrics.
- Stores.
- Inventory.

### Developer B

Validate:

- Products.
- Customers.
- Suppliers.

### Shared Task

Perform:

- End-to-end pipeline testing.
- Regression testing.
- Data reconciliation.
- Fresh environment setup.
- Documentation review.
- Known limitation review.

**Expected output:**

QA report and release candidate.

**Acceptance criteria:**

- Pipeline runs from raw data to dashboard.
- Row counts are reconciled.
- Critical metrics are checked independently.
- No unresolved critical defects remain.
- Setup instructions work in a fresh environment.

---

## Day 24 — Final Demonstration and Handover

**Objective:** Deliver the completed project.

### Developer A

Demonstrate:

- Transaction processing.
- Sales analytics.
- Store analytics.
- Inventory analytics.

### Developer B

Demonstrate:

- Product analytics.
- Customer analytics.
- Supplier analytics.

### Shared Task

- Demonstrate complete dashboard.
- Explain architecture.
- Explain validation framework.
- Explain major business metrics.
- Review limitations.
- Complete README.
- Tag the release.

**Expected output:**

Final Retail Business Intelligence Platform release.

**Acceptance criteria:**

- Both developers can run the application.
- Both developers can explain the full architecture.
- Both developers can explain major business rules.
- Documentation is complete.
- Final code is committed and tagged.

---

# 6. Target Repository Structure

```text
retail-business-intelligence-platform/
│
├── data/
│   ├── raw/
│   ├── processed/
│   └── quarantine/
│
├── reports/
│
├── notebooks/
│
├── src/
│   └── retail_bi/
│       ├── ingestion/
│       ├── validation/
│       ├── cleaning/
│       ├── models/
│       ├── analytics/
│       ├── services/
│       └── visualization/
│
├── app/
│   ├── pages/
│   └── components/
│
├── tests/
│
├── docs/
│
├── requirements.txt
├── README.md
└── .gitignore
```

## Folder Responsibilities

| Folder | Responsibility |
|---|---|
| `data/raw` | Original input datasets |
| `data/processed` | Cleaned and integrated datasets |
| `data/quarantine` | Rejected or problematic records |
| `reports` | Generated charts and reports |
| `notebooks` | Exploration and experimentation |
| `ingestion` | Reading input datasets |
| `validation` | Data quality rules |
| `cleaning` | Data cleaning operations |
| `models` | Data structures and domain models |
| `analytics` | Business metrics and analysis |
| `services` | Application-level orchestration |
| `visualization` | Reusable chart generation |
| `app` | Streamlit application |
| `tests` | Automated tests |
| `docs` | Technical and business documentation |

---

# 7. Final Dashboard Scope

The final dashboard will contain seven pages.

## 1. Executive Overview

- Total net sales.
- Total orders.
- Total units sold, with return treatment documented.
- Estimated gross profit.
- Sales trend.
- Store performance.
- Product category contribution.

## 2. Sales Analytics

- Gross and net sales.
- Discount analysis.
- Sales trends.
- Return analysis.
- Order metrics.
- Average order value, if valid.

## 3. Product Analytics

- Product performance.
- Category performance.
- Product price distribution.
- Estimated product profitability.
- Top and bottom products.

## 4. Customer Analytics

- Customer purchase summaries.
- Customer contribution.
- Purchase frequency.
- Customer segmentation.
- Customer activity analysis.

## 5. Store Analytics

- Store-level sales.
- Store profitability estimates.
- Store comparison.
- Sales trends by store.

## 6. Inventory and Supplier Analytics

- Quarterly inventory snapshots.
- Stock by product and store.
- Snapshot-to-snapshot stock changes.
- Supplier lead-time attributes.
- Supplier product coverage.

## 7. Data Quality

- Dataset row counts.
- Missing values.
- Duplicate records.
- Invalid values.
- Referential integrity failures.
- Quarantined records.
- Validation summary.

---

# 8. Daily Working Process

Every working day must follow this process.

1. Review the day's learning objective.
2. Complete individual assignments independently.
3. Run the code and verify outputs.
4. Review each other's code.
5. Complete the shared task.
6. Test expected scenarios and edge cases.
7. Commit changes to Git.
8. Update the project tracker.
9. Record blockers and technical decisions.
10. Mark the day complete only after acceptance criteria pass.

## Daily Completion Status

Use these statuses:

- `Not Started`
- `In Progress`
- `Needs Rework`
- `Blocked`
- `Done`

A day is not complete merely because code has been written.

It is complete when:

- The assignment is implemented.
- Expected output is produced.
- Tests pass.
- Code review is complete.
- Shared work is integrated.
- Acceptance criteria are met.

---

# 9. Definition of Done

The overall project is considered complete when all the following are true.

## Data Engineering

- [ ] All seven datasets can be loaded.
- [ ] Raw datasets remain unchanged.
- [ ] Data profiling is available.
- [ ] Validation rules are implemented.
- [ ] Cleaning rules are documented.
- [ ] Quarantine records are preserved.
- [ ] Dataset relationships are validated.
- [ ] Joins are checked for cardinality issues.

## Analytics

- [ ] Sales metrics are implemented.
- [ ] Return treatment is documented.
- [ ] Product analytics are implemented.
- [ ] Customer analytics are implemented.
- [ ] Store analytics are implemented.
- [ ] Estimated profitability is implemented.
- [ ] Inventory snapshot analytics are implemented.
- [ ] Supplier attribute analysis is implemented.
- [ ] Metric definitions are documented.

## Visualization

- [ ] Matplotlib charts are available.
- [ ] Seaborn charts are available where appropriate.
- [ ] Dashboard pages are implemented.
- [ ] Filters work correctly.
- [ ] Exports work correctly.
- [ ] Data quality information is visible.

## Engineering

- [ ] Code is organized into modules.
- [ ] Error handling is implemented.
- [ ] Logging is implemented.
- [ ] Type hints are used where practical.
- [ ] Automated tests are available.
- [ ] Git workflow is followed.
- [ ] README is complete.
- [ ] Fresh environment setup is verified.

## Team Readiness

- [ ] Developer A can explain Developer B's modules.
- [ ] Developer B can explain Developer A's modules.
- [ ] Both developers can run the complete pipeline.
- [ ] Both developers can explain major business metrics.
- [ ] Both developers can explain data quality decisions.
- [ ] Both developers can demonstrate the dashboard.

---

# 10. Technical Learning Checklist

By the end of the project, both developers should be comfortable with:

## Python

- [ ] Variables and data types.
- [ ] Conditional statements.
- [ ] Loops.
- [ ] Functions.
- [ ] Lists, tuples, sets, and dictionaries.
- [ ] Comprehensions.
- [ ] File handling.
- [ ] Modules and packages.
- [ ] Exception handling.
- [ ] Custom exceptions.
- [ ] Logging.
- [ ] Type hints.
- [ ] OOP.
- [ ] Iterators and generators, where appropriate.

## NumPy

- [ ] Arrays.
- [ ] Shape and dimensions.
- [ ] Data types.
- [ ] Indexing and slicing.
- [ ] Boolean indexing.
- [ ] Vectorization.
- [ ] Aggregations.
- [ ] Numerical analysis.

## Pandas

- [ ] Series and DataFrames.
- [ ] CSV ingestion.
- [ ] Data inspection.
- [ ] Missing value handling.
- [ ] Duplicate detection.
- [ ] Type conversion.
- [ ] String operations.
- [ ] Date handling.
- [ ] GroupBy.
- [ ] Aggregation.
- [ ] Merge and joins.
- [ ] Pivot tables.
- [ ] Data validation.
- [ ] Exporting.

## Visualization

- [ ] Matplotlib.
- [ ] Seaborn.
- [ ] Chart selection.
- [ ] Chart interpretation.
- [ ] Business insight communication.

## Software Engineering

- [ ] Modular architecture.
- [ ] Reusable code.
- [ ] Unit testing.
- [ ] Integration testing.
- [ ] Git branches.
- [ ] Pull requests.
- [ ] Code reviews.
- [ ] Documentation.
- [ ] Application orchestration.

## Dashboard

- [ ] Streamlit fundamentals.
- [ ] Page navigation.
- [ ] Interactive filters.
- [ ] KPI presentation.
- [ ] Charts.
- [ ] Data exports.
- [ ] Error and empty-state handling.

---

# 11. Important Project Principles

1. Understand before implementing.
2. Do not blindly copy code.
3. Do not hide data quality issues.
4. Do not delete records without a documented reason.
5. Do not mix cleaning logic with analytics logic.
6. Do not mix UI code with business calculations.
7. Do not assume joins are correct just because they execute.
8. Do not report metrics without defining their formulas.
9. Do not claim insights that the dataset cannot support.
10. Do not mark a task complete without evidence.
11. Both developers must understand the complete application.
12. Code quality and correctness are more important than finishing quickly.

---

# 12. Final Deliverables

At the end of the 24-day project, the team should have:

1. Complete Python source code.
2. Seven-dataset ingestion pipeline.
3. Data profiling report.
4. Data validation framework.
5. Data cleaning pipeline.
6. Quarantine outputs.
7. Integrated analytical datasets.
8. Retail business metrics.
9. Inventory and supplier analytics.
10. Matplotlib and Seaborn visualizations.
11. Streamlit dashboard.
12. Automated tests.
13. Git repository with meaningful commit history.
14. README and technical documentation.
15. Final QA report.
16. Final project demonstration.

**Final goal:** Both developers should be able to independently explain, run, test, and extend the Retail Business Intelligence Platform—not merely demonstrate code written during the project.

