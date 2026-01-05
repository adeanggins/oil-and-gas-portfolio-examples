import pandas as pd
import numpy as np

def generate_synthetic_crm_data():
    np.random.seed(42)
    
    # Configuration
    n_days = 1000
    n_injectors = 10
    n_producers = 40
    date_range = pd.date_range(start='2020-01-01', periods=n_days, freq='D')
    
    # 1. Generate Injection Rates (I) with some variability
    # Injectors fluctuate (e.g., maintenance, pump changes)
    I = np.abs(np.random.normal(loc=1000, scale=300, size=(n_days, n_injectors)))
    injector_names = [f'I{i+1:02d}' for i in range(n_injectors)]
    
    # 2. Define "True" Connectivity (f_ij) and Tau (tau_j)
    # Random sparse connectivity: not every injector supports every producer
    true_gains = np.zeros((n_producers, n_injectors))
    true_taus = np.random.uniform(10, 50, size=n_producers) # Time constants between 10 and 50 days
    
    for p in range(n_producers):
        # Each producer connects strongly to 2-3 random injectors
        connected_inj = np.random.choice(range(n_injectors), size=np.random.randint(2, 4), replace=False)
        weights = np.random.uniform(0.1, 0.4, size=len(connected_inj))
        true_gains[p, connected_inj] = weights

    # 3. Simulate Production Rates (q) using CRMP Equation
    # q(t) = q(t-1)*exp(-dt/tau) + sum(f_ij * (1-exp(-dt/tau)) * I(t))
    Q = np.zeros((n_days, n_producers))
    
    # Initial rates
    Q[0, :] = np.random.uniform(500, 1000, size=n_producers)
    
    print("Simulating physics-based production data...")
    for t in range(1, n_days):
        for p in range(n_producers):
            tau = true_taus[p]
            decay = np.exp(-1 / tau)
            
            # Injection contribution
            inj_contribution = 0
            for i in range(n_injectors):
                inj_contribution += true_gains[p, i] * (1 - decay) * I[t, i]
            
            # Update production with physics + some random noise
            Q[t, p] = Q[t-1, p] * decay + inj_contribution
            
            # Add measurement noise
            Q[t, p] += np.random.normal(0, 5) 

    # 4. Create DataFrame
    df_inj = pd.DataFrame(I, columns=injector_names, index=date_range)
    df_prod = pd.DataFrame(Q, columns=[f'P{p+1:02d}' for p in range(n_producers)], index=date_range)
    
    df_final = pd.concat([df_inj, df_prod], axis=1)
    df_final.index.name = 'Date'
    
    # Save
    filename = 'production_injection_data.csv'
    df_final.to_csv(filename)
    print(f"Successfully generated {filename} with {n_injectors} Injectors and {n_producers} Producers.")

if __name__ == "__main__":
    generate_synthetic_crm_data()