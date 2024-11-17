# Scaling Machine Learning at Uber with Michelangelo

- Michelangelo, Uber's Machine Learning Platform
- data scientists, engineers, product managers, and researchers work on ML solutions
- organizational and process design considerations

## Zero to 100 in three years

- to democratize ML across Uber
- initial focus: enable large-scale batch training and productionizing batch prediction jobs

ML use cases at Uber

- key areas: ad optimization or content relevance
- Uber Eats: optimize the eater experiecne, ranking models based on both historical data and information from the user's current session
- Marketplace Forecasting: spatiotemporal forecasting models, based on forecasted imbalances between supply and demand
- Customer Support: tickets are routed to customer service representatives. boosted tree 10%, deep learning model 6%
- Ride Check: GPS data on phone, an increased safety risk
- Eastimated Times of Arrival: ETAs are notoriously difficult to get right, predict errors and use the predicted error to make a correction
- One-Click Chat: driver-partners respond to rider chat messages with a single button
- Self-Driving Cars: object detection and motion planning, Horovod for efficient distributed training of large models

## How we scaled ML at Uber

- For data scientists, to own their work end-to-end
- For engineers, to train sufficiently high-quality models without needing a data scientist

Organization

- Getting the right people working on the right problems has been critical to building high quality solutions and deploying them consistently and successfully in production.
- product teams: own the models they build and deploy in production
- specialist teams: deep expertise across different domains - NLP, computer vision, recommender systems, forecasting
- research teams: collaborate on probelms and help guide the direction for future research
- ML platform teams: builds and operates a general purpose ML workflow and toolset

Process

- Sharing ML best practices (e.g., data organization methods, experimentation, and deployment maanagement)
- launching models: unintended behaviors, tricky edge cases, and complicated legal/ethical/privacy problems.
- coordinated planning across ML teams: the company is making good engineering tradeoffs to avoid fragmentation and technical debt
- community: host an annual internal ML conference called UberML
- education: proper channels to efficiently share information and educate on ML-related topics are critical

Technology

- **End-to-end workflow**: the whole ML workflow: manage data, train models, evaluate models, deploy models, and make predictions, monitor predictions
- **ML as software engineering**: apply patterns from software development tools and methodologies back to our approach to ML
- **Model developer velocity**: a very iterative process
- **Modularity and tiered architecture**:

- Finding the right combination of data, algorithm, and hyperparameters is an experimental and iterative process.
- at deploy time, offline job for scheduled batch predictions or online containers for real-time request-response predictions via Thrift
- compute precise accuracy metrics
- monitor the distributions of the features and predictions and compare them over time
- a model is like a compiled software library - training configurations, reproducibility
- iteration speed affects both how ML scales out across the organization and how prodcutive a team can be on any given problem

![Uber ML](https://blog.uber-cdn.com/cdn-cgi/image/width=2160,quality=80,onerror=redirect,format=auto/wp-content/uploads/2022/08/image6-32.png)

Develop quickly, deploy reliably

1. solve the data problem so data scientists don't have to
1. automate or provide powerful tools to speed up common flows
1. make the deployment process fast and magical
1. let the user use the tools they love with minimal cruft - "Go to the customer"
1. enable collaboration and reuse
1. guide the user through a structured workflow

speed with deep learning

- developers typically write a lot more detailed training code and require specialized compute resources (GPUs)
- we have specialized tools to help modelers track their experiments and development
- using AutoTune: state-of-the-art black box Bayesian optimization algorithms

## Key lessions learned

- Let developers use the tools that they want:
- Data is the hardest part of ML and the most important piece to get right:
- It can take significant effort to make open source and commercial components work well at scale:
- Develop iteratively based on user feedback, with the long-term vision in mind:
- Real-time ML is challenging to get right:
