from read import load_velodyne_scan
import os
import numpy as np
import csv
import sys
from shutil import copyfile





if __name__ == '__main__':
    nonempty = len(sys.argv) > 0

    if nonempty:
        datasplit = sys.argv[0]
        extension = sys.argv[1]
        dir = sys.argv[2]
        dstdir = sys.argv[3]
    else:
        datasplit = "../../../splits/all.txt"
        extension = "bin"
        dir = "/Volumes/Samsung_T5/SeeingThroughFogData/lidar_hdl64_last/"
        dstdir = "data/"

    cnt = 0
    with open(datasplit, newline='') as csvfile:
        spamreader = csv.reader(csvfile, delimiter=',')
        for row in spamreader:
            fn = dir + '_'.join(row) + "." + extension
            copyfile(fn, dstdir + str(cnt).zfill(6) + "." + extension)
            cnt += 1



    # for file in os.listdir(dir):
    #     if cnt < lim:
    #         if file.endswith(".bin") or file.endswith(".npz"):
    #             v = load_velodyne_scan(dir + file)
    #             file_velo = "data/" + str(cnt).zfill(6) + ".bin"
    #             np.array(v, np.float32).tofile(file_velo)
    #             cnt += 1
    #     else:
    #         break



    # file_velo = "data/" + str(j) + "/velodyne/" + str(counter) + ".bin"
    # np.array(scan, np.float32).tofile(file_velo)
    print("lol")