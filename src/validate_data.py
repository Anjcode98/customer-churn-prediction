from pathlib import Path
import pandas as pd


PROJECT_ROOT = Path(__file__).resolve().parents[1]

DATA_PATH = (
    PROJECT_ROOT
    / "data"
    / "raw"
    / "WA_Fn-UseC_-Telco-Customer-Churn.csv"
)

REQUIRED_COLUMNS = {
    "customerID",
    "tenure",
    "Contract",
    "MonthlyCharges",
    "TotalCharges",
    "Churn",
}


def validate_dataset(path: Path) -> dict:
    if not path.is_file():
        raise FileNotFoundError(f"Dataset not found: {path}")

    df = pd.read_csv(path)

    missing_columns = REQUIRED_COLUMNS - set(df.columns)

    if missing_columns:
        raise ValueError(
            f"Missing required columns: {sorted(missing_columns)}"
        )

    if df.empty:
        raise ValueError("Dataset is empty")

    duplicate_ids = int(df["customerID"].duplicated().sum())

    invalid_churn = int(
        (~df["Churn"].isin(["Yes", "No"])).sum()
    )

    numeric_charges = pd.to_numeric(
        df["TotalCharges"],
        errors="coerce"
    )

    invalid_charges = int(numeric_charges.isna().sum())

    return {
        "rows": len(df),
        "columns": len(df.columns),
        "duplicate_customer_ids": duplicate_ids,
        "invalid_churn_values": invalid_churn,
        "missing_or_invalid_total_charges": invalid_charges,
    }


if __name__ == "__main__":
    results = validate_dataset(DATA_PATH)

    for key, value in results.items():
        print(f"{key}: {value}")

    if (
        results["duplicate_customer_ids"] > 0
        or results["invalid_churn_values"] > 0
    ):
        raise SystemExit("Critical validation checks failed")
