#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jul 10 23:01:32 2018

@author: libo

assignment 1 part b
"""

annual_salary = float(input('Enter your annual salary: '))
portion_saved = float(input('Enter the percent of your salary to save, as a decimal: '))
total_cost = float(input('Enter the cost of your dream home: '))
semi_annual_raise = float(input('Enter the semi-annual raise, as decimal: '))
portion_down_payment = 0.25
current_saving = 0.0
r = 0.04
months = 0
while current_saving <= total_cost * portion_down_payment:
    current_saving += (annual_salary / 12) * portion_saved + current_saving * r / 12
    months += 1
    if (months % 6 == 1 and months != 1):
        annual_salary *= (1 + semi_annual_raise)

print('Number of months: ', months)