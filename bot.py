from telegram import Update
from telegram.ext import Application, CommandHandler, ContextTypes
import os
TOKEN = os.getenv("TOKEN")

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "👋 Bienvenue !\n\nUtilisez /semio pour voir le cours disponible."
    )

async def semio(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        """
📚 Cours de Sémiologie Digestive

Transformé et réorganisé pour un apprentissage plus clair, rapide et efficace.

💰 Prix : 600 DA

💳 CCP / BaridiMob :
00799999002796476450

📸 Après le paiement, envoyez une capture d'écran du reçu.

✅ Vous recevrez immédiatement :
• L'accès complet au cours sur Notion
• Des cas cliniques
• Des QCM
• Des images récapitulatives
• Un tracker de progression

🎯 Objectif : comprendre, retenir et réviser plus efficacement.
"""
    )

app = Application.builder().token(TOKEN).build()

app.add_handler(CommandHandler("start", start))
app.add_handler(CommandHandler("semio", semio))

print("Bot lancé...")

app.run_polling()
