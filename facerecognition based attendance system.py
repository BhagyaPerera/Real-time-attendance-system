
import tkinter
import cv2
import PIL.Image, PIL.ImageTk

# Create a window
window = tkinter.Tk()

window.configure(background="#9802fd")







def function():
    import face_recognition
    import cv2
    import csv

    ##import datetime



    # Get a reference to webcam #0 (the default one)
    video_capture = cv2.VideoCapture(0)
    
    
    #image_1 = face_recognition.load_image_file("AS2016304.JPG")
    #image_1_face_encoding = face_recognition.face_encodings(image_1)[0]
    
    image_5 = face_recognition.load_image_file("AS2016467.JPG")
    image_5_face_encoding = face_recognition.face_encodings(image_5)[0]

    image_3 = face_recognition.load_image_file("AS2016436.JPG")
    image_3_face_encoding = face_recognition.face_encodings(image_3)[0]
        
    image_4 = face_recognition.load_image_file("AS2016533.JPG")
    image_4_face_encoding = face_recognition.face_encodings(image_4)[0]
        
    #Create arrays of known face encodings and their names
    known_face_encodings = [
        
        #image_1_face_encoding,
        image_5_face_encoding,
        image_3_face_encoding,
        #image_3_face_encoding, 
        image_4_face_encoding
        
    ]
    known_face_names = [
        
        #'2016467',
        #'2016322',
        #'2016304',
        '2016467',
        '2016436',
        '2016533'
       
    ]
    
    # Initialize some variables
    face_locations = []
    face_encodings = []
    face_names = []
    matches=[]
    process_this_frame = True
    
    ### Load present date and time
    ##now= datetime.datetime.now()
    ##today=now.day
    ##month=now.month

    while(True):
        # Grab a single frame of video
            ret, frame = video_capture.read()
        
        # Resize frame of video to 1/4 size for faster face recognition processing
            small_frame = cv2.resize(frame,(0,0), fx=0.25, fy=0.25)
        
        # Convert the image from BGR color (which OpenCV uses) to RGB color (which face_recognition uses)
            rgb_small_frame = small_frame[:, :, ::-1]
        
        # Only process every other frame of video to save time
            if process_this_frame:                          
        # Find all the faces and face encodings in the current frame of video
                    face_locations = face_recognition.face_locations(rgb_small_frame)
                    face_encodings = face_recognition.face_encodings(rgb_small_frame, face_locations)
    
            
            for face_encoding in face_encodings:
                # See if the face is a match for the known face(s)
                matches = face_recognition.compare_faces(known_face_encodings, face_encoding)

            name="Unknown"
    
             # If a match was found in known_face_encodings, just use the first one.
            if True in matches:
                     first_match_index = matches.index(True)
                     name=known_face_names[first_match_index]
                      
            if name not in face_names:          
             
                face_names.append(name)
                print(face_names)
        
                with open("attendance.csv", "w") as f:
                    writer = csv.writer(f)
                    writer.writerow(face_names)
    
            # Display the results
            for (top, right, bottom, left), name in zip(face_locations, face_names):
            # Scale back up face locations since the frame we detected in was scaled to 1/4 size
                         top *= 4
                         right *= 4
                         bottom *= 4
                         left *= 4
    
            # Draw a box around the face
                         cv2.rectangle(frame, (left, top), (right, bottom), (0, 0, 255), 2)
    
            # Draw a label with a name below the face
                         cv2.rectangle(frame, (left, bottom - 35), (right, bottom), (0, 0, 255), cv2.FILLED)
                         font = cv2.FONT_HERSHEY_SIMPLEX
                         cv2.putText(frame,name, (left + 6, bottom - 6), font, 1.0, (0, 0, 0), 4)

            

    
            # Display the resulting image
            cv2.imshow('LIVE', frame)
           
            
    
    
            # Hit 'q' on the keyboard to quit!
            if cv2.waitKey(1) & 0xFF == ord('q'):
                        break





    video_capture.release()        
    cv2.destroyAllWindows()



lab1=tkinter.Label(window,text="AUTOMATED ATTENDANCE SYSTEM", font=("times new roman",25,),fg="black",bg="#9802fd",height=1)
lab1.pack(anchor=tkinter.CENTER, expand=True)

lab2=tkinter.Label(window,text="University of Sri Jayawardenapura"+"\n"+"Department Of Computer Science", font=("times new roman",22,),fg="black",bg="#9802fd",height=2)
lab2.pack(anchor=tkinter.CENTER, expand=True)

 # Load an image using OpenCV
cv_img = cv2.imread("background.jpg")
img=cv2.resize(cv_img,(0,0), fx=0.005, fy=0.005)

# Get the image dimensions (OpenCV stores image data as NumPy ndarray)
height, width, no_channels = img.shape


height, width, no_channels = cv_img.shape
# Create a canvas that can fit the above image
canvas = tkinter.Canvas(window, width = width, height = height)
canvas.pack()


photo = PIL.ImageTk.PhotoImage(image = PIL.Image.fromarray(cv_img))

# Add a PhotoImage to the Canvas
canvas.create_image(0, 0, image=photo, anchor=tkinter.NW)

start=tkinter.Button(window, text="mark your Attendance",font=("times new roman",22),bg="red",fg='white', width=20,command=function)
start.pack(anchor=tkinter.CENTER, expand=True)




# Run the window loop
window.mainloop()
