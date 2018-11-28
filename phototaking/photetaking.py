import cv2
import os


def make_photo():
    """使用opencv拍照"""
    cap = cv2.VideoCapture(1)  # 默认的摄像头
    i = 1
    while True:
        ret, frame = cap.read()
        if ret:
            cv2.imshow("capture", frame)  # 弹窗口
            num = '%d' % i
            Img_Name = os.path.join("C:\\Users\\Liu Wenjing\\Desktop\\save\\" + num + ".bmp")
            cv2.imwrite(Img_Name, frame)
            cv2.waitKey(100)
            i= i + 1

    cap.release()
    cv2.destroyAllWindows()

if __name__ == '__main__':
    make_photo()
