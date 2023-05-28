import numpy as np

def calculate_distance(lat1, lon1, lat2, lon2, r=6371):
    """
    Function to calculate the distance between two sets of coordinates.

    Args:
        lat1: Latitude of the first point.
        lon1: Longitude of the first point.
        lat2: Latitude of the second point.
        lon2: Longitude of the second point.
        r: Radius of the Earth (default: 6371).

    Returns:
        d: Distance between the two points.
    """
    coordinates = lat1, lon1, lat2, lon2
    phi1 = np.radians(lat1)
    lambda1 = np.radians(lon1)
    phi2 = np.radians(lat2)
    lambda2 = np.radians(lon2)
    a = (np.square(np.sin((phi2 - phi1) / 2)) + np.cos(phi1) * np.cos(phi2) *
         np.square(np.sin((lambda2 - lambda1) / 2)))
    d = 2 * r * np.arcsin(np.sqrt(a))
    
    return d
