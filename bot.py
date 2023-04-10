from pyrogram import Client, filters
import subprocess
bot = Client(
    "myfirs",
    api_id=17983098,
    api_hash="ee28199396e0925f1f44d945ac174f64",
    bot_token="6169974916:AAFO4oyy5fiYM19VrLiJ0lyc-MN9gCFVgd0"
)
def run_command(command):
    result = subprocess.run(
        command.split(),
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE
    )
    return result.stdout.decode('utf-8'), result.stderr.decode('utf-8')
@bot.on_message(filters.command('start') & filters.private)
def command1(bot,message):
    bot.send_message(message.chat.id, " السلام عليكم أنا بوت منتجة الفيديوهات . فقط أرسل التصميم ( الغلاف)  ")
    
@bot.on_message(filters.private & filters.incoming & filters.photo )
def _telegram_file(client, message):
  user_id = message.from_user.id
  sent_message = message.reply_text('الآن أرسل الصوتية', quote=True)
  file = message.audio
  file_path = message.download(file_name="pic")
    

@bot.on_message(filters.private & filters.incoming & filters.audio )
def _telegram_file(client, message):
  user_id = message.from_user.id
  sent_message = message.reply_text('[جار منتجة الفيديو', quote=True)
  file = message.audio
  file_path = message.download(file_name="aud")
  subprocess.call(['itv'])

    # Upload transcription file to user
  with open('resultx.mp4', 'rb') as f:
        bot.send_video(message.chat.id, f)

bot.run()
