import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from scipy.signal import savgol_filter

class ReservoirDiagnostics:
    """
    A toolkit for Water-Oil displacement and Injection surveillance.
    
    Attributes:
        well_name (str): Name of the well or reservoir unit.
        prod_data (pd.DataFrame): Production history.
        inj_data (pd.DataFrame): Injection history.
    """
    
    def __init__(self, well_name="Generic Well"):
        self.well_name = well_name
        self.prod_data = None
        self.inj_data = None

    def load_production_data(self, filepath):
        """Loads production data (Time, Np, WOR)."""
        try:
            self.prod_data = pd.read_csv(filepath)
            # Ensure sorting
            if 'Cumulative_Oil_bbl' in self.prod_data.columns:
                self.prod_data = self.prod_data.sort_values('Cumulative_Oil_bbl')
            print(f"[{self.well_name}] Production data loaded successfully.")
        except FileNotFoundError:
            print(f"Error: File {filepath} not found.")

    def load_injection_data(self, filepath):
        """Loads injection data (Time, Pressure, Rate)."""
        try:
            self.inj_data = pd.read_csv(filepath)
            print(f"[{self.well_name}] Injection data loaded successfully.")
        except FileNotFoundError:
            print(f"Error: File {filepath} not found.")

    def _calculate_wor_derivative(self, window_length=5, poly_order=2):
        """
        Internal helper to calculate smoothed WOR derivative.
        Returns: (raw_derivative, smoothed_derivative)
        """
        df = self.prod_data
        
        # 1. Finite Difference
        d_wor = np.diff(df['Water_Oil_Ratio'])
        d_np = np.diff(df['Cumulative_Oil_bbl'])
        d_np[d_np == 0] = 1e-6 # Avoid div/0
        
        raw_deriv = d_wor / d_np
        raw_deriv = np.insert(raw_deriv, 0, np.nan) # Pad
        
        # 2. Savitzky-Golay Smoothing
        # Ensure window length is valid
        eff_window = window_length
        if len(df) < window_length:
            eff_window = len(df) if len(df) % 2 != 0 else len(df) - 1
            if eff_window < 3: eff_window = 3

        valid_mask = ~np.isnan(raw_deriv)
        smooth_deriv = np.full(raw_deriv.shape, np.nan)

        if np.sum(valid_mask) > eff_window:
            smooth_deriv[valid_mask] = savgol_filter(
                raw_deriv[valid_mask], 
                window_length=eff_window, 
                polyorder=poly_order
            )
        else:
            smooth_deriv = raw_deriv

        return raw_deriv, smooth_deriv

    def plot_chan(self, window_length=5):
        """
        Generates Chan Plot (Log-Log WOR vs Np).
        """
        if self.prod_data is None:
            print("Error: Load production data first.")
            return

        raw, smooth = self._calculate_wor_derivative(window_length)
        
        fig, ax = plt.subplots(figsize=(10, 6))
        
        # Main WOR trend
        ax.loglog(self.prod_data['Cumulative_Oil_bbl'], self.prod_data['Water_Oil_Ratio'], 
                  'b-o', label='WOR (stb/stb)', linewidth=1.5, markersize=4)
        
        # Derivative (Smooth)
        ax.loglog(self.prod_data['Cumulative_Oil_bbl'], smooth, 
                  'r--', label=f'WOR Derivative (Smoothed)', linewidth=2)

        ax.set_title(f"{self.well_name}: Chan Diagnostic Plot")
        ax.set_xlabel("Cumulative Oil Production ($N_p$)")
        ax.set_ylabel("WOR & Derivative")
        ax.grid(True, which="both", ls="--", alpha=0.5)
        ax.legend()
        
        plt.tight_layout()
        plt.show()

    def plot_hall(self):
        """
        Generates Hall Plot (Cumulative Pressure vs Cumulative Injection).
        """
        if self.inj_data is None:
            print("Error: Load injection data first.")
            return

        # Calculations
        df = self.inj_data.copy()
        df['Wi'] = df['Daily_Injection_Rate_bbl'].cumsum()
        df['P_dt'] = df['Injection_Pressure_psi'].cumsum() # Assuming dt=1 day

        # Plotting
        fig, ax = plt.subplots(figsize=(10, 6))
        
        ax.plot(df['Wi'], df['P_dt'], 'g-o', label='Actual Trend')
        
        # Baseline (First 4 points)
        if len(df) > 4:
            slope, intercept = np.polyfit(df['Wi'].iloc[:4], df['P_dt'].iloc[:4], 1)
            ax.plot(df['Wi'], slope*df['Wi'] + intercept, 'k--', alpha=0.5, label='Baseline')

        ax.set_title(f"{self.well_name}: Hall Plot")
        ax.set_xlabel("Cumulative Injection ($W_i$)")
        ax.set_ylabel("$\int P \cdot dt$ (psi-days)")
        ax.grid(True, ls="--", alpha=0.5)
        ax.legend()
        
        plt.tight_layout()
        plt.show()