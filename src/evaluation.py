import numpy as np

def evaluate_performance(dfOutput, dfGroundTruth):
    """
    Evaluate the performance by calculating the L1 error (mean absolute difference)
    between the predicted values (dfOutput) and the ground truth values (dfGroundTruth).

    Args:
        dfOutput (numpy.ndarray or list): Array or list of predicted values.
        dfGroundTruth (numpy.ndarray or list): Array or list of ground truth values.

    Returns:
        float: L1 error (mean absolute difference) between the predicted and ground truth values.
    """
    dfOutput = np.array(dfOutput)
    dfGroundTruth = np.array(dfGroundTruth)

    # Calculate the absolute difference between predicted and ground truth values
    absolute_diff = np.abs(dfOutput - dfGroundTruth)

    # Calculate the mean absolute difference (L1 error)
    l1_error = np.mean(absolute_diff)

    print(f"The mean absolute difference (L1 error) is {l1_error}")

    return l1_error
