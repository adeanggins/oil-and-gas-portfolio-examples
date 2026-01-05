import pandas as pd
import numpy as np
import random

def generate_esp_data(n_pumps=5, distinct_cycles_per_pump=2):
    """
    Generates synthetic run-to-failure data for Electrical Submersible Pumps.
    Simulates degradation in Amperage and Vibration until failure.
    """
    data = []
    
    for pump_id in range(1, n_pumps + 1):
        for cycle in range(1, distinct_cycles_per_pump + 1):
            # Random lifetime for this pump cycle (e.g., between 500 to 1500 hours)
            lifetime = np.random.randint(500, 1500)
            
            # Base sensor readings
            base_amp = 50 + np.random.normal(0, 2)
            base_vib = 0.5 + np.random.normal(0, 0.1)
            base_temp = 180 + np.random.normal(0, 5)
            
            for t in range(lifetime):
                # RUL is the reverse of time elapsed
                rul = lifetime - t - 1
                
                # Degradation function (exponential increase as we near failure)
                # Healthy phase: 0 to 80% of life. Fault phase: 80% to 100%.
                health_factor = 1 if t < 0.8 * lifetime else np.exp((t - 0.8 * lifetime) / 50)
                
                # Add noise and degradation
                amp = base_amp + np.random.normal(0, 1) + (0.05 * health_factor if t > 0.8 * lifetime else 0)
                # Vibration spikes heavily near end of life
                vib = base_vib + np.random.normal(0, 0.05) + (0.02 * health_factor if t > 0.8 * lifetime else 0)
                # Temp rises slowly
                temp = base_temp + (0.1 * (t/lifetime * 10)) + np.random.normal(0, 1)
                
                data.append({
                    'pump_id': pump_id,
                    'cycle_id': cycle,
                    'timestamp_hour': t,
                    'amperage': amp,
                    'vibration': vib,
                    'motor_temp_f': temp,
                    'RUL': rul
                })
                
    df = pd.DataFrame(data)
    df.to_csv('esp_sensor_data.csv', index=False)
    print(f"Data generated: {len(df)} rows saved to esp_sensor_data.csv")

if __name__ == "__main__":
    generate_esp_data()