# Threshold constants
MAX_PRESSURE = 120
MAX_TEMPERATURE = 350


def calculate_health_score(df):
    score = 100

    pressure_violations = int((df["Pressure"] > MAX_PRESSURE).sum())
    temperature_violations = int((df["Temperature"] > MAX_TEMPERATURE).sum())

    score -= pressure_violations * 10
    score -= temperature_violations * 10

    return int(max(score, 0))


def health_status(score):
    if score >= 80:
        return "Healthy"
    elif score >= 60:
        return "Needs Attention"
    else:
        return "Critical"


def analyze(df):
    alerts = []
    recommended_actions = []

    for _, row in df.iterrows():
        pressure = float(row["Pressure"])
        temperature = float(row["Temperature"])
        name = str(row["Equipment Name"])

        if pressure > 140:
            alerts.append(f"🔴 CRITICAL: {name} pressure dangerously high")
            recommended_actions.append(
                f"Immediately reduce pressure and inspect safety valve for {name}"
            )
        elif pressure > MAX_PRESSURE:
            alerts.append(f"🟡 WARNING: {name} pressure above safe limit")
            recommended_actions.append(
                f"Monitor pressure and schedule maintenance for {name}"
            )

        if temperature > 400:
            alerts.append(f"🔴 CRITICAL: {name} temperature dangerously high")
            recommended_actions.append(
                f"Shut down and inspect cooling system for {name}"
            )
        elif temperature > MAX_TEMPERATURE:
            alerts.append(f"🟡 WARNING: {name} temperature above safe limit")
            recommended_actions.append(
                f"Reduce load and check heat dissipation for {name}"
            )

    health_score = calculate_health_score(df)

    return {
        "total_equipment": int(len(df)),
        "avg_flowrate": float(round(df["Flowrate"].mean(), 2)),
        "avg_pressure": float(round(df["Pressure"].mean(), 2)),
        "avg_temperature": float(round(df["Temperature"].mean(), 2)),
        "type_distribution": df["Type"].value_counts().to_dict(),
        "health_score": health_score,
        "health_status": health_status(health_score),
        "alerts": alerts,
        "recommended_actions": recommended_actions,
        "equipment_details": [
            {
                "name": str(row["Equipment Name"]),
                "type": str(row["Type"]),
                "flowrate": float(row["Flowrate"]),
                "pressure": float(row["Pressure"]),
                "temperature": float(row["Temperature"]),
            }
            for _, row in df.iterrows()
        ],
    }