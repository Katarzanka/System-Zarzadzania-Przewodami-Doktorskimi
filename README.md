# System-Zarzadzania-Przewodami-Doktorskimi

## Opis
Webowy system administracyjny dla wydziału, wspierający zarządzanie przewodami doktorskimi, generowanie dokumentów i obsługę użytkowników z różnymi uprawnieniami.

## Technologie
- Django 5.2 (Python)
- LaTeX (pdflatex) do generowania PDF
- Docker (konteneryzacja)
- SQLite (domyślnie)

## Funkcjonalności
- Logowanie i role (admin, sekretarz, rada)
- Panel dla każdej roli
- Formularz przewodu doktorskiego
- Generowanie dokumentów z LaTeX
- Podgląd i pobieranie PDF

## Jak uruchomić
```bash
docker-compose build
docker-compose up
