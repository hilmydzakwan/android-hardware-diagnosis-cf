rulesCF = {

    # ======================================================
    # 1. Perangkat tidak merespons tombol daya (g1)
    # ======================================================
    "g1": {
        "Baterai Drop": 0.85,                
        "Konektor Baterai Tidak Menyalurkan Arus": 0.75,
        "Tombol Power Rusak": 0.70
    },

    # ======================================================
    # 2. Perangkat menyala tapi layar gelap (g2)
    # ======================================================
    "g2": {
        "Modul LCD Rusak": 0.90,
        "Fleksibel Layar Putus / Terlipat": 0.80,
        "Konektor Layar Tidak Terhubung": 0.75
    },

    # ======================================================
    # 3. Layar bergaris / tampilan pecah (g3)
    # ======================================================
    "g3": {
        "Panel LCD Rusak": 0.90,
        "Fleksibel Display Bermasalah": 0.80
    },

    # ======================================================
    # 4. Tidak bisa mengisi daya (g4)
    # ======================================================
    "g4": {
        "Port Charging Longgar / Rusak": 0.85,
        "Jalur Charger Terputus": 0.75,
        "IC Charging Rusak": 0.80
    },

    # ======================================================
    # 5. Mati tiba-tiba saat digunakan (g5)
    # ======================================================
    "g5": {
        "Baterai Drop": 0.80,
        "Overheat Komponen Internal": 0.75,
        "Jalur Daya Bermasalah": 0.70
    },

    # ======================================================
    # 6. Perangkat terasa panas (g6)
    # ======================================================
    "g6": {
        "IC Internal Bekerja Tidak Normal": 0.85,
        "Jalur Mengalami Short Ringan": 0.75
    },

    # ======================================================
    # 7. Suara tidak keluar (g7)
    # ======================================================
    "g7": {
        "Speaker Rusak": 0.85,
        "Soket Speaker Longgar": 0.70,
        "Jalur Audio Terputus": 0.75
    },

    # ======================================================
    # 8. Suara kecil (g8)
    # ======================================================
    "g8": {
        "Speaker Melemah": 0.80,
        "Membran Speaker Kotor": 0.70
    },

    # ======================================================
    # 9. Kamera buram / tidak bisa dibuka (g9)
    # ======================================================
    "g9": {
        "Modul Kamera Rusak": 0.85,
        "Konektor Kamera Tidak Stabil": 0.75
    },

    # ======================================================
    # 10. Sinyal seluler tidak muncul (g10)
    # ======================================================
    "g10": {
        "Modul Antena Rusak": 0.80,
        "Soket Antena Longgar": 0.75,
        "Jalur Sinyal Putus": 0.70
    },

    # ======================================================
    # 11. Tidak respons sentuhan (g11)
    # ======================================================
    "g11": {
        "Modul Touchscreen Rusak": 0.85,
        "Fleksibel Touchscreen Bermasalah": 0.75
    },

    # ======================================================
    # 12. Tidak terdeteksi via USB (g12)
    # ======================================================
    "g12": {
        "Port USB Rusak": 0.85,
        "Jalur Data Putus": 0.70
    },

    # ======================================================
    # 13. Restart berulang (g13)
    # ======================================================
    "g13": {
        "Baterai Tidak Stabil": 0.78,
        "Jalur Daya Bermasalah": 0.72,
        "Overheat Komponen Internal": 0.70
    },

    # ======================================================
    # 14. Ghost touch (g14)
    # ======================================================
    "g14": {
        "Modul Touchscreen Rusak": 0.85,
        "Fleksibel Touchscreen Rusak": 0.75,
        "IC Touch Rusak": 0.72
    },

    # ======================================================
    # 15. WiFi tidak aktif (g15)
    # ======================================================
    "g15": {
        "IC WiFi/Bluetooth Rusak": 0.85,
        "Jalur WiFi Terputus": 0.72
    },

    # ======================================================
    # 16. Baterai melembung (g16)
    # ======================================================
    "g16": {
        "Baterai Rusak Parah": 0.95,
        "Kualitas Baterai Buruk / Usia Tua": 0.80,
        "Efek Overcharging": 0.70
    }
}
