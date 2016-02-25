import numpy as np


class ForwardBackward(object):
    """
    A class implementing the Forward-Backward algorithm for smoothing as described in figure
    15.4 on page 576 in "A Modern Approach". This is available from the public function
    `forward_backward`. Running only forward is also available with the public function
    `prediction`.
    """

    def __init__(self, config=None):
        """
        Constructor that instantiates the class with a configuration
        :param config: A configuration object. See `main` for details of what it must include.
        """
        if not config:
            raise ValueError("A config must be passed during instantiation")
        self.config = config

    def forward_backward(self, evidence_sequence, prior):
        """
        The implementation of the Forward-Backward algorithm
        :param evidence_sequence: A vector of the evidence for values 1...t
        :param prior: Belief for the initial state, P(X_0) as a 1D numpy array
        :return: A vector of the smoothed estimates (probability distribution)
        """
        time_t = len(evidence_sequence) + 1  # The total time frame (number of time slices)
        fv, sv = [None] * time_t, [None] * time_t  # Instantiates a vector for the forward-messages # and smoothed estimates
        fv[0], sv[0] = prior, prior  # Insert the initial belief as the first element in both lists
        b = np.array([1, 1])  # Instantiate the first backward message

        for t in range(1, time_t):
            """
            Calculating the forward equation for the current time slice.
            This is done according to the equation 15.12 in the text book.
            15.12: f_1:t+1 = O_t+1 * T^T * f_1:t
            """
            fv[t] = self._forward(fv[t - 1], evidence_sequence[t - 1])  # _forward(f_1:t, e_t+1)

        print('# BACKWARD-MESSAGES:')
        for i in range(time_t - 1, -1, -1):
            """
            Calculating the backward equation the current time slice.
            This is done according to the equation 15.13 in the text book
            15:13: b_k+1:t = T * O_k+1 * b_k+2:t
            """
            print('\tMessage %i: %s' % (i, b))
            sv[i] = self._normalize(fv[i] * b)
            b = self._backward(evidence_sequence[i - 1], b)  # _backward(e_k+1, b_k+2:t)

        # The following loops are only a pretty print of fv and sv
        print('# FORWARD-MESSAGES:')
        for i in range(len(fv)):
            print('\tMessage %i: %s' % (i, fv[i]))

        print("# SMOOTHED ESTIMATES:")
        for i in range(len(sv)):
            print('\tEstimate %i: %s' % (i, sv[i]))

        return sv

    def prediction(self, evidence_sequence, prior):
        """
        A public function to only run the forward-procedure on a given evidence sequence
        :param evidence_sequence: A vector of the evidence for values 1...t
        :param prior: Belief for the initial state, P(X_0) as a 1D numpy array
        :return: A vector of all forward messages
        """
        forward_messages = [None] * len(evidence_sequence)
        forward_messages[0] = prior
        print('# FORWARD-MESSAGES:')
        for t in range(len(evidence_sequence)):
            """
            Does exactly the same as the first for-loop in the forward-backward algorithm.
            Look there for a detailed description
            """
            prior = self._forward(prior, evidence_sequence[t])  # _forward(f_1:t, e_t+1)
            print('\tMessage %i: %s' % (t + 1, prior))
        return forward_messages

    def _forward(self, likelihood, evidence):
        """
        A private function implementing the forward equation. Returns the
        final value either normalized or not, given the setting in the config
        :param likelihood: The forwarded message f_1:t as a 1D numpy array
        :param evidence: The evidence for the current time slice t
        :return: The new forward message f_1:t+1 as a 1D numpy array
        """
        s, t = self.config['sensor_model'], self.config['transition_model']  # Get the global sensor- and transition model
        if not evidence:
            """
            If the evidence for this time slice t is false, we to a local update of s to T^-1 to get the false values.
            (Subtract the sensor model from the identity matrix)
            """
            s = np.identity(len(s)) - s  # Local update to T^-1 (subtract with identity matrix to get false values)
        r = np.dot(s, t)  # The matrix product between S_t+1 and T (sensor model and transition model)
        r = np.dot(r, likelihood)  # The dot product between the result of the previous operation and the forwarded message
        if not self.config['normalize_result']:
            return r
        return self._normalize(r)

    def _backward(self, evidence, b):
        """
        A private function implementing the backward equation. Returns the new backward message
        :param evidence: The evidence for the current time slice t
        :param b: The previous backward message as a 1D numpy array
        :return: The new backward message as a 1D numpy array
        """
        s, t = self.config['sensor_model'], self.config['transition_model']  # Get the global sensor- and transition model
        if not evidence:
            """
            The same procedure as in _forward. Look there for a detailed description
            """
            s = np.identity(len(s)) - s  # Local update to T^-1 (subtract with identity matrix to get false values)
        r = np.dot(t, s)  # The matrix product between T and S_k+1 (transition model and sensor model)
        r = np.dot(r, b)  # The dot product between the result of the previous operation and the backwarded message
        return r

    @staticmethod
    def _normalize(estimate):
        """
        Normalizes the estimate to make the probabilities equals 1
        :param estimate: The vector to be normalized
        :return: The normalized value
        """
        return estimate / estimate.sum()


def run_algorithm(algorithm, num_of_evidences):
    initial_belief = np.array([.5, .5])
    day_2 = [True, True]  # Evidence for Part B.1 and C.1
    day_5 = [True, True, False, True, True]  # Evidence for Part B.2 and C.2

    if num_of_evidences == 2:
        algorithm.prediction(day_2, initial_belief)
        print()
        algorithm.forward_backward(day_2, initial_belief)
    elif num_of_evidences == 5:
        algorithm.prediction(day_5, initial_belief)
        print()
        algorithm.forward_backward(day_5, initial_belief)
    else:
        "Invalid number of evidences"


if __name__ == "__main__":
    transition_model = np.array([[.7, .3],
                                 [.3, .7]])

    sensor_model = np.array([[.9, 0],
                             [.0, .2]])

    # The main configuration passed to ForwardBackward during instantiation
    main_config = {
        'transition_model': transition_model,
        'sensor_model': sensor_model,
        'normalize_result': True
    }

    hmm = ForwardBackward(config=main_config)

    run_algorithm(hmm, 5)
