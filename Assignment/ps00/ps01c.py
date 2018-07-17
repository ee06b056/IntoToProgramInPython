#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jul 10 23:10:37 2018

@author: libo

assignment 1 part c
"""

annual_salary_init = float(input('Enter the starting salary: '))
portion_min = 0
portion_max = 10000
total_cost = 1000000
semi_annual_raise = 0.07
portion_down_payment = 0.25

r = 0.04
months = 36
num_guess = 0
find = False
while portion_max - portion_min > 1:
    num_guess += 1
    portion_guess = (portion_min + portion_max) // 2
    current_saving = 0.0
    annual_salary = annual_salary_init
    for i in range(months):
        if (i % 6 == 0 and i > 0):
            annual_salary *= (1 + semi_annual_raise)
        current_saving += (annual_salary / 12) * portion_guess / 10000 + current_saving * r / 12
    if (current_saving - (total_cost * portion_down_payment)) < -100:
        portion_min = portion_guess
        continue
    elif (current_saving - (total_cost * portion_down_payment)) > 100:
        portion_max = portion_guess
        continue
    else:
        print('Best saving rate: ',portion_guess/10000)
        print('Steps in bisection search: ',num_guess)
        find = True
        break
    
if not find:
    print('It is not possible to pay the down payment in three years.')