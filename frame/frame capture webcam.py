import cv2
import datetime  # Import modul datetime

# Inisialisasi kamera
cap = cv2.VideoCapture(0)  # Angka 0 mengacu pada kamera utama laptop

# Pastikan kamera terbuka
if not cap.isOpened():
    print("Gagal membuka kamera.")
else:
    is_capturing = False

    while True:
        # Baca frame dari kamera
        ret, frame = cap.read()

        # Periksa apakah bacaan frame berhasil
        if not ret:
            print("Gagal membaca frame.")
            break

        # Resize frame jika diperlukan
        frame = cv2.resize(frame, (640, 480))

        # Tampilkan frame
        cv2.imshow("Webcam", frame)

        # Menyimpan gambar saat tombol spasi ditekan
        key = cv2.waitKey(1)
        if key & 0xFF == ord(' '):
            is_capturing = True
        elif key & 0xFF == ord('q'):
            break

        if is_capturing:
            # Membuat timestamp
            timestamp = datetime.datetime.now().strftime("%Y%m%d%H%M%S")
            file_name = f"hasil_foto_{timestamp}.jpg"

            # Simpan frame sebagai gambar dengan timestamp
            cv2.imwrite(file_name, frame)
            print(f"Gambar {file_name} berhasil disimpan.")
            is_capturing = False

    # Tutup kamera dan jendela tampilan
    cap.release()
    cv2.destroyAllWindows()
