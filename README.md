# Divar

Python package for crawling from Divar website.
divar.ir is the biggest website in the middle-east that people post their properties and try to sell them online.

## Installation
Simply you can install it from PyPi by following command:

```bash
pip install -U divar-scraper
```

or if you prefer the latest development version, you can install it from the source:

```bash
git clone https://github.com/softcoder24/divar.git
cd divar
python setup.py install
```

## Usage

A very simple usage for getting the phone number could be like:

```python
from divar import client

session = 'eyJ0eXAiOiJKV1QiLCJhbGciOiJI................UzI1NiJ9zRumpqq1wrfGpYaD'

divar = client.Divar()

divar.load(session=session)

divar.contact('wXSTyUdO')

```

Sample response for contact:
```
09991112233
```

```python
from divar import client

divar = client.Divar()
divar.post('wXSTyUdO')

```

Sample response for post:

```
{
    'title': '۳خوابه امامت۱۴', 
    'description': 'کلا ۴ واحد\nسرامیک\nام دی اف\n۰۹۱۵۱۰۰۳۵۲۴\n۰۹۱۵۲۰۰۳۵۲۴\nرجایی\nهیچ جا خونه ی خود آدم نمیشه',
    'web_url': 'https://divar.ir/v/wXSTyUdO', 
    'price': None, 
    'rent': 1000, 
    'credit': 245000000, 
    'category': 'apartment-rent', 
    'business_type': 'personal', 
    'images': ['https://s100.divarcdn.com/static/pictures/1607624286/wXSTyUdO.webp'], 
    'city': 'مشهد',
    'district': 'آزادشهر'
}
```

```python
from divar import client

divar = client.Divar()
divar.search(city_code=3, category='real-estate')

```

Sample response for search:

```
{
    'last_post_date': 613049590941897, 
    'posts': [
              {'token': 'wXLnEJOQ', 'title': 'فروش زمین باغی در مجتمع شاهنامه محدوده زاک ماریان', 'image': 'https://s100.divarcdn.com/static/thumbnails/1607791740/wXLnEJOQ.webp', 'description': 'توافقی', 'city': 'مشهد', 'district': 'بلوار توس', 'category': 'زمین و کلنگی', 'normal_text': 'لحظاتی پیش در بلوار توس'}, 
              {'token': 'wXULcoir', 'title': 'دفترکار 140متری حاشیه بلوارفردوسی', 'image': '', 'description': 'ودیعه: ۱۰۰,۰۰۰,۰۰۰ تومان\nاجاره ماهیانه: ۴,۰۰۰,۰۰۰ تومان', 'city': 'مشهد', 'district': 'فرامرز عباسی', 'category': 'دفتر کار، اتاق اداری و مطب', 'normal_text': 'لحظاتی پیش در فرامرز عباسی'},
              ...
              {'token': 'wXUL8s-R', 'title': '160متر اپارتمان نوساز حاشیه گلشن ()', 'image': '', 'description': 'ودیعه: ۱۰۰,۰۰۰,۰۰۰ تومان\nاجاره ماهیانه: ۷,۰۰۰,۰۰۰ تومان', 'city': 'مشهد', 'district': 'محله هنرستان', 'category': 'آپارتمان', 'normal_text': 'لحظاتی پیش در محله هنرستان'},
              {'token': 'wXCaNi92', 'title': 'اجاره باغ ویلا واستخرسرپوشیده', 'image': 'https://s100.divarcdn.com/static/thumbnails/1607791726/wXCaNi92.webp', 'description': 'ودیعه: توافقی\nاجاره ماهیانه: توافقی', 'city': 'مشهد', 'district': 'بلوار توس', 'category': 'خانه و ویلا', 'normal_text': 'لحظاتی پیش در بلوار توس'}
             ]
}

```