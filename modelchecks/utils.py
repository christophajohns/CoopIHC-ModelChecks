import numpy
import collections
import inspect

def bic(log_likelihood, k, n):
    """Returns the score for the Bayesian information criterion (BIC-score) for the given log-likelihood, number
        of parameters k and and number of observations n

    :param log_likelihood: The maximized value of the likelihood function for the model
    :type log_likelihood: float
    :param k: The number of parameters
    :type k: int
    :param n: The number of observations or rounds of the task that were played
    :type n: int
    :return: The score for the Bayesian information criterion (BIC-score) for the given log-likelihood, number of
        parameters k and and number of observations n
    :rtype: float
    """
    return -2 * log_likelihood + k * numpy.log(n)


def aic(log_likelihood, k):
    """Returns the score for the Akaike information criterion (AIC-score) for the given log-likelihood and number
        of parameters k.

    :param log_likelihood: The maximized value of the likelihood function for the model
    :type log_likelihood: float
    :param k: The number of parameters
    :type k: int
    :return: The score for the Akaike information criterion (AIC-score) for the given log-likelihood and number of
        parameters k
    :rtype: float
    """
    return 2 * k - 2 * log_likelihood


def order_class_parameters_by_signature(cls, unordered_parameters):
    """Returns an OrderedDict representing the supplied parameters ordered by the class signature.

    :param cls: The class whose signature forms the basis for the ordering
    :type unordered_parameters: (*args: Any, **kwargs: Any) -> Any
    :param unordered_parameters: A dictionary of the parameter names and some value.
    :type unordered_parameters: dict
    :return: An OrderedDict representing the supplied parameters ordered by the class signature.
    :rtype: collections.OrderedDict
    """
    # Create an OrderedDict to store the ordered parameters
    ordered_parameters = collections.OrderedDict()

    # Get an OrderedDict of the parameter names and types of the operator class constructor
    operator_parameters = inspect.signature(cls).parameters

    # For each parameter in the operator class instructor...
    for param_name, _ in operator_parameters.items():

        # If the parameter name is included in the provided unordered parameters...
        if param_name in unordered_parameters.keys():

            # Add the associated values to the OrderedDict under the parameter name
            ordered_parameters[param_name] = unordered_parameters[param_name]

    # And return the ordered parameter fit bounds
    return ordered_parameters


def f1(precision, recall):
    """Returns the F1-score for the given precision and recall.

    :param precision: The precision value.
    :type precision: float
    :param recall: The recall value.
    :type recall: float
    :return: The F1-score for the given precision and recall
    :rtype: float
    """
    return 2 * (precision * recall) / (precision + recall)

