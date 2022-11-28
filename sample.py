
import requests



# url = 'https://api.telegram.org/bot{0}/sendMessage?chat_id={1}&text={2}'
url = 'https://api.telegram.org/bot5238925279:AAG-MA4LlKpLE6-EQrMq3N1ylnRuGRckALA/sendMessage?chat_id=@daily_nagu_jobs&text=Hello from Suresh'


x = requests.post(url)

print(x.text)

