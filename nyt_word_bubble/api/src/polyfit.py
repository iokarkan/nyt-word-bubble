import numpy as np
from matplotlib.pyplot import Figure
from sklearn.linear_model import LinearRegression

class Polyfit:
    
    X = None
    y = None

    def __init__(self, order=2, n_points=10) -> None:
        self.order = order
        self.n_points = n_points
        
    def generate_XY(self):
        X = np.linspace(-3,3,self.n_points)
        a = 0.2
        b = 0.6
        c = 2
        d = 0.5
        e = 0.6
        noise = np.random.normal(loc=0, scale=10, size=X.shape)
        y = a*X**4 + b*X**3 + c*X**2 + d*X + e + noise

        self.X = X
        self.y = y
        return (X,y)

    def fit_Y(self):
        model = LinearRegression(fit_intercept=True)

        if self.order==0:
            X_train = np.vstack([self.X**0]).T
        else:
            X_train = np.vstack([self.X**n for n in range(1,self.order+1)]).T

        model.fit(X_train, self.y)
        return model

    def pred_Y(self, n=100):
        model = self.fit_Y()

        x_pred = np.linspace(-3,3,n)
        if self.order==0:
            y_pred = model.predict(np.vstack([x_pred**0]).T)
        else:
            y_pred = model.predict(np.vstack([x_pred**n for n in range(1,self.order+1)]).T)

        return x_pred, y_pred
    
    def create_fig(self):
        x_pred, y_pred = self.pred_Y()
        fig = Figure(figsize=(7, 5))
        axis = fig.add_subplot(1, 1, 1)
        axis.scatter(self.X, self.y)
        axis.plot(x_pred, y_pred, linestyle="dashed", c="red")
        axis.margins(0.005, tight=True)
        axis.set_ylim((-5)*abs(min(self.y)), max(self.y)*2)
        return fig


if __name__=="__main__":
    import matplotlib.pyplot as plt
    pfit = Polyfit(order=0, n_points=10)
    x_pred, y_pred = pfit.pred_Y()
    
    plt.scatter(pfit.X, pfit.y)
    plt.plot(x_pred, y_pred, linestyle='dashed', c='red')
    plt.show()