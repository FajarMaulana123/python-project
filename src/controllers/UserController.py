import sys
from flask import render_template, redirect, url_for, request, abort, jsonify, flash
from flask_mysqldb import MySQL

from models.UserModel import User, countUser
from producer import publish

mysql = MySQL()

def index():
    return render_template('user.html')

def user_():
    if request.method == 'POST':
        draw = request.form['draw'] 
        row = int(request.form['start'])
        rowperpage = int(request.form['length'])
        searchValue = request.form["search[value]"]
        # print(draw)
        # print(row)
        # print(rowperpage)
        # print(searchValue)

        list_data = User(searchValue, row, rowperpage)
        allcount = countUser(searchValue, row, rowperpage)
        totalRecords = allcount['allcount']
        # print(totalRecords) 

        filtercount = countUser(searchValue, row, rowperpage)
        totalRecordsFilter = filtercount['allcount']
        # print(totalRecordsFilter) 

        data = []
        for row in list_data:
            
            aksi = '<div class="d-flex justify-content-center align-items-center"><div class="text-warning align-items-center text-decoration-none edit mr-1" data-id="'+str(row['id'])+'" data-nama="'+str(row['nama'])+'" data-email="'+str(row['email'])+'" data-nohp="'+str(row['nohp'])+'"  role="button"><i class="fa fa-pencil-alt mr-1"></i> Edit</div><div class="text-danger align-items-center delete" data-id="'+str(row['id'])+'" role="button" ><i class="fa fa-trash-alt mr-1"></i> Delete</div></div>'
            data.append({
                'id': row['id'],
                'nama': row['nama'],
                'email': row['email'],
                'nohp': row['nohp'],
                'aksi': aksi
            })
        # tot_user = countUser(searchValue, row, rowperpage)
        
        response = {
            'draw': draw,
            'recordsTotal': totalRecords,
            'recordsFiltered': totalRecordsFilter,
            'data': data,
        }
        return jsonify(response)

def createUser():
    if request.method == "POST":
        flash("Data Inserted Successfully")
        data = []
        nama = request.form['nama']
        email = request.form['email']
        nohp = request.form['nohp']
        data.extend([nama, email, nohp])
        cur = mysql.connection.cursor()
        cur.execute("INSERT INTO user (nama, email, nohp) VALUES (%s, %s, %s)", data)
        mysql.connection.commit()
        publish('users_created',data)
        r = {'result': True}
        return jsonify(r)

def updateUser():
    if request.method == 'POST':
        data = []
        id_data = request.form['hidden_id']
        nama = request.form['nama']
        email = request.form['email']
        nohp = request.form['nohp']
        data.extend([nama, email, nohp, id_data])
        cur = mysql.connection.cursor()
        cur.execute("""
               UPDATE user
               SET nama=%s, email=%s, nohp=%s
               WHERE id=%s
            """, data)
        flash("Data Updated Successfully")
        mysql.connection.commit()
        publish('users_updated',data)
        r = {'result': True}
        return jsonify(r)

def deleteUser():
    id_data = request.form['id']
    flash("Record Has Been Deleted Successfully")
    cur = mysql.connection.cursor()
    data_id = [id_data]
    data = cur.execute("DELETE FROM user WHERE id=%s", (id_data))
    mysql.connection.commit()
    publish('users_deleted',data_id)
    if data:
        r = {
            'title': 'Sukses!',
            'icon': 'success',
            'status': 'Berhasil dihapus'
        }
    else:
        r = {
            'title': 'Maaf!',
            'icon': 'error',
            'status': '<br><b>Tidak dapat di Hapus! <br> Silakan hubungi Administrator.</b>'
        }

    return jsonify(r)