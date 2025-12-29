import pandas as pd
import numpy as np
import random

def get_facies_properties():
    """
    Define 10 distinct Facies with Mean and StdDev for:
    GR (Gamma Ray), RHOB (Density), NPHI (Neutron), RT (Resistivity)
    """
    # Format: 'Name': {'Log': (Mean, StdDev)}
    return {
        0:  {'Name': 'Clean Sand',      'GR': (30, 5),   'RHOB': (2.20, 0.03), 'NPHI': (0.15, 0.02), 'RT': (50, 10)},
        1:  {'Name': 'Shaly Sand',      'GR': (60, 8),   'RHOB': (2.35, 0.04), 'NPHI': (0.22, 0.03), 'RT': (20, 5)},
        2:  {'Name': 'Siltstone',       'GR': (80, 10),  'RHOB': (2.45, 0.03), 'NPHI': (0.25, 0.03), 'RT': (10, 2)},
        3:  {'Name': 'Marine Shale',    'GR': (120, 15), 'RHOB': (2.55, 0.05), 'NPHI': (0.35, 0.04), 'RT': (3, 1)},
        4:  {'Name': 'Organic Shale',   'GR': (150, 20), 'RHOB': (2.30, 0.05), 'NPHI': (0.30, 0.04), 'RT': (15, 5)}, # High GR, Low Rho (Kerogen)
        5:  {'Name': 'Limestone',       'GR': (15, 5),   'RHOB': (2.71, 0.02), 'NPHI': (0.02, 0.01), 'RT': (200, 50)},
        6:  {'Name': 'Dolomite',        'GR': (20, 8),   'RHOB': (2.85, 0.03), 'NPHI': (0.05, 0.02), 'RT': (150, 40)},
        7:  {'Name': 'Anhydrite',       'GR': (5, 2),    'RHOB': (2.95, 0.01), 'NPHI': (0.01, 0.01), 'RT': (1000, 200)},
        8:  {'Name': 'Tight Sand',      'GR': (40, 8),   'RHOB': (2.55, 0.04), 'NPHI': (0.08, 0.02), 'RT': (80, 20)},
        9:  {'Name': 'Coal',            'GR': (25, 5),   'RHOB': (1.40, 0.10), 'NPHI': (0.45, 0.05), 'RT': (30, 10)} 
    }

def generate_master_stratigraphy(n_layers=500):
    """
    Creates a reference sequence of layers (Geologic Time).
    This ensures all wells encounter the same 'zones', just at different depths/thicknesses.
    """
    layers = []
    # Markov-like transition probabilities to ensure realistic bedding
    # (e.g., Sand is more likely to be near Shaly Sand than Anhydrite)
    current_facies = 3 # Start with Marine Shale
    
    for _ in range(n_layers):
        # Pick next facies (simple random walk for variety)
        change = np.random.choice([0, 0, 0, 1, -1, 2, -2]) # High chance to stay or move slightly
        current_facies = np.clip(current_facies + change, 0, 9)
        
        # Base thickness for this layer in the master template (in samples)
        # Average 500 samples per layer to fill space
        base_thickness = np.random.randint(100, 800) 
        
        layers.append({
            'Facies': current_facies,
            'Base_Thickness': base_thickness
        })
    return layers

def generate_field_data(n_wells=15, rows_per_well=15000):
    np.random.seed(99) # Reproducible geology
    
    facies_props = get_facies_properties()
    master_layers = generate_master_stratigraphy()
    
    all_data = []
    
    # Define Well Locations (X, Y) to create structural dip
    # We arrange wells in a generic 3x5 grid logic or random scatter
    well_locations = []
    for i in range(n_wells):
        well_locations.append({
            'WellID': f'WELL-{i+1:02d}',
            'X': np.random.randint(0, 10000),
            'Y': np.random.randint(0, 10000)
        })
        
    print(f"Generating data for {n_wells} wells with 'Dynamic Contour' simulation...")
    
    for well in well_locations:
        well_data = []
        
        # 1. Structural Dip Simulation
        # Calculate a Start Depth based on X, Y (Plane equation: Z = aX + bY + c)
        # This makes the same zones appear deeper in some wells (contouring)
        dip_x = 0.05  # 5m drop per 100m X
        dip_y = -0.02 # 2m rise per 100m Y
        start_depth = 1000 + (well['X'] * dip_x) + (well['Y'] * dip_y)
        
        current_depth = start_depth
        rows_generated = 0
        
        # 2. Stratigraphic Variation
        # We iterate through the Master Layers, but stretch/squeeze them for this specific well
        layer_idx = 0
        
        while rows_generated < rows_per_well:
            # Cycle through master layers (loop if we run out)
            layer_template = master_layers[layer_idx % len(master_layers)]
            
            # Apply "Stretch/Squeeze" factor (Heterogeneity)
            # Each well sees the layer with +/- 30% thickness variation
            thickness_factor = np.random.uniform(0.7, 1.3) 
            thickness = int(layer_template['Base_Thickness'] * thickness_factor)
            
            # Don't exceed the requested rows_per_well
            if rows_generated + thickness > rows_per_well:
                thickness = rows_per_well - rows_generated
            
            # Get Facies Properties
            fid = layer_template['Facies']
            props = facies_props[fid]
            
            # Generate Curves with Noise
            gr = np.random.normal(props['GR'][0], props['GR'][1], thickness)
            rhob = np.random.normal(props['RHOB'][0], props['RHOB'][1], thickness)
            nphi = np.random.normal(props['NPHI'][0], props['NPHI'][1], thickness)
            rt = np.random.normal(props['RT'][0], props['RT'][1], thickness)
            
            # Add some "Trend" noise (drift) to make logs look less synthetic
            drift = np.linspace(-0.5, 0.5, thickness)
            rhob += drift * 0.05
            
            # Clip to physical limits
            gr = np.clip(gr, 0, 500)
            rhob = np.clip(rhob, 1.1, 3.5)
            nphi = np.clip(nphi, 0, 0.8)
            rt = np.clip(rt, 0.1, 5000)
            
            # Create Depth Array (0.1524m or 0.5ft increments)
            depths = np.linspace(current_depth, current_depth + (thickness * 0.1524), thickness)
            
            # Stack data
            for i in range(thickness):
                well_data.append([
                    well['WellID'],
                    well['X'],
                    well['Y'],
                    depths[i],
                    gr[i],
                    rhob[i],
                    nphi[i],
                    rt[i],
                    fid, # The Label (Integer)
                    props['Name'] # The Label (String)
                ])
                
            # Update counters
            rows_generated += thickness
            current_depth = depths[-1]
            layer_idx += 1
            
        all_data.extend(well_data)
        print(f"Finished {well['WellID']} from depth {start_depth:.1f}m")

    # Create DataFrame
    cols = ['Well_ID', 'X_Loc', 'Y_Loc', 'Depth_m', 'GR', 'RHOB', 'NPHI', 'RT', 'Facies_Label', 'Facies_Name']
    df = pd.DataFrame(all_data, columns=cols)
    
    # Save
    filename = 'field_well_data.csv'
    df.to_csv(filename, index=False)
    print(f"Successfully generated {len(df)} rows across {n_wells} wells.")
    print(f"File saved as: {filename}")

if __name__ == "__main__":
    generate_field_data()