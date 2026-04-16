import pandas as pd

# Soglie basate sui sensori reali (Valori tipici industriali)
EXHAUST_LIMIT = 500.0   # °C
BEARING_LIMIT = 80.0    # °C
VIBRATION_LIMIT = 0.5   # mm/s (Esempio)

class HealthMonitor:
    def __init__(self, data: pd.DataFrame):
        self.data = data

    def find_anomalies(self):
        """Rileva criticità basate sui sensori reali."""
        # Filtriamo usando i nomi esatti delle colonne
        thermal_issues = self.data[self.data['exhaust_temp'] > EXHAUST_LIMIT]
        bearing_issues = self.data[self.data['bearing_temp'] > BEARING_LIMIT]
        # Somma vettoriale delle vibrazioni (Pitagora) per un'analisi più seria
        vibration_issues = self.data[(self.data['vibration_x']**2 + self.data['vibration_y']**2)**0.5 > VIBRATION_LIMIT]
        
        return {
            "thermal_alerts": thermal_issues,
            "bearing_alerts": bearing_issues,
            "vibration_alerts": vibration_issues
        }

    def get_system_summary(self):
        """Riassunto statistico dei sensori principali."""
        return {
            "avg_exhaust": self.data['exhaust_temp'].mean(),
            "avg_bearing": self.data['bearing_temp'].mean(),
            "max_vibration_x": self.data['vibration_x'].max(),
            "total_records": len(self.data)
        }

if __name__ == "__main__":
    from data_loader import load_turbine_data
    df = load_turbine_data()
    if df is not None:
        monitor = HealthMonitor(df)
        anomalies = monitor.find_anomalies()
        summary = monitor.get_system_summary()
        
        print("\n--- ANALISI SENSORI REALI COMPLETATA ---")
        print(f"Record totali: {summary['total_records']}")
        print(f"Temperatura Media Scarico: {summary['avg_exhaust']:.2f}°C")
        print(f"Alert Cuscinetti (Attrito): {len(anomalies['bearing_alerts'])}")
        print(f"Alert Vibrazioni: {len(anomalies['vibration_alerts'])}")