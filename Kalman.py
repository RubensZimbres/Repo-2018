# KALMAN FILTER
from numpy import ma
from pykalman import KalmanFilter
kf = KalmanFilter(initial_state_mean=0, n_dim_obs=XX.shape[1])
measurements = ma.asarray(XX)

kf = kf.em(measurements, n_iter=5)

(filtered_state_means, filtered_state_covariances) = kf.filter(measurements)
(smoothed_state_means, smoothed_state_covariances) = kf.smooth(measurements)
