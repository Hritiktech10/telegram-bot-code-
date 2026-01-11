from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import (
    ApplicationBuilder,
    CommandHandler,
    MessageHandler,
    ContextTypes,
    filters
)

# ---------------- AI TOOLS DATABASE ----------------
AI_TOOLS = {
    "chatgpt": {
        "website": "https://chat.openai.com",
        "app": "https://play.google.com/store/apps/details?id=com.openai.chatgpt"
    },
    "midjourney": {
        "website": "https://www.midjourney.com",
        "app": "https://discord.com"
    },
    "bard": {
        "website": "https://gemini.google.com",
        "app": "https://play.google.com/store/apps/details?id=com.google.android.apps.bard"
    },
    "copilot": {
        "website": "https://copilot.microsoft.com",
        "app": "https://play.google.com/store/apps/details?id=com.microsoft.copilot"
    }
}

# ---------------- START COMMAND ----------------
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "🤖 Drop an AI tool name.\n"
        "I’ll open doors like a corporate concierge.\n\n"
        "Example: chatgpt, midjourney, copilot"
    )

# ---------------- SEARCH HANDLER ----------------
async def search_ai(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.message.text.lower().strip()

    if query in AI_TOOLS:
        tool = AI_TOOLS[query]

        keyboard = [
            [InlineKeyboardButton("🌐 Go to Website", url=tool["website"])],
            [InlineKeyboardButton("📱 Go to App", url=tool["app"])]
        ]

        reply_markup = InlineKeyboardMarkup(keyboard)

        await update.message.reply_text(
            f"🚀 *{query.upper()} found.*\nChoose your launchpad:",
            reply_markup=reply_markup,
            parse_mode="Markdown"
        )
    else:
        await update.message.reply_text(
            "❌ Tool not found.\n"
            "Either it doesn’t exist or it’s hiding from capitalism.\n"
            "Try another AI tool name."
        )

# ---------------- MAIN ----------------
def main():
    app = ApplicationBuilder().token("8332656093:AAH55nHKrFj8kUcWrMKqJI16SztP2nirll4").build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, search_ai))

    print("🤖 Bot is live. KPI green. Revenue imaginary.")
    app.run_polling()

if _name_ == "_main_":
    main()
