import pandas as pd
from datasets import load_dataset

def load_turbine_data():
    """
    Carica il dataset delle turbine da Hugging Face.
    Ritorna un DataFrame pandas.
    """
    print("Tentativo di caricamento dati da Hugging Face...")
    try:
        # Carichiamo il dataset scelto da te
        dataset = load_dataset("davidfertube/turbine-sensor-data")
        
        # Convertiamo la sezione 'train' in un DataFrame pandas
        df = pd.DataFrame(dataset['train'])
        
        print(f"Caricamento completato! Righe: {len(df)}, Colonne: {len(df.columns)}")
        return df
    
    except Exception as e:
        print(f"Errore critico durante il caricamento: {e}")
        return None

if __name__ == "__main__":
    # Test rapido del modulo
    df_sensors = load_turbine_data()
    if df_sensors is not None:
        print(df_sensors.head())