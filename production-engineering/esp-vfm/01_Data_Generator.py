import pandas as pd
import numpy as np

def generate_esp_data(n_samples=2000):
    np.random.seed(42)
    
    # 1. Randomize Pump Frequency (30Hz to 60Hz)
    freq = np.random.uniform(30, 60, n_samples)
    
    # 2. Randomize Intake Pressure (Resevoir pressure fluctuations)
    # Range: 400 psi to 800 psi
    p_intake = np.random.uniform(400, 800, n_samples)
    
    # 3. Simulate Liquid Rate (Target) based on system capacity
    # Higher frequency allows for higher potential rates
    # We simulate a random operational setpoint for the choke/well
    max_rate_at_freq = 50 * freq  # Theoretical max rate capability
    rate = np.random.uniform(0.5 * max_rate_at_freq, 0.95 * max_rate_at_freq)
    
    # 4. Calculate Discharge Pressure using Pump Curve Physics
    # Pump Head (psi) approx = A * freq^2 - B * rate^2
    # This is a simplified pump curve equation.
    
    # Coefficients (tuned for realistic oilfield values)
    A = 0.5  
    B = 0.0002 
    
    generated_head_psi = (A * freq**2) - (B * rate**2)
    
    # Add noise to simulate sensor error and fluid property changes (viscosity/gas)
    noise = np.random.normal(0, 15, n_samples) 
    
    # Discharge = Intake + Head + Noise
    p_discharge = p_intake + generated_head_psi + noise
    
    # Create DataFrame
    df = pd.DataFrame({
        'pump_frequency_hz': np.round(freq, 1),
        'intake_pressure_psi': np.round(p_intake, 1),
        'discharge_pressure_psi': np.round(p_discharge, 1),
        'liquid_rate_bpd': np.round(rate, 1)
    })
    
    # Filter out impossible physics (negative pressure diff)
    df = df[df['discharge_pressure_psi'] > df['intake_pressure_psi']]
    
    return df

if __name__ == "__main__":
    df = generate_esp_data()
    df.to_csv('esp_vfm_data.csv', index=False)
    print("Dataset 'esp_vfm_data.csv' created successfully!")