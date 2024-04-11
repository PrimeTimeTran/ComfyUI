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
          - Activation:
            - Activations in one layer determine the activations in the next layer/
            - "Heart of the network",
            - "Info processing mechanism",
            - "Exactly how those activations from one layer bring about activations in the next layer."
      - "Hidden" layers
        - 2 x 16:
        - Sigmoid Functions
          a^(1) = σ(Wa^(0)+ b)
        - Find "patterns":
          - Loops, lines, edges.
          - Hopefully a neuron will be set off or learn
        - Bias
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
