# FaceRecognitionAPI
**A simple Django OpenCV wrapper as a RESTful API (features include face recognition, face detection and smile detection**

### Installation
Make sure OpenCV3 (`conda install -c menpo opencv3=3.1.0`), Django (`conda install django`) and PIL (`conda install PIL`) are installed. Download or clone the project and execute  
`python manage.py migrate`  
Once migrations finish executing, run the project using  
`python manage.py runserver`  

### Usage
You can use the API by making a `POST` request to `http://localhost:8000/recognize/`. You can either pass your image as
a URL (using a `url` field) or as a base64 encoded image (using the `imageBase64` field).

Take a look at the [MirrorOS Project](https://github.com/wassgha/MirrorOS) for an example of usage of the API.
