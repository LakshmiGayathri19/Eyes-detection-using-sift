# Eyes-detection-using-sift
This project explores the concept of Shift Invariant Feature Transform(SIFT). The detail explanation of SIFT is demonstrated in the following articles. 

* Part 1 - [Implementing SIFT in Python: A Complete Guide](https://medium.com/@russmislam/implementing-sift-in-python-a-complete-guide-part-1-306a99b50aa5)
* Part 2 - [Implementing SIFT in Python: A Complete Guide](https://medium.com/@russmislam/implementing-sift-in-python-a-complete-guide-part-2-c4350274be2b)

The main aim of this project is to identify the person by detecting the persons eyes using a template(here the template is eyes itself, as shown in picture below). The person face is taken as the input by capturing the video of the person's face and is matched against the person's eyes template. The main use case of this project is this application can be used in security or surveillence systems where the identity of the person is found using biometric identification. 

The eyes of the person which are to be matched are already stored in the file system and are matched against the real time face. If the eyes match, then a bounding box is drew around the eyes.

### Template of the eyes:
![alt text](https://github.com/LakshmiGayathri19/Eyes-detection-using-sift/blob/main/eyes.png)

### Person face whose eyes were detected:
![alt text](https://github.com/LakshmiGayathri19/Eyes-detection-using-sift/blob/main/Result.png)
 
---
### How to run the code:
* Create a virtual environment for the project - [link](https://www.google.com/url?sa=t&rct=j&q=&esrc=s&source=web&cd=&cad=rja&uact=8&ved=2ahUKEwj84bKm5Jj_AhXwlWoFHfqnBtUQFnoECA8QAQ&url=https%3A%2F%2Fdocs.python.org%2F3%2Flibrary%2Fvenv.html&usg=AOvVaw1SQ6VGTcJCX7W6wOs1SpnV)
* Install the required depedencies in your project virtual environment
    * Python3
    * Numpy
    * OpencCV - Python
* Copy the template image to your project directory where the main code sift.py is present.
* Run the sift.py by exueting the command `python sift.py`.
