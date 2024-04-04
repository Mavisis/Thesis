import open3d as o3d

def voxelize_point_cloud(point_cloud, voxel_size):
    # Voxelization
    voxel_grid = o3d.geometry.VoxelGrid.create_from_point_cloud(point_cloud, voxel_size=voxel_size)

    return voxel_grid

# Load point cloud data from file (replace 'point_cloud.pcd' with your file name)
point_cloud = o3d.io.read_point_cloud('01_01.pcd')

# Define the variable that determines the voxel size
variable = 2  # This can be any value you want, just an example here

# Calculate voxel size based on the variable
if variable == 1:
    voxel_size = 0.1
else:
    voxel_size = 0.5

# Voxelize the point cloud with the chosen voxel size
voxel_grid = voxelize_point_cloud(point_cloud, voxel_size)

# Visualize the voxel grid
o3d.visualization.draw_geometries([voxel_grid])
