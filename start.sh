echo "Cloning Repo...."
git clone https://github.com/konichiwa55115/vidmk /LazyDeveloper
cd /LazyDeveloper
git clone https://github.com/GregorR/rnnoise-models
pip3 install -r requirements.txt
echo "Starting Bot...."
python3 bot.py
