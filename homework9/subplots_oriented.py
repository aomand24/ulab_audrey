import numpy as np
import matplotlib.pyplot as plt

def horizontal_subplots(x_range):
# takes a range of x and returns two horizontal subplots that display cos(x) on left and sin(x) on right
    x_vals = np.linspace(x_range[0], x_range[1], 400)
    y_vals_h = np.cos(x_vals)
    y_vals_k = np.sin(x_vals)
    fig, axs = plt.subplots(1, 2, figsize=(12, 6))
    axs[0].plot(x_vals, y_vals_h, label=r'$h(x) = \cos(x)$', color='blue')
    axs[0].set_title(r'Plot of $h(x) = \cos(x)$')
    axs[0].set_xlabel('x')
    axs[0].set_ylabel('h(x)')
    axs[0].legend()
    axs[1].plot(x_vals, y_vals_k, label=r'$k(x) = \sin(x)$', color='orange')
    axs[1].set_title(r'Plot of $k(x) = \sin(x)$')
    axs[1].set_xlabel('x')
    axs[1].set_ylabel('k(x)')
    axs[1].legend()
    plt.tight_layout()
    plt.show()

def vertical_subplots(x_range):
# takes a range of x and returns two vertical subplots that display cos(x) on top and sin(x) on bottom
    x_vals = np.linspace(x_range[0], x_range[1], 400)
    y_vals_h = np.cos(x_vals)
    y_vals_k = np.sin(x_vals)
    fig, axs = plt.subplots(2, 1, figsize=(12, 6))
    axs[0].plot(x_vals, y_vals_h, label=r'$h(x) = \cos(x)$', color='blue')
    axs[0].set_title(r'Plot of $h(x) = \cos(x)$')
    axs[0].set_xlabel('x')
    axs[0].set_ylabel('h(x)')
    axs[0].legend()
    axs[1].plot(x_vals, y_vals_k, label=r'$k(x) = \sin(x)$', color='orange')
    axs[1].set_title(r'Plot of $k(x) = \sin(x)$')
    axs[1].set_xlabel('x')
    axs[1].set_ylabel('k(x)')
    axs[1].legend()
    plt.tight_layout()
    plt.show()
