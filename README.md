<div align="center">

# 🐦 Flappy Bird 2D — OpenGL & FreeGLUT

Reimplementasi game **Flappy Bird** dalam grafik 2D menggunakan **C++**, **OpenGL**, dan **FreeGLUT**.
Dibuat sebagai project mata kuliah **Komputer Grafik**.

![Language](https://img.shields.io/badge/Language-C%2B%2B-blue?style=flat-square)
![Graphics](https://img.shields.io/badge/Graphics-OpenGL-5586A4?style=flat-square)
![Library](https://img.shields.io/badge/Library-FreeGLUT-orange?style=flat-square)
![Platform](https://img.shields.io/badge/Platform-Windows-0078D6?style=flat-square)
![License](https://img.shields.io/badge/License-MIT-green?style=flat-square)

</div>

---

## 📸 Preview

<div align="center">

![Gameplay Demo](assets/screenshots/demo.gif)

| Start Screen | Gameplay | Game Over |
|:---:|:---:|:---:|
| ![Start](assets/screenshots/start.png) | ![Gameplay](assets/screenshots/gameplay.png) | ![Game Over](assets/screenshots/gameover.png) |

</div>


## ✨ Fitur

- 🎮 Physics sederhana: **gravity** & **jump** pada burung
- 🌀 Rotasi burung dinamis mengikuti arah kecepatan (efek "diving" & "flying")
- 🟩 Pipa dengan celah (gap) acak yang **mengecil seiring skor bertambah** (tingkat kesulitan naik)
- ⚡ Kecepatan pipa bertambah secara progresif → game makin menantang
- 🎵 Background music & sound effect saat mencetak skor (via Windows Multimedia API)
- ☁️ Elemen visual dekoratif (awan) yang digambar prosedural dengan `GL_TRIANGLE_FAN`
- 🏆 Sistem skor & high score real-time
- 🔁 Restart cepat dengan satu tombol

---

## 🕹️ Kontrol

| Tombol | Aksi |
|:---:|---|
| `SPACE` | Mulai game / membuat burung terbang (jump) |
| `R` | Restart game |

---

## 🛠️ Tech Stack

- **Bahasa:** C++
- **Grafik:** OpenGL (Fixed-Function Pipeline / Immediate Mode)
- **Windowing & Input:** FreeGLUT
- **Audio:** Windows Multimedia API (`winmm.lib`, `mciSendString`, `PlaySound`)
- **Platform:** Windows

---

## 📁 Struktur Project

```
flappy-bird-2d-opengl/
├── .vscode/
│   └── tasks.json          # Konfigurasi build task VS Code
├── assets/
│   ├── musik.wav            # Background music
│   ├── sound.wav             # Sound effect skor
│   └── screenshots/          # Screenshot & GIF untuk README
├── src/
│   └── main.cpp              # Source code utama game
├── .gitignore
├── LICENSE
└── README.md
```

---

## ⚙️ Instalasi & Menjalankan

### Prasyarat

- **Windows OS** (menggunakan Windows Multimedia API untuk audio)
- Compiler C++ (disarankan **MinGW-w64** / g++)
- **FreeGLUT** (header & library) sudah terpasang dan ter-link di compiler
- **VS Code** (opsional, sudah ada konfigurasi `.vscode/tasks.json`)

### Build via terminal (g++ / MinGW)

```bash
g++ src/main.cpp -o flappybird.exe -lfreeglut -lopengl32 -lglu32 -lwinmm
```

### Menjalankan

```bash
./flappybird.exe
```

> ⚠️ Pastikan file `musik.wav` dan `sound.wav` berada satu folder dengan file `.exe`, atau sesuaikan path pada `main.cpp` (`playBackgroundMusic()` dan `PlaySound()`).

### Build via VS Code

1. Buka folder project di VS Code
2. Pastikan ekstensi **C/C++** dari Microsoft terpasang
3. Tekan `Ctrl+Shift+B` untuk menjalankan build task dari `.vscode/tasks.json`
4. Jalankan file `.exe` yang dihasilkan

---

## 🎓 Tentang Project

Project ini dibuat untuk memenuhi tugas mata kuliah **Komputer Grafik**, dengan fokus pada penerapan konsep:

- Transformasi 2D (translasi & rotasi objek menggunakan `glTranslatef`, `glRotatef`)
- Primitif grafik (`GL_TRIANGLE_FAN`, `GL_POLYGON`, `GL_TRIANGLES`)
- Animasi berbasis waktu (`glutTimerFunc`) dan double buffering
- Deteksi collision sederhana berbasis bounding area
- Rendering teks pada layar (`glutBitmapCharacter`)

---

## 🗺️ Roadmap / Pengembangan Selanjutnya

- [ ] Mengaktifkan kembali sistem collision detection
- [ ] Menambahkan efek particle saat game over
- [ ] Leaderboard/high score tersimpan (file-based)
- [ ] Cross-platform build (Linux/macOS) dengan library audio alternatif

---

## 🖼️ Menambahkan Screenshot & GIF

1. Buat folder `assets/screenshots/` di root repo
2. Rekam gameplay (misalnya dengan **ScreenToGif**, **OBS Studio**, atau **ShareX**)
3. Simpan sebagai `demo.gif`, `gameplay.png`, `start.png`, `gameover.png`
4. Commit & push — README di atas akan otomatis menampilkannya di GitHub

---

## 📄 Lisensi

Project ini dilisensikan di bawah [MIT License](LICENSE) — bebas digunakan, dimodifikasi, dan didistribusikan dengan mencantumkan atribusi.

---

<div align="center">

Dibuat dengan ❤️ oleh **[Hilmy Dzakwan](https://github.com/hilmydzakwan)**

</div>
