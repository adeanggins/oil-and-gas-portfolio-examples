import pandas as pd
import numpy as np

def generate_data():
    np.random.seed(42)
    n_samples = 3000
    n_months = 24  # Forecasting 2 years

    # 1. Generate Static Reservoir Inputs
    data = {
        'Porosity': np.random.uniform(0.15, 0.35, n_samples),
        'Permeability_mD': np.random.uniform(50, 800, n_samples),
        'Initial_Pressure_psi': np.random.uniform(2500, 4500, n_samples),
        'Thickness_ft': np.random.uniform(20, 100, n_samples)
    }
    df = pd.DataFrame(data)

    # 2. Generate Time-Series Output (Production Profiles)
    # We will use the Arps Decline Curve equation: q(t) = qi / (1 + b * Di * t)^(1/b)
    # We derive qi (Initial Rate) and Di (Decline Rate) from the geological inputs.

    profiles = []
    
    for i in range(n_samples):
        # Physics-based heuristics:
        # Initial Rate (qi) is high if Perm, Pressure, and Thickness are high.
        qi = (df.loc[i, 'Permeability_mD'] * 0.5) * \
             (df.loc[i, 'Initial_Pressure_psi'] * 0.1) * \
             (df.loc[i, 'Thickness_ft'] * 0.2) / 1000
        
        # Decline Rate (Di) is high if Perm is high (drains fast) or Porosity is low (less storage).
        Di = (df.loc[i, 'Permeability_mD'] / 1000) / (df.loc[i, 'Porosity'] * 5)
        
        # b-factor (curvature), typically between 0 and 1.
        b = 0.4 

        # Generate monthly rates
        t = np.arange(1, n_months + 1)
        q_t = qi / ((1 + b * Di * t) ** (1/b))
        
        # Add slight noise to mimic simulator numerical instability
        noise = np.random.normal(0, qi * 0.02, n_months)
        q_t += noise
        
        profiles.append(q_t)

    # 3. Create DataFrame Columns for each Month
    cols = [f'Month_{m}' for m in range(1, n_months + 1)]
    df_profiles = pd.DataFrame(profiles, columns=cols)
    
    # Combine Inputs and Outputs
    final_df = pd.concat([df, df_profiles], axis=1)
    
    final_df.to_csv('reservoir_timeseries_data.csv', index=False)
    print(f"Generated data with shape: {final_df.shape}")

if __name__ == "__main__":
    generate_data()