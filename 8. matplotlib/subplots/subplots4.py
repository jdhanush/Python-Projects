# -*- coding: utf-8 -*-
"""
Created on Thu May 14 12:55:05 2026

@author: user
"""


import pandas as pd
from matplotlib import pyplot as plt

plt.style.use('seaborn-v0_8')

data = pd.read_csv('data.csv')
ages = data['Age']
dev_salaries = data['All_Devs']
py_salaries = data['Python']
js_salaries = data['JavaScript']

fig1, ax1 = plt.subplots()
fig2, ax2 = plt.subplots()

ax1.plot(ages, dev_salaries, color='#444444',
         linestyle='--', label='All Devs')

ax1.legend()
ax1.set_title('Median Salary (USD) by Age')
ax1.set_xlabel('Ages')
ax1.set_ylabel('Median Salary (USD)')



ax2.plot(ages, py_salaries, label='Python')
ax2.plot(ages, js_salaries, label='JavaScript')

ax2.legend()
#ax2.set_title('Median Salary (USD) by Age')
ax2.set_xlabel('Ages')
ax2.set_ylabel('Median Salary (USD)')

plt.tight_layout()

plt.show()

# this line used to save a figure
fig1.savefig(r'D:\Dhanush\Python Concept Snippets\8. matplotlib\subplots\devs.png')