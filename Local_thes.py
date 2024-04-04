import open3d as o3d
import numpy as np
import open3d.core as o3c
# import tensorflow
import copy
import laspy


class Bridge:
    def __init__(self, file, file2, vox_size, vox_size2):
        self.loadFile1 = o3d.io.read_point_cloud(file)
        self.loadFile2 = o3d.io.read_point_cloud(file2)

        self.vox_size = vox_size
        self.vox_size2 = vox_size2


    def voxelize(self):
        voxel_grid = o3d.geometry.VoxelGrid.create_from_point_cloud(self.loadFile1, voxel_size=self.vox_size)
        voxel_grid2 = o3d.geometry.VoxelGrid.create_from_point_cloud(self.loadFile2, voxel_size=self.vox_size2)
        return voxel_grid, voxel_grid2

    def draw(self):
        # o3d.visualization.draw_geometries([self.loadFile], window_name='Origional data', width=1800, height=1080)
        o3d.visualization.draw_geometries([self.voxelize()], window_name='Voxelized data', width=1800, height=1080)
        # print((np.array(self.loadFile.points)))

if __name__ == "__main__":
    build = Bridge(('points_with_label_1.pcd'), 0.5, ('points_with_label_6.pcd'), 1)
    build.voxelize()
    build.draw()

# depending on the relative size of object, can you change amount of downsampling by voxelization. A pole needs more downsampling than a insulator  because of hte size difference.
# does shaply work with dynamic sized voxels
#next meeting, get the algorihtm working on the origional data, and also try and make a branch/copy for voxel data.