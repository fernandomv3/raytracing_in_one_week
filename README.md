# raytracing_in_one_week
Python code for Peter Shirley's book

##Structure

Every chapter in the book has a directory with the code that generates the final image of that chapter, chapter0 was excluded because it didn't had any code or images.

##Notes
The code was written while learning raytracing from the book, even if I tried to make the code efficent or "pythonic", there's still room for improvement so feel free to submit pull requests.

The code was written in python3, it is not compatible with python2

Since I tried to use pure pyhton3 and the standart library (No external libraries), the code outputs the image in ppm format directly to standart input, be sure to redirect stdout to a file in your console e.g 
```bash
~$ python3 raytracer.py > image.ppm
```

Another thing to be aware of is that this raytracer is really slow.
