import open3d as o3d
import numpy as np
import open3d.core as o3c
# import tensorflow
import copy
import laspy


class Bridge:
    def __init__(self, file, vox_size):
        self.loadFile = o3d.io.read_point_cloud(file)
        self.tfile = o3d.t.geometry.PointCloud(o3c.Tensor([[0,0,0],[1,1,1]], o3c.float32))
        self.length_loadFile = len(self.loadFile.points)
        self.vox_size = vox_size
        self.map_to_tensors = {}


    def reading(self, file):
        readz = open(file)
        readz.read()
        print(readz)

    def voxelize(self):
        voxel_grid = o3d.geometry.VoxelGrid.create_from_point_cloud(self.loadFile, voxel_size=self.vox_size)
        # print(len(voxel_grid.points))
        # print(self.loadFile)
        # print(np.array(self.loadFile.points))
        # self.map_to_tensors["FIELDS"] = o3c.Tensor([0,1], o3c.int64)
        # labels = self.tfile.point.labels = o3c.Tensor([0,1], o3c.int64)
        # print(labels)
        # test = o3d.t.geometry.PointCloud(self.map_to_tensors)

        # print( self.map_to_tensors)
        # print("test:", test)
        # print("voxel size:", self.vox_size)
        # print(voxel_grid)
        # position = self.loadFile.point.positions
        # print(position, "/n")
        print(type(voxel_grid))
        return voxel_grid

    def draw(self):
        o3d.visualization.draw_geometries([self.loadFile], window_name='Origional data', width=1800, height=1080)
        o3d.visualization.draw_geometries([self.voxelize()], window_name='Voxelized data', width=1800, height=1080)
        # print((np.array(self.loadFile.points)))


# pass the return from def voxelize as a parameter into the draw function

if __name__ == "__main__":
    build = Bridge(('01_01.pcd'), 0.05)
    build.voxelize()
    build.draw()

# depending on the relative size of object, can you change amount of downsampling by voxelization. A pole needs more downsampling than a insulator  because of hte size difference.
# does shaply work with dynamic sized voxels
#next meeting, get the algorihtm working on the origional data, and also try and make a branch/copy for voxel data.