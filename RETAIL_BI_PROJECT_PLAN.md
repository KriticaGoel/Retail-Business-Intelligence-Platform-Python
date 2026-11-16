# Retail Business Intelligence Platform
## 19-Day Project Plan

**Project:** Retail Business Intelligence Platform  
**Duration:** 19 working days  
**Team:** 2 developers  
**Language:** Python  
**Primary libraries:** NumPy, Pandas, Matplotlib, Seaborn, Streamlit, Pytest  
**Version:** 2.0

---

# 1. Project Overview

## 1.1 Objective

Build a complete Retail Business Intelligence Platform using Python. The application will transform raw retail datasets into validated, cleaned, integrated data, calculate business metrics, and present actionable insights through an interactive dashboard.

The project develops practical skills in:

- Python fundamentals, collections, functions, modules, and OOP.
- File handling, exception handling, logging, configuration, and type hints.
- NumPy and Pandas.
- Data profiling, cleaning, validation, and integration.
- Retail business analytics and metric design.
- Matplotlib, Seaborn, and Streamlit.
- Software architecture, testing, Git collaboration, QA, and documentation.

## 1.2 Final Outcome

At completion, the team will deliver an application that:

1. Reads multiple raw retail datasets.
2. Profiles and validates incoming data.
3. Identifies data quality problems.
4. Cleans data without modifying original raw files.
5. Preserves rejected or problematic records for investigation.
6. Integrates related datasets safely.
7. Calculates retail business metrics.
8. Analyzes sales, products, customers, stores, inventory, and suppliers.
9. Presents results through an interactive dashboard.
10. Includes automated tests and technical documentation.

# 2. Team Responsibilities

Ownership divides implementation work, not learning. Both developers must understand the complete application and be able to explain and execute every major module.

## Developer A — Primary Ownership

- Transactions and sales analytics.
- Stores.
- Inventory.
- Sales-related metrics.
- Sales and store dashboard pages.

## Developer B — Primary Ownership

- Products.
- Customers.
- Suppliers.
- Product and customer analytics.
- Product and customer dashboard pages.

## Shared Responsibilities

- Project architecture and common ingestion/validation framework.
- Data dictionary and calendar data.
- Data cleaning standards and integration.
- Testing and Git workflow.
- Dashboard shell, executive overview, and data quality page.
- Final QA, documentation, and demonstration.

## Collaboration Rules

1. Complete individual assignments first.
2. Review each other's implementation.
3. Complete shared tasks together.
4. Test code before integration.
5. Commit significant changes to Git.
6. Review the impact of changes to shared modules before merging.
7. Both developers must be able to run the complete application independently.
8. A task is complete only when its acceptance criteria pass.

# 3. Dataset Inventory

The project uses seven synthetic retail CSV datasets.

| Dataset | Approximate rows | Purpose |
|---|---:|---|
| `transactions.csv` | 20,000 | Retail transaction lines |
| `products.csv` | 49 | Product catalog |
| `customers.csv` | 2,501 | Customer master data |
| `stores.csv` | 12 | Store information |
| `calendar.csv` | 731 | Date dimension |
| `inventory.csv` | 2,304 | Quarterly inventory snapshots |
| `suppliers.csv` | 15 | Supplier information |

Row counts include intentionally introduced data quality issues, including duplicate records in some files.

## 3.1 Dataset Relationships

- Transactions reference products, customers, stores, and calendar dates.
- Inventory references products and stores.
- Products may reference suppliers.
- Calendar provides date attributes for analytical reporting.

Verify these relationships against the actual data. Do not assume every reference is valid.

## 3.2 Dataset Limitations

- Inventory represents quarterly snapshots, not live stock.
- Supplier lead time is an attribute, not evidence of actual delivery performance.
- Historical transaction prices may differ from current catalog prices.
- A transaction line is not necessarily a distinct order.
- Average Order Value (AOV) requires a validated order identifier.
- Estimated gross profit is not net profit.

# 4. Business Rules and Data Quality Standards

## 4.1 Raw Data Preservation

- Never overwrite raw source files.
- Store cleaned outputs separately.
- Preserve source information needed for auditing.
- Record rejected records in quarantine outputs.

## 4.2 Duplicate Records

- Identify exact duplicate rows and duplicate business identifiers separately.
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

- Preserve historical transaction unit prices.
- Do not replace historical prices with current catalog prices.
- Validate discounts against the agreed business range.
- Identify and handle invalid numeric values explicitly.

## 4.6 Identifier Normalization

- Normalize identifiers before joining datasets.
- Handle unwanted trailing decimal notation such as `1001.0`.
- Trim unnecessary whitespace.
- Preserve original source values when needed for auditability.

## 4.7 Referential Integrity

Validate transaction references to products, customers, stores, and dates, plus inventory references to products and stores and supplier references where applicable. Do not silently remove orphan records.

## 4.8 Financial Metric Definitions

**Net sales**

`quantity × transaction_unit_price × (1 - discount_pct / 100)`

**Estimated gross profit**

`net_sales - (quantity × product_unit_cost)`

This estimate excludes operating expenses, taxes, shipping, and other costs. Missing costs must not silently be treated as zero.

**Average Order Value**

`net sales / distinct valid orders`

Calculate AOV only after validating order identifiers and using distinct orders rather than transaction lines.

**Returns:** Negative quantities remain signed in calculations. Report returns separately when that improves business interpretation.

## 4.9 Inventory Limitations

Inventory records are quarterly snapshots. The project may analyze stock levels, snapshot-to-snapshot differences, low recorded stock, and store-level distribution. It must not claim to show live stock availability.

## 4.10 Supplier Limitations

Supplier lead time can be analyzed as a stated supplier attribute. Without actual purchase-order and delivery-event data, the project cannot calculate a true on-time delivery rate.

# 5. Project Timeline — 19 Working Days

# Phase 1 — Python Foundation and Reusable Processing Framework

## Day 1 — Consolidated Python Foundation

**Objective:** Consolidate Python fundamentals, OOP, file handling, exception handling, logging, and configuration into a reusable foundation. This combines the original Days 1–6. The goal is not to repeat basic exercises; it is to build reusable project components.

### Developer A — Transaction Processing

1. Read `transactions.csv`.
2. Create a reusable transaction reader.
3. Validate required columns.
4. Validate missing and invalid values.
5. Identify duplicate transaction IDs.
6. Preserve negative quantities as returns.
7. Handle recoverable row-level errors.
8. Generate transaction summaries.
9. Record processing and validation results.

### Developer B — Product Processing

1. Read `products.csv`.
2. Create a reusable product reader.
3. Validate required columns.
4. Validate missing and invalid values.
5. Identify duplicate product IDs.
6. Validate product prices and unit costs.
7. Handle recoverable row-level errors.
8. Generate product summaries.
9. Record processing and validation results.

### Shared Tasks

Build a common foundation containing:

- Reusable CSV reading functionality.
- Common validation functions.
- Custom exceptions.
- Logging configuration.
- Configuration management for file paths.
- Type hints and docstrings.
- A consistent processing result structure.
- A common validation report structure.
- Invalid-row handling and quarantine capability.
- Unit tests for shared functionality.

Apply Python concepts where they improve the implementation: functions, modules, packages, collections, comprehensions, classes, encapsulation, abstraction, inheritance and polymorphism where appropriate, composition, duck typing, exception handling, logging, `pathlib`, and type hints.

### Expected Starting Architecture

```text
src/
└── retail_bi/
    ├── __init__.py
    ├── config/
    │   ├── __init__.py
    │   └── settings.py
    ├── ingestion/
    │   ├── __init__.py
    │   ├── base_reader.py
    │   ├── transaction_reader.py
    │   └── product_reader.py
    ├── validation/
    │   ├── __init__.py
    │   ├── base_validator.py
    │   ├── transaction_validator.py
    │   └── product_validator.py
    ├── exceptions/
    │   ├── __init__.py
    │   └── custom_exceptions.py
    ├── reporting/
    │   ├── __init__.py
    │   └── validation_report.py
    └── utils/
        ├── __init__.py
        └── logger.py

tests/
├── test_transaction_reader.py
├── test_product_reader.py
└── test_validation.py

data/
├── raw/
├── processed/
└── quarantine/

logs/
```

This is a starting point, not a requirement to introduce unnecessary abstractions. Use inheritance only where readers genuinely share behavior. Prefer simple, composable components over an elaborate framework.

### Expected Deliverables

1. Reusable CSV reading mechanism.
2. Separate transaction and product processors.
3. Reusable validation functions.
4. Custom exception handling.
5. Consistent logging.
6. Configurable file paths.
7. Structured validation reports.
8. Invalid-row handling and quarantine capability.
9. Automated tests.
10. Documentation explaining how to add another dataset.

### Acceptance Criteria

- Both readers run successfully.
- Raw files remain unchanged.
- Missing columns are detected.
- Missing and invalid values are reported.
- Duplicate identifiers are identified.
- Negative quantities are preserved.
- Recoverable row errors do not unnecessarily terminate processing.
- Fatal file-level errors produce meaningful exceptions.
- Logs contain useful processing information.
- Configuration is separated from business logic.
- Tests cover normal and failure scenarios.
- Both developers can explain the architecture.

**Critical extensibility test:** Add a customer reader later without copying the transaction reader and changing column names. The common framework should support the new reader with minimal duplication.

# Phase 2 — NumPy

## Day 2 — NumPy Fundamentals

**Objective:** Understand numerical computation with NumPy.

### Both Developers

Study and practice:

- NumPy arrays, creation, dimensions, and shape.
- Data types (`dtype`).
- Indexing and slicing.
- Boolean masks.
- Vectorized operations.
- Aggregations.
- Missing and invalid numerical values.

### Developer A

Apply NumPy to transaction quantities, transaction prices, quantity summaries, and numerical transaction analysis.

### Developer B

Apply NumPy to product prices, product costs, price summaries, and numerical product analysis.

**Expected deliverable:** Small numerical analysis modules using NumPy.

**Acceptance criteria:** Both developers understand array shape and dtype; demonstrate vectorized operations; compare results against equivalent Python calculations; and explain when NumPy is useful versus ordinary Python.

## Day 3 — Applied NumPy and Numerical Validation

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

### Shared Tasks

Discuss outliers versus invalid data, why an extreme value is not automatically incorrect, how numerical validation should be documented, and how NumPy results can be checked independently.

**Expected deliverable:** Numerical investigation reports and reusable NumPy functions.

**Acceptance criteria:** Outliers are investigated rather than automatically deleted; assumptions are documented; calculations are reproducible; and both developers can explain the difference between an invalid value and a valid but unusual value.

# Phase 3 — Pandas and Data Engineering

## Day 4 — Pandas Ingestion and Profiling

**Objective:** Load and inspect all datasets with Pandas.

- **Developer A:** Profile transactions, stores, and inventory.
- **Developer B:** Profile products, customers, and suppliers.
- **Shared:** Profile calendar data and agree on a common profiling format.

For every dataset inspect shape, column names, data types, missing values, duplicate rows, unique values, and descriptive statistics.

**Expected deliverable:** Initial dataset profiling report covering all seven datasets.

**Acceptance criteria:** Every dataset loads; row and column counts are recorded; missing values are quantified; duplicates are investigated; unexpected data types are documented; and profiling is reproducible.

## Day 5 — Data Cleaning

**Objective:** Clean datasets while preserving source data.

- **Developer A:** Clean transactions, stores, and inventory.
- **Developer B:** Clean products, customers, and suppliers.
- **Shared:** Clean calendar data and agree on standards for date parsing, numeric parsing, identifier normalization, string trimming, category standardization, missing values, duplicate handling, and quarantine handling.

**Expected deliverable:** Cleaned datasets saved separately from raw datasets.

**Acceptance criteria:** Raw files remain unchanged; invalid records are not silently lost; cleaning decisions are documented; original and cleaned row counts can be reconciled; negative transaction quantities are retained; and conflicting duplicate identifiers are investigated.

## Day 6 — Data Validation Framework

**Objective:** Build reusable validation rules.

- **Developer A:** Implement rules for transactions, stores, and inventory.
- **Developer B:** Implement rules for products, customers, and suppliers.
- **Shared:** Implement reusable checks for required fields, data types, uniqueness, nullability, numeric ranges, date validity, referential integrity, and duplicate detection.

**Expected deliverable:** Reusable validation framework and dataset-specific validation rules.

**Acceptance criteria:** Rules are separated from cleaning logic; results identify the affected dataset and field; invalid rows can be traced; results are reproducible; and developers can add rules without changing unrelated dataset logic.

## Day 7 — Data Integration and Joins

**Objective:** Integrate datasets safely.

- **Developer A:** Join transactions with stores and calendar; investigate inventory-to-store relationships.
- **Developer B:** Join transactions with products and customers; investigate product-to-supplier relationships.
- **Shared:** Validate join keys, key normalization, one-to-one and one-to-many relationships, many-to-many risks, orphan records, and row counts before and after joins.

**Expected deliverable:** Integrated analytical datasets with documented join behavior.

**Acceptance criteria:** No accidental many-to-many multiplication; join cardinality is checked; orphan records are reported; joined row counts are explained; historical transaction prices are preserved; and both developers can explain the join strategy.

# Phase 4 — Retail Business Analytics

## Day 8 — Sales and Business Metrics

**Objective:** Calculate core retail metrics.

### Developer A

- Total transaction line count.
- Distinct order count.
- Total signed quantity.
- Gross sales before discount.
- Net sales after discount.
- Return quantities and values.
- Sales by store.
- Sales over time.

### Developer B

- Sales by product.
- Sales by category.
- Product performance.
- Customer purchase summaries.

### Shared Tasks

Create a metric dictionary containing metric name, business definition, formula, required columns, assumptions, and known limitations.

**Expected deliverable:** Sales analytics module and metric dictionary.

**Acceptance criteria:** Formulas are documented; distinct orders are not confused with transaction lines; returns are handled consistently; AOV is calculated only when order identifiers are validated; and metrics reconcile against independently calculated sample results.

## Day 9 — Profitability and Customer Analytics

**Objective:** Analyze estimated profitability and customer behavior.

- **Developer A:** Calculate estimated gross profit, estimated gross margin, store-level profitability, and product-level profitability.
- **Developer B:** Analyze customer purchase frequency, customer net sales, customer segmentation, and customer contribution to sales.
- **Shared:** Review metric definitions, validate financial calculations, document assumptions and limitations, and review segmentation rules.

**Expected deliverable:** Profitability and customer analytics modules.

**Acceptance criteria:** Cost calculations use transaction quantities and available product cost; estimated gross profit is clearly labelled; missing costs are not silently treated as zero; unsupported customer lifetime value claims are avoided; and segmentation rules are documented and reproducible.

## Day 10 — Inventory and Supplier Analytics

**Objective:** Analyze inventory snapshots and supplier attributes.

- **Developer A:** Analyze inventory by store and product, quarterly stock changes, negative or invalid stock records, and products with low recorded stock.
- **Developer B:** Analyze supplier lead time, products by supplier, supplier catalog coverage, and missing supplier attributes.
- **Shared:** Document data limitations, validate inventory and supplier relationships, define appropriate summary metrics, and review calculations.

**Expected deliverable:** Inventory and supplier analytics modules.

**Acceptance criteria:** Inventory is described as quarterly snapshot data; stock comparisons use comparable snapshots; supplier lead time is not presented as actual delivery performance; invalid records are accounted for; and no live-stock or unsupported restocking claims are made.

# Phase 5 — Data Visualization

## Day 11 — Matplotlib

**Objective:** Create meaningful static visualizations.

- **Developer A:** Sales trend, store sales comparison, return analysis, and sales distribution.
- **Developer B:** Product category comparison, top products, customer contribution, and product price distribution.
- **Shared:** Agree on chart naming, units, labels, titles, reusable visualization conventions, and output directory structure.

**Expected deliverable:** Matplotlib charts saved under the reports directory.

**Acceptance criteria:** Every chart has a meaningful title and labelled axes; units are clear; aggregation levels are correct; and charts use analytical outputs rather than hardcoded values.

## Day 12 — Seaborn and Insight Development

**Objective:** Develop advanced visualizations and communicate findings.

- **Developer A:** Create store and sales visualizations.
- **Developer B:** Create product and customer visualizations.
- **Shared:** Use Seaborn for appropriate distributions, category comparisons, correlation heatmaps, and analytical plots. Write business observations for major charts.

**Expected deliverable:** Visualization report containing charts and written observations.

**Acceptance criteria:** Visualizations answer defined business questions; correlation is not described as causation; observations are supported by calculated data; charts are readable; and major observations include relevant metrics or evidence.

# Phase 6 — Testing and Git Collaboration

## Day 13 — Unit and Integration Testing

**Objective:** Test the application systematically.

- **Developer A:** Test transaction ingestion, transaction validation, sales calculations, and inventory analytics.
- **Developer B:** Test product ingestion, product validation, customer analytics, and supplier analytics.
- **Shared:** Use Pytest fixtures, parameterized tests, edge cases, integration tests, and error-handling tests.

**Expected deliverable:** Automated test suite.

**Acceptance criteria:** Core business calculations have tests; invalid inputs and expected exceptions are tested; tests run from the project root; tests do not depend on machine-specific paths; and critical edge cases are covered.

## Day 14 — Git and Team Integration

**Objective:** Establish a professional collaboration workflow.

Both developers practice branch creation, meaningful commits, pull requests, code reviews, merging, conflict resolution, and reverting changes.

**Shared tasks:** Integrate completed modules, review shared module changes, resolve integration issues, and confirm that the main branch remains runnable.

**Expected deliverable:** Integrated codebase with reviewed changes.

**Acceptance criteria:** Developers use separate working branches; changes are reviewed before merging; main remains runnable; integration issues are recorded and resolved; and unreviewed changes are not merged into main.

# Phase 7 — Application Architecture and Dashboard

## Day 15 — Application Architecture

**Objective:** Organize the project into maintainable layers.

- **Developer A:** Prepare sales, store, and inventory services.
- **Developer B:** Prepare product, customer, and supplier services.
- **Shared:** Define ingestion, validation, cleaning, model, analytics, service, visualization, and application layers.

**Expected deliverable:** Integrated application architecture with clear module responsibilities.

**Acceptance criteria:** Business logic is separate from UI logic; modules have clear responsibilities; dependencies are understandable; application services can be called independently of Streamlit; and shared functionality is not unnecessarily duplicated.

## Day 16 — Streamlit Dashboard Foundation

**Objective:** Build the interactive dashboard foundation.

- **Developer A:** Build the Sales page.
- **Developer B:** Build Product and Customer pages.
- **Shared:** Build application entry point, sidebar navigation, dashboard layout, shared filters, common KPI components, Executive Overview, and Data Quality page.

**Expected deliverable:** Working Streamlit dashboard with the first core pages.

**Acceptance criteria:** Application starts successfully; navigation works; filters affect relevant charts and metrics; UI contains no duplicated business logic; and empty or invalid data states are handled clearly.

## Day 17 — Complete Dashboard and Export Features

**Objective:** Complete dashboard functionality.

- **Developer A:** Build Store and Inventory pages.
- **Developer B:** Build Supplier analytics and Product/Customer drill-downs.
- **Shared:** Implement date, store, and relevant product/category filters; data exports; data quality summary; and inventory snapshot freshness labels.

**Expected deliverable:** Complete dashboard with all agreed pages.

**Acceptance criteria:** All seven dashboard pages are accessible; filters behave consistently; exported data matches selected filters; inventory dates are clearly displayed; unsupported metrics are not presented; and dashboard calculations use the analytics layer.

# Phase 8 — Quality Assurance and Delivery

## Day 18 — End-to-End QA

**Objective:** Validate the entire system.

- **Developer A:** Validate transactions, sales metrics, stores, and inventory.
- **Developer B:** Validate products, customers, and suppliers.
- **Shared:** Perform end-to-end pipeline testing, regression testing, data reconciliation, fresh environment setup, documentation review, and known limitation review.

**Expected deliverable:** QA report and release candidate.

**Acceptance criteria:** Pipeline runs from raw data to dashboard; row counts are reconciled; critical metrics are checked independently; no unresolved critical defects remain; setup instructions work in a fresh environment; and data quality issues are visible and accounted for.

## Day 19 — Final Demonstration and Handover

**Objective:** Deliver the completed project.

- **Developer A:** Demonstrate transaction processing, sales analytics, store analytics, and inventory analytics.
- **Developer B:** Demonstrate product analytics, customer analytics, and supplier analytics.
- **Shared:** Demonstrate the complete dashboard; explain architecture, validation framework, business metrics, and limitations; complete README; and tag the release.

**Expected deliverable:** Final Retail Business Intelligence Platform release.

**Acceptance criteria:** Both developers can run the application, explain the full architecture and major business rules, documentation is complete, final code is committed and tagged, and both developers can independently demonstrate the application.

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
├── notebooks/
│
├── src/
│   └── retail_bi/
│       ├── config/
│       ├── ingestion/
│       ├── validation/
│       ├── cleaning/
│       ├── exceptions/
│       ├── reporting/
│       ├── models/
│       ├── analytics/
│       ├── services/
│       ├── utils/
│       └── visualization/
│
├── app/
│   ├── pages/
│   └── components/
│
├── tests/
├── docs/
├── logs/
├── requirements.txt
├── README.md
└── .gitignore
```

| Folder | Responsibility |
|---|---|
| `data/raw` | Original input datasets |
| `data/processed` | Cleaned and integrated datasets |
| `data/quarantine` | Rejected or problematic records |
| `reports` | Generated charts and reports |
| `notebooks` | Exploration and experimentation |
| `config` | Application and file path configuration |
| `ingestion` | Reading input datasets |
| `validation` | Data quality rules |
| `cleaning` | Data cleaning operations |
| `exceptions` | Custom exceptions |
| `reporting` | Validation and processing reports |
| `models` | Data structures and domain models |
| `analytics` | Business metrics and analysis |
| `services` | Application-level orchestration |
| `utils` | Shared utilities such as logging |
| `visualization` | Reusable chart generation |
| `app` | Streamlit application |
| `tests` | Automated tests |
| `docs` | Technical and business documentation |
| `logs` | Application logs |

The structure should evolve as the application grows. Do not create empty modules or unnecessary layers merely to match the proposed structure.

# 7. Final Dashboard Scope

The final dashboard contains seven pages.

## 1. Executive Overview

- Total net sales.
- Total orders.
- Total signed quantity, with return treatment documented.
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

# 8. Daily Working Process

Every working day follows this process:

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

A day is not complete merely because code has been written. It is complete when the assignment is implemented, expected output is produced, tests pass, code review is complete, shared work is integrated, and acceptance criteria are met.

# 9. Definition of Done

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

# 10. Technical Learning Checklist

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
13. Avoid unnecessary abstractions; build only what the project needs.
14. Every reusable component must have a clear reason to exist.

# 12. Final Deliverables

At the end of the 19-day project, the team should have:

1. Complete Python source code.
2. Seven-dataset ingestion pipeline.
3. Reusable processing and validation foundation.
4. Data profiling report.
5. Data validation framework.
6. Data cleaning pipeline.
7. Quarantine outputs.
8. Integrated analytical datasets.
9. Retail business metrics.
10. Inventory and supplier analytics.
11. Matplotlib and Seaborn visualizations.
12. Streamlit dashboard.
13. Automated tests.
14. Git repository with meaningful commit history.
15. README and technical documentation.
16. Final QA report.
17. Final project demonstration.

**Final goal:** Both developers should be able to independently explain, run, test, and extend the Retail Business Intelligence Platform—not merely demonstrate code written during the project.

