import pandas as pd
import numpy as np

def generate_synthetic_crm_data():
    np.random.seed(42)
    
    # Configuration
    n_days = 1000
    n_injectors = 10
    n_producers = 40
    date_range = pd.date_range(start='2020-01-01', periods=n_days, freq='D')
    
    # --- 1. Generate Locations (New for Expert Viz) ---
    # Random X, Y coordinates in a 5km x 5km field
    loc_data = []
    for i in range(n_injectors):
        loc_data.append({'Well': f'I{i+1:02d}', 'Type': 'Inj', 'X': np.random.uniform(0, 5000), 'Y': np.random.uniform(0, 5000)})
    for p in range(n_producers):
        loc_data.append({'Well': f'P{p+1:02d}', 'Type': 'Prod', 'X': np.random.uniform(0, 5000), 'Y': np.random.uniform(0, 5000)})
    
    df_loc = pd.DataFrame(loc_data).set_index('Well')
    df_loc.to_csv('well_locations.csv')
    print("Generated well_locations.csv")

    # --- 2. Generate Injection Rates ---
    I = np.abs(np.random.normal(loc=1000, scale=300, size=(n_days, n_injectors)))
    injector_names = [f'I{i+1:02d}' for i in range(n_injectors)]
    
    # --- 3. Define Physics & Connectivity ---
    true_gains = np.zeros((n_producers, n_injectors))
    true_taus = np.random.uniform(10, 50, size=n_producers)
    
    # Distance-based connectivity (Closer wells have higher connectivity)
    for p in range(n_producers):
        p_loc = df_loc.loc[f'P{p+1:02d}']
        distances = []
        for i in range(n_injectors):
            i_loc = df_loc.loc[f'I{i+1:02d}']
            dist = np.sqrt((p_loc.X - i_loc.X)**2 + (p_loc.Y - i_loc.Y)**2)
            distances.append(dist)
        
        # Connect to 3 closest injectors
        closest_indices = np.argsort(distances)[:3]
        weights = np.random.uniform(0.2, 0.5, size=3)
        true_gains[p, closest_indices] = weights

    # --- 4. Simulate Production ---
    Q = np.zeros((n_days, n_producers))
    Q[0, :] = np.random.uniform(500, 1000, size=n_producers)
    
    print("Simulating physics-based production data...")
    for t in range(1, n_days):
        for p in range(n_producers):
            tau = true_taus[p]
            decay = np.exp(-1 / tau)
            
            inj_contribution = 0
            for i in range(n_injectors):
                inj_contribution += true_gains[p, i] * (1 - decay) * I[t, i]
            
            Q[t, p] = Q[t-1, p] * decay + inj_contribution
            Q[t, p] += np.random.normal(0, 5) # Noise

    # --- 5. Save Data ---
    df_inj = pd.DataFrame(I, columns=injector_names, index=date_range)
    df_prod = pd.DataFrame(Q, columns=[f'P{p+1:02d}' for p in range(n_producers)], index=date_range)
    df_final = pd.concat([df_inj, df_prod], axis=1)
    df_final.index.name = 'Date'
    df_final.to_csv('production_injection_data_advance.csv')
    print("Generated production_injection_data_advance.csv")

if __name__ == "__main__":
    generate_synthetic_crm_data()