import cv2
import face_recognition

known_face_encodings=[]
known_face_names=[]

known_person1_image = face_recognition. load_image_file("dataset/2.jpg")
known_person2_image = face_recognition. load_image_file("dataset/4.jpg")
known_person3_image = face_recognition. load_image_file("dataset/6.jpg")

known_person1_encoding = face_recognition. face_encodings(known_person1_image) [0]
known_person2_encoding = face_recognition. face_encodings(known_person2_image) [0]
known_person3_encoding = face_recognition. face_encodings(known_person3_image) [0]

known_face_encodings.append(known_person1_encoding)
known_face_encodings.append(known_person2_encoding)
known_face_encodings.append(known_person3_encoding)

known_face_names. append ("Souhardya")
known_face_names. append("rudy")
known_face_names. append("paul")







# Open default camera (0). Change to 1 if you really need the second device.
cap = cv2.VideoCapture(0)



if not cap.isOpened():
    print("Cannot open camera")
    exit()

while True:
    ret, frame = cap.read()
   


    face_locations = face_recognition. face_locations(frame)
    face_encodings = face_recognition. face_encodings (frame, face_locations)   

    for (top, right, bottom, left), face_encoding in zip(face_locations, face_encodings) :
        # Check if the face matches any known faces
        matche = face_recognition. compare_faces(known_face_encodings, face_encoding)

    if True in matche:
        first_match_index = matche.index(True)
        name = known_face_names[first_match_index]

        # Draw a box around the face and label with the name
    cv2. rectangle(frame, (left, top), (right, bottom), (0, 0, 255), 2)
    cv2.putText (frame, name, (left, top - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.9, (0, 0, 255), 2)

    cv2.imshow("Frame", frame)
    if not ret:
        print("Failed to grab frame")
        break

   
    key = cv2.waitKey(1) & 0xFF

    # 1) Close on ESC
    if key == 27:
        break

    # 2) Close if window was closed by clicking the "X"
    if cv2.getWindowProperty("Frame", cv2.WND_PROP_VISIBLE) < 1:
        break



cap.release()
cv2.destroyAllWindows()
