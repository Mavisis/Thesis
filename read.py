from pypcd4 import PointCloud
import numpy as np
import open3d as o3d

# readfile = PointCloud.from_path("01_01.pcd")
#
# # pc.fields prints the different fields
# # print(pc.fields)
# # ('instance', 'label', 'Number_Of_Returns', 'Return_Number', 'x', 'y', 'z', '#$%&~~m4wKGr')
#
# #convert pcd to numpy Ndimentional array with atributes
# arr = readfile.numpy(("x", "y", "z", "label"))
# # print(arr)
# #[[-35.37345   52.28125    6.248251  14.      ] ... ]
#
# #convert back to .pcd file form numpy array
# newpc = PointCloud.from_xyzl_points(arr, label_type=np.uint32)
# # print(newpc)
# # PointCloud(fields=('x', 'y', 'z', 'label') size=(4, 4, 4, 4) type=('F', 'F', 'F', 'U') count=(1, 1, 1, 1) points=1586927 width=1586927 height=1 version='0.7' viewpoint=(0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0) data=<Encoding.BINARY_COMPRESSED: 'binary_compressed'>)
#
# # Save the file
# newpc.save("finalwork.pcd")


huts = PointCloud.from_path('01_01.pcd')
arr = huts.numpy(("x", "y", "z", "label"))
for label_value in range(17):
    indices = np.where(arr[:, 3] == label_value)
    points_with_current_label = arr[indices]
    # print(points_with_label_6)
    pcd = PointCloud.from_xyzl_points(points_with_current_label, label_type=np.uint32)
    filename = f"points_with_label_{label_value}.pcd"
    # pcd.save(filename)





# point_cloud = o3d.io.read_point_cloud('01_01.pcd')
# voxel_size =
# voxel_grid = o3d.geometry.VoxelGrid.create_from_point_cloud(point_cloud, voxel_size=voxel_size)






