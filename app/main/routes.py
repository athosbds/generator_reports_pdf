from flask import render_template, redirect, url_for, request, send_file
from . import main_dp
from weasyprint import HTML
import os

@main_dp.route('/')
def form():
    return render_template('form.html')
@main_dp.route('/generatepdf', ['POST'])
def generate_pdf():
    name = request.form['name']
    age = request.form['age']
    placetext = request.form['placetext']
    html = render_template('finished.html', name=name, age=age, placetext=placetext)
    file_pdf = os.path.join('app', 'static', 'finished.html')
    HTML(string=html).write_pdf(file_pdf)
    def remover_arquivo(response):
        try:
            os.remove(file_pdf)
        except Exception as e:
            print(f"Erro ao deletar o PDF: {e}")
        return response
    return send_file(file_pdf, as_attachment=True, download_name='relatorio.pdf')

