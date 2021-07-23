# MKAD distance API
## _Simple implementation, but does the job_



[![Build Status](https://travis-ci.org/joemccann/dillinger.svg?branch=master)](https://travis-ci.org/joemccann/dillinger)

MKAD distance API gives you the distance between the address you make the request and the Moscow Ring Road (also know as MKAD). The information of the address is obtain by using the Yandex Geocode API.




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

This will create the dillinger image and pull in the necessary dependencies.
Be sure to swap out `${package.json.version}` with the actual
version of Dillinger.

Once done, run the Docker image and map the port to whatever you wish on
your host. In this example, we simply map port 8000 of the host to
port 8080 of the Docker (or whatever port was exposed in the Dockerfile):


> Note: `--capt-add=SYS-ADMIN` is required for PDF rendering.

Verify the deployment by navigating to your server address in
your preferred browser.

```sh
$ heroku create <app-name>
$ heroku login
$ heroku container:push web --app <app-name>
$ heroku container:release web --app <app-name>

```
If you want to access to the logs of the Docker container use the following command.
````shell
$ heroku run bash
````

## How it works?
![Earth great circle](https://i.imgur.com/iD3X3Ax.png)

When I start working in the project divided the problem in two. The first problem was how to measure the distance between two coordinates points.
So I thought to use euclidean distance but that will make no sense because I'm not flat-Earther, so I searched for a more viable solution. After some research I found the haversine formula gives great-circle distances between two points on a sphere from their longitudes and latitudes. The sphere in this case is the surface of the Earth.


![Earth great circle](https://i2.wp.com/macalupu.com/wp-content/uploads/2019/03/haversineFormula.png?w=878&ssl=1)

The next step was to determine if the address that the user input to the API is inside the Moscow Ring Road. 
My first approach to tackle this challenge was to take advantage of the metadata data that Yandex API returns. And compare the list of all the districts that are inside the MKAD with the district of the address.
But I found another approach. The idea was to get all the coordinate points that surround the region to see it as a polygon and then apply an algorithm to identify if the point is inside of it






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
- Import a HTML file and watch it magically convert to Markdown
- Drag and drop images (requires your Dropbox account be linked)
- Import and save files from GitHub, Dropbox, Google Drive and One Drive
- Drag and drop markdown and HTML files into Dillinger
- Export documents as Markdown, HTML and PDF

Markdown is a lightweight markup language based on the formatting conventions
that people naturally use in email.
As [John Gruber] writes on the [Markdown site][df1]

> The overriding design goal for Markdown's
> formatting syntax is to make it as readable
> as possible. The idea is that a
> Markdown-formatted document should be
> publishable as-is, as plain text, without
> looking like it's been marked up with tags
> or formatting instructions.

This text you see here is *actually- written in Markdown! To get a feel
for Markdown's syntax, type some text into the left window and
watch the results in the right.


## Plugins

Dillinger is currently extended with the following plugins.
Instructions on how to use them in your own application are linked below.

| Plugin | README |
| ------ | ------ |
| Dropbox | [plugins/dropbox/README.md][PlDb] |
| GitHub | [plugins/github/README.md][PlGh] |
| Google Drive | [plugins/googledrive/README.md][PlGd] |
| OneDrive | [plugins/onedrive/README.md][PlOd] |
| Medium | [plugins/medium/README.md][PlMe] |
| Google Analytics | [plugins/googleanalytics/README.md][PlGa] |

## Development

Want to contribute? Great!

Dillinger uses Gulp + Webpack for fast developing.
Make a change in your file and instantaneously see your updates!

Open your favorite Terminal and run these commands.

First Tab:

```sh
node app
```

Second Tab:

```sh
gulp watch
```

(optional) Third:

```sh
karma test
```

#### Building for source

For production release:

```sh
gulp build --prod
```

Generating pre-built zip archives for distribution:

```sh
gulp build dist --prod
```

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
