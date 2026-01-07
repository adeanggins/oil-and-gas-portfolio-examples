import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

def smooth_curve(y, box_pts=5):
    """Simple moving average to smooth sensor noise"""
    box = np.ones(box_pts)/box_pts
    y_smooth = np.convolve(y, box, mode='same')
    return y_smooth

def generate_base_stroke(n_points=100):
    """
    Generates a generic stroke cycle (0 -> 1 -> 0).
    Represents the Polished Rod Position.
    """
    t = np.linspace(0, 2*np.pi, n_points)
    # Sinusoidal motion of the rod (standard pumping unit geometry)
    position = 0.5 * (1 - np.cos(t)) 
    return t, position

def generate_normal_card(n_points=100, noise_level=0.02):
    t, pos = generate_base_stroke(n_points)
    
    # Physics: 
    # Upstroke (0 to pi): Load is high (lifting fluid + rods)
    # Downstroke (pi to 2pi): Load is low (rod weight only)
    
    load = np.zeros_like(pos)
    half = n_points // 2
    
    # Upstroke (High Load) with elastic stretch slope
    load[:half] = 0.8 + (0.1 * pos[:half]) 
    
    # Downstroke (Low Load) with elastic relaxation slope
    load[half:] = 0.25 - (0.05 * pos[half:])
    
    # Add transition zones (Simulating valve opening/closing time)
    transition_width = n_points // 10
    
    # Smooth transition at top (Reversal)
    load[half-transition_width:half+transition_width] = np.linspace(0.9, 0.2, 2*transition_width)
    
    # Smooth transition at bottom
    load[-transition_width:] = np.linspace(0.2, 0.8, transition_width)
    load[:transition_width] = np.linspace(0.2, 0.8, transition_width) # Wrap around fix

    # Add Noise and Smooth
    load += np.random.normal(0, noise_level, n_points)
    load = smooth_curve(load, box_pts=3)
    
    return pos, load

def generate_fluid_pound(n_points=100, severity=0.6, noise_level=0.02):
    """
    Simulates Fluid Pound:
    The pump is not full. On downstroke, the traveling valve stays closed 
    (load remains high) until it hits the fluid level, then load drops sharply.
    """
    t, pos = generate_base_stroke(n_points)
    half = n_points // 2
    
    load = np.zeros_like(pos)
    
    # Upstroke: Normal
    load[:half] = 0.8 + (0.1 * pos[:half])
    
    # Downstroke: 
    # Load STAYS HIGH for the first part of downstroke (supporting fluid column)
    pound_index = half + int((n_points // 2) * severity) # Point where we hit fluid
    
    # High load part of downstroke
    load[half:pound_index] = 0.75 - (0.05 * pos[half:pound_index])
    
    # The Drop (Impact)
    drop_width = 5
    load[pound_index:pound_index+drop_width] = np.linspace(0.7, 0.25, drop_width)
    
    # Rest of downstroke (Low load)
    load[pound_index+drop_width:] = 0.25 - (0.05 * pos[pound_index+drop_width:])
    
    # Fix Top Transition (Normal turnaround)
    trans = 5
    load[half-trans:half+trans] = np.linspace(0.9, 0.75, 2*trans)

    # Wrap around fix (Bottom transition)
    load[-5:] = np.linspace(0.25, 0.8, 5)
    load[:5] = np.linspace(0.25, 0.8, 5)

    # Add Noise
    load += np.random.normal(0, noise_level, n_points)
    load = smooth_curve(load, box_pts=3)
    
    return pos, load

def generate_gas_interference(n_points=100, noise_level=0.02):
    """
    Simulates Gas Interference:
    Gas compresses and expands. The card looks like a loop or football.
    Valves don't open/close sharply.
    """
    t, pos = generate_base_stroke(n_points)
    
    # Gas acts like a spring -> Load is proportional to Position (Slope)
    # But with hysteresis (loop width)
    
    base_slope = 0.5 * pos + 0.2
    hysteresis = 0.15 * np.sin(t) # Creates the loop opening
    
    load = base_slope + hysteresis
    
    # Add "wobble" common in gas locking
    load += 0.02 * np.sin(t * 5)
    
    # Add Noise
    load += np.random.normal(0, noise_level, n_points)
    load = smooth_curve(load, box_pts=5)
    
    return pos, load

# --- Main Generation Loop ---
data = []

classes = ['Normal', 'Fluid Pound', 'Gas Interference']
n_samples_per_class = 300

print("Generating realistic dyno cards...")

for label in classes:
    for i in range(n_samples_per_class):
        
        # Add random variations to input parameters so every card is unique
        rand_noise = np.random.uniform(0.01, 0.03)
        
        if label == 'Normal':
            x, y = generate_normal_card(noise_level=rand_noise)
        elif label == 'Fluid Pound':
            # Vary the severity (where the pound happens)
            rand_sev = np.random.uniform(0.3, 0.7) 
            x, y = generate_fluid_pound(severity=rand_sev, noise_level=rand_noise)
        elif label == 'Gas Interference':
            x, y = generate_gas_interference(noise_level=rand_noise)
        
        # Flatten for CSV
        for j in range(len(x)):
            data.append({
                'Card_ID': f"{label}_{i}",
                'Label': label,
                'Position': x[j],
                'Load': y[j],
                'Sequence_Index': j
            })

df = pd.DataFrame(data)
df.to_csv('synthetic_dyno_cards.csv', index=False)
print("Done! Dataset saved to 'synthetic_dyno_cards.csv'")

# Quick check plot
def plot_check():
    fig, axes = plt.subplots(1, 3, figsize=(15, 4))
    ids = [
        df[df['Label']=='Normal']['Card_ID'].iloc[0],
        df[df['Label']=='Fluid Pound']['Card_ID'].iloc[0],
        df[df['Label']=='Gas Interference']['Card_ID'].iloc[0]
    ]
    for ax, cid in zip(axes, ids):
        d = df[df['Card_ID']==cid]
        ax.plot(d['Position'], d['Load'], color='black')
        ax.set_title(d['Label'].iloc[0])
        ax.grid(True)
    plt.show()

plot_check()