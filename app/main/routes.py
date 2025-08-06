from flask import render_template, redirect, url_for, request, send_file, after_this_request
from . import main_dp
from weasyprint import HTML
import os

@main_dp.route('/')
def form():
    return render_template('form.html')
@main_dp.route('/generatepdf', methods=['POST'])
def generate_pdf():
    name = request.form.get('name')
    age = request.form.get('age')
    placetext = request.form.get('placetext')
    html = render_template('finished.html', name=name, age=age, placetext=placetext)
    file_pdf = os.path.join(os.path.dirname(__file__), '..', 'static', 'relatorio.pdf')
    file_pdf = os.path.abspath(file_pdf)
    HTML(string=html).write_pdf(file_pdf)
    @after_this_request
    def remover_arquivo(response):
        try:
            os.remove(file_pdf)
        except Exception as e:
            print(f"Erro ao deletar o PDF: {e}")
        return response
    return send_file(file_pdf, as_attachment=False, download_name='relatorio.pdf')

