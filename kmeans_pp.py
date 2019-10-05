import numpy as np
import matplotlib.pyplot as plt

class Kmeans(object):

    def __init__(self, K=3, max_iter=20, init='', seed=None):
        self.K = K;
        self.max_iter = max_iter
        self.SSE = []
        self.labels = []
        self.init = init
        self.centroid = None
        np.random.seed(seed)

    def compute_distance(self, A, B):  # compute distance of numpy array A & B
        return np.sum(np.square(A - B), axis=1)  # euclidean^2

    def rand_centroids(self, X):
        m, num_dims = X.shape
        if (self.init == 'kmeans++'):  
            self.centroids = X[np.random.choice(m, 1), :]  # random choose one centroid from X
            while (self.centroids.shape[0] < self.K):  # until num centroids = K
                distance = np.zeros((m, self.centroids.shape[0]))  # init distance
                for i in range(self.centroids.shape[0]):  
                    distance[:, i] = self.compute_distance(X, self.centroids[i, :])
                total_distance = np.sum(np.min(distance, axis=1)) 
                prob_list = np.min(distance, axis=1) / total_distance  
                self.centroids = np.vstack([self.centroids, X[np.random.choice(m, 1, p=prob_list), :]]) # concat new centroid
        elif(self.init == 'kmeans'):
            self.centroids = np.zeros((self.K, num_dims))
            rand_index = np.random.choice(m, self.K, replace=False)  # random choose K node of X
            self.centroids = X[rand_index]
        else:
            raise NameError('Wrong init selected, please select between "kmeans" and "kmeans++"')
        return self

    def change_centroids(self, X):
        m, num_dims = X.shape
        self.centroids = np.zeros((self.K, num_dims))
        for i in range(self.K):
            index = np.where(self.idx[:] == i)  
            self.centroids[i] = np.mean(X[index], axis=0)
        return self

    def calculate_sse(self, X):
        # calculate SSE
        sse = 0
        for i in range(self.K):
            idx_ = np.where(self.idx[:] == i)
            sse += np.sum(np.square(X[idx_, :] - self.centroids[i, :]))
        self.SSE.append(sse)
        return self

    def fit(self, X):
        self.idx = np.zeros(X.shape[0])  # record every x belong to which centroid
        self.cent_record = {}   # use dictionary to save centroids
        clusterchanged = True   # to record whether the cluster changed

        self.rand_centroids(X)  # initialize K centroids

        for k in range(self.K):
            self.cent_record[str(k)] = []
            self.cent_record[str(k)].append(self.centroids[k, :].tolist())  # append initial centroids

        epochs = 0
        while (clusterchanged): # we could use while (epochs < self.max_iter): to stop by max_iter
                                # with while(clusterchanged): we will stop when cluster not changed.
            epochs += 1
            clusterchanged = False

            # compute distance between every x and K centroids
            distance = np.zeros((X.shape[0], self.K))
            for c in range(self.K):
                distance[:, c] = self.compute_distance(X, self.centroids[c, :])

            min_distance_index = np.argmin(distance, axis=1)  # find the closest centroid's index
            if ((min_distance_index != self.idx[:]).any()):   # check if any node change cluster
                clusterchanged = True
            self.idx[:] = min_distance_index  # update the distance between every data and centroids.

            self.calculate_sse(X)  # saved SSE to list

            # update centroids
            self.change_centroids(X)
            for k in range(self.K):
                self.cent_record[str(k)].append(self.centroids[k, :].tolist())
        
        self.labels = min_distance_index
        return self
