from django.shortcuts import render
from django.http import HttpResponse


def home(request):
    return render(request, 'home.html')
def about(request):
    return render(request, 'about.html')
def contact(request):
    return render(request, 'contact.html')
def app1(request):
    return render(request, 'app1.html')


def app(request):
    ar_olahraga = ['Sepedahan', 'Lari', 'Jalan Santai', 'Renang']

   
    context = {'ar_olahraga': ar_olahraga}
    return render(request, 'app.html', context)

def process_calories(request):
    if request.method == "POST":
        nama = request.POST.get("nama")
        berat_badan = float(request.POST.get("berat_badan"))
        tinggi_badan = float(request.POST.get("tinggi_badan"))
        usia = int(request.POST.get("usia"))
        jam_olahraga = float(request.POST.get("jam_olahraga"))
        jenis_olahraga = request.POST.get("jenis_olahraga")

        olahraga_met = {
            "Sepedahan": 7.5,
            "Lari": 11.0,
            "Jalan Santai": 3.3,
            "Renang": 8.0,
        }

       
        def hitung_kalori(berat_badan, jam_olahraga, met):
            return met * berat_badan * jam_olahraga

    
        met = olahraga_met.get(jenis_olahraga, 0)
        kalori_dibakar = hitung_kalori(berat_badan, jam_olahraga, met)

        slip_calories = {
            "nama": nama,
            "berat_badan": f"{berat_badan} kg",
            "tinggi_badan": f"{tinggi_badan} cm",
            "usia": f"{usia} tahun",
            "jam_olahraga": f"{jam_olahraga} jam",
            "jenis_olahraga": jenis_olahraga,
            "kalori_dibakar": f"{kalori_dibakar:.2f} kalori",
        }

        return render(request, 'hasil_calories.html', {"slip_calories": slip_calories})

    return render(request, 'app.html')


def hitung_kebutuhan_kalori(request):
    if request.method == "POST":
        nama = request.POST.get("nama")
        berat_badan = float(request.POST.get("berat_badan", 0))
        tinggi_badan = float(request.POST.get("tinggi_badan", 0))
        usia = int(request.POST.get("usia", 0))
        jenis_kelamin = request.POST.get("jenis_kelamin")
        aktivitas = request.POST.get("aktivitas")

        if jenis_kelamin == "Laki-laki":
            bmr = 88.362 + (13.397 * berat_badan) + (4.799 * tinggi_badan) - (5.677 * usia)
        else:
            bmr = 447.593 + (9.247 * berat_badan) + (3.098 * tinggi_badan) - (4.330 * usia)

       
        aktivitas_faktor = {
            "Tidak Banyak Bergerak": 1.2,
            "Aktif Ringan": 1.375,
            "Cukup Aktif": 1.55,
            "Sangat Aktif ": 1.725,
            "Sangat - sangat Aktif": 1.9,
        }

      
        total_kalori = bmr * aktivitas_faktor.get(aktivitas, 1)

        hasil_kalori = {
            "nama": nama,
            "berat_badan": f"{berat_badan} kg",
            "tinggi_badan": f"{tinggi_badan} cm",
            "usia": f"{usia} tahun",
            "jenis_kelamin": jenis_kelamin,
            "aktivitas": aktivitas,
            "bmr": f"{bmr:.2f} kalori",
            "kebutuhan_kalori": f"{total_kalori:.2f} kalori",
        }

        return render(request, 'hitung_kebutuhan_kalori.html', {"hasil_kalori": hasil_kalori})

    return render(request, 'app1.html')