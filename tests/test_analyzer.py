import pytest
import pandas as pd
from src.analyzer import HealthMonitor

def test_anomaly_detection_logic():
    """
    Verifica che il monitor rilevi correttamente un'anomalia 
    quando i dati superano le soglie.
    """
    # Creiamo un DataFrame "finto" con un caso critico
    fake_data = pd.DataFrame({
        'exhaust_temp': [900.0, 100.0], # Uno sopra soglia, uno sotto
        'bearing_temp': [90.0, 40.0],   # Uno sopra soglia, uno sotto
        'vibration_x': [0.1, 0.1],
        'vibration_y': [0.1, 0.1]
    })
    
    monitor = HealthMonitor(fake_data)
    alerts = monitor.find_anomalies()
    
    # Verifichiamo che venga trovato esattamente 1 alert per tipo
    assert len(alerts['thermal_alerts']) == 1
    assert len(alerts['bearing_alerts']) == 1
    assert alerts['bearing_alerts'].iloc[0]['bearing_temp'] == 90.0

def test_vibration_math():
    """Verifica che il calcolo vettoriale della vibrazione sia corretto."""
    # Se X=0.6 e Y=0, la vibrazione totale è 0.6 (sopra la soglia 0.5)
    high_vibration_data = pd.DataFrame({
        'exhaust_temp': [100.0],
        'bearing_temp': [40.0],
        'vibration_x': [0.6],
        'vibration_y': [0.0]
    })
    
    monitor = HealthMonitor(high_vibration_data)
    alerts = monitor.find_anomalies()
    
    assert len(alerts['vibration_alerts']) == 1