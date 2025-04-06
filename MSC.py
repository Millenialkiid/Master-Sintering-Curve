import numpy as np
import matplotlib.pyplot as plt
from scipy import stats
import math

class SinteringCurvePlotter:
    """Python implementation of Master Sintering Curve plotter"""
    
    @staticmethod
    def calculate_mean_residual_square(q, time, temperature, dl_by_l):
        """Calculate Mean Residual Square for a given Q value"""
        # Calculate log_theta values
        log_theta = [np.log(t * np.pow(temp, q)) for t, temp in zip(time, temperature)]
        
        if np.all(log_theta == log_theta[0]) and len(log_theta) > 1:  # Check if all values are equal and there's more than one value
            print(f"Warning: All log_theta values are identical for Q = {q}. Skipping this Q value.")  # Add a warning message for user clarity
            return float('inf')
        # Perform linear regression
        slope, intercept, r_value, p_value, std_err = stats.linregress(log_theta, dl_by_l)
        
        # Calculate residuals and mean residual square
        predicted = [slope * x + intercept for x in log_theta]
        residuals = [actual - pred for actual, pred in zip(dl_by_l, predicted)]
        mean_residual_square = sum([r**2 for r in residuals]) / len(residuals)
        
        return mean_residual_square
    
    @staticmethod
    def plot_curves(time, temperature, dl_by_l):
        """Plot MRS vs Q curve and Master Sintering Curve"""
        # Range of Q values for the MRS vs Q curve
        q_values = [100, 150, 200, 250, 300, 350, 400, 450]
        mrs_values = []
        
        # Calculate MRS for each Q value
        for q in q_values:
            mrs = SinteringCurvePlotter.calculate_mean_residual_square(q, time, temperature, dl_by_l)
            mrs_values.append(mrs)
        
        # Create figure with two subplots
        fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(16, 8))
        
        # Plot MRS vs Q curve
        ax1.plot(q_values, mrs_values, 'o-', label='MRS vs Q')
        ax1.set_xlabel('Q Value')
        ax1.set_ylabel('Mean Residual Square')
        ax1.set_title('MRS vs Q Value')
        ax1.legend()
        ax1.grid(True)
        
        # Find the optimal Q value (min MRS)
        optimal_q_index = np.argmin(mrs_values)
        optimal_q = q_values[optimal_q_index]
        
        # Calculate θ(t, T(t)) for optimal Q
        log_theta_values = [np.log(t * np.pow(temp, optimal_q)) for t, temp in zip(time, temperature)]
        
        # Plot the Master Sintering Curve
        ax2.plot(log_theta_values, dl_by_l, 'o-', label=f'Optimal Q = {optimal_q}')
        ax2.set_xlabel('Log(θ(t,T(t)))')
        ax2.set_ylabel('Relative Density')
        ax2.set_title('Relative Density vs Log(θ(t,T(t)))')
        ax2.legend()
        ax2.grid(True)
        
        plt.tight_layout()
        plt.show()
        
        print(f"Optimal Q value: {optimal_q}")
        print(f"Minimum MRS: {mrs_values[optimal_q_index]}")
        
        return optimal_q, log_theta_values, dl_by_l

def main():
    """Main function to get user input and plot sintering curves"""
    print("Enter number of data points:")
    n = int(input())
    
    print("Enter time values (space-separated):")
    time = list(map(float, input().split()))
    
    print("Enter temperature values (space-separated):")
    temperature = list(map(float, input().split()))
    
    print("Enter dL/L values (space-separated):")
    dl_by_l = list(map(float, input().split()))
    
    # Validate input lengths
    if len(time) != n or len(temperature) != n or len(dl_by_l) != n:
        print("Error: Number of input values doesn't match the specified number of data points.")
        return
    
    # Plot the sintering curves
    SinteringCurvePlotter.plot_curves(time, temperature, dl_by_l)

if __name__ == "__main__":
    main()