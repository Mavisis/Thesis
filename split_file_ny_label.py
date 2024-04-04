from pypcd4 import PointCloud
import numpy as np
import open3d as o3d

readfile = PointCloud.from_path("01_01.pcd")
arr = readfile.numpy(("x", "y", "z", "label"))
for label_value in range(17):
    indices = np.where(arr[:, 3] == label_value)
    points_with_current_label = arr[indices]
    # print(points_with_label_6)
    pcd = PointCloud.from_xyzl_points(points_with_current_label, label_type=np.uint32)
    filename = f"points_with_label_{label_value}.pcd"
    pcd.save(filename)