def identifikasi_hama(gejala):
    # Aturan-aturan berbasis logika
    if 'daun menguning' in gejala and 'tanaman layu' in gejala:
        return 'Kutu Daun'
    elif 'terdapat bercak hitam' in gejala and 'daun menguning' in gejala:
        return 'Virus'
    elif 'terdapat bercak hitam' in gejala:
        return 'Penyakit Jamur'
    elif 'daun berlubang' in gejala:
        return 'Ulat'
    else:
        return 'Hama tidak diketahui'

# Contoh penggunaan:
gejala_input = ['daun menguning', 'tanaman layu']
hasil = identifikasi_hama(gejala_input)
print(f"Jenis hama terdeteksi: {hasil}")
