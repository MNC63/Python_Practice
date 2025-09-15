import cv2
import dlib

# read the image
img = cv2.imread("123.jpg")
if img is None:
    raise FileNotFoundError("Image not found. Check path!")

# initialize detector
face_detector = dlib.get_frontal_face_detector()

# detect faces
faces = face_detector(img)

print(f"Number of faces detected: {len(faces)}")

# draw rectangles
for face in faces:
    x1, y1, x2, y2 = face.left(), face.top(), face.right(), face.bottom()
    cv2.rectangle(img, (x1, y1), (x2, y2), (0, 255, 0), 3)

# show result
cv2.imshow("Face Recognition App", img)
cv2.waitKey(0)
cv2.destroyAllWindows()
