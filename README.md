# InstaKart
InstaKart is a solution to the massive hassle of inefficient grocery shopping.
With a lost cost screen built right into your shopping cart and a mobile app, we'll let you know exactly what path makes
the most sense to pickup all your items. We also let you track your todo list straight on the cart!

## Table of Contents
- [How it Works](#how-it-works)
- [Materials Used](#materials-used)

## How it Works

### Front End 
A simple Apache Web Server hosts our web UI powered by HTML, CSS, JavaScript.
This front-end is designed specifically for our Raspberry Pi Display.
The front-end allows you to track your grocery list and cross things off of it. To the right of your list is a map
letting you know the best path to take in order to pickup all your items.

### Back End
Back end entirely powered by python. Using Raspberry Pi's library to interface with the hardware and image processing + pathing calculations entirely done by our python backend. We push data directly to our webserver through sftp to show to our users.
Calculating the most efficient path was a travelling salesman problem so we took the greedy approach.

## Materials Used
Raspberry Pi B+ with screen, button, and camera modules
Wood Panels + Metal Frame on wheels for prototype of cart
Lots and lots of Caffeine
