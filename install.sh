echo -e "Creating Python Virtual Environment"
python3 -m venv venv

echo -e "Installing required modules from requirements.txt" 
source venv/bin/activate
pip3 install -r requirements.txt
