import telebot

# اطلاعات ربات
TOKEN = "7859389117:AAFUV99C988B2B4akXwQMEkL21Ju8qE1M7U"  # توکن ربات خود را جایگزین کنید
ADMIN_ID = 1271793615  # شناسه عددی شما (مثلاً 123456789)

bot = telebot.TeleBot(TOKEN)

# دریافت پیام و ارسال آن همراه با User ID ارسال‌کننده
@bot.message_handler(func=lambda message: True)
def forward_message(message):
    try:
        user_info = f"👤 ارسال‌کننده: [{message.from_user.first_name}](tg://user?id={message.from_user.id})\n🆔 User ID: `{message.from_user.id}`\n"
        bot.send_message(ADMIN_ID, user_info, parse_mode="Markdown")  # ارسال اطلاعات فرستنده
        bot.copy_message(ADMIN_ID, message.chat.id, message.message_id)  # ارسال پیام اصلی
        bot.send_message(message.chat.id, "✅ پیام شما دریافت و برای ادمین ارسال شد.")
    except Exception as e:
        bot.send_message(message.chat.id, "❌ مشکلی پیش آمد، لطفاً دوباره تلاش کنید.")

# اجرای ربات
print("ربات فعال شد...")
bot.polling(none_stop=True)
import telebot

# اطلاعات ربات
TOKEN = "YOUR_BOT_TOKEN"  # توکن ربات خود را جایگزین کنید
ADMIN_ID = YOUR_NUMERIC_ID  # شناسه عددی شما (مثلاً 123456789)

bot = telebot.TeleBot(TOKEN)

# دریافت پیام و ارسال آن همراه با User ID ارسال‌کننده
@bot.message_handler(func=lambda message: True)
def forward_message(message):
    try:
        user_info = f"👤 ارسال‌کننده: [{message.from_user.first_name}](tg://user?id={message.from_user.id})\n🆔 User ID: `{message.from_user.id}`\n"
        bot.send_message(ADMIN_ID, user_info, parse_mode="Markdown")  # ارسال اطلاعات فرستنده
        bot.copy_message(ADMIN_ID, message.chat.id, message.message_id)  # ارسال پیام اصلی
        bot.send_message(message.chat.id, "✅ پیام شما دریافت و برای ادمین ارسال شد.")
    except Exception as e:
        bot.send_message(message.chat.id, "❌ مشکلی پیش آمد، لطفاً دوباره تلاش کنید.")

# اجرای ربات
print("ربات فعال شد...")
bot.polling(none_stop=True)
