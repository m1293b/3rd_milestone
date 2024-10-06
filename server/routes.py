from server import app, db
from server.models import Users, Recipes
from flask import render_template, request, flash, redirect, url_for, session
from flask_sqlalchemy import SQLAlchemy

## route for Main page, no login required

@app.route('/')
def index_page():
    top_starter = Recipes.query.filter_by(course = "starter").order_by(Recipes.recipe_id.desc()).first()
    top_main = Recipes.query.filter_by(course = "main").order_by(Recipes.recipe_id.desc()).first()
    top_dessert = Recipes.query.filter_by(course = "dessert").order_by(Recipes.recipe_id.desc()).first()
    top_kids_meal = Recipes.query.filter_by(course = "kids_meal").order_by(Recipes.recipe_id.desc()).first()
    session['prev_url'] = 'index_page'
    # updates = Updates.query.all()
    return render_template("index.html", page_title = 'Main page', top_starter = top_starter, top_main = top_main, top_dessert = top_dessert, top_kids_meal = top_kids_meal, prev_page = session['prev_url']) #updates = updates)

current_users = {}

## route for Recipes page, no login required

@app.route('/recipes')
def recipes_page():
    starters = Recipes.query.filter_by(course = "starter").order_by(Recipes.recipe_id.desc()).limit(4)
    mains = Recipes.query.filter_by(course = "main").order_by(Recipes.recipe_id.desc()).limit(4)
    desserts = Recipes.query.filter_by(course = "dessert").order_by(Recipes.recipe_id.desc()).limit(4)
    kids_meals = Recipes.query.filter_by(course = "kids_meal").order_by(Recipes.recipe_id.desc()).limit(4)
    session['prev_url'] = 'recipes_page'
    return render_template("recipes.html", page_title = 'Recipes page', starters = starters, mains = mains, desserts = desserts, kids_meals = kids_meals, prev_page = session['prev_url'])

## route for About page, no login required

@app.route('/about')
def about_page():
    return render_template("about.html", page_title = 'About page')

## route for Sign in page, no login required

@app.route('/sign_in')
def sign_in_page():
    return render_template("sign_in.html", page_title = 'Sign in page')

## route for Sign up page, no login required

@app.route('/sign_up')
def sign_up_page():
    return render_template("sign_up.html", page_title = 'Sign up page')

## route for Home page, login required

@app.route('/home')
def home_page():
    return render_template("home.html", page_title = 'Home page')

# View logged in user's recipes

@app.route('/my_recipes')
def my_recipes_page():
    starters = Recipes.query.filter_by(course = "starter", user_id = session['user_id']).all()
    mains = Recipes.query.filter_by(course = "main", user_id = session['user_id']).all()
    desserts = Recipes.query.filter_by(course = "dessert", user_id = session['user_id']).all()
    kids_meals = Recipes.query.filter_by(course = "kids_meal", user_id = session['user_id']).order_by(Recipes.recipe_id.desc()).limit(4)
    session['prev_url'] = 'my_recipes_page'
    return render_template("my_recipes.html", page_title = 'My Recipes page', starters = starters, mains = mains, desserts = desserts, kids_meals = kids_meals, prev_page = session['prev_url'])

@app.route('/new_recipe')
def add_new_recipe_page():
    return render_template("add_new_recipe.html", page_title = 'Adding a recipe')

# View selected recipe

@app.route('/view_recipe', methods=["POST"])
def view_recipe():
    session['current_recipe'] = request.form['selected_recipe']
    current_recipe = Recipes.query.filter_by(recipe_id = session['current_recipe']).first()
    return render_template("view_recipe.html", page_title = 'View recipe', current_recipe = current_recipe)

# List all recipe

@app.route('/all_recipes', methods=["POST"])
def all_recipes():
    session['current_course'] = request.form['selected_course']
    current_recipes = Recipes.query.filter_by(course = session['current_course']).all()
    course = session['current_course'] + "s"
    return render_template("all_recipes.html", page_title = 'All recipe', current_recipes = current_recipes, course = current_recipes[0].course.capitalize() + "s", course_class = current_recipes[0].course + "s", course_path = f"{{url_for('../assets/{course}.jpg')}}")

# Edit selected recipe

@app.route('/edit_recipe', methods=["POST"])
def edit_recipe():
    session['current_recipe'] = request.form['selected_recipe']
    current_recipe = Recipes.query.filter_by(recipe_id = session['current_recipe']).first()
    return render_template("edit_recipe.html", page_title = 'Edit recipe', current_recipe = current_recipe)

# Delete selected recipe

@app.route('/delete_recipe', methods=["POST"])
def delete_recipe():
    session['current_recipe'] = request.form['selected_recipe']
    current_recipe = Recipes.query.filter_by(recipe_id = session['current_recipe']).first()
    flash(f'{current_recipe.recipe_name} has been successfully deleted.')
    db.session.delete(current_recipe)
    db.session.commit()
    return redirect(url_for('my_recipes_page'))

# Update selected recipe

@app.route('/update_recipe', methods=["POST"])
def update_recipe():
    session['current_recipe'] = request.form['selected_recipe']
    current_recipe = Recipes.query.filter_by(recipe_id = session['current_recipe']).first()
    current_recipe.recipe_name = request.form['recipe_name'] if current_recipe.recipe_name!=request.form['recipe_name'] else current_recipe.recipe_name
    current_recipe.course = request.form['course']
    current_recipe.ingredients = request.form['ingredients']
    current_recipe.instructions = request.form['instructions']
    current_recipe.vegetarian = request.form['vegetarian'] if request.form.get('vegetarian') else 'no'
    current_recipe.gluten_free = request.form['gluten_free'] if request.form.get('gluten_free') else 'no'
    current_recipe.nut_free = request.form['nut_free'] if request.form.get('nut_free') else 'no'
    current_recipe.shellfish_free = request.form['shellfish_free'] if request.form.get('shellfish_free') else 'no'
    db.session.commit()
    flash(f'"{current_recipe.recipe_name}" has been updated.')
    return render_template("edit_recipe.html", page_title = 'Update recipe', current_recipe = current_recipe)

## route to take user to their profile page where they will be able to edit their details

@app.route('/my_profile')
def my_profile_page():
    return render_template("my_profile.html", page_title = 'My Profile page')

## route to take user to Events page

@app.route('/events')
def events_page():
    return render_template("events.html", page_title = 'Events page')

## route to log user in, data to be verified is pulled from input fields

@app.route('/login', methods=["POST"])
def login():
    username = request.form['username']
    password = request.form['password']
    user = Users.query.filter_by(username = username).first()
    if user and user.check_password(password):
        session['username'] = username
        session['user_id'] = user.user_id
        return redirect(url_for('home_page'))
    else:
        flash('User does not exist or wrong password was used.')
        return render_template('sign_in.html')

## route to log user out from session

@app.route('/logout', methods=["GET", "POST"])
def logout():
    session.pop('username')
    session.pop('user_id')
    flash('You have been logged out.')
    return redirect(url_for('sign_in_page'))


## route to register an account, data is pulled from input fields

@app.route('/register', methods=["POST"])
def register():    
    username = request.form['username']
    password = request.form['password']
    email_address = request.form['email_address']
    user = Users.query.filter_by(username = username).first()
    if user:
        flash("User already exists.")
        return render_template('sign_up.html', error="User already exists")
    else:
        new_user = Users()
        new_user.username = username
        new_user.set_password(password)
        new_user.email_address = email_address
        new_user.points = 0
        new_user.liked_recipes = []
        db.session.add(new_user)
        db.session.commit()
        user = Users.query.filter_by(username = username).first()
        session['username'] = username
        session['user_id'] = user.user_id
        return redirect(url_for('home_page'))  

## route to add a new recipe, data is pulled from input fields
    
@app.route('/adding_new_recipe', methods=["POST"])
def adding_new_recipe():    
    recipe_name = request.form['recipe_name']
    course = request.form['course']
    ingredients = request.form['ingredients']
    instructions = request.form['instructions']
    vegetarian = request.form['vegetarian'] if request.form.get('vegetarian') else 'no'
    gluten_free = request.form['gluten_free'] if request.form.get('gluten_free') else 'no'
    nut_free = request.form['nut_free'] if request.form.get('nut_free') else 'no'
    shellfish_free = request.form['shellfish_free'] if request.form.get('shellfish_free') else 'no'
    recipe = Recipes.query.filter_by(recipe_name = recipe_name).first()
    if recipe:
        flash("Recipe already exists")
        return render_template('add_new_recipe.html', error="Recipe already exists")
    else:
        user = Users.query.filter_by(user_id = session['user_id']).first()
        new_recipe = Recipes()
        new_recipe.recipe_name = recipe_name
        new_recipe.course = course
        new_recipe.users = user
        new_recipe.ingredients = ingredients
        new_recipe.instructions = instructions
        new_recipe.vegetarian = vegetarian
        new_recipe.gluten_free = gluten_free
        new_recipe.nut_free = nut_free
        new_recipe.shellfish_free = shellfish_free
        db.session.add(new_recipe)
        db.session.commit()
        user = Users.query.filter_by(user_id = session['user_id']).first()
        flash(f'{recipe_name} has been added to your collection')
        return redirect(url_for('my_recipes_page'))