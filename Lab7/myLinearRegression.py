class MyLinearUnivariateRegression:
    def __init__(self):
        self.intercept_ = 0.0
        self.coef_ = []
    # learn a linear univariate regression model by using training inputs (x) and outputs (y) 
    # http://faculty.cas.usf.edu/mbrannick/regression/Part3/Reg2.html
    def fit(self, x1, x2, y):
        sx1 = sum(x1)
        sx2 = sum(x2)
        sy = sum(y)
        sx12 = sum(i * i for i in x1)
        sx22 = sum(i * i for i in x2)
        sx1y = sum(i * j for (i,j) in zip(x1, y))
        sx2y = sum(i * j for (i,j) in zip(x2, y))
        sx1x2 = sum(i * j for (i,j) in zip(x1, x2))
        w1 = (sx22 * sx1y - sx1x2 * sx2y) / (sx12 * sx22 - sx1x2 * sx1x2)
        w2 = (sx12 * sx2y - sx1x2 * sx1y) / (sx12 * sx22 - sx1x2 * sx1x2)
        w0 = (sy - w1 * sx1 - w2 * sx2) / len(x1)
        self.intercept_ = w0
        self.coef_.append(w1)
        self.coef_.append(w2)