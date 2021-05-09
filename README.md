# Flask tutorial

[The Flask Mega Tutorial](https://blog.miguelgrinberg.com/post/the-flask-mega-tutorial-part-i-hello-world) series.

## How to build and run the application

```bash
export APP_VERSION=0.0.1
docker build . -t flask-tutorial:${APP_VERSION}
docker run  -p 5000:5000 flask-tutorial:${APP_VERSION}
```
