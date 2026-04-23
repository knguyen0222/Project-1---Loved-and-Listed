# Project 1 Loved & Listed

A full-stack personal inventory and resale web app built with Django and PostgreSQL.

## Live Demo
https://project-1-loved-and-listed-production.up.railway.app

## About
Loved & Listed is a personal wardrobe and inventory tracker with built-in resale features. Users can manage everything they own, list items for sale, track profits, and browse other users' shops.

## Features
- Browse public listings without an account
- Sign up and create your own personal inventory
- Add, edit, and delete items with photo uploads
- Filter items by category
- Mark items as Keeping, Listed, or Sold
- Track listing price, sold price, and profit
- Money dashboard showing total spent, earned, and listed value
- Public shop page for each user
- Browse all sellers page
- User profiles with display names and @usernames
- Login, logout, and signup

## Tech Stack
- **Backend:** Python, Django
- **Database:** PostgreSQL (Retool)
- **Image Storage:** Cloudinary
- **Deployment:** Railway
- **Frontend:** HTML, CSS (custom pink theme)

## Local Setup
1. Clone the repo
2. Install dependencies
3. Add your database credentials to `settings.py`
4. Run migrations
5. Start the server

## Reflection
  When I started this project, my goal was to convert my existing Streamlit closet tracker into a professional Django web app. My Streamlit app was functional but limited. For starters, it had no login system, no real design, and it wasn't something I could realistically show to anyone outside of class. I wanted to build something that actually looked and worked like a real product.
  I started creating a Django project with Claude's help, connecting it to my existing PostgreSQL database, and converting my Streamlit models into Django models. From there, I added user authentication so each person could have their own private inventory, then image uploads through Cloudinary, then a money dashboard to track spending and resale profits, then public shop profiles so other users could browse your listed items, and finally a browse page that acts as the public homepage of the app. These ideas gradually came to me as I was building my app.
  The hardest part was the deployment. I tried PythonAnywhere first but ran into issues with external database connections on the free plan. It cost $10 a month to deploy, so I ended up switching to Railway which solved everything and the app deployed smoothly. I also ran into several smaller issues too, like Django's logout requiring a POST request instead of a GET, template syntax errors, and redirect issues after switching the home URL to the browse page. Each bug taught me something new about how Django works.
  What surprised me most was how far the project evolved from my original plan. I went in thinking I'd just rebuild what I had in Streamlit with a nicer interface. Instead I ended up building something much closer to a real marketplace app. I included user accounts, public profiles, image uploads, and financial tracking. Features I never planned for ended up being the most interesting and fun parts of the project.
  If I had more time I would add a search bar so users could search across all listings, a messaging feature so buyers could contact sellers directly, and a way to mark items as sold directly from the public profile page. I'd also clean up the mobile experience since the app was designed primarily for desktop. When testing the app on my phone, it was not nearly as organized as I’d like it compared to the desktop.
  Overall, this project gave me hands-on experience with Django, PostgreSQL, Cloudinary, Railway, and GitHub. It's something I'm very proud of and plan to keep building on after the class ends. Hopefully, I can build an app that allows Gonzaga students to buy and sell products and furniture through a similar platform.


## Author
Khanh Nguyen
