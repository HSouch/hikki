import cv2
from numpy import shape, median, ndarray


def get_video_data(filename: str, verbose=False) -> list:
    """
    Uses cv2 to analyze an input video to obtain an numpy ndarray of rgb pixels.
    :param filename: name of file to analyze (absolute path recommended)
    :param verbose: print live information during runtime
    :return: np ndarray of rgb values.
    """
    full_video = cv2.VideoCapture(filename)
    ret, frame = full_video.read()

    if verbose:
        print("Frame is type:", type(frame))
        print("Frame is shape:", shape(frame))

    frame_count = int(full_video.get(cv2.CAP_PROP_FRAME_COUNT))
    frames = []
    this_frame = 0
    while this_frame < frame_count:
        ret, frame = full_video.read()
        if not ret:
            break
        frames.append(frame)
        this_frame += 1

    if verbose:
        print("Total Frames:", len(frames), "which should be", str(frame_count - 1))

    full_video.release()
    cv2.destroyAllWindows()

    return frames


def get_slice(rgb_array, slice_index):
    """
    Returns a specific z slice of the rgb picture array.
    For example, to return the green slice you would set slice_index to 1.
    :param rgb_array: Original array
    :param slice_index:
    :return:
    """
    slice = rgb_array[:, :, slice_index]
    return slice


def get_position(frame, color, threshold = 10, accuracy=5):
    """
    Analyzes frames for all pixels of a given colour within a certain threshold. Determines and returns the median x
    and y position.
    :param frame:
    :param color:
    :param threshold:
    :return:
    """
    good_x, good_y = [], []
    for x in range(0, frame.shape[0], accuracy):
        for y in range(0, frame.shape[1], accuracy):
            pixel = frame[x][y]
            diff = abs(pixel[0] - color[0]) + abs(pixel[1] - color[1]) + abs(pixel[2] - color[2])
            if diff < threshold:
                good_x.append(x)
                good_y.append(y)
    return median(good_x), median(good_y)


def get_position_arrays(frame_set, ideal_colour, framerate=10, accuracy=10, threshold=10):
    """
    Obtains x and y position arrays from the list of input frames.
    :param frame_set: The list of frames to analyze.
    :param ideal_colour: The colour Hikki is looking for [r, g, b]
    :param framerate: The number of frames Hikki will check (setting as 1 will check all frames. SLOW!)
    :param accuracy: The number of pixels Hikki will check (setting as 1 will check all pixels)
    :param threshold: How much the pixel colour can differ from the ideal colour while still being counted as valid.
    :return: Returns x and y position arrays. (Note a flip in x and y. Not sure why a transposition is needed).
    """
    xs, ys = [], []
    for n in range(0, len(frame_set), framerate):
        print(n)
        x, y = get_position(frame_set[n], ideal_colour, threshold=threshold, accuracy=accuracy)
        xs.append(y)
        ys.append(x)
    return xs, ys


# name = 'C:/Users/HSouc/Hikki//test_vid.mp4'
# frames = get_video_data(name)
# xs, ys = get_position_arrays(frames, [85, 54, 106])
