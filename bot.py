from pyrogram import Client, filters
import subprocess
bot = Client(
    "myfirs",
    api_id=17983098,
    api_hash="ee28199396e0925f1f44d945ac174f64",
    bot_token="6251349619:AAHy593169xkJUIwbqIue9jLd18bwVmY-jc"
)
@bot.on_message(filters.command('start') & filters.private)
def command1(bot,message):
    bot.send_message(message.chat.id, "  السلام عليكم أنا بوت منتجة الفيديوهات . فقط أرسل التصميم ( الغلاف) بدون ضغط للحفاظ على جودة الفيديو \n\n Send without compression \n\n لبقية البوتات هنا \n\n https://t.me/ibnAlQyyim/1120",disable_web_page_preview=True)
    
@bot.on_message(filters.private & filters.incoming & filters.document )
def _telegram_file(client, message):
  try: 
    with open("resultx.mp4", 'r') as fh:
       
            sent_message = message.reply_text('هناك منتجة تتم الآن . أرسل التصميم بعد مدة من فضلك', quote=True)
            return
  except FileNotFoundError: 
    pass  
  user_id = message.from_user.id
  sent_message = message.reply_text('الآن أرسل الصوتية', quote=True)
  file = message.document
  file_path = message.download(file_name="pic")

@bot.on_message(filters.private & filters.incoming & filters.photo )
def _telegram_file(client, message):
  try: 
    with open("resultx.mp4", 'r') as fh:
        
            sent_message = message.reply_text('هناك منتجة تتم الآن . أرسل التصميم بعد مدة من فضلك', quote=True)
            return
  except FileNotFoundError: 
    pass  
  user_id = message.from_user.id
  sent_message = message.reply_text('الآن أرسل الصوتية', quote=True)
  file = message.photo
  file_path = message.download(file_name="pic")
    

@bot.on_message(filters.private & filters.incoming & filters.audio )
def _telegram_file(client, message):
  try: 
    with open("resultx.mp4", 'r') as fh:
       
            sent_message = message.reply_text('هناك منتجة تتم الآن . أرسل التصميم بعد مدة من فضلك', quote=True)
            return
  except FileNotFoundError: 
    pass  
  user_id = message.from_user.id
  sent_message = message.reply_text('[جار منتجة الفيديو', quote=True)
  file = message.audio
  file_path = message.download(file_name="aud")
  subprocess.call(['itv'])

    # Upload transcription file to user
  with open('resultx.mp4', 'rb') as f:
        bot.send_video(message.chat.id, f)
  subprocess.call(['unlink','./downloads/pic'])
  subprocess.call(['unlink','./downloads/aud'])
  subprocess.call(['unlink','resultx.mp4'])

@bot.on_message(filters.private & filters.incoming & filters.voice )
def _telegram_file(client, message):
  try: 
    with open('resultx.mp4', 'r') as fh:
        
            sent_message = message.reply_text('هناك منتجة تتم الآن . أرسل التصميم بعد مدة من فضلك', quote=True)
            return
  except FileNotFoundError: 
    pass  
  user_id = message.from_user.id
  sent_message = message.reply_text('[جار منتجة الفيديو', quote=True)
  file = message.voice
  file_path = message.download(file_name="aud")
  subprocess.call(['itv'])

    # Upload transcription file to user
  with open('resultx.mp4', 'rb') as f:
        bot.send_video(message.chat.id, f)
  subprocess.call(['unlink','./downloads/pic'])
  subprocess.call(['unlink','./downloads/aud'])
  subprocess.call(['unlink','resultx.mp4'])

bot.run()
