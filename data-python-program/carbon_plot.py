import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import itertools
import matplotlib.lines as mlines
import matplotlib.patches as mpatches

carbon12 = pd.read_csv("c12-c13.csv")
carbon13 = pd.read_csv("c13-c14.csv")
carbon14 = pd.read_csv("c14-c15.csv")

hydro2 = pd.read_csv("H2-He3.csv")
hydro3 = pd.read_csv("H3-He4.csv")

#organize by author
# Create a list of marker styles to cycle through
marker_styles = [
    'o', 's', '^', 'v', 'D', 'd', '*', 'P', 'H', 'h',
    '<', '>', '8', 's', 'p'
]

markers = itertools.cycle(marker_styles)

# Create a figure
plt.figure(figsize=(6,4))

#for name, group in carbon12.groupby('author1'):
#
#    plt.plot(group['x2(eV)']*10**(-6), group['y'], marker=next(markers),color = "lightsteelblue",linestyle="None", markersize=12)
#
#for name, group in carbon13.groupby('author1'):
#    #print(f"author1: {name}")
#
#    plt.plot(group['x2(eV)']*10**(-6), group['y'], marker=next(markers), markerfacecolor='none', markeredgecolor='Navy', linestyle="None",markersize=12,markeredgewidth=2)
#
#for name, group in carbon14.groupby('author1'):
#
#    plt.plot(group['x2(eV)']*10**(-6), group['y'], marker=next(markers),color = "navy", linestyle="None",markersize=12)
#
# Create custom legend handles

for name, group in hydro2.groupby('author1'):

    plt.plot(group['x2(eV)']*10**(-6), group['y'], marker=next(markers),color = "lightsteelblue",linestyle="None", markersize=12)

for name, group in hydro3.groupby('author1'):
    #print(f"author1: {name}")

    plt.plot(group['x2(eV)']*10**(-6), group['y'], marker=next(markers), markerfacecolor='none', markeredgecolor='Navy', linestyle="None",markersize=12,markeredgewidth=2)


carbon12_legend = mlines.Line2D([], [], color='lightsteelblue', marker='o', linestyle='None',
                            markersize=10, label=r'$^2$H(p,$\gamma$)$^3$He')

carbon13_legend = mlines.Line2D([], [], color='navy', linestyle='None',marker="s", markerfacecolor="None", label=r'$^3$H(p,$\gamma$)$^4$He', markersize=10, markeredgewidth=2)




#carbon14_legend = mlines.Line2D([], [], color='navy', marker='d', linestyle='None',
#                            markersize=10, label='c14(n,y)c15')
#"""carbon14_legend"""
# Add them manually
plt.legend(handles=[carbon12_legend, carbon13_legend ], loc='upper left', fontsize=32)
plt.xlabel('Energy (MeV)', fontsize=32)
plt.ylabel('Cross Section (Barns)',fontsize=32)
plt.xlim(10**(-3), 10**(0))
plt.tick_params(axis='both', labelsize=32)
plt.yscale("log")
plt.xscale("log")

plt.grid(True)
plt.show()

#pull energy, cross, and error bars to plot


#plot on same plot

