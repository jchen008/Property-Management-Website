from flask import Flask, render_template, request, jsonify, redirect, url_for
import sqlite3 as sql

app = Flask(__name__)

@app.route("/")
def welcome():
	return "Welcome!"

@app.route("/task1")
def task1():
	return "Hello World!"

@app.route('/task2')
def task2():
   con = sql.connect("Database.db")
   con.row_factory = sql.Row
   
   cur1 = con.cursor()
   cur1.execute("select * from Property")
   Query1 = cur1.fetchall();

   cur2 = con.cursor()
   cur2.execute("select Count(*)as PropertyNum, SUM(MarketValue)as TotalMarketValue, SUM(Cost) as TotalCost, (SUM(MarketValue) - SUM(Cost)) as ProfitOrLoss from Property")
   Query2 = cur2.fetchall();

   return render_template("tabular.html", Query1 = Query1, Query2 = Query2)

@app.route('/task3_insert', methods=["POST"])
def task3_insert():
	data = request.form
	property = data['PropertyName']
	city = data['City']
	market_val = data['MarketValue']
	cost = data['Cost']
	print(data)
	print(property, city, market_val, cost)
	try:
		with sql.connect("database.db") as con:
			cur = con.cursor()
			cur.execute("INSERT INTO Property (PropertyName,City,MarketValue,Cost) VALUES (?,?,?,?)",(property,city,market_val,cost))
			con.commit()
	except:
	    con.rollback()
      
	finally:
		con.close()
		return redirect("http://localhost:5000/task2", code=200)
        

@app.route('/task3_delete', methods=["POST"])
def task3_delete():
	data = request.form
	property_id = data['PropertyID']
	print(data)
	print(property_id)
	try:
		with sql.connect("database.db") as con:
			cur = con.cursor()
			cur.execute("DELETE FROM Property WHERE PropertyID = ? ",(property_id))
			con.commit()
	except:
	    con.rollback()
      
	finally:
		con.close()
		return redirect("http://localhost:5000/task2", code=200)

# Edit Article
@app.route('/task3_edit/<string:id>', methods=['GET'])
def task3_edit(id):

	property_id = id
	print("id", id)
    # Create cursor
	con = sql.connect("Database.db")
	con.row_factory = sql.Row
	cur = con.cursor()
	cur.execute("SELECT * FROM Property WHERE PropertyID = ?", [property_id])
	Query1 = cur.fetchall();
	print(Query1)
	return render_template("edit.html", Query1 = Query1, id = property_id)


@app.route('/task3_edit_data', methods=['POST'])
def task3_edit_data():
	data = request.form
	id = data['PropertyID']
	name = data['PropertyName']
	city = data['City']
	market_val = data['MarketValue']
	cost = data['Cost']
	print(data)
	try:

		with sql.connect("database.db") as con:
			cur = con.cursor()
			cur.execute("UPDATE Property SET PropertyName=?,City=?,MarketValue=?,Cost=? WHERE PropertyID = ?",(name,city,market_val,cost,id))
			con.commit()
			print("commit successfully")
	except:
		print("commit error")
		IDcon.rollback()
      
	finally:
		con.close()
		print("begin redirect to homepage")
		return redirect("http://localhost:5000/task2", code=200)


if __name__ == '__main__':
   app.run()


