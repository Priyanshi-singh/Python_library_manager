import pkg_resources
from flask import Flask, render_template, request, redirect, flash, url_for
from operation import install_lib, upgrade_lib, uninstall_lib, search_lib

app = Flask(__name__)


@app.route('/')
def login():
    return render_template('login.html')

@app.route('/view_list')
def view_list():
    try:
        if request.method == 'POST':
            lib_name = request.args.get('Library_name')
            return redirect(url_for('uninstall', lib_name=lib_name ))
    except:
        flash("Something Went Wrong")

    return render_template('view.html')

@app.route('/uninstall')
def uninstall():
    uninstall_lib(lib_name)
    return render_template('uninstall.html',title = 'uninstall Library')


if __name__ == '__main__':
    app.run(host='127.0.0.1', port=8000, debug=True)
 