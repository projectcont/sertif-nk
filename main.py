

from dispence_ import dispence
from sqlf.crud import prodlist_add
from excel.excel1  import  get_pr_list_from_excel
from excel.excel2  import  get_prodlist_from_excel

import sqlf.сountprod
from flask import  Flask, render_template, url_for, request
import webbrowser
import go_
from configuration import excel_format, showdebug
import location
import sys, traceback

app=Flask(__name__)

session = go_.go()

prod_list=[]
global prod_list_excel
prod_list_excel=[]
prod_list_site=[]
prod_list_update=[]
prod_list_add=[]

with open("not_accepted.txt", "w") as file:
    file.write(" НЕ ПРИНЯТЫЕ АНКЕТЫ   \n")

@app.route("/",methods=["GET","POST"])
@app.route("/index",methods=["GET","POST"])
def index():

    print("url= ",url_for('index'))
    result_import = 0
    result_export = 0
    countprod=[0, 0]

    if request.method=='POST':

        if 'get_from_excel_button' in request.form:
            try:
                location_file = location.getit('1.xlsx')
                pr = get_pr_list_from_excel ( file=location_file, number_or_lines=0)

                global prod_list_excel
                prod_list_excel = get_prodlist_from_excel (pr)

                print('ДАННЫЕ ИЗВЛЕЧЕНЫ ИЗ EXCEL-ФАЙЛА')
                result_import = 1

            except FileNotFoundError:
                # traceback.print_exc()
                print('ВНЕШНЯЯ ОШИБКА ИЗВЛЕЧЕНИЯ ДАННЫХ ИЗ EXCEL-ФАЙЛА')
                raise SystemExit



        if 'send_to_db_button' in request.form:

            try:

                prod_list_add = dispence(session, prod_list_excel)
                prodlist_add(prod_list_add, session)

                countprod=[sqlf.сountprod.Countprod.update, sqlf.сountprod.Countprod.add]
                print('ДАННЫЕ ЭКСПОРТИРОВАНЫ НА САЙТ')

                result_export = 1
                #print('result_export=', result_export)

            except Exception:
                traceback.print_exc()
                webbrowser.open('http://127.0.0.1:5222/index', new=0, autoraise=True)
                print('ВНЕШНЯЯ ОШИБКА ЭКСПОРТА')
                raise SystemExit



    return render_template('index.html',result_import=result_import, result_export=result_export, excel_format=excel_format, countprod=countprod )


if __name__ == "__main__":

    webbrowser.open('http://127.0.0.1:5000/index', new=1, autoraise=True)
    app.run(debug=showdebug)


























