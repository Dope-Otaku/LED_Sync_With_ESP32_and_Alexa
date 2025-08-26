import numpy as np
import matplotlib.pyplot as plt
from scipy.io import wavfile
import matplotlib.animation as animation

def plot_flower_visualization(file_path):
    """
    Reads a sound file, performs Fourier Transform, and visualizes frequencies in a rotating flower-like design.
    
    Parameters:
        file_path (str): Path to the sound file (must be in WAV format).
    """
    try:
        # Read the audio file
        sample_rate, data = wavfile.read(file_path)
        
        # If stereo, take only one channel
        if len(data.shape) > 1:
            data = data[:, 0]
        
        # Perform Fourier Transform
        n = len(data)
        fft_values = np.fft.fft(data)
        magnitude = np.abs(fft_values[:n//2])  # Only positive frequencies
        
        # Normalize magnitudes
        normalized_magnitude = magnitude / np.max(magnitude)
        
        # Generate angles for the flower-like design
        num_points = len(normalized_magnitude)
        angles = np.linspace(0, 2 * np.pi, num_points)
        
        # Create the figure
        fig, ax = plt.subplots(subplot_kw={'polar': True})
        ax.set_xticks([])
        ax.set_yticks([])
        ax.grid(False)
        ax.set_title("Flower-like Frequency Visualization", va='bottom', fontsize=14)
        
        # Function to update the animation
        def update(frame):
            ax.clear()
            ax.set_xticks([])
            ax.set_yticks([])
            ax.grid(False)
            ax.set_title("Flower-like Frequency Visualization", va='bottom', fontsize=14)
            
            # Rotate the flower by shifting the angles
            rotated_angles = angles + frame * np.pi / 180
            ax.plot(rotated_angles, normalized_magnitude, color='purple', linewidth=1.5)
        
        # Create the animation
        ani = animation.FuncAnimation(fig, update, frames=360, interval=50, repeat=True)
        
        plt.show()
    
    except Exception as e:
        print(f"Error: {e}")

file_path = "day7.wav"  # Replace with the path to your sound fil
plot_flower_visualization(file_path)