# geocode

Run this file to get the latitude and longitude of the address that you put in the 
address variable

# docker_build

This file is used to build the container to execute the geocode file

# requirements.txt

# Running geocode

create a folder called geocode and put the geocode file and the docker file into 
the directory put the geocode, the docker_build, and the requirements.txt files
into that directory

Open up GitBash and run the command below

	docker build -f docker_build.txt -t proj:geoacc  .
	
Then run the following command
	
	docker run proj:geoacct

You should have the latitude, longitude, and state printed out

# Loading GIS data

Run the Shapefile.py file to create the table

Then open the PostGIS shapefile and dbf loader

Once its open select add file and choose the shp file to load into the database
