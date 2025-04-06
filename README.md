# Master Sintering Curve
 
 # Master Sintering Curve Plotter  This Python code implements a Master Sintering Curve (MSC) plotter based on the work of Suzanne J. Lombardo and Randall M. German. The MSC is a powerful tool used in materials science and engineering to model and predict the densification behavior of ceramic materials during sintering.  
 ## How it Works  
 The code uses a least-squares regression approach to determine the optimal activation energy (Q) for the sintering process. It then plots the relative density as a function of a combined time-temperature parameter, known as the "theta" value. This plot represents the Master Sintering Curve.  
 **Key Features:**  
 *   Calculates the Mean Residual Square (MRS) for a range of Q values.
 *   Identifies the optimal Q value that minimizes the MRS.
 *   Plots the MRS vs. Q curve to visualize the optimization process.
 *   Plots the Master Sintering Curve using the optimal Q value.
 *   Provides the optimal Q value and minimum MRS as output. 
