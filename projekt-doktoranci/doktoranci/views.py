import os
import subprocess
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.decorators import user_passes_test
from .forms import PrzewodDoktorskiForm
from .models import get_user_role
from .utils import role_required


def home(request):
    return render(request, 'home.html')


@role_required('sekretarz')
def sekretarz_view(request):
    return render(request, 'sekretarz.html')


@role_required('rada')
def rada_view(request):
    return render(request, 'rada.html')


@role_required('admin')
def admin_panel(request):
    return render(request, 'admin_panel.html')


def is_admin(user):
    return user.is_authenticated and user.profiluzytkownika.rola == 'admin'


@user_passes_test(is_admin)
def dodaj_przewod(request):
    if request.method == 'POST':
        form = PrzewodDoktorskiForm(request.POST)
        if form.is_valid():
            przewod = form.save()

            # Ustal katalog roboczy
            base_path = os.path.join(os.getcwd(), 'generated')
            os.makedirs(base_path, exist_ok=True)

            tex_path = os.path.join(base_path, 'przewod.tex')
            pdf_path = os.path.join(base_path, 'przewod.pdf')

            # Zapisz plik LaTeX
            latex_content = f"""
            \\documentclass{{article}}
            \\usepackage[utf8]{{inputenc}}
            \\usepackage[T1]{{fontenc}}
            \\usepackage{{lmodern}}
            \\usepackage[polish]{{babel}}

            \\begin{{document}}
            \\section*{{Przewód doktorski}}

            \\textbf{{Doktorant}}: {przewod.doktorant} \\\\
            \\textbf{{Temat}}: {przewod.temat} \\\\
            \\textbf{{Promotor}}: {przewod.promotor} \\\\
            \\textbf{{Data złożenia}}: {przewod.data_zlozenia}

            \\end{{document}}
            """
            with open(tex_path, 'w', encoding='utf-8') as f:
                f.write(latex_content)

            # Uruchom pdflatex
            result = subprocess.run(
                ['pdflatex', '-output-directory', base_path, tex_path],
                stdout=subprocess.PIPE,
                stderr=subprocess.PIPE
            )

            if result.returncode != 0:
                error_message = result.stderr.decode()
                print("LaTeX ERROR:", error_message)
                return HttpResponse(f"Błąd podczas generowania PDF:<br><pre>{error_message}</pre>")

            # Sprawdź czy PDF istnieje
            if not os.path.exists(pdf_path):
                return HttpResponse("Nie udało się znaleźć wygenerowanego pliku PDF.")

            # Otwórz PDF i zwróć do przeglądarki
            with open(pdf_path, 'rb') as pdf_file:
                response = HttpResponse(pdf_file.read(), content_type='application/pdf')
                response['Content-Disposition'] = 'inline; filename="przewod.pdf"'
                return response
    else:
        form = PrzewodDoktorskiForm()

    return render(request, 'dodaj_przewod.html', {'form': form})
