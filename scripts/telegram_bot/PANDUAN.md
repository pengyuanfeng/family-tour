# Cara Memulai Family Tutor Bot 🚀

## 1. Buat Bot Telegram

Buka Telegram, cari **@BotFather**, kirim:

```
/newbot
```

Ikuti petunjuknya:
- Nama bot: `Family Tutor` (atau terserah)
- Username: `family_tutor_bot` (atau terserah, harus unik)
- Selesai → @BotFather akan kirim **token**, simpan token ini

## 2. Setup API Key

Buka https://platform.deepseek.com/ → Login/Register → Dapatkan API Key

## 3. Isi File .env

Di folder `D:\family-tutor\scripts\telegram_bot\`:

1. Copy `.env.example` jadi `.env`
2. Edit `.env` dengan Notepad:

```
BOT_TOKEN=7212345678:AAF...token_dari_botfather...
DEEPSEEK_API_KEY=sk-...api_key_dari_deepseek...
```

## 4. Jalankan Bot

Buka Terminal (CMD atau PowerShell), ketik:

```bash
cd D:\family-tutor\scripts\telegram_bot
pip install -r requirements.txt
python bot.py
```

Kalau muncul "Family Tutor Bot berjalan..." → bot sudah siap!

## 5. Ibu Priska Bisa Pake

Cari bot di Telegram (pakai username yg tadi dibuat), kirim:

| Perintah | Fungsi |
|----------|--------|
| `/start` | Lihat menu bantuan |
| `/soal warna` | Minta PR tema warna |
| `/game angka` | Minta game tema angka |
| `/story` | Minta cerita Mandarin |
| `/semangat` | Kalo butuh support |

Atau tinggal chat aja biasa, misal:
- "Bikin PR buah-buahan dong"
- "Kakak males belajar, ada game?"
- "Hari ini capek..."
