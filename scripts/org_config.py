#!/usr/bin/env python3
"""Declarative configuration for the Healthy Research Labs (@healthyinc-labs) profile pipeline.

Defines organization-scoped scientific research domain classification rules, methodology
badges, and collaborator display metadata for the scientific R&D subsidiary profile.
"""

ORG_NAME = "healthyinc-labs"
REPO_FULL_NAME = "healthyinc-labs/.github"

MATRIX_SUBTITLE = "Active Scientific Research Capability Overview"
MATRIX_HEADERS = (
    "Scientific Research Domain",
    "Tooling & Methodology Stack",
    "Domain Scope & Research Deliverables",
)

STATS_HEADING = "### 📈 Global Research Activity & Infrastructure"
VELOCITY_UNIT_LABEL = "Commits across active scientific research workstreams"
ACTIVE_CONTRIBUTORS_LABEL = "Active Researchers"
MIN_DISPLAY_ACTIVE_CONTRIBUTORS = 3

# Ordered baseline research maintainers and collaborators displayed in the avatar strip.
# Any additional organization member or outside collaborator in @healthyinc-labs is
# appended automatically during each twice-daily scheduled refresh.
CORE_COLLABORATORS = [
    ("Chali-healthy", "Chalinda Weerasinghe (@Chali-healthy)"),
    ("anbhimi", "Ananth (@anbhimi)"),
    ("pradeeban", "Dr. Pradeeban Kathiravelu (@pradeeban)"),
]
AUTO_INCLUDE_ALL_ORG_MEMBERS = True

BADGE_LIBRARY = {
    "python": "![Python](https://img.shields.io/badge/Python-3572A5?style=flat-square&logo=python&logoColor=white)",
    "jupyter": "![Jupyter](https://img.shields.io/badge/Jupyter_Notebooks-F37626?style=flat-square&logo=jupyter&logoColor=white)",
    "duckdb": "![DuckDB](https://img.shields.io/badge/DuckDB-FFF000?style=flat-square&logo=duckdb&logoColor=black)",
    "polars": "![Polars](https://img.shields.io/badge/Polars-CD792C?style=flat-square&logo=polars&logoColor=white)",
    "mimic": "![MIMIC Clinical Data](https://img.shields.io/badge/MIMIC_Clinical_Data-007ACC?style=flat-square&logo=git&logoColor=white)",
    "physionet": "![PhysioNet DUA](https://img.shields.io/badge/PhysioNet_DUA-2B7489?style=flat-square&logo=apache&logoColor=white)",
    "plpgsql": "![PostgreSQL](https://img.shields.io/badge/PostgreSQL_PLpgSQL-336791?style=flat-square&logo=postgresql&logoColor=white)",
    "nsf": "![NSF SBIR/STTR/TTP](https://img.shields.io/badge/NSF_SBIR/STTR/TTP-003366?style=flat-square&logo=usps&logoColor=white)",
    "nih": "![NIH Framework](https://img.shields.io/badge/NIH_Framework-004B87?style=flat-square&logo=gov&logoColor=white)",
    "tex": "![LaTeX](https://img.shields.io/badge/LaTeX_Manuscripts-008080?style=flat-square&logo=latex&logoColor=white)",
    "open_science": "![Data Management Plan](https://img.shields.io/badge/Data_Management_Plan-34C759?style=flat-square&logo=gitbook&logoColor=white)",
    "pytorch": "![PyTorch](https://img.shields.io/badge/PyTorch-EE4C2C?style=flat-square&logo=pytorch&logoColor=white)",
    "gymnasium": "![Gymnasium](https://img.shields.io/badge/Gymnasium_Environments-000000?style=flat-square&logo=openai&logoColor=white)",
    "dag": "![DAG State Machines](https://img.shields.io/badge/DAG_State_Machines-6A1B9A?style=flat-square&logo=diagramsdotnet&logoColor=white)",
    "ido_agent": "![IDO Agents](https://img.shields.io/badge/Intelligent_Data_Objects-0A84FF?style=flat-square&logo=target&logoColor=white)",
    "cpp": "![Embedded C++](https://img.shields.io/badge/Embedded_C%2B%2B-00599C?style=flat-square&logo=c%2B%2B&logoColor=white)",
    "tinyml": "![TinyML](https://img.shields.io/badge/TinyML_Inference-FF6F00?style=flat-square&logo=tensorflow&logoColor=white)",
    "biosignals": "![Wearable Biosignals](https://img.shields.io/badge/Wearable_Biosignals-4CAF50?style=flat-square&logo=apple&logoColor=white)",
    "isac": "![ISAC RF Sensing](https://img.shields.io/badge/ISAC_Biosensor_Fusion-14F195?style=flat-square&logo=rss&logoColor=black)",
}

DEFAULT_DOMAIN = "Clinical Data Science & Benchmarking"

DOMAINS = [
    {
        "name": "Clinical Data Science & Benchmarking",
        "badges": ["python", "jupyter", "duckdb", "polars", "mimic", "physionet", "plpgsql"],
        "scope": "Reproducible Cohort Isolation, Synthetic Health Datasets & Clinical Benchmarks under PhysioNet Data Use Agreements and HIPAA Standards",
        "keywords": [
            "mimic", "benchmark", "synthetic", "dataset", "cohort", "clinical",
            "physionet", "duckdb", "polars", "ehr", "de-identif",
        ],
        "languages": ["jupyter notebook", "plpgsql", "sql", "r"],
    },
    {
        "name": "Federal Grants & Empirical Reproducibility",
        "badges": ["nsf", "nih", "tex", "open_science"],
        "scope": "NSF/NIH Empirical Validation Harnesses, Statistical Power Analysis & Formal Data Management and Sharing Plans (DMSP)",
        "keywords": [
            "nsf", "nih", "sbir", "sttr", "ttp", "grant", "reproducib",
            "dmsp", "manuscript", "proposal", "profile", "organization",
        ],
        "languages": ["tex", "markdown"],
    },
    {
        "name": "Hospital Reinforcement Learning & Simulation",
        "badges": ["pytorch", "gymnasium", "dag", "ido_agent"],
        "scope": "Multi-Agent Care Traffic Control Environments, Bed Allocation Optimization & Directed Acyclic Graph (DAG) Verification for Intelligent Data Objects (IDO)",
        "keywords": [
            "reinforcement", "rl", "hospital", "simulation", "gymnasium",
            "pettingzoo", "care-traffic", "ido", "dag", "agent", "pytorch",
        ],
        "languages": ["go"],
    },
    {
        "name": "Physical AI & Biosensor Edge Telemetry",
        "badges": ["cpp", "tinyml", "biosignals", "isac"],
        "scope": "Low-Power Biosensor Fusion, Heart Rate Variability (HRV) & Photoplethysmography (PPG) Extraction, and Integrated Sensing and Communication (ISAC)",
        "keywords": [
            "physical-ai", "biosensor", "wearable", "hrv", "ppg", "ecg",
            "scg", "tinyml", "embedded", "firmware", "isac", "iheart", "edge",
        ],
        "languages": ["c", "c++", "verilog", "systemverilog", "matlab"],
    },
]
