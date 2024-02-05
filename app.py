from flask import Flask, render_template, redirect, url_for
import face_recognition
import cv2

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/dashboard')
def dashboard():
    return "Welcome to the dashboard!"

@app.route('/face_recognition', methods=['POST'])
def face_recognition_route():
    image_path = 'known_faces/test.jpg'
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
                detected_name = "AYUSH "  
                return render_template('Facerec.html', detected_name=detected_name)
                
            else:
                print("Unknown face")
        else:
            print("No face detected")

        for (top, right, bottom, left) in face_locations:
            cv2.rectangle(frame, (left, top), (right, bottom), (0, 0, 255), 2)

        cv2.imshow('Video', frame)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    video_capture.release()
    cv2.destroyAllWindows()

    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)