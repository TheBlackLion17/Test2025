if [ -z $UPSTREAM_REPO ]
then
  echo "Cloning main Repository"
  git clone https://github.com/TheBlackLion17/Test2025.git /Test2025
else
  echo "Cloning Custom Repo from $UPSTREAM_REPO "
  git clone $UPSTREAM_REPO /Test2025
fi
cd /Test2025
pip3 install -U -r requirements.txt
echo "Starting Bot...."
python3 bot.py
