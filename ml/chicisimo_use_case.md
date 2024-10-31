# How we grew from 0 to 4 million women on our fashion app, with a vertical machine learning approach

## Our thesis: Outfits & closets are the best assets to understand people's tasts. Understanding taste will transform online fashion

- How could we build a system that learns fashion taste?
- we saw how a collaborative filtering tool transformed the music industry from blindness to totally understanding people.

the infrastructure to automate outfit advice:

1. a consumer app storing the clothes in your closet, and an interface focused on capturing the right input and providing the right output
1. a data platform that automates the jobs of interpreting incoming data (taste) and providing the correct output to the delivery mechanisms
1. a dataset that reflects what people wear, what people own in their closet, and how people think, when they think about clothes
1. an IP portfolio protecting all of the above

## 1st step: Builing the app for people to express their needs

Three things helped with retention:

1. identify retention levers using behavioral cohorts.
1. re-think the onboarding process, once we knew the levers of retention.
1. define how we learn.

- how people relate to the problem
- how people relate to the product

![image](https://miro.medium.com/v2/resize:fit:720/format:webp/1*CSql8uQfM2HBxTSCrqH_nQ.png)

## 2nd step: Building the data platform to learn people's fashion needs

- we realized it was actually a nightmare because, being chaotic, the data wasn’t actionable.
- But then we decided to start giving some structure to parts of the data, and we ended inventing what we called the Social Fashion Graph.
- We ended up building our fashion ontology — a multilevel list of all descriptors that are needed to define an a fashion product or an outfit, and the relations among all these descriptors.
- The end result is our current unsupervised learning model. A system that learns the meaning of an outfit, how to respond to a need, or the taste of an individual.
