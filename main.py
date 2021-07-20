# Name: Rick Schoenmaker
# Date: 20/07/2021

from flask import Flask, render_template, request
from DBconnection import search_value, search_vin, getall, insert_db, delete_from_db

app = Flask(__name__)

# A list of all types of vehicles that can be present in this tool.
types = ['Car', 'Truck', 'Motorcycle']

# calls a function to get all vehicle Makes present in the database.
extract_all_makes = getall("Make")

# a list containing one value.
listone = ["one"]

# a empty string for use in function.
option = ""

@app.route('/')
# Define index() function provides user with the home screen.
def index():
    return render_template('index.html')


@app.route('/search_db', methods=['GET', 'POST'])
# Define search_db() function to provide the user an interface to search for values in the mongodb database.
def search_db():
    # Check if something is posted to the page.
    if request.method == 'POST':
# Get vehicles by Type
        try:
            # Check if the Type provided is accepted in our application
            if types.__contains__(request.form['TYPE']):
                vehicle_type = request.form["TYPE"]
                result = search_value("Type", str(vehicle_type))
                listtest = [result]

                # Return statement that gives a result page and visualizes the found results for that vehicles type
                return render_template("result_type.html",
                                       listtest=listtest)
            else:
                print("No type provided")
        except:
                print("No type provided")

# Get vehicles by Make
        try:
            # Check if the vehicle make is present in the database
            if extract_all_makes.__contains__(request.form['MAKE']):
                vehicle_make = request.form["MAKE"]
                result = search_value("Make", str(vehicle_make))
                listtest = [result]

                # Return statement that gives a result page and visualizes the found results for that vehicles Make
                return render_template("result_make.html",
                                       listtest=listtest)
            # If statement that returns a error page if a invalid make is provided.
            if TypeError:
                return render_template("error.html")
            else:
                pass
        except :
            print("no make provided")

#Get vehicle by VIN ID
        try:
            extract_all_ids = getall("_id")
            # Check if the vehicle VIN is present in the database
            if extract_all_ids.__contains__(int(request.form['VIN'])):
                vehicle_id = request.form["VIN"]
                print(vehicle_id)
                result = search_vin("_id", int(vehicle_id))
                print(result)
                listtest = [result]

                # Return statement that gives a result page and visualizes the found results for that vehicles VIN
                return render_template("result_vin.html",
                                       listtest=listtest)

            # If statement that returns a error page if a invalid make is provided.
            if TypeError:
                return render_template("error.html")
            else:
                pass
        except TypeError as e:
            print(e)
            return render_template("error.html")
    else:
        return render_template("retrieve_information.html")

@app.route('/fill_db', methods=['GET','POST'])
# Define fill_db() function to provide the user an interface to add values from the mongodb database.
def fill_db():
    # Check if something is posted to the page.
    if request.method == 'POST':
        try:
            # Obtain the posted values using request.form
            vehicle_type = request.form['TYPE']
            vehicle_make = request.form['MAKE']
            vehicle_model = request.form['MODEL']
            vehicle_year = request.form['YEAR']
            vehicle_seat = request.form['SEAT']

            # Check which Type of vehicle was provided so only vehicle specific options will be saved to the database
            if request.form['TYPE'] == 'Car':
                vehicle_option = bool(request.form['ROOF'])
                option = "Roof rack availability:"

            else:
                pass
            if request.form['TYPE'] == 'Truck':
                vehicle_option = int(request.form['HAUL'])
                option = "Haul capacity(KG):"

            else:
                pass

            if request.form['TYPE'] == 'Motorcycle':
                vehicle_option = bool(request.form['SIDE'])
                option = "Sidecar capability:"
            else:
                pass
            # Get all present vehicle ids in the database.
            extract_all_ids = getall("_id")
            # Create a dictionary with all obtained vehicle values.
            input_dict = {"_id": int(len(extract_all_ids))+1, "Type": str(vehicle_type), "Make": str(vehicle_make), "Model": str(vehicle_model),
                          "Year": int(vehicle_year), "Seat capacity": int(vehicle_seat), str(option): vehicle_option}

            # Call insert_db function to add the created dictionary to the database
            insert_db(input_dict)
        except:
            return print("Error in fill_db")

    else:
        return render_template("filldb.html")

    return render_template("result_filldb.html",
                                       listone=listone,
                                       vehicle_type=vehicle_type,
                                       vehicle_make=vehicle_make,
                                       vehicle_model=vehicle_model,
                                       vehicle_year=vehicle_year,
                                       vehicle_seat=vehicle_seat,
                                       vehicle_option=vehicle_option,
                                       option=option)


@app.route('/delete', methods=['GET', 'POST'])
# Define delete() function to provide the user an interface to delete values from the mongodb database.
def delete():
    # Check if something is posted to the page.
    if request.method == 'POST':
        try:
            # Obtain the posted values using request.form.
            vehicle_id = request.form['ID']
            # Call function getall to get all VIN ids present in the database.
            extract_all_ids = getall("_id")
            # Check if provided VIN id is present in the database.
            if extract_all_ids.__contains__(int(request.form['ID'])):
                # Delete provided value from the database
                delete_from_db(int(vehicle_id))

            else:
                return render_template("error_vin.html")

        except:
            return print("Error in delete function")

    else:
        return render_template("delete.html")

    return render_template("result_delete.html",
                                       listone=listone,
                                       vehicle_id=vehicle_id)
if __name__ == "__main__":
    app.run(debug=True)


