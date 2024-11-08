# Machine Learning-Powered Search Ranking of Airbnb Experiences

- Stage 1: Offline ML model, small data size, experience features, offline scoring
- Stage 2: Personalized Offline ML model, medium, experience features, user features, offline scoring
- Stage 3: Personalized Online ML model, large, experience features, user features, query features, online scoring

## Stage 1: Build a strong baseline

at that moment, the best choice was to just randomly re-rank experiences daily, until a small dataset is coolected for development of the Stage 1 ML model.

**collecting training data**: we collected search logs (i.e. clicks) of users who ended up making bookings
**labeling training data**: experiences that were booked (positive lavel) or experiences that were clicked but not booked (negative label), ~50,000 examples
**building signals based on which we will rank**: solely based on experience features, 25 features
**training the ranking model**: Gradient Boosted Decision Tree, binary classification with log-loss loss function, normalized features
**testing the ranking model**: AUC and NDCG, hold-out data, plot partial dependency plots
**implementation details**: implemented offline and ran daily in Airflow

## Stage 2: Personalize

- personalization: feature engineering given collected data about users.

### 1. Personalize based on booked Airbnb Homes

- distance between booked home and experience.
- experience available during booked trip.

### 2. Personalize based on the user's clicks

- infer user interest in certain categories
- infer the user's time-of-day availablity

**Training the ranking model**: 4000 experiences, 250K labeld examples with 50 ranking features
**Testing the ranking model**: A/B test
**Implementation details**: we created a look-up table keyed off of user id that contained personalized ranking of all Experiences for that user.

## Stage 3: Move to Online Scoring

- web browser information - location, language

**Training the ranking model**: to train the model with Query Features we first added them to our historical training data.

- Model for logged-in users, with experience features, query features, and user features
- Model for logged-out traffic, with experience & query features, data (clicks & bookings) of logged-in users but not considering personalization features

**Testing the ranking model**: A/B test to compare the stage 3 model to stage 2 model
**Implementation details**: 1) getting model input from various places in real time, 2) model deployment to production, and 3) model scoring

## Stage 4: Handle Businesss Rules

- ranking model's objective was to grrow bookings. other secondary objectives -> Business Rules
- **Promote Quality**: 1) star ratings, ranging from 1 to 5, and 2) structured multiple-response feedback
- discovering and promoting potential new hits early using cold-start signals and promoting them in ranking
- enforcing diversity in the top 8 results
- optimize search without location for clickability

## Monitoring and explaining rankings

- Apache Superset, Airflow -> dashboards
