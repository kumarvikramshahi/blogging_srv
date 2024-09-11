# Blogging service
A Service that allows user to do blogging.

### Quick Start
```
git clone https://github.com/kumarvikramshahi/blogging_srv.git
```
```
cd blogging_srv
```
#### Docker-compose
Go to root folder of project, there you'll se `docker-compose.yaml` file.
Run below cmd and wait for few seaconds.
```
docker-compose up -d
```
#### Minikube
Go to root folder of project, there you'll se `kubernetes` folder.
Make sure minikube and minikube tunnel is running.
* create configmap from `env/dev.env` file
```
kubectl create configmap dev-env --from-env-file=../env/dev.env
```
* start resources
```
kubectl apply -k kubernetes/
```

<details>
<summary>Local enviroment - for development </summary>

#### For development purpose only
Make sure you have python>=v3.9.6 installed

* Create python virtual enviroment
```
python3 -m venv venv
```
* Activate virtual enviroment
```
source venv/bin/activate
```
* Install dependencies
```
pip install -r requirement.txt --no-cache-dir
```
* Go to decker-compose.yaml file and comment out `blogging-srv` section.
* Start docker-compose
```
docker-compose up -d
```
* creatte `.env` file in root folder
* Add these below lines in `.env` files.
```
ENV_NAME=dev

KAFKA_BROKER=localhost:9092
BLOGGING_TOPIC_NAME=blogging_srv

MONGODB_USER=
MONGODB_PASSWORD=
MONGODB_HOST=
MONGODB_NAME=blogging_qa

ELASTIC_PASSWORD=
ELASTIC_USER=
ELASTIC_HOST=http://localhost:9200

SELF_HOST=http://localhost:3000
```
* Now start fast api server on port 3000
```
uvicorn main:app --reload --port 3000
```

</details>

### Service have two endpoints for client:
Use below for domain:
* `localhost:3000` = When running as docker-compose or local enviroment way.
* `localhost:80`   = When running in Minikube cluster

#### ``GET`` -  `blogging/v1/health` 
Health API
```
curl --location 'localhost:80/blogging/v1/health'
```

#### ``POST`` - `/blogging/v1/add_blog`  
For adding blog. It may take few seconds to upload blog as it is saved asyncronously.
```
curl --location 'localhost:3000/blogging/v1/add_blog' \
--header 'Content-Type: application/json' \
--data '{
    "blog_title": "How to build website",
    "blog_text": "main blog",
    "user_id": "user-id"
}'
```
Example request:
```
{
    "blog_title": "How to build website",
    "blog_text": "main blog",
    "user_id": "user-id"
}
```
Example response:
```
{
    "data": {
        "message": "Blog added"
    }
}
```

#### ``GET`` - `/blogging/v1/search_blog`
For searching blog by passing query body.
```
curl --location --request GET 'localhost:3000/blogging/v1/search_blog' \
--header 'Content-Type: application/json' \
--data '{
    "query": {
        "wildcard": {
            "blog_title": "How to*"
        }
    }
}'
```
Example request:
```
{
    "query": {
        "wildcard": {
            "blog_title": "How to*"
        }
    }
}
```
Example response:
```
{
    "data": [
        {
            "id": "bDd34pEBSPTrjg_2fo2S",
            "score": 1.0,
            "data": {
                "blog_title": "How to build website",
                "blog_text": "main blog",
                "author": "user-name",
                "length": 9,
                "created_at": 1726081367290,
                "updated_at": 1726081367290
            }
        }
    ]
}
```