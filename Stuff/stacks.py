# coding: utf-8
left = np.ones((4, 4))
right = np.zeros((4,2))
left
right
center = np.hstack((left, right))
center
center = np.hstack((right, center))
center
center.shape
down = np.zeros((2,8))
center = np.vstack((down, center))
center
center = np.vstack((down, center))
center
get_ipython().magic(u'save stacks 168-181')
center.shape
c = center[2:,:]
c
center = c
center.shape
center = np.vstack((center, down))
center
