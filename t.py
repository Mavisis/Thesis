import numpy as np
import matplotlib.pyplot as plt
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

def visualize():
# Visualize the voxel grid
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    ax.voxels(voxel_grid, edgecolor='k')
    ax.set_xlabel('X')
    ax.set_ylabel('Y')
    ax.set_zlabel('Z')
    plt.show()





# Example usage within the loop over label values
for label_value in range(17):

    voxel_size = 1*label_value+1

# voxel_grid = create_voxel_grid(arr[:, :3], voxel_size)
voxel_grid = create_voxel_grid(arr[:, :3], voxel_size)
visualize()