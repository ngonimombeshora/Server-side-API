<h1 align="center">
Smart home hub server-side API
</h1>

## 🚀 Getting Started

API is dockerised. Getting it to run locally requires only three commands...

1. **Clone the repo**

```sh
git clone https://github.com/ngonimombeshora/Server-side-API
```

2. **Build the docker image.**

Navigate into your new site's directory and use the cli to start it up.

```sh
cd hub-API
docker-compose build
```

3. **Run the container and start developing.**

```sh
docker-compose up
```

🌟 API can now be accessed and used at http://0.0.0.0:8000/

## 🤔 Usage

The documentation endpoint provides useful insight on how to use the API, available endpoints,
and you can even test it out with some requests and check the responses received. This is found at
http://0.0.0.0:8000/documentation/

## 🤔 No docker?

The submodule hubAPI can be fount at https://github.com/ngonimombeshora/hubAPI for usage without docker. Simply run the command below.

```sh
python3 manage.py runserver
```

🌟 Available at http://127.0.0.1:8000/
