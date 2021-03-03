import os
import sys

import numpy as np


if __name__ == '__main__':

    nonempty = len(sys.argv) > 0

    if nonempty:
        folder = sys.argv[0]
        outf = sys.argv[1]
    else:
        folder = '/Volumes/Samsung_T5/SeeingThroughFogData/lidar_hdl64_strongest/'
        outf = '/Users/kirill/PycharmProjects/SeeingThroughFog/kitti_velo/'

    # folder = '/Users/kirill/PycharmProjects/SeeingThroughFog/kitti_velo/'

    ins = os.listdir(folder)

    for i, fl in enumerate(ins):
        if fl.endswith(".bin") or fl.endswith(".npz"):
            scan = np.fromfile(folder + fl, dtype=np.float32)
            scan = scan.reshape(-1, 5)
            scan = scan[:, [0, 1, 2, 3]]
            scan[:, 3] = scan[:, 3] / 255
            data = scan
            data.tofile(outf + fl)
        if i % 100 == 0:
            print(i)

