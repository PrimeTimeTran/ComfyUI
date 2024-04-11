- Intro
  - Neural networks:
    - A beautiful biologically-inspired programming paradigm which enables a computer to learn from observational data
  - Deep learning:
    - A powerful set of techniques for learning in neural networks
- Neural Networks

  - Types
    - Convolutional -> Good for image recognition
    - Long short-term Memory Network -> Good for speech recognition
  - Structure

    - Recognizing Numbers

      - Layers
      - Uses Convolutional
      - "Lines, loops, edges"
      - Layer 1
        - Image: 28 x 28: 784 neurons
          - Classify given image as digit.
          - Neuron holds number
            - "Holds number" between 0 & 1
            - Vector
      - Activation:

        - Activations in one layer determine the activations in the next layer.
        - "Heart of the network".
        - "Info processing mechanism".
        - "Exactly how those activations from one layer bring about activations in the next layer."
        - Which parameters should exist?
          - Assign a weight to each connection between neurons to each neuron in previous layer
            - w1a1 + w2a2 + w3a3 + w4a4 + ...
          - Compute weighted sum
            - Activations become some value between 0 & 1
            - Pump weighted sum into Sigmoid Function/logistics curve.
              σ (x) = 1 / (1+e^(-x))
            - Bias
              - Sometimes we ant it to be active when it's +10 or -10 not just 1.
              - Add a weighted value
              - "How high it needs to be before the neuron starts getting meaningful active".

      - Learning: Finding the right weights & biases
        - Notation
          - $a_{0}^{(1)} = σ(w_{0}0 \ a_{0}0 + w_{}1 \ a_{1}0 + w_{0}2 \ a_{2}0 + \dots + w_{0}n \ a_{n}0 + b_{0})$
          - Simplifies to 
          - $a^{(1)} = σ(Wa^{0}+ b)$
      - "Hidden" layers 
        - 2 x 16:
        - Find "patterns":
          - Loops, lines, edges.
          - Hopefully a neuron will be set off or learn

      - Last Layer:
        - 10 neurons(for each number)
      - Sigmoid function
        - a^(1) = σ(Wa^(0)+ b)

  - Train a bunch of times
  - See how accurately it classifies
  - Just calculus, find minimum of a function
  - Cost functions:
    - "Bad Computer"
    - Points network to what the final output of a network should be for a given input.
    - Parameters: many many training examples
  - Average cost:
    - How lousy the network is
    - How bad the network should feel.
  - Backtrack propagation

- Learn

  - How?

    - Gradient Descent

      - Multi variable calculus
      - Gradient of a function is the variable of steepest descent
      - Ho

    - Analyze
      - s

- Learning Paradigms
  - Supervised
  - Unsupervised
  - Reinforcement
    - Differs from supervised learning in not needing labelled input/output pairs to be presented, and in not needing sub-optimal actions to be explicitly corrected
    - Instead focuses on finding a balance between exploration (of uncharted territory) & exploitation (of current knowledge) with the goal of maximizing the long term reward, whose feedback might be incomplete or delayed.
    - Environment is typically in the form of Markov decision process (MDP)
