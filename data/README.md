# Point cloud dataset of catenary arches
An 800 m stretch of railway track near Delft, the Netherlands containing 15 catenary arches, was digitised into a point cloud. The point cloud data was collected with a Trimble TX8 laser scanner using the level 2 operation mode. This model has a scan duration of three minutes and a point spacing of 11.3 mm at 30 m. Points are referenced within the Rijksdriehoeksstelsel coordinate system, a national standard coordinate system of the Netherlands. This coordinate system uses units of meter. The dataset only contains `xyz` data. No colour information, intensity or normals are stored for the points. The number of points per arch ranges from 1.6 M to 11 M points.

## Arch cropping
The raw data was made available in four large chunks. Each of the arches is cropped from one of the chunks. The major axis of the rectangular crop coincides with the line being defined by the poles of the catenary arch. A padding of 2 m is used around each arch. Each of the arches is  stored individually in a compressed LAS.  Each of the samples was manually labelled into 14 different classes using CloudCompare.

## Classes
Each of the points in the point cloud has a label attribute. The following values are used to define the classes. **Warning:** the label ids are not consecutive, so take special care when using the data.

| Label ID| Description|
| -------- | --------|
| 0| unlabelled|
| 1| top bar|
| 2| messenger wire support  | 
| 3| drop post |
| 4| steady arm|
| 5| insulator|
| 6| pole|
| 7| pole foundation|
| 8| dropper|
| 9| stitch wire|
|10| wheel tension device|
|11| tension rods |
|12| **not present** |
|13| tension rods foundation |
|14| contact wire|
|15| top tie|
|16| bracket|

## Naming convention
Each of the files uses the following file naming convention: `xx_yy.laz`. Here `xx` refers to the larger chunk and `yy` refers to the individual arch in the chunk. This naming convention is not relevant for working with the dataset, but is provided as background information.

# Usage

## Visualisation
The individual arches can easily be visualised with [CloudCompare](https://www.cloudcompare.org), an open source point cloud visualiser.

## Python code
Below is a sample Python snippet how to read a LAS file.

```Python
import pylas

las =  laspy.read("01_01.laz")
pc = np.stack([las.x, las.y, las.z], axis=1)
labels = las.label
```
The variable `pc` will have dimensions `npoints x 3` and the variable `labels` will have dimensions `npoints x 1`.

An important distinction between capital `XYZ` and lower case `xyz` when using the pylas library:
> The dimensions ‘X’, ‘Y’, ‘Z’ are signed integers without the scale and offset applied. To access the coordinates as doubles simply use ‘x’, ‘y’ , ‘z’
> -- [*Pylas documentation*](https://pylas.readthedocs.io/en/latest/intro.html#point-records)

# Acknowledgements
Strukton Rail for providing the point cloud dataset. Students Benjamin Bakir, Job Jonkers, Joey Teunissen, Thomas Tunc and Rehan Ahmed, from the Saxion University of Applied Sciences, for their support in labelling the dataset.

# Citing
Please cite as:

Strukton Rail, B. Ton, High resolution labelled point cloud
dataset of catenary arches in the Netherlands, 4TU.ResearchData
(2021). doi:10.4121/17048816