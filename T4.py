# Lines of symetry with mtcnn
import cv2
from matplotlib import pyplot
from matplotlib.patches import Rectangle
from mtcnn.mtcnn import MTCNN


# создаем метод, чтобы он прорисовывал линии нобнаруженных точках
def draw_image_with_boxes(filename, result_list):
    # загрузить фотографию
    data = pyplot.imread(filename)
    # загрузить фото на график
    pyplot.imshow(data)
    # получение данных для прорисовки линий и прямоугольников
    ax = pyplot.gca()
    # просмотреть все лица
    for result in result_list:
        # получить координаты лиц
        x, y, width, height = result['box']
        # создание прямоуголников по координатам лица
        rect = Rectangle((x, y), width, height, fill=False, color='red')
        # добавление их на фото
        ax.add_patch(rect)
        # нарисовать линии симметрии
        for key, value in result['keypoints'].items():
            if key in ['left_eye', 'right_eye', 'nose']:
               line = Rectangle((value[0], y), 0, height, fill=False, color='red')
               ax.add_patch(line)
    # показать итог
    pyplot.show()


filename = '1.pgm'
# загрузить фотографию
pixels = cv2.imread(filename)
# Инициализировать mtcnn
detector = MTCNN()
# используя mtcnn получить координаты лиц
faces = detector.detect_faces(pixels)
# произвести обводку лица, нарисовать линии симметрии
draw_image_with_boxes(filename, faces)
