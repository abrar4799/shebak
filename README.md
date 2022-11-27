# Shebak Assessment
- Endpoint Authentication. 
- Custom decorator methon verify the authorization header.
- The endpoint should pick a random quote, and send it, along with its author, as a JSON response.
- Generate an excel report file after every 100 calls composed of one sheet.

# Setup
To get started with this project we highly recommend the following:
 - Clone this repository by running https://github.com/abrar4799/shebak.git in your terminal.
 - Install project dependancies by running pip3 install -r requirements.txt
 - Run python3 manage.py makemigrations
 - Run python3 manage.py migrate
 - Run the project using python3 manage.py runserver

# Get Token
- Run python3 manage.py createsuperuser with your username and password
- Sending post request to this route http://127.0.0.1:8000/get-token 

# Get Random Quote
- Using this route http://127.0.0.1:8000/quote/random/
- Sending your token in headers as key and value pairs
- Ex: { key: Authorization , value: Token 8ac76bae227187e04977c5206f8a2e0c5af3f763 }
- After 100 call of API excel report file automatically generated with name quotes_api_report_ and date , time Ex: quotes_api_report_27_11_2022_16_24_52.xlsx
