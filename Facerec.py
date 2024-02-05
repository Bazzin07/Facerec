import face_recognition
import cv2
import subprocess



image_path = 'test.jpg'
known_image = face_recognition.load_image_file(image_path)
known_face_encodings = face_recognition.face_encodings(known_image)


video_capture = cv2.VideoCapture(0)
while True:
   
    ret, frame = video_capture.read()


    face_locations = face_recognition.face_locations(frame)

   
    if face_locations:
        
        current_face_encoding = face_recognition.face_encodings(frame, face_locations)[0]

       
        results = face_recognition.compare_faces(known_face_encodings, current_face_encoding)

        if results[0]:
            
            Call_URL = "D:\Facerec\Website\Facerec.html"
            mycmd = r'start msedge /new-tab {}'.format(Call_URL)
            subprocess.Popen(mycmd,shell = True) 
            print("loopfound")
            break
        else:
            print("unknown")
    else:
        print("hgjkj")

    
    for (top, right, bottom, left) in face_locations:
        cv2.rectangle(frame, (left, top), (right, bottom), (0, 0, 255), 2)

    
    cv2.imshow('Video', frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break


video_capture.release()
cv2.destroyAllWindows()