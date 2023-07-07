from pyrogram import Client, filters
import subprocess
import os

bot = Client(
    "myfirs",
    api_id=17983098,
    api_hash="ee28199396e0925f1f44d945ac174f64",
    bot_token="6251349619:AAHWY6-_BIwHqTUzvH62ukVUThjohP13d5k"
)
@bot.on_message(filters.command('start') & filters.private)
def command1(bot,message):
    bot.send_message(message.chat.id, "  السلام عليكم أنا بوت منتجة الفيديوهات . فقط أرسل التصميم ( الغلاف) بدون ضغط للحفاظ على جودة الفيديو \n\n Send without compression \n\n لبقية البوتات هنا \n\n https://t.me/ibnAlQyyim/1120",disable_web_page_preview=True)
    
@bot.on_message(filters.private & filters.incoming & filters.document | filters.photo)
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
  global picture
  pictrue=file_path


    

@bot.on_message(filters.private & filters.incoming & filters.audio | filters.voice )
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
  global file_path
  file_path = message.download(file_name="./downloads/")
  filename = os.path.basename(file_path)
  realname, ext = os.path.splitext(filename)
  global mp3file
  mp3file = realname+".mp3"
  global mp4file
  mp4file=realname+".mp4"
  global picture
  picture = "./downloads/pic"
  global res 
  res = '1920:1080'
  subprocess.call(['ffmpeg','-i',file_path,'-af','arnndn=m=./rnnoise-models/beguiling-drafter-2018-08-30/bd.rnnn',"mod"+mp3file,'-y']) 
  subprocess.call(['ffmpeg','-i',"mod"+mp3file,'-af', "volume=4",mp3file,'-y']) 
  subprocess.call(['ffmpeg', '-r', '1' ,'-loop', '1', '-y', '-i', f'{picture}' ,'-i', f'{mp3file}', '-c:v', 'libx264', '-tune', 'stillimage', '-c:a', 'copy', '-shortest', f'{res}', f'{mp4file}'])
    # Upload transcription file to user
  with open(mp4file, 'rb') as f:
        bot.send_video(message.chat.id, f)
  subprocess.call(['unlink',picture])
  subprocess.call(['unlink',mp3file])
  subprocess.call(['unlink',mp4file])
  subprocess.call(['unlink',"mod"+mp3file])
  subprocess.call(['unlink',file_path])





bot.run()
