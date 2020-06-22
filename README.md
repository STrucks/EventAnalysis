#EventAnalyse
This project is supposed to crawl news from a social platform
and analyse/classify historical events (such as the death of XY).
It will look at the headlines of posts, and with the help of basic 
NLP, it should be able to extract information from the headlines.

### Ideas:
- given a time window, find the most relevant Persons and plot them in
a simple histogram

### Configuration:
TBA

### Setup:
TBA

#### Start the MongoDb as a Docker container:
- install Docker
- pull the MongoDB image (docker pull mongo), I used version 4.2.7
- `docker run -d -p 27017-27019:27017-27019 --name mongodb --restart unless-stopped -v /home/ubuntu/data:/data/db mongo`
 
