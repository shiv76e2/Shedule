# Set base image (host OS)
FROM python:3.8.10

# By default, listen on port 5000
EXPOSE 5000/tcp

# Set the working directory in the container
WORKDIR /app

# Copy the dependencies file to the working directory
COPY requirements.txt .
 
# Install any dependencies
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

# Copy the content of the local src directory to the working directory
COPY app.py .
COPY uwsgi.ini .
ADD flaskblog ./flaskblog



#uwsgi --plugin python --wsgi-file app.py --callable app -H ../../venv

#docker run -p 5000:5000 schedule-container --host 0.0.0.0
#docker exec -it schedule bash
#docker exec -it schedule bash




#docker run --name sd -it -p 5000:5000 schedule-container
#exit()
#restart
#docker exec -it sd bash
#uwsgi --ini uwsgi.ini


#Lightsailデプロイ
#docker build -t schedule-container .
#aws lightsail push-container-image --service-name flask-service --label schedule-container --image schedule-container
