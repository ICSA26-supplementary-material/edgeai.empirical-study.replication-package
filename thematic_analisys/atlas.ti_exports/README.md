# ATLAS.ti Exports

This folder contains all **ATLAS.ti exports** used in our EdgeAI architecture study.  
The goal of this README is to help readers understand **what each export file contains**,  
**how it was generated**, and **how it can be reused or replicated**.

> 🧭 **How to read this document**  
> For each exported file we provide a **short, focused description**:
> - **Purpose:** why this file exists in the pipeline.
> - **Contents:** what kind of data it includes (codes, quotations, networks, etc.).
> - **Usage:** how this export is used in our analyses or replication.

---

## 1. ATLAS.ti Project Context

- **Tool version:** ATLAS.ti (desktop) – *version to be added if needed*  
- **Project scope:** qualitative/thematic coding of EdgeAI-related architectural fragments,
  including codes, categories, memos, and relationships used for RQ1.x.  
- **Main tasks supported by these exports:**
  - Reconstructing the **coding scheme** (codes, categories, families).
  - Inspecting **quotations / fragments** and their assigned codes.
  - Generating tables and statistics for **guidelines, domains, and quality attributes**.
  - Validating and replicating the **thematic analysis process**.

---

## 2. File Overview

Below we will document **each export file** individually.

For every file, we will add a mini-section in the following format:


### 2.1 20250914_theme_frequencies.csv

This file contains the **frequency distribution of the 18 top-level themes** (T1–T18) that form the EdgeAI guideline taxonomy.
It is generated from the ATLAS.ti Code Manager by exporting **only the top-level codes**, each of which represents a major architectural concern in EdgeAI systems.

Each row corresponds to one thematic family (e.g., T1, T2, …, T18) and reports the number of quotations coded with that theme.

### **Columns**

| Column                          | Description                                                               |
| ------------------------------- | ------------------------------------------------------------------------- |
| **Code**                        | The theme name (e.g., “T1. Edge Connectivity & Communication Protocols”). |
| **Magnitude Degree**            | Total number of quotations associated with that theme.                    |
| **Density**                     | Number of relationships with other codes (0 for themes, unless linked).   |
| **Groups**                      | Code group classification (“Themes”).                                     |
| **Number of Groups**            | Count of groups the theme belongs to.                                     |
| **Comment**                     | Any memo associated with the theme (empty here).                          |
| **Creation/Modification Dates** | Metadata recorded during coding.                                          |

### **Purpose**

This file summarizes the **overall thematic landscape** of the analyzed repositories, showing which architectural concerns are more or less represented in real-world EdgeAI projects.
It supports:

* quantitative analysis of guideline relevance,
* cross-theme comparisons,
* and the generation of figures showing frequency distributions across themes.

- **Purpose:**  
  This export summarizes the **frequency of all themes** identified during the ATLAS.ti coding process. It provides a quantitative view of how often each high-level theme appeared across the coded fragments.

- **Contents:**  
  A CSV table containing at least two columns:  
  - **theme** – the thematic label or category assigned during axial/thematic coding.  
  - **frequency** – the number of times that theme appeared in the dataset (i.e., total quotations coded with that theme or aggregated subcodes).  

  This export represents the **final consolidated theme frequency table** used for descriptive statistics in the study.

- **Usage:**  
  
  Researchers replicating this study can recompute this table by regrouping codes → categories → themes following the same hierarchical structure documented in the coding scheme.


### 2.2 20250914_code_list_frequencies.csv


This file is an export of the **Code Manager** in ATLAS.ti and contains the full hierarchical structure of the coding scheme used in the study.
It lists each **code family**, its **sub-codes**, and their quantitative metadata.

The file includes:

* the **hierarchical organization** of the guideline themes (e.g., T1, T2, ...),
* all **individual codes** within each theme,
* the **magnitude degree** (i.e., the number of quotations coded with each code),
* code **densities** (number of relationships with other codes),
* membership in **code groups** (e.g., “Themes”, “ATLAS”),
* the number of groups per code, and
* creation/modification timestamps.

### **Columns**

| Column                | Description                                                         |
| --------------------- | ------------------------------------------------------------------- |
| **Code**              | The family or individual code (hierarchical indentation preserved). |
| **Magnitude Degree**  | Number of quotations coded with this code (frequency).              |
| **Density**           | Number of relationships this code has with other codes.             |
| **Groups**            | The groups/categories this code belongs to (e.g., “Themes”).        |
| **Number of Groups**  | Count of groups associated with the code.                           |
| **Comment**           | Any memo associated with the code.                                  |
| **Creation Date**     | When the code was created.                                          |
| **Modification Date** | When the code was last updated.                                     |

This file represents the **complete coding taxonomy** used during the thematic analysis, linking each guideline theme to its constituent codes and providing the frequencies used to support the quantitative analysis of EdgeAI architectural guidelines.


- **Purpose:**  
  This file provides the **frequency of each individual code** used during the ATLAS.ti open coding phase.  
  While the theme frequency export aggregates information at a higher level, this file captures the **granular coding activity**, enabling deeper quantitative inspection of the coding scheme.

- **Contents:**  
  A CSV table typically containing:  
  - **code** – the exact code label assigned to quotations during open coding.  
  - **frequency** – the number of quotations associated with each code.  

  The table includes both low-level codes and more abstract codes, depending on how the coding hierarchy was structured.

- **Usage:**  
 
  This export is essential for replicating the **open coding stage** and for reconstructing the prevalence of each architectural construct identified in the study.

### 2.3 20250914_code_coocurrrence.xlsx

This file contains the **complete code co-occurrence analysis** exported from ATLAS.ti.
It provides a detailed view of how often pairs of codes appeared together in the same quotation, enabling the identification of semantic relationships and supporting the construction of higher-level categories and themes.

The workbook contains **three sheets**:

### **1. Code Co-occurrence Table (Visual Heatmap)**

A matrix visualization where:

* rows and columns represent codes,
* cell values indicate co-occurrence counts,
* color intensity (green scale) reflects the strength of the relationship.

### **2. Code Co-occurrence Count**

A numeric matrix with raw co-occurrence frequencies.
This sheet supports quantitative analyses, chart generation, and replication.

### **3. Code Co-occurrence Coefficient**

A normalized co-occurrence matrix calculated by ATLAS.ti using similarity coefficients (e.g., Jaccard-based metrics).
Values range from 0 to 1 and represent the relative strength of association between code pairs.

### **Purpose**

This file supports:

* mapping semantic relationships between architectural concerns,
* validating the theme hierarchy (T1–T18),
* generating quantitative insights for the thematic analysis, and
* ensuring methodological transparency and replicability.

- **Purpose:**  
  This export contains the **code co-occurrence matrix** generated by ATLAS.ti.  
  It documents how frequently two codes appear together in the same quotation or fragment, enabling analysis of relationships, patterns, and conceptual proximity across the coded dataset.

- **Contents:**  
  An Excel file (`.xlsx`) typically containing:
  - A **matrix/table** where rows and columns represent all codes.
  - Each cell contains the **co-occurrence frequency** between the pair (row code ↔ column code).
  - Depending on the ATLAS.ti export, the file may also include:
    - normalized co-occurrence values  
    - percentage co-occurrence  
    - filters for minimum frequency  

  This dataset reflects **associations between architectural concerns** emerging from the repositories.

- **Usage:**  
 
  This export is particularly valuable for **data-driven theme formation** and validating the cohesion of guideline families.

### 2.4 20250914_quotation_export.csv


## **File: `20250914_citation_manager.csv` (Quotation Export)**

This file is the **full export of all quotations (fragments)** that were coded during the thematic analysis.
Despite the filename, the content corresponds to an **ATLAS.ti Quotation Report**, not to citation metadata.

Each row represents a distinct **fragment extracted from the GitHub repositories** and coded according to the EdgeAI guideline taxonomy.
The file integrates:

* the **raw text of each fragment**,
* the **document of origin**,
* all **codes applied**,
* the **researcher’s comments**,
* **positional metadata** (start/end), and
* timestamps for creation and modification.

### **Columns**

| Column                | Description                                                               |
| --------------------- | ------------------------------------------------------------------------- |
| **Number**            | Unique quotation identifier (e.g., 1:1).                                  |
| **Reference**         | Paragraph marker in the source document.                                  |
| **Name**              | Optional label (usually empty for raw fragments).                         |
| **Text Content**      | The full text of the extracted fragment.                                  |
| **Document**          | Source document name (e.g., “[ATLAS] – Codifying Fragments”).             |
| **Codes**             | List of all codes applied to the fragment.                                |
| **Number of Codes**   | Total number of codes associated with the fragment.                       |
| **Comment**           | Researcher notes or analytic memos.                                       |
| **Initial Position**  | Start coordinate of the quotation in the source document.                 |
| **Final Position**    | End coordinate.                                                           |
| **Extensão**          | Length of the quotation (characters or lines depending on configuration). |
| **Creation Date**     | When the fragment was created during coding.                              |
| **Modification Date** | When it was last updated.                                                 |

This file represents the **core dataset** used for generating codes, categories, themes, and ultimately architectural guidelines for EdgeAI systems.

---

- **Purpose:**  
  This export contains all **quotation-level citation references** generated inside ATLAS.ti.  
  It links each coded fragment to its **original source repository**, commit, file, or documentation segment.  
  This file ensures **traceability**, allowing any researcher to verify where each fragment came from.

- **Contents:**  
  A CSV table typically including:
  - **quotation_id** – unique ID assigned by ATLAS.ti to each fragment.  
  - **source_reference / document / origin** – the file or repository from which the quotation was extracted.  
  - **metadata** – additional contextual information such as authorship, repository name, filename, or other identifiers.  
  - **links or citation strings** – used internally to track provenance from GitHub to ATLAS.ti.  

  This dataset captures **the mapping between qualitative evidence and source artifacts**, essential for reproducibility.

- **Usage:**  
  
  It is especially important for reviewers and replicators who need to verify  
  **“Where did this fragment come from?”** for any guideline, category, or theme.

### 2.5 20250914_codebook_full.csv


This file contains the **complete codebook** used during the thematic analysis.
Exported directly from ATLAS.ti, it documents the full hierarchical structure of the coding schema developed for the study.

Each row represents a **code** or **sub-code**, along with its assigned **code groups**, which indicate the thematic families or analytical categories it belongs to.

### **Columns**

| Column                                 | Description                                                                                                    |
| -------------------------------------- | -------------------------------------------------------------------------------------------------------------- |
| **Código / Code**                      | The name of the code, including theme-prefix hierarchy (e.g., “T1.”).                                          |
| **Comentário / Comment**               | The code definition or explanatory note (if provided).                                                         |
| **Grupo de Códigos 1–4 / Code Groups** | The groups, families, or thematic categories to which the code belongs (e.g., “Themes”, “ATLAS”, “Research2”). |

### **Purpose**

This codebook defines the complete analytic structure used in the study, including:

* the **18 high-level thematic families** (T1–T18),
* all **sub-codes** associated with each theme,
* classification groups indicating the origin and role of each code,
* and the organization used to interpret the 400 curated textual fragments.

It is an essential document for ensuring **replicability**, **traceability**, and **methodological transparency** in the thematic analysis of EdgeAI architectural guidelines.

- **Purpose:**  
  This file contains the **complete ATLAS.ti codebook** used in the study.  
  It documents every code created during open, axial, and thematic coding, including definitions, descriptions, and hierarchical relationships.  
  It serves as the **authoritative reference** for understanding the meaning and intent behind each code.

- **Contents:**  
  A CSV file typically including the following fields:
  - **code** – the exact name of the code.  
  - **description / definition** – a short explanation detailing what the code represents.  
  - **category / group / family** – higher-level grouping assigned to the code (if structured).  
  - **theme (if applicable)** – the theme or conceptual cluster associated with the code.  
  - **created_by / created_on** – optional metadata about authorship or session.  
  - **remarks / comments** – any additional guidance used during coding.

  This export consolidates the **semantic meaning** behind the entire coding scheme used in the EdgeAI architectural analysis.

- **Usage:**  
  
  This file is particularly important for reviewers who want to understand **exactly how codes were defined**, and for researchers who wish to replicate or extend the thematic analysis.