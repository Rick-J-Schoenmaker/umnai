from flask import Flask, render_template, request
from DBconnection import search_value, search_vin, getall, insert_db, delete_from_db

app = Flask(__name__)

types = ['Car', 'Truck', 'Motorcycle']
extract_all_makes = getall("Make")
listone = ["one"]
option = ""

@app.route('/')
def index():
    return render_template('index.html')


@app.route('/search_db', methods=['GET', 'POST'])
def search_db():
    if request.method == 'POST':
#get vehicles by Type
        try:
            if types.__contains__(request.form['TYPE']):
                vehicle_type = request.form["TYPE"]
                result = search_value("Type", str(vehicle_type))
                listtest = [result]
                return render_template("result_type.html",
                                       listtest=listtest)
            else:
                print("No type provided")
        except:
                print("No type provided")

# Get vehicles by Make
        try:
            if extract_all_makes.__contains__(request.form['MAKE']):
                vehicle_make = request.form["MAKE"]
                result = search_value("Make", str(vehicle_make))
                listtest = [result]
                return render_template("result_make.html",
                                       listtest=listtest)
            if TypeError:
                return render_template("error.html")
            else:
                pass
        except :
            print("no make provided")

#Get vehicle by VIN ID
        try:
            extract_all_ids = getall("_id")
            if extract_all_ids.__contains__(int(request.form['VIN'])):
                vehicle_id = request.form["VIN"]
                print(vehicle_id)
                result = search_vin("_id", int(vehicle_id))
                print(result)
                listtest = [result]
                return render_template("result_vin.html",
                                       listtest=listtest)
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
def fill_db():
    if request.method == 'POST':
        try:
            vehicle_type = request.form['TYPE']
            vehicle_make = request.form['MAKE']
            vehicle_model = request.form['MODEL']
            vehicle_year = request.form['YEAR']
            vehicle_seat = request.form['SEAT']
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
            extract_all_ids = getall("_id")
            input_dict = {"_id": int(len(extract_all_ids))+1, "Type": str(vehicle_type), "Make": str(vehicle_make), "Model": str(vehicle_model),
                          "Year": int(vehicle_year), "Seat capacity": int(vehicle_seat), str(option): vehicle_option}

            insert_db(input_dict)
            print(input_dict)

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
def delete():
    if request.method == 'POST':
        try:
            vehicle_id = request.form['ID']
            extract_all_ids = getall("_id")
            print(extract_all_ids)
            if extract_all_ids.__contains__(int(request.form['ID'])):
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


