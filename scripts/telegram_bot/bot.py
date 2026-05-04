"""
Family Tutor Telegram Bot
=========================
Bot pendamping keluarga untuk Ibu Priska.
Bisa bikin PR, game, cerita, dan support emosional.

Cara jalanin:
  pip install -r requirements.txt
  # Isi BOT_TOKEN dan DEEPSEEK_API_KEY di .env
  python bot.py

Buat bot token: https://t.me/BotFather
"""
import logging
import html

from telegram import Update
from telegram.constants import ParseMode
from telegram.ext import Application, CommandHandler, MessageHandler, filters, ContextTypes

import config
import ai_handler

logging.basicConfig(format="%(asctime)s - %(name)s - %(levelname)s - %(message)s", level=logging.INFO)
logger = logging.getLogger(__name__)

# ── Command: /start ──

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text = (
        "Halo Ibu Priska! 👋\n\n"
        "Aku asisten keluarga untuk membantu:\n"
        "📝 Bikin PR untuk Kakak & Adek\n"
        "🎮 Game belajar yang seru\n"
        "📖 Cerita Mandarin + Indonesia\n"
        "💪 Support untuk Ibu\n\n"
        "Cukup chat aku langsung, atau pake perintah:\n"
        "/soal - Minta PR (bilang mau untuk Kakak/Adek & topiknya)\n"
        "/game - Minta game belajar\n"
        "/story - Minta cerita Mandarin\n"
        "/semangat - Kalo Ibu butuh support\n\n"
        "Mari kita bikin belajar jadi menyenangkan! 🚀"
    )
    await update.message.reply_text(text)


# ── Command: /soal (minta PR) ──

async def soal(update: Update, context: ContextTypes.DEFAULT_TYPE):
    topic = " ".join(context.args) if context.args else "umum"
    prompt = (
        f"Tolong buatkan PR bahasa Mandarin untuk anak-anak dengan topik: {topic}.\n"
        f"Buat versi untuk Kakak (11 tahun) dan Adek (8 tahun).\n"
        f"Pakai Bahasa Indonesia + Mandarin + pinyin.\n"
        f"Buat yang gampang di-print atau ditulis ulang."
    )
    await update.message.reply_chat_action("typing")
    reply = ai_handler.ask_ai(prompt)
    await update.message.reply_text(reply)


# ── Command: /game (minta game) ──

async def game(update: Update, context: ContextTypes.DEFAULT_TYPE):
    topic = " ".join(context.args) if context.args else "bahasa Mandarin"
    prompt = (
        f"Tolong buatkan game belajar yang seru dan gampang untuk anak-anak "
        f"dengan topik: {topic}.\n"
        f"Game harus tanpa alat ribet (cuma kertas/pensil atau tanpa alat).\n"
        f"Cocok untuk Kakak (11 tahun) dan Adek (8 tahun).\n"
        f"Pakai Bahasa Indonesia + Mandarin + pinyin."
    )
    await update.message.reply_chat_action("typing")
    reply = ai_handler.ask_ai(prompt)
    await update.message.reply_text(reply)


# ── Command: /story (minta cerita) ──

async def story(update: Update, context: ContextTypes.DEFAULT_TYPE):
    prompt = (
        "Tolong buatkan cerita pendek bahasa Mandarin untuk anak-anak.\n"
        "Topik: kehidupan sehari-hari yang seru.\n"
        "Tulis dalam Bahasa Mandarin + pinyin + terjemahan Bahasa Indonesia.\n"
        "Buat yang lucu dan menarik untuk Kakak (11 tahun) dan Adek (8 tahun)."
    )
    await update.message.reply_chat_action("typing")
    reply = ai_handler.ask_ai(prompt)
    await update.message.reply_text(reply)


# ── Command: /semangat (support buat Ibu) ──

async def semangat(update: Update, context: ContextTypes.DEFAULT_TYPE):
    prompt = (
        "Ibu Priska lagi butuh semangat. Tolong beri kata-kata dukungan "
        "yang hangat dalam Bahasa Indonesia. Ingatkan dia bahwa dia sudah "
        "hebat dan tidak perlu sempurna. Beri saran kegiatan 10 menit "
        "yang gampang buat hari ini."
    )
    await update.message.reply_chat_action("typing")
    reply = ai_handler.ask_ai(prompt)
    await update.message.reply_text(reply)


# ── Handle non-command message ──

async def handle_text(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text = update.message.text.strip()
    await update.message.reply_chat_action("typing")
    reply = ai_handler.ask_ai(text)
    await update.message.reply_text(reply)


# ── Main ──

def main():
    if not config.BOT_TOKEN or config.BOT_TOKEN == "your_bot_token_here":
        print("❌ BOT_TOKEN belum diisi!")
        print("   1. Buka https://t.me/BotFather, buat bot baru, dapatkan token")
        print("   2. Isi BOT_TOKEN di file .env")
        print("   3. Juga isi DEEPSEEK_API_KEY di .env")
        return

    if not config.DEEPSEEK_API_KEY or config.DEEPSEEK_API_KEY == "your_deepseek_api_key_here":
        print("❌ DEEPSEEK_API_KEY belum diisi!")
        print("   Dapatkan API key dari https://platform.deepseek.com/")
        return

    app = Application.builder().token(config.BOT_TOKEN).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("soal", soal))
    app.add_handler(CommandHandler("game", game))
    app.add_handler(CommandHandler("story", story))
    app.add_handler(CommandHandler("semangat", semangat))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_text))

    print("🤖 Family Tutor Bot berjalan... (tekan Ctrl+C untuk stop)")
    app.run_polling(allowed_updates=Update.ALL_TYPES)


if __name__ == "__main__":
    main()
