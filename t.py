import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from pypcd4 import PointCloud

huts = PointCloud.from_path('01_01.pcd')
arr = huts.numpy(("x", "y", "z", "label"))


def create_voxel_grid(points, voxel_size):
    # Determine the range of the points
    min_bound = np.min(points, axis=0)
    max_bound = np.max(points, axis=0)

    # Calculate the dimensions of the voxel grid
    dims = np.ceil((max_bound - min_bound) / voxel_size).astype(int)

    # Initialize the voxel grid
    voxel_grid = np.zeros(dims, dtype=bool)

    # Convert points to voxel indices
    voxel_indices = ((points - min_bound) / voxel_size).astype(int)

    # Set voxels containing points to True
    voxel_grid[voxel_indices[:, 0], voxel_indices[:, 1], voxel_indices[:, 2]] = True

    return voxel_grid


# ####Generate some random point cloud data
# num_points = 1000
# points = np.random.rand(num_points, 3)
# print(points)

# #####data
# points = PointCloud.from_points('01_01.pcd', ["x", "y", "z", "label"], [np.float32, np.float32, np.float32])

points = arr[:, :3]

# Define voxel size
voxel_size = 0.1

# Create the voxel grid
voxel_grid = create_voxel_grid(points, voxel_size)

# Visualize the voxel grid
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.voxels(voxel_grid, edgecolor='k')
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')
plt.show()
