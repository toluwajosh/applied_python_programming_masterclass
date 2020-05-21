"""Script to process frame
"""
import cv2


def get_paper_corners(frame):
    """get corner of papers using mouse callback
    Arguments:
        frame {numpy array} -- input frame or image
    Raises:
        an AssertionError: Selected corner points must be equal to 4.
    Returns:
        [list] -- a list of corner points
    """
    corners = []

    def get_click_coord(event, x, y, flags, param):
        """Callback function to get coordinate of clicked points
        Arguments:
            event {cv2.EVENT} -- OpenCV Event
            x {int} -- x coordinate
            y {int} -- y coordinate
            flags {[type]} -- event flag. Not used
            param {[type]} -- event parameter. Not used
        """
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
    window_name = "display"
    cv2.namedWindow(window_name)
    cv2.setMouseCallback(window_name, get_click_coord)

    cv2.imshow(window_name, frame)
    cv2.waitKey(0)

    # raise an error if the number of corners supplied is no up to 4
    assert len(corners) > 3, "Corner points are not complete. Must be 4!"
    return corners


if __name__ == "__main__":
    pass
