
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import StandardScaler
from sklearn.pipeline import make_pipeline
from sklearn.model_selection import GridSearchCV
from sklearn.ensemble import RandomForestRegressor
from sklearn.svm import SVR
from sklearn.gaussian_process.kernels import RBF, ConstantKernel
from sklearn.gaussian_process import GaussianProcessRegressor

##LINEAR REGRESSION
lr_reg = make_pipeline(LinearRegression())

# ##RandomForestRegressor
# rf_reg = make_pipeline(StandardScaler(), RandomForestRegressor(max_depth = 3))

# ##SVM
# svr = make_pipeline(StandardScaler(), SVR(kernel='linear', kernel ='rbf', epsilon = 0.3, C = 0.5))

# ##guassian process
# # Instantiate a Gaussian Process model
# gp = make_pipeline(StandardScaler(),
#                    GaussianProcessRegressor(n_restarts_optimizer=20, normalize_y=True, copy_X_train=False,kernel=RBF()))

