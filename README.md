GUIDELINES

In the backend folder, create a .env file and add the below line..

    MONGO_URI=mongodb+srv://<username>:<password>@cluster0.myrelgk.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0


Add your admin <username> and <password> for the db..
Above uri is an example of mongodb atlas uri, as i have used the same for my project..


Use the following commands:-

docker compose up

docker compose down

docker compose build

