# Space, Time and Groceries

- [link](https://tech.instacart.com/space-time-and-groceries-a315925acf3a)

Challenge: complete every delivery on-time, with the right groceries!

1. introduce the logistics problem
1. outline the architecture of the system
1. describe the GPS data
1. touring a series of datashader visualizations

>> Visualizations like these help us to build intuition about our system, generate hypotheses for improvements,
>> sanity check our changes, identify best practices and improve our operations.

## Logistics @ Instacart

- choose a retailer, shop for groceries, in a few hours, thousands of orders to deliver
- TSP (traveling salesman problem) to find the shortest route to deliver all orders
- VRP (vehicle routing problem), which generalizes the traveling salesman problem
- VRPTW (vehicle routing problem with time windows), which generalizes the VRP
- CVRPTWMTW (capacitated vehicle routing problem with time windows for multiple trips)
- SCVRPTWMTW (stochastic capacitated vehicle routing problem with time windows for multiple trips)

## Naive to Novel

1. sort orders by when they are due
1. find the shopper who is free that can do the first order the fastest
1. search remaining orders for any that can be added without being late
1. dispatch the orders found to this shopper
1. repeat

Improvements:

- machine learning to predict the distribution of time expected for any given shopper and assignment
- decomposing the CVRPTW into sub-problems (clustering deliveries, shopper assignment) and solving these sub-problems to near optimality
- applying heuristics for limiting search spaces, dealing with anomalies, fine-tuning solutions and adapting under uncertainty
- re-computing batch plans every minute and making dispatching decisions just in time

## The Data

we collected a stream of GPS location data. ["shopper_id", "measured_at", "latitue", "longitude", "speed", direction", "accuracy"]

## Datashader

[Datashader](http://datashader.readthedocs.io/) and [plotting pitfalls](https://anaconda.org/jbednar/plotting_pitfalls/notebook)

## Accuracy, speed and direction
