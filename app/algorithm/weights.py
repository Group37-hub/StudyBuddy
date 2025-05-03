class QLearningWeightAdjuster:
    def __init__(self, initial_weights, learning_rate=0.1, discount_factor=0.9):
        """
        initial_weights: Dict (e.g., {"subjects": 0.4, "availability": 0.3})
        learning_rate: How quickly to update Q-values (0.1 is conservative)
        discount_factor: Importance of future rewards (0.9 focuses on long-term)
        """
        self.q_table = initial_weights.copy()
        self.lr = learning_rate
        self.df = discount_factor

    def update_weights(self, feedback):
        """
        Update Q-values (weights) based on user feedback (1-5 stars).
        Simplified Q-learning: Reward = feedback, no explicit state transitions.
        """
        reward = feedback / 5.0  # Normalize feedback to [0, 1]

        # Update Q-values for each feature
        for feature in self.q_table:
            old_q = self.q_table[feature]
            # Simplified Q-learning update (no next state)
            new_q = old_q + self.lr * (reward + self.df * old_q - old_q)
            self.q_table[feature] = new_q

        # Normalize weights to sum to 1
        total = sum(self.q_table.values())
        self.q_table = {k: v / total for k, v in self.q_table.items()}
        return self.q_table