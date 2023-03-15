export $(grep -v '^#' .env | xargs)
python3 main.py
unset $(grep -v '^#' .env | sed -E 's/(.*)=.*/\1/' | xargs)