REQUIRED_COLUMNS = [
    "Equipment Name", "Type", "Flowrate", "Pressure", "Temperature"
]

def validate_csv(df):
    for col in REQUIRED_COLUMNS:
        if col not in df.columns:
            raise ValueError(f"Missing column: {col}")