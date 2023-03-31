# py-project_starry_music_bar

Django project for a website of a "Starry" music-bar.


## Features

* Authentication fuctionality for Visitor/User.
* Managing Positions, Genres, Musicians, Rockbands, Events, Visitors, directly from the site interface for admin-user.
* Powerful admin panel for advanced managing


## Instalation

pyton 3.11 must be already installed

```shell
gti clone https://github.com/DmytryTong/Starry_project
cd Starry_project
python3 - venv venv
source venv/bin/activate
python manage.py runserver
```

## Project description
```
    On this website you can learn about events that take place in a "Starry"
music-bar, about bands, that take part in that events, and about the musicians
that perform in that bands. If you would like - you can login/register on 
website and choose the event you like. You can add any event in a events list 
to your "want to go" list in your private cabinet by pressing "I want to go!"
button on a event-detail page. You can refuse to go by pressing "I don't want 
to go" button on the same page. If you are administration of a site, you can 
also add, delete, update events, bands, positions, genres pages according to 
your needs.
```
## Database overlook:
```
     In this project models: Position, Genre, Musician, Rockband, Event,
 Visitor(User) were implemented. 
     Position has a "name" field, that describes position of a musician, 
 for example "drummer", bass, etc.
      Genre has a "name" field, that is a name of a genre (metal, j-rock, 
 etc.), a "description" field which contain description of a genre.
      Musician has a "first_name" field, that is a first name of a musician, 
 a "last_name" field, that is a last name of a musician, a "position" field
 which contain musician's position in a band.
      Rockband has a "band_name" field, that is a band's name, a "genres" 
 field, that contain a genre this band represents, a "musicians" field 
 which contain musicians which perform in a band.
      Event has a "name" field, that is a event's name, a "show_time" field,
 that contain a time, when event will take place, a "bands" field which 
 contain bands which perform during event, a "visitors" field thas contains
 all visitors, that want to attend event.
      Visitor - standard Django user model.
      Position connected to Musician as Many-to-Many, Rockband connected to 
 Genre as Many-to-One, Rockband connected to Musician as Many-to-Many, 
 Event connected to Rockband as Many-to-Many, Event connected to Visitor as 
 Many-to-Many.
```

## Demo

[Wibsite interface](Demo.png)
