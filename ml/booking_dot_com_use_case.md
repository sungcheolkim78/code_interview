# 150 successful machine learning models: 6 lessons learned at Booking.com

1. Projects introducing machine learned models deliver strong business value
1. Model performance is not the same as business performance
1. Be clear about the problem you're trying to solve
1. Prediction serving latency matters
1. Get early feedback on model quality
1. Test the business impact of your model using randomized controlled trials (follows from #2)

>> Our main conclusion is that an iterative, hypothesis driven process, integrated with other disciplines
>> was fundamental to build 150 successful products enabled by machine learning.

## Context of the booking.com case

- The stakes are high for recommendations
- User's provide scant information about what they're really looking for when booking a trip
- The supply of accomodations is constrained, and changing prices impact guest preferences
- Guest preferences may change each time they use the platform
- There is a lot of rich information available regarding accomodations, which can be overwhelming for users

## Different types of model

- Traveller preferences models
- Traveller context models
- Item space navigation models
- User interface optimization models
- Content curation models
- Content augmentation models

## Lession 1: Projects introducing machine learned models deliver strong business value

## Lession 2: Model performance is not the same as business performance

>> An interesting finding is that increasing the performance of a model does not necessarily
>> translate into a gain in [business] value.

## Lession 3: Be clear about the problem you're trying to solve

>> The problem construction process takes as input a business case or concept and outputs
>> a well-defined modeling problem (usually a supervised machine learning problem), such
>> that a good solution effectively models the given business case or concept.

## Lession 4: Prediction serving latency matters

Booking.com go to some lengths to minimise the latency introduced by models, including
horizontally scaled distributed copies of models, a in-house developed custom linear
prediction engine, favouring models with fewer parameters, batching requests, and
pre-computation and/or caching.

## Lession 5: Get early feedback on model quality

- incomplete feedback due to the difficulty of observing true labels
- delayed feedback e.g. a prediction made at time of booking as to whether a user will leave a review cannot be assessed until after the trip has been made.

>> ... Response Distribution Analysis has proved to be a very useful tool that allows
>> us to detect defects in the models very early.

## Lession 6: Test the business impact of your model using randomized controlled trials (follows from #2)

- When not all subjects are eligible to be exposed to a change (e.g. they don't have a feature that the
model requires), create treatment and non-treatments groups from within the eligible subset.

>> Hypothesis driven iteration and interdisciplinary integration are the core of our approach to deliver
>> value with machine learning, and we wish this work to serve as guidance to other machine learning
>> practitioners and spark further investigations on the topic.

[link](https://www.kdd.org/kdd2019/accepted-papers/view/150-successful-machine-learning-models-6-lessons-learned-at-booking.com)
