#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jun 27 11:40:32 2024

@author: tara
"""

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# Load the CSV file
file_path = 'regularization.csv'
data = pd.read_csv(file_path)

# Define a function to map (l, m) to dipole labels
def get_dipole_label(l, m):
    if l == 4 and m == 3:
        return 'dipole1'
    elif l == 4 and m == 4:
        return 'dipole2'
    elif l == 4 and m == 5:
        return 'dipole3'
    else:
        return f'l={l}, m={m}'

# Get unique combinations of l and m
unique_combinations = data[['l', 'm']].drop_duplicates()

# Create a plot for each combination of l and m for s_reg
fig, ax = plt.subplots(figsize=(10, 6))

for _, row in unique_combinations.iterrows():
    l_val = row['l']
    m_val = row['m']
    subset = data[(data['l'] == l_val) & (data['m'] == m_val)]
    label = get_dipole_label(l_val, m_val)
    ax.plot(subset['R'], subset['s_reg'], label=label)

# Set the scale to logarithmic for x-axis
ax.set_xscale('log')
ax.set_xlabel('R')
ax.set_ylabel('s_reg')
ax.legend()

plt.show()

# Create a plot for each combination of l and m for s_long2
fig, ax = plt.subplots(figsize=(10, 6))

for _, row in unique_combinations.iterrows():
    l_val = row['l']
    m_val = row['m']
    subset = data[(data['l'] == l_val) & (data['m'] == m_val)]
    label = get_dipole_label(l_val, m_val)
    ax.plot(subset['R'], subset['s_long2'], label=label)

# Set the scale to logarithmic for x-axis
ax.set_xscale('log')
ax.set_xlabel('R')
ax.set_ylabel('s_long2')
ax.legend()

plt.show()
