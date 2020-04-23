"""Script to process frame
"""

import cv2


def get_paper_corners(frame):
    """get corner of papers using mouse callback

    Arguments:
        frame {numpy array} -- input frame

    Raises:
        an: [description]

    Returns:
        [type] -- [description]
    """
    corners = []

    def get_click_coord(event, x, y, flags, param):
        if event == cv2.EVENT_LBUTTONDOWN:
            if len(corners) > 4:
                corners.pop()
            corners.append([x, y])
            print(corners)
        elif event == cv2.EVENT_MBUTTONDOWN:
            if len(corners) > 0:
                corners.pop()
                print(corners)

    # give our window a name
    cv2.namedWindow("display")
    cv2.setMouseCallback("display", get_click_coord)

    cv2.imshow("display", frame)
    cv2.waitKey(0)

    # raise an error if the number of corners supplied is no up to 4
    assert len(corners) > 3, "Corner points are not complete. Must be 4!"
    return corners
