# 15.093-Optimization

Vassili Chesterkine, Maïwenn Danno

---

This project is part of the 15.093 Optimization Methods course at MIT, taught by Prof. Dimitris Bertsimas and Prof. Alexandre Jacquillat. 

## Project Description

Bluebikes is Boston’s bike-sharing system, giving access to more than 4000 bikes across just under 450 stations in 11 municipalities of the Boston area. With close to 500,000 recorded trips in August 2022, the system is rapidly growing in popularity. While Bluebikes are, in theory, a very convenient way to get around the city, the reality is more complex. During peak hours, some stations are full, while other stations are empty, making Bluebikes very unreliable as users are not able to pick up a bike at their origin, or return it at their destination.

A viable solution is to use vans to move bikes between stations, freeing up docks at full stations and refilling empty stations. In this project, we develop mixed-integer optimization methods to efficiently reallocate bikes. Using JuMP and Gurobi, we achieve a 47% reduction in unmet demand.

## Formulation 

The details of the optimization formulation can be found in the [final report](final_report.pdf), along with the simplifying assumptions to were made to model the problem.

## Data

We leverage [individual-level trip data](https://s3.amazonaws.com/hubway-data/index.html) provided by Bluebikes, which contains an exhaustive list of all Bluebikes trips since 2015. Additionally, we use real-time system information provided as part of the General Bikeshare Feed Specification program (GBFS), including station position, capacity and inventory.
