# MKAD distance API
## _Simple implementation, but does the job_



[![Build Status](https://travis-ci.org/joemccann/dillinger.svg?branch=master)](https://travis-ci.org/joemccann/dillinger)

MKAD distance API gives you the distance between the address 
 passed to the application in an HTTP request and the Moscow Ring Road (also known as MKAD). 
The information of the address is obtained by using the Yandex Geocode API.




## Dependency

The API is works with the following libraries

- [Flask] - Micro web framework written in Python
- [numpy] - Python library used for working with arrays
- [shapely] - Python package for manipulation and analysis of planar geometric objects
- [pytest] -  Testing tool that helps you write better programs.
- [requests] - a simple, yet elegant, HTTP library.




## Installation

MKAD API requires [Python](https://nodejs.org/) 3.8 or above to run.

Install the dependencies that are the in the requirement file

```sh
cd MoscowRingRoad
pip install requirements.txt
```



## Docker

MKAD API is very easy to install and deploy in a Docker container.

By default, the Docker will expose port 8080, so change this within the
Dockerfile if necessary. In my case I had to modify the port number by getting it from 
the environment variable in Heroku

````python
from flask import Flask
import os    

app = Flask(__name__)

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
````



```shell
$ docker build -t <your username>/flask-docker .

$ docker run -it -p 2000:5000 <your username>/flask-docker
```

I deploy the application to Heroku. If you want to use the same platform create your account and excecute the following commands. Deploying in heroku is pretty straightforward.

```sh
$ heroku login

$ heroku create <app-name>

$ heroku container:push web --app <app-name>

$ heroku container:release web --app <app-name>
```
If you want to access to the logs file of the Docker container use the following command.
````shell
$ heroku run bash
````

## How it works?
![Earth great circle](https://i.imgur.com/iD3X3Ax.png)

The first problem was how to measure the distance between two coordinates points.
So I thought to use euclidean distance but that will make no sense because I'm not flat-Earther, so I searched for a more viable solution. After some research I found the haversine formula gives great-circle distances between two points on a sphere from their longitudes and latitudes. The sphere in this case is the surface of the Earth.


![Earth great circle](https://i2.wp.com/macalupu.com/wp-content/uploads/2019/03/haversineFormula.png?w=878&ssl=1)

The next step was to determine if the coordinate location address is inside the Moscow Ring Road. 
My first approach to tackle this challenge was to take advantage of the metadata data that Yandex API returns. And compare the list of all the districts that are inside the MKAD with the district of the address.
But I found another approach. The idea was to get all the coordinate points that surround the region to see it as a polygon and then apply an algorithm to identify if the point is inside of it

![Test Image 2](images/mkad_map.png?raw=true)


I used the website https://www.findlatitudeandlongitude.com/ to get the coordinates points and to make the work of saving the points quicker I created a Javascript function that store coordinates
in a list after pressing the button "A" and if you have miss clicked you can erase the last data saved by pressing "D". To make it works you only need to open the dev tools and paste it in the console to make it work. Dont worry it doesnt do anything else than extracting and saving points.
````js

let points = []
document.addEventListener('keyup', (e) => {
  
    if (e.code === "KeyA"){
        let longitude = document.getElementsByClassName("text coordinate")[1].value;
        let latitude = document.getElementsByClassName("text coordinate")[0].value;
        console.log(`Inserted: ${latitude},${longitude}`)
        points.push([longitude, latitude]);
    }else if (e.code === "KeyD"){
        let temp = points.pop();
        console.log(`Deleted: ${temp[0]},${temp[1]}`)
    }
  });
````
## DEMO

If you want to test this api you can try by using this link and replacing the address parameter a location name

https://hendrikneuro.herokuapp.com/distance/**Address**

## License

MIT

**Free Software, holly **

[//]: # (These are reference links used in the body of this note and get stripped out when the markdown processor does its job. There is no need to format nicely because it shouldn't be seen. Thanks SO - http://stackoverflow.com/questions/4823468/store-comments-in-markdown-syntax)

   [Flask]: <https://github.com/pallets/flask>
   [numpy]: <https://github.com/numpy/numpy>
   [shapely]: <https://github.com/Toblerity/Shapely>
   [pytest]: <https://github.com/pytest-dev/pytest>
   [requests]: <https://github.com/psf/requests>
   [python]: <>
   [PlDb]: <https://github.com/joemccann/dillinger/tree/master/plugins/dropbox/README.md>
   [PlGh]: <https://github.com/joemccann/dillinger/tree/master/plugins/github/README.md>
   [PlGd]: <https://github.com/joemccann/dillinger/tree/master/plugins/googledrive/README.md>
   [PlOd]: <https://github.com/joemccann/dillinger/tree/master/plugins/onedrive/README.md>
   [PlMe]: <https://github.com/joemccann/dillinger/tree/master/plugins/medium/README.md>
   [PlGa]: <https://github.com/RahulHP/dillinger/blob/master/plugins/googleanalytics/README.md>
