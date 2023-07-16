echo "Cloning Repo...."
git clone https://github.com/konichiwa55115/vidmk /LazyDeveloper
git clone https://github.com/GregorR/rnnoise-models  /LazyDeveloper
cd /LazyDeveloper
pip3 install -r requirements.txt
echo "Starting Bot...."
gunicorn app:app & python3 bot.py
