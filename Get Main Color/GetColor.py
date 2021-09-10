from cv2 import cv2
import numpy as np
import collections

imageFile = input("Please enter the full path of the picture: ")
frame = cv2.imread(imageFile)

def getColorList():
    dict = collections.defaultdict(list)
    # 黑色
    color_list = []
    color_list.append(np.array([0, 0, 0]))  # lower_black
    color_list.append(np.array([180, 255, 46]))  # upper_black
    dict['black'] = color_list
    # 灰色
    color_list = []
    color_list.append(np.array([0, 0, 46]))  # lower_gray
    color_list.append(np.array([180, 43, 220]))  # upper_gray
    dict['gray'] = color_list
    # 白色
    color_list = []
    color_list.append(np.array([0, 0, 221]))  # lower_white
    color_list.append(np.array([180, 30, 255]))  # upper_white
    dict['white'] = color_list
    # 红色
    color_list = []
    color_list.append(np.array([156, 43, 46]))  # lower_red
    color_list.append(np.array([180, 255, 255]))  # upper_red
    dict['red'] = color_list
    # 红色2
    color_list = []
    color_list.append(np.array([0, 43, 46]))  # lower_red
    color_list.append(np.array([10, 255, 255]))  # upper_red
    dict['red'] = color_list
    # 橘色
    color_list = []
    color_list.append(np.array([11, 43, 46]))  # lower_orange
    color_list.append(np.array([25, 255, 255]))  # upper_orange
    dict['orange'] = color_list
    # 黃色
    color_list = []
    color_list.append(np.array([26, 43, 46]))  # lower_yellow
    color_list.append(np.array([34, 255, 255]))  # upper_yellow
    dict['yellow'] = color_list
    # 綠色
    color_list = []
    color_list.append(np.array([35, 43, 46]))  # lower_green
    color_list.append(np.array([77, 255, 255]))  # upper_green
    dict['green'] = color_list
    # 靛色
    color_list = []
    color_list.append(np.array([78, 43, 46]))  # lower_cyan
    color_list.append(np.array([99, 255, 255]))  # upper_cyan
    dict['cyan'] = color_list
    # 藍色
    color_list = []
    color_list.append(np.array([100, 43, 46]))  # lower_blue
    color_list.append(np.array([124, 255, 255]))  # upper_blue
    dict['blue'] = color_list
    # 紫色
    color_list = []
    color_list.append(np.array([125, 43, 46]))  # lower_purple
    color_list.append(np.array([155, 255, 255]))  # upper_purple
    dict['purple'] = color_list

    return dict


def getColor(image):
    hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
    maxsum = -100
    color = None
    color_dict = getColorList()
    for d in color_dict:
        mask = cv2.inRange(hsv, color_dict[d][0], color_dict[d][1])
        # cv2.imwrite(d+'.png',mask)
        binary = cv2.threshold(mask, 127, 255, cv2.THRESH_BINARY)[1]
        binary = cv2.dilate(binary, None, iterations=2)
        cnts = cv2.findContours(
            binary.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)[0]
        sum = 0
        for c in cnts:
            sum += cv2.contourArea(c)
        if sum > maxsum:
            maxsum = sum
            color = d
    return color

color = getColor(frame)
print("主要顏色：" + color)