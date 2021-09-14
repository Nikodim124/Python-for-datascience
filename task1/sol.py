a = np.genfromtxt('out.csv', delimiter=',', skip_header=True)
ematrix = np.eye(*a.shape)
res = np.dot(a, ematrix.transpose())
np.savetxt("new_out.csv", res, delimiter=",")
