# FaceRecognitionAPI
**A Django OpenCV wrapper that acts as a RESTful API for face recognition**
## Dependencies

Make sure you have all the dependencies installed before running the API server. This project is dependent on:
- Python3 (`brew install python3`)
- OpenCV3 (`brew install opencv3 --with-contrib --with-python3 --without-python`) built with [extra modules](https://github.com/opencv/opencv_contrib)
- Django (`pip install django`)
- PIL (`pip install Pillow`)

If you encounter any problems installing OpenCV3 with Python3, consult [this StackOverflow answer](https://stackoverflow.com/questions/32420853/homebrew-installation-of-opencv-3-0-not-linking-to-python).

## Installation
Download or clone the project and execute  
`python manage.py migrate`  
Once migrations finish executing, run the project using  
`python manage.py runserver`  

## Usage

### Requests
You can use the API by making a `GET` request to the following endpoints:

| Endpoint     | Description    |
| ------------- |:-------------:|
| `/new`   | Used to add a user profile before training |
| `/train`   | Used to add a known photo to a user profile and use it to identify the user later |
| `/recognize`   | Given a photo, recognize the user in the photo |
| `/users`   | Lists all registered users |



#### `/new`

Creates a new user profile and prepares an internal folder to host all photos of this user's face.

#### `/recognize`

Recognizes a user based on a provided photo. Call should provide exactly one of the following parameters.


| Parameter     | Description    | Type  |
| ------------- |:-------------:| -----:|
| imageBase64   | Base64 encoded photo of the user to be recognized | string (Base64 encoded) |
| url      | URL to the photo of the user to be recognized      |   string (Valid URL) |


**Example:**

Example Request:

```javascript
GET localhost:8000/recognize/?url=http://..
```

Example Response:

```javascript
{
  "detected": true,
  "identity": 1,
  "user": {
    "first_name": "John",
    "last_name": "Appleseed",
    "username": "appleseedj",
    "email": "appleseedj@gmail.com",
    "id": 1
  },
  "box": [[246, 104, 948, 806]],
  "smiling": true
}
```

#### `/train`

Trains a registered user's model using a given photo of the user. The image is cropped, saved and used in the model on the next restart of the API server.

#### `/users`

Lists all users currently registered.


Take a look at the [MirrorOS Project](https://github.com/wassgha/MirrorOS) for an example of usage of the API.
