import cv2 as cv
import copy
import math
import numpy as np
import imageio as io


def corr(c_list, filter):
    """
    This function correlates the given data using the given filter
    :param c_list: The color list to be manipulated
    :param filter: The filter to be used for manipulation
    :return: list of manipulated data
    """
    ans = []
    center = math.floor(len(filter) / 2)
    for i in range(len(c_list) - len(filter) + 1):
        start = 0
        end = len(c_list)
        temp = c_list[i:i + len(filter)]
        while start < end - 1:
            mat = []
            for i in range(len(temp)):
                mat.append(temp[i][start:start + len(filter)])
            if len(mat[0]) != len(filter):
                start += 1
                continue
            else:
                start += 1
                mult = 0
                for i in range(len(mat)):
                    for j in range(len(mat[i])):
                        mult += mat[i][j] * filter[i][j]
                mat[center][center] = mult
                ans.append(mult)
    return ans


def main():
    """
    This function manipulates data format for the corr function to process it and saves the filtered image as new_lenna.png
    :return: -
    """
    filter = [[-2, 3, -1], [4, -1, 2], [0, 5, 3]]
    img = cv.imread('Lenna.png')
    b, g, r = cv.split(img)

    b_list = b.tolist()
    r_list = r.tolist()
    g_list = g.tolist()

    for arr in b_list:
        arr.insert(0, arr[0])
        arr.append(arr[-1])
    b_list.insert(0, b_list[0])
    b_list.append(b_list[-1])

    for arr in r_list:
        arr.insert(0, arr[0])
        arr.append(arr[-1])
    r_list.insert(0, r_list[0])
    r_list.append(r_list[-1])

    for arr in g_list:
        arr.insert(0, arr[0])
        arr.append(arr[-1])
    g_list.insert(0, g_list[0])
    g_list.append(g_list[-1])

    ans_b = corr(b_list, filter)
    ans_r = corr(r_list, filter)
    ans_g = corr(g_list, filter)

    b_rows = []
    g_rows = []
    r_rows = []

    new_img = []

    i = 0
    while i < len(ans_b):
        temp = ans_b[i: i + 512]
        b_rows.append(temp)
        i += 512

    i = 0
    while i < len(ans_g):
        temp = ans_g[i: i + 512]
        g_rows.append(temp)
        i += 512

    i = 0
    while i < len(ans_r):
        temp = ans_r[i: i + 512]
        r_rows.append(temp)
        i += 512

    new_img = np.dstack((r_rows, g_rows, b_rows))

    io.imsave('new_lenna.png', new_img)


main()