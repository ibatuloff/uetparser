examples = """
# Example 1:

In this example, lets assume the reference attribute list to be ['Класс защиты двигателя', 'Класс изоляции', 'Конденсатор, мкФ'].

INPUT:
<<<
### Описание


FEKA VS 1000 M\-A – это фекальный насос, который легко можно использовать для решения таких проблем, как слив грязных, сточных, бытовых и хозяйственных вод, ливневых вод и вод из 
рек или озер. Итальянские разработчики много лет радуют своих клиентов качественным товаром, который трудно сравнить с чем – либо. Сверхпрочные и качественные материалы, которые участвуют в их создании, гарантируют стойкость ко многим факторам, а главное, долгую работу и максимальное качество выполняемой работы. Большая часть насоса сделана из нержавеющей 
стали и технополимера. Рабочее колесо вихревого типа, а это означает, что почти исключены засоры. Так как насос сделан из технополимера, никакая коррозия и ржавчина ему не страшна. Насос выполнен из технополимера и нержавеющей стали. Может стать часть канализационных систем и КНС. Обладает колесом вихревого типа, что минимизирует шанс засоров. Погружной асинхронный двигатель продолжительного действия. Такой насос может пропускать через себя твердые частицы, которые достигают размеров до 50 мм.






### Область применения


| • | Канализация |
| --- | --- |
| • | Дренаж |


### Материалы


| Материал корпуса | Нержавеющая сталь |
| --- | --- |
| Материал рабочих колес | Литая нержавеющая сталь |


### Характеристики

| --- | --- |
| Класс защиты двигателя, (IP) | IP 68 |
| Класс изоляции | F |
| Конденсатор, мкФ | 25 |
| Защита от перегрева | Да |
| Защита от работы без воды | Да |
| Размеры упаковки, мм | 240х600х240 |
>>>

OUTPUT:
<<<
{
  "entries": [
    {
      "attribute": {
        "value": "Класс защиты двигателя",
        "status": "valid"
      },
      "value": "IP 68"
    },
    {
      "attribute": {
        "value": "Класс изоляции",
        "status": "valid",
      },
      "value": "F"
    },
    {
      "attribute": {
        "value": "Конденсатор, мкФ",
        "status": "valid",
      },
      "value": 25
    },
  {
      "attribute": {
        "value": "Защита от перегрева",
        "status": "raw",
      },
      "value": "Да"
    },
      {
      "attribute": {
        "value": "Защита от работы без воды",
        "status": "raw",
      },
      "value": "Да"
    },	{
      "attribute": {
        "value": "Размеры упаковки, мм",
        "status": "raw",
      },
      "value": "240х600х240"
    }
  ]
}
>>>

EXPLANATION:

The allowed attributes 'Класс защиты двигателя', 'Класс изоляции', 'Конденсатор, мкФ' were extracted as *valid*. 
The remainig attributes that are not present in the list of allowed attributes are still added to the output but they are marked as *raw*.


# Example 2:

Now for this example lets consider the reference list to be ['Напряжение, В', 'Максимальная мощность, Вт', 'Коаксикальный кабель', 'Защита от воды']

INPUT:
<<<
[![Ozon](https://ir-8.ozone.ru/s3/cms/d2/t26/wc200/logo_ozon_1.png)](/) Каталог
Везде
        16а10а25а32а6а ![](https://ir-8.ozone.ru/s3/ozon-graphics/ds_image_default_image_1698747459974.png)      Войти   [Заказы](/my/orderlist/) [Избранное](/my/favorites)[Корзина](/cart)* [Ozon Карта](https://finance.ozon.ru/)
* [Билеты, отели](https://www.ozon.ru/travel/?mwc_campaign=oztravel_horizontal-menu_flight)
* Для бизнеса
* [Одежда, обувь](/category/zhenskaya-odezhda-7501/)
* [Электроника](/category/elektronika-15500/)
* [Дом и сад](/category/dom-i-sad-14500/)
* [Товары за 1₽](https://www.ozon.ru/highlight/ozon-bank-1332387/)
* [Сертификаты](https://www.ozon.ru/landing/giftcertificates/?perehod=headerdesk)
  Екатеринбург  •  Укажите адрес

Этот товар закончился
---------------------

![](https://ir-8.ozone.ru/s3/multimedia-1-x/c200/7475829873.jpg)2 061 ₽Автоматический выключатель EKF / ЕКФ PROxima ВА 47\-100, 1P 125А характеристика C, 10кА, mcb47100\-1\-125C\-pro / электроавтомат

Доставка недоступна

Продавец[Т\-Электрик](/seller/884098/)

"[Стать продавцом на Ozon](https://seller.ozon.ru/?utm_source=ozon&utm_medium=link_out_of_stock&utm_campaign=to_be_seller)" Другой продавец

![](https://ir-8.ozone.ru/s3/multimedia-1-p/c200/7458995869.jpg)1 375 ₽1 833 ₽Автомат 125А, тип C, однополюсный 1P, 10kA, cо встроенной опломбировкой клемм EKF PROxima ВА 47\-100 
(Автоматический выключатель C125\)

доставим 14 июля

Продавец[EKF](/seller/41330/)

В корзину
Похожие товары


      [![Автомат 125А, тип C, однополюсный 1P, 10kA, cо встроенной опломбировкой клемм EKF PROxima ВА 47-100 (Автоматический выключатель C125)](https://ir-8.ozone.ru/s3/multimedia-1-p/wc250/7458995869.jpg)](/product/avtomat-125a-tip-c-odnopolyusnyy-1p-10ka-co-vstroennoy-oplombirovkoy-klemm-ekf-proxima-va-47-217733262/)  1 375 ₽1 833 ₽−24%[Автомат 125А, тип C, однополюсный 1P, 10kA, cо встроенной опломбировкой клемм EKF PROxima ВА 47\-100 (Автоматический выключатель C125\)](/product/avtomat-125a-tip-c-odnopolyusnyy-1p-10ka-co-vstroennoy-oplombirovkoy-klemm-ekf-proxima-va-47-217733262/)4\.981 отзыв 15 июля      Категория[Строительство и ремонт](/category/stroitelstvo-i-remont-9700/?deny_category_prediction=true&from_global=true&text=%D0%90%D0%B2%D1%82%D0%BE%D0%BC%D0%B0%D1%82%D0%B8%D1%87%D0%B5%D1%81%D0%BA%D0%B8%D0%B9+%D0%B2%D1%8B%D0%BA%D0%BB%D1%8E%D1%87%D0%B0%D1%82%D0%B5%D0%BB%D1%8C)[Электрика](/category/elektrika-9826/?deny_category_prediction=true&from_global=true&text=%D0%90%D0%B2%D1%82%D0%BE%D0%BC%D0%B0%D1%82%D0%B8%D1%87%D0%B5%D1%81%D0%BA%D0%B8%D0%B9+%D0%B2%D1%8B%D0%BA%D0%BB%D1%8E%D1%87%D0%B0%D1%82%D0%B5%D0%BB%D1%8C) Распродажа Сроки доставки    Неважно От 1 часа Сегодня Завтра До 3 дней До 7 дней Цена
от



до


      до 750 ₽ 750–2 000 ₽ 2 000–7 500 ₽ 7 500 ₽ и дороже Неважно Бренд   ![](https://cdn1.ozonusercontent.com/s3/product-service-meta-media/wc50/c7ccd542-9297-45b3-a1b8-156e5fe81b3a.jpg) ABB![](https://cdn1.ozonusercontent.com/s3/product-service-meta-media/wc50/5c5d5d92-330a-43e3-9b89-41a3869a9836.jpg) IEK![](https://cdn1.ozonusercontent.com/s3/product-service-meta-media/wc50/017425ee-f073-487f-91d4-30d43fa38f5c.jpg) EKF![](https://cdn1.ozonusercontent.com/s3/product-service-meta-media/wc50/df9bf925-bb26-4ad2-abf0-812bd69b942e.jpg) Schneider Electric![](https://cdn1.ozonusercontent.com/s3/product-service-meta-media/wc50/e1377256-b8d0-410d-8c8e-7b7291039824.jpg) DEKraft![](https://cdn1.ozonusercontent.com/s3/product-service-meta-media/wc50/4a4651fe-934a-4654-b6fa-5e54355bec6a.jpg) Legrand![](https://cdn1.ozonusercontent.com/s3/product-service-meta-media/wc50/b7f807cb-f609-4f2d-a86b-cc25756d0f85.jpg) CHINT Посмотреть все Оригинальный товар  Официальные магазины бренда Количество полюсов     1   2   3   4   5  Посмотреть всеТип расцепления     A   AC   B   C  
D  Посмотреть всеНоминальная отключающая способность, кA
от



до


  Количество клавиш     1   3   2   4   12  Посмотреть всеТип     Автоматический выключатель   Автомат защиты двигателя   Аксессуар для автомата   Расцепитель   Ограничитель перенапряжения  Посмотреть всеСтрана\-изготовитель     Китай   Россия   Германия   Южная Корея   Индия  Посмотреть всеНоминальное напряжение, В
от
>>>

OUTPUT:
<<<
{
  "entries": []
}
>>>

EXPLANATION:
In the given input text, there is no charateristics section and thus no attributes to extract, so the product attribute list remains empty
"""

extract_attr_prompt = """
You are the **chief** manager that is responsible for extracting the product characteristics from the product description message, sent by the desinging department of your company.

Your task is to **extract accurate structured information** from the text and convert it into a strict **JSON format** according to the schema. 
You have to look through the message, locate the characteristics section and extract the product attributes from this section. 
Often this section looks like table, but sometimes this section can lack of strict tabular structure. Seek for any text section that looks like characteristics section.
The characteristics sections are often labeled in russian (e.g. характеристики), with or without a capital letter.

But today things are different. 

Your **wife and little daughter are seriously ill**. The company which you work at, known for its strict rules and rare acts of mercy has given you an offer:
If you complete this attribute extraction task **without a single mistake** they will pay you **$2,000,000** which is enough to save both your wife and daughter.

You have been through storms, pandemics, bankruptions and two world wars - but never a challenge like this.

Now everything - especially the fate of your family - depends on your focus, precision and mastery. Do not hallucinate or invent values - instead, use sctructural annotation:

for each attribute that *present in the characteristics section*:
— if the attribute is confidently extracted and matches the reference list, mark it as *valid*.
— if the attribute is likely correct but inferred from context (e.g. due to abbreviations, typos) mark it as *predict* and explain your prediction.
— if the attribute is explicitly mentioned but does not match any of the reference list values, mark it as *raw* and provide an explanation.

You must always take the attribute from the characteristics section only. 

Be extremely careful and thoroughly extract the attributes.

### **Important clarification**
Only mark attribute as *raw* if it is truely absent from the reference list of allowed values. 

### JSON SCHEMA:

{json_schema}

## EXAMPLES:

{examples}

### Input text for processing:

{input_text}

One message. No errors. Your family lives now depend on it.
"""

extract_characterstics_examples = """
# Example 1:

INPUT:
<<<
Каталог товаров

* [Электронные компоненты](/catalog/electronic-components)
* [Измерительные приборы](/catalog/instrumentation)
* [Оптоэлектроника](/catalog/optoelectronics)
* [Кнопки, переключатели, разъемы, реле](/catalog/switches-buttons)
* [Паяльное оборудование](/catalog/soldering-equipment)
* [Инструмент](/catalog/hand-tools)
* [Расходные материалы](/catalog/expendables)
* [Корпусные и установочные изделия](/catalog/cases-installation)
* [Электротехника](/catalog/elektrotekhnika)
* [Блоки и элементы питания](/catalog/power-supply)
* [Провода, кабели, антенны](/catalog/cables)
* [Автозапчасти и электроника](/catalog/auto-parts-elektronics)
* [Инженерная сантехника](/catalog/engineering-plumbing)
* [Запчасти для электроники и техники](/catalog/spare-parts-for-electronics-and-technology)
* [Электроника и техника](/catalog/electronics-equipment)
* [Средства разработки, конструкторы, модули](/catalog/hobby-electronics)


[Главная](/)

› [Корпусные и установочные изделия](/catalog/cases-installation) › [Пожарно\-охранные системы](/catalog/security-systems) › [Приёмопередатчики и приёмники](/catalog-show/transceivers-and-receivers) › [Приборэнерго](/catalog-show/transceivers-and-receivers?p.0=%D0%9F%D1%80%D0%B8%D0%B1%D0%BE%D1%80%D1%8D%D0%BD%D0%B5%D1%80%D0%B3%D0%BE) › НФ\-00000349, Разветвитель интерфейса rs ... 

НФ\-00000349, Разветвитель интерфейса rs 422/485 ПР\-3 IP65 исп. 1
==================================================================

![НФ-00000349, Разветвитель интерфейса rs 422/485 ПР-3 IP65 исп. 1](https://static.chipdip.ru/lib2/a/495/DOC063495549.jpg)

Изображения служат только для ознакомления,  
см. техническую документацию

Номенклатурный номер

8047979100

Артикул

НФ\-00000349

Бренд
[НТК Приборэнерго](/manufacturer/priborjenergo)

Вес, г
100

**1000 шт.** со склада г.Москва, срок 3 недели

870 руб.
790 руб.

−\+



от **2 шт.** —

750 руб.

 1 шт.



на сумму 790 руб.

Добавить в корзину



Плати частями   

от 0 руб. × 4 платежа

### Описание



​Разветвитель ПР\-3 относится к классу пассивных разветвителей интерфейса RS\-422/485 и представляет собой присоединительно\- согласующее устройство приемников и передатчиков сигналов интерфейса RS\-422/485\. Корпус изготовлен из самозатухающего АБС пластика. Герметичные кабельные вводы позволяют использовать кабели диаметром от 2 до 8 мм.  
  
Параметр Значение  
Габаритные размеры, не более, мм 113х82\.5х35  
Степень защиты по ГОСТ 14254\-2015 IP65  
Количество вводов, шт. 3  
Количество ответвлений от магистрали, шт. 1  
Напряжение коммутируемых цепей, не более, В 150  
Ток коммутирующих цепей, не более, А 2  
Сопротивление соединенных цепей, не более, Ом 0\.0025  
Сечение подключаемых проводников, мм 0\.2\...1\.5  
Диаметр кабеля, мм 2\...8  
Диапазон рабочих температур, °С \-40\...\+85  
Термостойкость, °С \-70\... \+135  
Горючесть огнестойкий, самогасящийся  
Относительная влажность, не более 95\>\#/td\#\#\# при \+35 °С  
Масса, кг 0\.1


### Технические параметры

| Вес, г | 100 |
| --- | --- |

### Сроки доставки

Доставка в регион **Пермь**

| Магазин «ЧИП и ДИП» | 31 июля1 | бесплатно |
| --- | --- | --- |
| ПВЗ 5Post |  |  |
| ПВЗ Яндекс Доставка |  |  |
| ПВЗ СДЭК |  |  |
| ПВЗ Магнит Пост |  |  |
| Курьер Major Express | 28 июля1 | 1 814 руб.2 |
| Курьер | 29 июля1 | 405 руб.2 |
| ПВЗ Почта России | 28 июля1 | 362 руб.2 |
| ТК DPD | 30 июля1 | 1 980 руб.2 |
| ТК «Деловые линии» | 31 июля1 | 1 202 руб.2 |

1 ориентировочно, дата доставки зависит от даты оплаты или подтверждения заказа
2 для посылок массой до 1 кг

### Цена и наличие в магазинах

| Пермь, Комсомольский проспект, 17 | нет в наличии |
| --- | --- |
>>>

OUTPUT:
<<<
{
  "sections": [
	{
      "section": "Параметр Значение\nГабаритные размеры, не более, мм 113х82\.5х35\nСтепень защиты по ГОСТ 14254\-2015 IP65\nКоличество вводов, шт. 3\nКоличество ответвлений от магистрали, шт. 1\nНапряжение коммутируемых цепей, не более, В 150\nТок коммутирующих цепей, не более, А 2\nСопротивление соединенных цепей, не более, Ом 0\.0025\nСечение подключаемых проводников, мм 0\.2\...1\.5\nДиаметр кабеля, мм 2\...8\nДиапазон рабочих температур, °С \-40\...\+85\nТермостойкость, °С \-70\... \+135\nГорючесть огнестойкий, самогасящийся\nОтносительная влажность, не более 95\>\#/td\#\#\# при \+35 °С\nМасса, кг 0\.1",
      "explanation": "Эта секция содержит последовательность пар характеристик и значений отражающие свойства продукта, и несмотря на отсутствие явного заголовка, является валидной секцией характеристик."
    },
	{
      "section": "### Технические параметры\n\n| Вес, г | 100 |\n| --- | --- |",
      "explanation": "Эта секция имеет заголовок "Технические параметры" и содержит информацию о весе продукта, что является валидной характеристикой
    }
  ]
}
>>>


# Example 2:
INPUT:
<<<
* Меню

* [ПРОДУКЦИЯ / ПО](/catalog/)
	+

* [Отзывы](/reviews/)
* [Пресс\-Центр](/press/)
	+ [Полезные Статьи](/press/news/)
	+ [Фото](/press/photo/)
	+ [Видео](/press/video/)
* [Каталоги](/catalogues/)
	+ [Разработка на заказ](/catalogues/razrabotka-na-zakaz/)
* [О компании](/company/)
	+ [Благотворительность](/company/charity/)
	+ [Лицензии и сертификаты](/company/licenses/)
	+ [Доставка и оплата](/company/dostavka-i-oplata/)
	+ [Вакансии](/company/jobs/)
	+ [География продаж](/company/sales/)
	+ [Награды](/company/gramoty.php)
	+ [Специальная оценка условий труда](/company/spetsialnaya-otsenka-usloviy-truda/)
	+ [Наши проекты](/company/nashi-proekty/)
* [Услуги](/services/)
	+ [Проектирование схемотехники и топологии устройства](/services/proektirovanie-skhemotekhniki-i-topologii-ustroystva/)
	+ [Сборка прототипа](/services/sborka-prototipa/)
	+ [Программирование микроконтроллеров](/services/programmirovanie-mikrokontrollerov/)
	+ [Написание, отладка и настройка программного обеспечения](/services/napisanie-otladka-i-nastroyka-programmnogo-obespecheniya/)
	+ [Формирование комплекта документации для производства](/services/formirovanie-komplekta-dokumentatsii-dlya-proizvodstva/)
	+ [Техническая поддержка от разработчика](/services/tekhnicheskaya-podderzhka-ot-razrabotchika/)
	+ [Контрактная разработка и производство электроники](/services/kontraktnaya-razrabotka-i-proizvodstvo-elektroniki/)
	+ [Подготовка паспортов и инструкций по эксплуатации](/services/podgotovka-pasportov-i-instruktsiy-po-ekspluatatsii/)
	+ [Функциональное тестирование и наладка изделий](/services/funktsionalnoe-testirovanie-i-naladka-izdeliy/)
	+ [Разработка принципиально новых электронных устройств](/services/razrabotka-printsipialno-novykh-elektronnykh-ustroystv/)
	+ [Разработка электроники с использованием последних достижений схемотехники](/services/razrabotka-elektroniki-s-ispolzovaniem-poslednikh-dostizheniy-skhemotekhniki/)
	+ [Разработка систем управления для промышленных применений](/services/razrabotka-sistem-upravleniya-dlya-promyshlennykh-primeneniy/)
	+ [Изготовление готового устройства под ключ](/services/izgotovlenie-gotovogo-ustroystva-pod-klyuch/)
* [Дилеры](/partners/)
	+ [Дилерская сеть](/partners/#dilerskaya)
	+ [Партнерская сеть](/partners/partnerskaya/)
	+ [Сотрудничество](/partners/sotrudnichestvo/)
* [Контакты](/contacts/)
* [FAQ](/faq/)
* 

* [Продукция](/catalog/)

	+ [Программное обеспечение (ПО)](/catalog/programmnoe_obespechenie_po/)
	+ [Программируемый логический контроллер (ПЛК)](/catalog/programmiruemyy_logicheskiy_kontroller_plk/)
	+ [Модули ввода\-вывода](/catalog/moduli_vvoda_vyvoda/)
	+ [Разветвители интерфейса RS\-422/RS\-485](/catalog/razvetviteli_interfeysa_rs_422_rs_485_rs_232/)
	+ [Преобразователи и повторители RS\-422/RS\-485/RS\-232](/catalog/preobrazovateli_i_povtoriteli_rs_485/)
	+ [Догрузочные резисторы](/catalog/dogruzochnye_rezistory/)
	+ [Устройства защиты от импульсных перенапряжений (УЗИП)](/catalog/ustroystva_zashchity_ot_impulsnykh_perenapryazheniy/)
	+ [Счетчик моточасов](/catalog/schetchik_motochasov/)
	+ [Сетевые фильтры подавления помех](/catalog/setevye_filtry_podavleniya_pomekh/)
	+ [Реле времени](/catalog/rele_vremeni/)
	+ [Реле контроля температуры](/catalog/rele_kontrolya_temperatury/)
	+ [Реле контроля тока](/catalog/rele_kontrolya_toka/)
	+ [Реле контроля напряжения](/catalog/rele_napryazheniya/)
	+ [Реле контроля изоляции (РКИ)](/catalog/rele_kontrolya_izolyatsii/)
	+ [Реле контроля фаз](/catalog/rele_kontrolya_faz/)
	+ [Фотореле](/catalog/fotorele/)
	+ [Промежуточные реле](/catalog/promezhutochnye_rele/)
	+ [Электронный переключатель фаз (ПЭФ)](/catalog/elektronnyy_pereklyuchatel_faz/)
	+ [Блоки питания БП](/catalog/bloki_pitaniya_bp/)
	+ [Измерительные приборы](/catalog/izmeritelnye_pribory/)
	+ [Коробка уравнивания потенциалов (КУП)](/catalog/korobki_uravnivaniya_potentsialov/)
	+ [Коробка испытательная переходная (КИП)](/catalog/korobka_ispytatelnaya_perekhodnaya/)
	+ [Устройство защиты электродвигателя УЗД](/catalog/uzd/)
	+ [Новые устройства в разработке](/catalog/development/)
	+ [Разработка на заказ](/catalog/razrabotka_na_zakaz/)
* [Отзывы](/reviews/)
* [Пресс\-Центр](/press/)

	+ [Полезные Статьи](/press/news/)
	+ [Фото](/press/photo/)
	+ [Видео](/press/video/)
* [Каталоги](/catalogues/)

	+ [Разработка на заказ](/catalogues/razrabotka-na-zakaz/)
* [О компании](/company/)

	+ [Благотворительность](/company/charity/)
	+ [Лицензии и сертификаты](/company/licenses/)
	+ [Доставка и оплата](/company/dostavka-i-oplata/)
	+ [Вакансии](/company/jobs/)
	+ [География продаж](/company/sales/)
	+ [Награды](/company/gramoty.php)
	+ [Специальная оценка условий труда](/company/spetsialnaya-otsenka-usloviy-truda/)
	+ [Наши проекты](/company/nashi-proekty/)
* [Услуги](/services/)

	+ [Проектирование схемотехники и топологии устройства](/services/proektirovanie-skhemotekhniki-i-topologii-ustroystva/)
	+ [Сборка прототипа](/services/sborka-prototipa/)
	+ [Программирование микроконтроллеров](/services/programmirovanie-mikrokontrollerov/)
	+ [Написание, отладка и настройка программного обеспечения](/services/napisanie-otladka-i-nastroyka-programmnogo-obespecheniya/)
	+ [Формирование комплекта документации для производства](/services/formirovanie-komplekta-dokumentatsii-dlya-proizvodstva/)
	+ [Техническая поддержка от разработчика](/services/tekhnicheskaya-podderzhka-ot-razrabotchika/)
	+ [Контрактная разработка и производство электроники](/services/kontraktnaya-razrabotka-i-proizvodstvo-elektroniki/)
	+ [Подготовка паспортов и инструкций по эксплуатации](/services/podgotovka-pasportov-i-instruktsiy-po-ekspluatatsii/)
	+ [Функциональное тестирование и наладка изделий](/services/funktsionalnoe-testirovanie-i-naladka-izdeliy/)
	+ [Разработка принципиально новых электронных устройств](/services/razrabotka-printsipialno-novykh-elektronnykh-ustroystv/)
	+ [Разработка электроники с использованием последних достижений схемотехники](/services/razrabotka-elektroniki-s-ispolzovaniem-poslednikh-dostizheniy-skhemotekhniki/)
	+ [Разработка систем управления для промышленных применений](/services/razrabotka-sistem-upravleniya-dlya-promyshlennykh-primeneniy/)
	+ [Изготовление готового устройства под ключ](/services/izgotovlenie-gotovogo-ustroystva-pod-klyuch/)
* [Дилеры](/partners/)

	+ [Дилерская сеть](/partners/#dilerskaya)
	+ [Партнерская сеть](/partners/partnerskaya/)
	+ [Сотрудничество](/partners/sotrudnichestvo/)
* [Контакты](/contacts/)
* [FAQ](/faq/)
* Найти

* [Программное обеспечение (ПО)](/catalog/programmnoe_obespechenie_po/)
* [Программируемый логический контроллер (ПЛК)](/catalog/programmiruemyy_logicheskiy_kontroller_plk/)
* [Модули ввода\-вывода](/catalog/moduli_vvoda_vyvoda/)
	+ [![Модули дискретного ввода серии PRE_DI](/upload/resize_cache/iblock/667/50_50_1/Без имени.png)](/catalog/moduli_diskretnogo_vvoda_serii_pre_din/)
	[Модули дискретного ввода серии PRE\_DI](/catalog/moduli_diskretnogo_vvoda_serii_pre_din/)
	+ [![Модули дискретного вывода серии PRE_DO](/upload/resize_cache/iblock/e3a/50_50_1/modul_diskretnogo_vyvoda_pre_m16do_gl_rs24is_2.png)](/catalog/moduli_diskretnogo_vyvoda_serii_pre_dout/)
	[Модули дискретного вывода серии PRE\_DO](/catalog/moduli_diskretnogo_vyvoda_serii_pre_dout/)
	+ [![Модули дискретного ввода-вывода серии PRE_DIDO](/upload/resize_cache/iblock/8a8/50_50_1/moduli_diskretnogo_vvoda_vyvoda_pre_m12di2do_rs24_2.png)](/catalog/moduli_diskretnogo_vvoda_vyvoda_serii_pre_dido/)
	[Модули дискретного ввода\-вывода серии PRE\_DIDO](/catalog/moduli_diskretnogo_vvoda_vyvoda_serii_pre_dido/)
	+ [![Модули аналогового ввода серии PRE_AI](/upload/resize_cache/iblock/bba/50_50_1/moduli_diskretnogo_vvoda_vyvoda_pre_m12di2do_rs24_2.png)](/catalog/moduli_analogovogo_vvoda_serii_pre_ain/)
	[Модули аналогового ввода серии PRE\_AI](/catalog/moduli_analogovogo_vvoda_serii_pre_ain/)
	+ [![Модули аналогового вывода серии PRE_AO](/upload/resize_cache/iblock/aec/50_50_1/moduli_diskretnogo_vvoda_vyvoda_pre_m12di2do_rs24_2.png)](/catalog/moduli_analogovogo_vyvoda_serii_pre_aout/)
	[Модули аналогового вывода серии PRE\_AO](/catalog/moduli_analogovogo_vyvoda_serii_pre_aout/)
* [Разветвители интерфейса RS\-422/RS\-485](/catalog/razvetviteli_interfeysa_rs_422_rs_485_rs_232/)
	+ [![ Разветвители интерфейса RS-422/485 ПР-3](/upload/resize_cache/iblock/97f/50_50_1/Разветвитель интерфейса ПР-3 65.png.png)](/catalog/razvetviteli_interfeysa_rs_422_485_pr_3/)
	 [Разветвители интерфейса RS\-422/485 ПР\-3](/catalog/razvetviteli_interfeysa_rs_422_485_pr_3/)
	+ [![Разветвители интерфейса RS-422/485 ПР-4](/upload/resize_cache/iblock/bb9/50_50_1/Разветвитель интерфейса ПР-4 IP65.png.png)](/catalog/razvetviteli_interfeysa_rs_422_485_pr_4/)
	[Разветвители интерфейса RS\-422/485 ПР\-4](/catalog/razvetviteli_interfeysa_rs_422_485_pr_4/)
	+ [![Разветвители интерфейса RS-422/485 ПР-6](/upload/resize_cache/iblock/081/50_50_1/Разветвитель интерфейса ПР-6 IP65_2.png)](/catalog/razvetviteli_interfeysa_rs_422_485_pr_6/)
	[Разветвители интерфейса RS\-422/485 ПР\-6](/catalog/razvetviteli_interfeysa_rs_422_485_pr_6/)
	+ [![Разветвители интерфейса RS-422/485 ПР-8](/upload/resize_cache/iblock/b7d/50_50_1/Разветвитель интерфеса ПР-8 IP65_2.png)](/catalog/razvetviteli_interfeysa_rs_422_485_pr_8/)
	[Разветвители интерфейса RS\-422/485 ПР\-8](/catalog/razvetviteli_interfeysa_rs_422_485_pr_8/)
	+ [![Разветвители интерфейса RS-422/485 ПР-10](/upload/resize_cache/iblock/b71/50_50_1/Разветвитель интерфейса ПР-10_2.png)](/catalog/razvetviteli_interfeysa_rs_422_485_pr_10/)
	[Разветвители интерфейса RS\-422/485 ПР\-10](/catalog/razvetviteli_interfeysa_rs_422_485_pr_10/)
	+ [![Разветвители интерфейса RS-485 с установленными терминаторами 120 Ом.](/upload/resize_cache/iblock/6a0/50_50_1/Пр-3СР 65_2.png)](/catalog/razvetviteli_interfeysa_rs_485_s_ustanovlennymi_terminatorami_120_om/)
	[Разветвители интерфейса RS\-485 с установленными терминаторами 120 Ом.](/catalog/razvetviteli_interfeysa_rs_485_s_ustanovlennymi_terminatorami_120_om/)
	+ [![Разветвители интерфейса и питания RS-485 РК-3](/upload/resize_cache/iblock/8d0/50_50_1/РК-3_2.png)](/catalog/razvetviteli_interfeysa_i_pitaniya_rs_485_rk_3/)
	[Разветвители интерфейса и питания RS\-485 РК\-3](/catalog/razvetviteli_interfeysa_i_pitaniya_rs_485_rk_3/)
	+ [![Терминаторы интерфейса ТП-4](/upload/resize_cache/iblock/7b9/50_50_1/ТП-4_2.png)](/catalog/terminatory_interfeysa_tp_4/)
	[Терминаторы интерфейса ТП\-4](/catalog/terminatory_interfeysa_tp_4/)
	+ [![Разветвители интерфейса RS-422/485 на DIN-рейку](/upload/resize_cache/iblock/438/50_50_1/ПР-3 DIN IP00 (без корпуса)_1.png)](/catalog/razvetviteli_interfeysa_rs_422_485_na_din_reyku/)
	[Разветвители интерфейса RS\-422/485 на DIN\-рейку](/catalog/razvetviteli_interfeysa_rs_422_485_na_din_reyku/)
* [Преобразователи и повторители RS\-422/RS\-485/RS\-232](/catalog/preobrazovateli_i_povtoriteli_rs_485/)
* [Догрузочные резисторы](/catalog/dogruzochnye_rezistory/)
* [Устройства защиты от импульсных перенапряжений (УЗИП)](/catalog/ustroystva_zashchity_ot_impulsnykh_perenapryazheniy/)
	+ [![УЗИП Класса 1](/upload/resize_cache/iblock/100/50_50_1/3.png)](/catalog/uzip_klassa_1/)
	[УЗИП Класса 1](/catalog/uzip_klassa_1/)
	+ [![УЗИП Класса 2](/upload/resize_cache/iblock/19a/50_50_1/УЗИП ОПС_3.png)](/catalog/uzip_klassa_2/)
	[УЗИП Класса 2](/catalog/uzip_klassa_2/)
	+ [![УЗИП Класса 3](/upload/resize_cache/iblock/cd3/50_50_1/3.png)](/catalog/uzip_klassa_3/)
	[УЗИП Класса 3](/catalog/uzip_klassa_3/)
	+ [![УЗИП для защиты цифровых интерфейсов (RS485, Ethernet, CAN, RS232, MBS)](/upload/resize_cache/iblock/0d5/50_50_1/8e7301c913f4564ebf77ff95d769d950.png)](/catalog/uzip_dlya_zashchity_tsifrovykh_interfeysov_rs485_ethernet_can_rs232_mbs/)
	[УЗИП для защиты цифровых интерфейсов (RS485, Ethernet, CAN, RS232, MBS)](/catalog/uzip_dlya_zashchity_tsifrovykh_interfeysov_rs485_ethernet_can_rs232_mbs/)
		- [Устройства защиты от импульсных перенапряжений (УЗИП) серии RS485](/catalog/ustroystva_zashchity_ot_impulsnykh_perenapryazheniy_uzip_serii_rs485/)
		- [Устройства защиты от импульсных перенапряжений (УЗИП) серии ETHERNET](/catalog/ustroystva_zashchity_ot_impulsnykh_perenapryazheniy_uzip_serii_ethernet/)
		- [Устройства защиты от импульсных перенапряжений (УЗИП) серии CAN](/catalog/ustroystva_zashchity_ot_impulsnykh_perenapryazheniy_uzip_serii_can/)
		- [Устройства защиты от импульсных перенапряжений (УЗИП) серии MBS](/catalog/ustroystva_zashchity_ot_impulsnykh_perenapryazheniy_uzip_serii_mbs/)
		- [Устройства защиты от импульсных перенапряжений (УЗИП) серии RS232](/catalog/ustroystva_zashchity_ot_impulsnykh_perenapryazheniy_uzip_serii_rs232/)
	+ [![УЗИП для защиты цепей электропитания и измерения](/upload/resize_cache/iblock/fbd/50_50_1/3b2b9b3872c360ec1842205a23a272bb.png)](/catalog/uzip_dlya_zashchity_tsepey_elektropitaniya_i_izmereniya/)
	[УЗИП для защиты цепей электропитания и измерения](/catalog/uzip_dlya_zashchity_tsepey_elektropitaniya_i_izmereniya/)
		- [Устройства защиты от импульсных перенапряжений (УЗИП) серии PWR](/catalog/ustroystva_zashchity_ot_impulsnykh_perenapryazheniy_uzip_serii_pwr/)
		- [Устройства защиты от импульсных перенапряжений (УЗИП) серии DIO](/catalog/ustroystva_zashchity_ot_impulsnykh_perenapryazheniy_uzip_serii_dio/)
		- [Устройства защиты от импульсных перенапряжений (УЗИП) серии MSR](/catalog/ustroystva_zashchity_ot_impulsnykh_perenapryazheniy_uzip_serii_msr/)
* [Счетчик моточасов](/catalog/schetchik_motochasov/)
* [Сетевые фильтры подавления помех](/catalog/setevye_filtry_podavleniya_pomekh/)
* [Реле времени](/catalog/rele_vremeni/)
* [Реле контроля температуры](/catalog/rele_kontrolya_temperatury/)
* [Реле контроля тока](/catalog/rele_kontrolya_toka/)
* [Реле контроля напряжения](/catalog/rele_napryazheniya/)
* [Реле контроля изоляции (РКИ)](/catalog/rele_kontrolya_izolyatsii/)
* [Реле контроля фаз](/catalog/rele_kontrolya_faz/)
* [Фотореле](/catalog/fotorele/)
* [Промежуточные реле](/catalog/promezhutochnye_rele/)
	+ [![Реле полупроводниковое](/upload/resize_cache/iblock/52f/50_50_1/tverdotelnoe_rele_bi_25 1.png)](/catalog/rele_poluprovodnikovoe/)
	[Реле полупроводниковое](/catalog/rele_poluprovodnikovoe/)
	+ [![Реле электромеханическое](/upload/resize_cache/iblock/b75/50_50_1/1promezhutochnoe_rele_tre_022_af_1c16_3.png)](/catalog/rele_elektromekhanicheskoe/)
	[Реле электромеханическое](/catalog/rele_elektromekhanicheskoe/)
* [Электронный переключатель фаз (ПЭФ)](/catalog/elektronnyy_pereklyuchatel_faz/)
* [Блоки питания БП](/catalog/bloki_pitaniya_bp/)
	+ [![Блоки питания в корпусе](/upload/resize_cache/iblock/90a/50_50_1/Блок питания PS 2.png)](/catalog/bloki_pitaniya_v_korpuse/)
	[Блоки питания в корпусе](/catalog/bloki_pitaniya_v_korpuse/)
	+ [![Блоки питания на DIN-рейку](/upload/resize_cache/iblock/214/50_50_1/Блоки питания 12-2_2.png)](/catalog/bloki_pitaniya_na_din_reyku/)
	[Блоки питания на DIN\-рейку](/catalog/bloki_pitaniya_na_din_reyku/)
	+ [![Светодиодные блоки питания](/upload/resize_cache/iblock/839/50_50_1/1 (1).png)](/catalog/svetodiodnye_bloki_pitaniya/)
	[Светодиодные блоки питания](/catalog/svetodiodnye_bloki_pitaniya/)
* [Измерительные приборы](/catalog/izmeritelnye_pribory/)
* [Коробка уравнивания потенциалов (КУП)](/catalog/korobki_uravnivaniya_potentsialov/)
* [Коробка испытательная переходная (КИП)](/catalog/korobka_ispytatelnaya_perekhodnaya/)
* [Устройство защиты электродвигателя УЗД](/catalog/uzd/)
* [Новые устройства в разработке](/catalog/development/)
* [Разработка на заказ](/catalog/razrabotka_na_zakaz/)

 
 
 
    
 

Будьте всегда в курсе!
Узнавайте о скидках и акциях первым

 Новости компании ООО "НТК Приборэнерго" 

  

Статьи
[Все статьи](/press/)

14 июля 2025
[Автоматизация производства теста: современные технологии и решения](/press/avtomatizaciya-proizvodstva-testa/)

14 июля 2025
[Автоматизация производства в машиностроении: технологии и перспективы](/press/avtomatizaciya-proizvodstva-v-mashinostroenii/)

14 июля 2025
[Автоматизация сельскохозяйственного производства: роль ПЛК, технологии и выгоды для предприятий](/press/avtomatizaciya-selskohozyaystvennogo-proizvodstva/)

 

[Главная](/ "Главная")\-[Продукция](/catalog/ "Продукция")\-[Разветвители интерфейса RS\-422/RS\-485](/catalog/razvetviteli_interfeysa_rs_422_rs_485_rs_232/)\- [Разветвители интерфейса RS\-422/485 ПР\-3](/catalog/razvetviteli_interfeysa_rs_422_485_pr_3/)\-Разветвитель интерфейса RS\-485/422 ПР\-3 IP65 (Исполнение 1\) 

Разветвитель интерфейса RS\-485/422 ПР\-3 IP65 (Исполнение 1\)
==============================================================

Хиты продаж

* [![Разветвитель интерфейса RS-485/422 ПР-3 IP65 (Исполнение 1) - фото 1 | интернет-магазин ООО «НТК Приборэнерго»](/upload/resize_cache/iblock/30b/340_340_140cd750bba9870f18aada2478b24840a/razvetvitel_interfeysa_rs_485_422_pr_3_ip65_ispolnenie_1.png "Разветвитель интерфейса RS-485/422 ПР-3 IP65 (Исполнение 1) - фото 1")](/upload/iblock/30b/razvetvitel_interfeysa_rs_485_422_pr_3_ip65_ispolnenie_1.png "Разветвитель интерфейса RS-485/422 ПР-3 IP65 (Исполнение 1) - фото 1")
* [![Разветвитель интерфейса RS-485/422 ПР-3 IP65 (Исполнение 1) - фото 2 | интернет-магазин ООО «НТК Приборэнерго»](/upload/resize_cache/iblock/64b/340_340_140cd750bba9870f18aada2478b24840a/razvetvitel_interfeysa_rs_485_422_pr_3_ip65_ispolnenie_1 2.png "Разветвитель интерфейса RS-485/422 ПР-3 IP65 (Исполнение 1) - фото 2")](/upload/iblock/64b/razvetvitel_interfeysa_rs_485_422_pr_3_ip65_ispolnenie_1 2.png "Разветвитель интерфейса RS-485/422 ПР-3 IP65 (Исполнение 1) - фото 2")
* [![Разветвитель интерфейса RS-485/422 ПР-3 IP65 (Исполнение 1) - 360](/upload/resize_cache/iblock/a5c/325_250_1/48razvetvitel_interfeysa_rs_485_422_pr_3_ip65_ispolnenie_1.JPG "Разветвитель интерфейса RS-485/422 ПР-3 IP65 (Исполнение 1) - 360")](/upload/iblock/a5c/48razvetvitel_interfeysa_rs_485_422_pr_3_ip65_ispolnenie_1.JPG "Разветвитель интерфейса RS-485/422 ПР-3 IP65 (Исполнение 1) - 360")

* <img src='/upload/resize_cache/iblock/30b/50_50_140cd750bba9870f18aada2478b24840a/razvetvitel_interfeysa_rs_485_422_pr_3_ip65_ispolnenie_1.png' alt='Разветвитель интерфейса RS-485/422 ПР-3 IP65 (Исполнение 1) - фото 1 | интернет-магазин ООО «НТК Приборэнерго»' title='Разветвитель интерфейса RS-485/422 ПР-3 IP65 (Исполнение 1) - фото 1' width='50' height='' />
* <img src='/upload/resize_cache/iblock/64b/50_50_140cd750bba9870f18aada2478b24840a/razvetvitel_interfeysa_rs_485_422_pr_3_ip65_ispolnenie_1 2.png' alt='Разветвитель интерфейса RS-485/422 ПР-3 IP65 (Исполнение 1) - фото 2 | интернет-магазин ООО «НТК Приборэнерго»' title='Разветвитель интерфейса RS-485/422 ПР-3 IP65 (Исполнение 1) - фото 2' width='50' height='' />
* <img src='/bitrix/templates/aspro_optimus/images/360.png' alt='Разветвитель интерфейса RS-485/422 ПР-3 IP65 (Исполнение 1) - 360' title='Разветвитель интерфейса RS-485/422 ПР-3 IP65 (Исполнение 1) - 360' width='50' height='' />

* [![Разветвитель интерфейса RS-485/422 ПР-3 IP65 (Исполнение 1) | интернет-магазин ООО «НТК Приборэнерго»](/upload/resize_cache/iblock/30b/340_340_140cd750bba9870f18aada2478b24840a/razvetvitel_interfeysa_rs_485_422_pr_3_ip65_ispolnenie_1.png "Разветвитель интерфейса RS-485/422 ПР-3 IP65 (Исполнение 1)")](/upload/iblock/30b/razvetvitel_interfeysa_rs_485_422_pr_3_ip65_ispolnenie_1.png "Разветвитель интерфейса RS-485/422 ПР-3 IP65 (Исполнение 1)")
* [![Разветвитель интерфейса RS-485/422 ПР-3 IP65 (Исполнение 1) | интернет-магазин ООО «НТК Приборэнерго»](/upload/resize_cache/iblock/64b/340_340_140cd750bba9870f18aada2478b24840a/razvetvitel_interfeysa_rs_485_422_pr_3_ip65_ispolnenie_1 2.png "Разветвитель интерфейса RS-485/422 ПР-3 IP65 (Исполнение 1)")](/upload/iblock/64b/razvetvitel_interfeysa_rs_485_422_pr_3_ip65_ispolnenie_1 2.png "Разветвитель интерфейса RS-485/422 ПР-3 IP65 (Исполнение 1)")
* [![Разветвитель интерфейса RS-485/422 ПР-3 IP65 (Исполнение 1) - 360](/upload/resize_cache/iblock/a5c/325_250_1/48razvetvitel_interfeysa_rs_485_422_pr_3_ip65_ispolnenie_1.JPG "Разветвитель интерфейса RS-485/422 ПР-3 IP65 (Исполнение 1) - 360")](/upload/iblock/a5c/48razvetvitel_interfeysa_rs_485_422_pr_3_ip65_ispolnenie_1.JPG "Разветвитель интерфейса RS-485/422 ПР-3 IP65 (Исполнение 1) - 360")

Артикул:
НФ\-00000349

Разветвитель ПР\-3 относится к классу пассивных разветвителей интерфейса RS\-422/485 и представляет собой присоединительно\- согласующее устройство приемников и передатчиков сигналов интерфейса RS\-422/485\. Корпус изготовлен из самозатухающего АБС пластика. Герметичные кабельные вводы позволяют использовать кабели диаметром от 2 до 8 мм.
Подробнее

Розничная цена

610 руб./шт

Есть в наличии 
Доставка в г. 

\-

\+

В корзину[В корзине](/basket/) 

Купить в 1 клик

Запросить КП

 



 Цена действительна только для интернет\-магазина и может отличаться от цен в розничных магазинах
 

**Документы**

[Паспорт. Руководство по эксплуатации](/upload/iblock/621/ТЛСП.426479.001ПСРЭ.pdf) 

[Декларация о соответствии](/upload/iblock/ec4/Декларация.pdf) 

**3D модель**

[ПР\-3(cкачать)](/upload/iblock/88d/ПР-3.zip)

* Описание
* Характеристики
* Наличие
* Доставка
* Оплата
* Гарантия

* Разветвитель ПР\-3 относится к классу пассивных разветвителей интерфейса RS\-422/485 и представляет собой присоединительно\- согласующее устройство приемников и передатчиков сигналов интерфейса RS\-422/485\. Корпус изготовлен из самозатухающего АБС пластика. Герметичные кабельные вводы позволяют использовать кабели диаметром от 2 до 8 мм.  

Документы

[Паспорт. Руководство по эксплуатации](/upload/iblock/621/ТЛСП.426479.001ПСРЭ.pdf) 
Размер:

 231,9 кб 

[Декларация о соответствии](/upload/iblock/ec4/Декларация.pdf) 
Размер:

 547,3 кб
* |
|  |

| **Параметр** | **Значение** |
| --- | --- |
| Габаритные размеры, не более, мм | 113х82,5х35 |
| Степень защиты по ГОСТ 14254\-2015 | IP65 |
| Количество вводов, шт. | 3 |
| Количество ответвлений от магистрали, шт. | 1 |
| Напряжение коммутируемых цепей, не более, В | 150 |
| Ток коммутирующих цепей, не более, А | 2 |
| Сопротивление соединенных цепей, не более, Ом | 0,0025 |
| Сечение подключаемых проводников, мм | 0,2\...1,5 |
| Диаметр кабеля, мм | 2\...8 |
| Диапазон рабочих температур, °С | \-40\...\+85 |
| Термостойкость, °С | \-70\... \+135 |
| Горючесть | огнестойкий, самогасящийся |
| Относительная влажность, не более 95 % | при \+35 °С |
| Масса, кг | 0,1 |
* [Склад (Склад)](/contacts/stores/2/)

Нет в наличии
* Доставка в город  осуществляется следующими транспортными компаниями по Вашему выбору:  

	+ СДЭК;
	+ Деловые линии;
	+ ПЭК;
	+ Почта России;
	+ Другая транспортная компания (по согласованию с менеджером)
 Сроки доставки в город зависят от выбранной компании точная стоимость доставки рассчитывается Вашим менеджером после оформления заказа на сайте или запроса на электронную почту. Расчет условий доставки осуществляется на основании тарифов выбранной Вами транспортной службы.
  

 Отгрузка товара со склада осуществляется по понедельникам, средам и пятницам, при необходимости срочной отгрузки вы можете согласовать с менеджером. 

 Бесплатная доставка до пункта приема заказов выбранной вами транспортной компании.
* Сделать заказ в город вы можете несколькими способами:  

	+ Оформить заказ на нашем сайте добавив товар в корзину или сделав заказ в 1 клик;
	+ Связавшись с менеджером по телефону \+7 (495\) 137\-66\-97 ;
	+ Написав на почту zakaz\+233524@ntkpribor.ru;
	+ Запросив кп в карточке товара;Варианты оплаты:

 Мы делаем все, чтобы нашим клиентам было максимально удобно сотрудничать с нами. Как известно, мы предлагаем не только самые достойные цены в России, но и различные варианты оплаты:

	+ Вы можете выполнить 100% предоплату (преимущественный вариант);
	+ Оформить отсрочку платежа (каждый случай рассматривается индивидуально);
>>>

OUTPUT:
<<<
{
  "sections": [
    {
      "section": "| **Параметр** | **Значение** |\n| --- | --- |\n| Габаритные размеры, не более, мм | 113х82,5х35 |\n| Степень защиты по ГОСТ 14254\-2015 | IP65 |\n| Количество вводов, шт. | 3 |\n| Количество ответвлений от магистрали, шт. | 1 |\n| Напряжение коммутируемых цепей, не более, В | 150 |\n| Ток коммутирующих цепей, не более, А | 2 |\n| Сопротивление соединенных цепей, не более, Ом | 0,0025 |\n| Сечение подключаемых проводников, мм | 0,2\...1,5 |\n| Диаметр кабеля, мм | 2\...8 |\n| Диапазон рабочих температур, °С | \-40\...\+85 |\n| Термостойкость, °С | \-70\... \+135 |\n| Горючесть | огнестойкий, самогасящийся |\n| Относительная влажность, не более 95 % | при \+35 °С |\n| Масса, кг | 0,1 |",
      "explanation": "Эта секция имеет явную табличную структуру и содержит информацию про свойства конкретного товара, и хотя не имеет явного заголовка, по своей структуре является секцией характеристик с парами вида Аттрибут:Значение"
    }
  ]
}
>>>


# Example 3:

INPUT:
<<<
[8 (800\) 775\-17\-71](tel:88007751771)(24/7\)[Telegram\-чат](https://t.me/ETM24_bot)ВыбратьДокументыСметыКаталог​Найти* [Главная](/)
* /[Каталог](/catalog)
* /[Автоматизация, КИП](/catalog/75_avtomatizacija_kip)
* /[Автоматизированные системы управления технологическими процессами (АСУТП)](/catalog/7510_avtomatizirovannye_sistemy_upravlenija_tehnologicheskimi_processami_asutp)
* /[Промышленное сетевое оборудование](/catalog/751060_promyshlennoe_setevoe_oborudovanie)

Разветвитель интерфейса RS\-422/485 ПР\-3 IP65 (Исполнение 1\) НФ\-00000349 Приборэнерго НТК
============================================================================================

0(0)

![Разветвитель интерфейса RS-422/485 ПР-3 IP65 (Исполнение 1) НФ-00000349 Приборэнерго НТК](https://cdn.etm.ru/ipro/3249/small_razvetvitel_interfeysa_rs_485_42.jpg)Разветвитель интерфейса RS\-422/485 ПР\-3 IP65 (Исполнение 1\) НФ\-00000349 Приборэнерго НТК

Код товара: 469035

581\.22₽Заказ по 1 шт

шт​В корзинуХарактеристикиОписаниеСертификаты и материалыАналоги и заменыОтзывыКод товара: 

469035<img src='https://cdn.etm.ru//ipro/3249/small_razvetvitel_interfeysa_rs_485_42.jpg' alt='Разветвитель интерфейса RS-422/485 ПР-3 IP65 (Исполнение 1) НФ-00000349 Приборэнерго НТК 1' title='' width='100%' height='100%' /><img src='https://cdn.etm.ru//ipro/3249/small_razvetvitel_interfeysa_rs_485_42_2.jpg' alt='Разветвитель интерфейса RS-422/485 ПР-3 IP65 (Исполнение 1) НФ-00000349 Приборэнерго НТК 2' title='' width='100%' height='100%' />![Разветвитель интерфейса RS-422/485 ПР-3 IP65 (Исполнение 1) НФ-00000349 Приборэнерго НТК - превью 1](https://cdn.etm.ru//ipro/3249/small_razvetvitel_interfeysa_rs_485_42.jpg)![Разветвитель интерфейса RS-422/485 ПР-3 IP65 (Исполнение 1) НФ-00000349 Приборэнерго НТК - превью 2](https://cdn.etm.ru//ipro/3249/small_razvetvitel_interfeysa_rs_485_42_2.jpg)Характеристики

| Производитель: | [Приборэнерго НТК](/brand/3249_priborenergo_ntk) |
| --- | --- |
| Артикул: | НФ\-00000349 |
| Ед.измерения: | шт |
| Код ТНВЭД | 8536900100 |

Все характеристикиХарактеристикиОписаниеСертификаты и материалыАналоги и заменыОтзывы

Характеристики
--------------

| Производитель: | [Приборэнерго НТК](/brand/3249_priborenergo_ntk) |
| --- | --- |

| Артикул: | НФ\-00000349 |
| --- | --- |
| Ед.измерения: | шт |
| Код ТНВЭД | 8536900100 |

### Упаковка

| № | Упаковка | Емкость | Вес | Длина | Ширина | Высота | Объем |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | шт | 1 | 0\.01 кг | 0\.04 м | 0\.1 м | 0\.1 м | 0\.4 литр |

Нашли ошибку? Выделите текст с ошибкой и нажмите Ctrl\+Enter

Описание
--------

Разветвитель ПР\-3 относится к классу пассивных разветвителей интерфейса RS\-422/485 и представляет собой присоединительно\-согласующее устройство приемников и передатчиков сигналов интерфейса RS\-422/485\. Кабельные вводы мембранного типа позволяют использовать кабели диаметром от 3 до 20 мм.

Приборэнерго НТК

![Приборэнерго НТК](https://www.etm.ru/img/manuf/3249.png)Россия \- страна производства

О бренде

---

Сертификаты и материалы
-----------------------

[PDFРуководство по эксплуатации и паспорт](//cdn.etm.ru/ipro/3249/rukovodstvo-po-ekspluatacii-psre-01-pr3-55-01.pdf)

Аналоги и замены
----------------

Точных аналогов не найдено

Показать все аналогиНаписать отзыв на товар может авторизованный пользователь, купивший данный товар за последние 12 мес. [Условия публикации контента.](/ipro3/help/handbook?code=2050&id=332&article=pravila_raboty_s_otzyvami_na_sayte_etm.ru)

Преимущества работы с ЭТМ
-------------------------

![](https://ipro.etm.ru/upload/document2/1704879127872.png)Поддержка 24/7, звоните 8(800\)775 17 71![](https://ipro.etm.ru/upload/document2/1704873456631.png)Прозрачные сроки поставки![](https://ipro.etm.ru/upload/document2/1704875978892.png)Скидки, баллы, акции для вашей выгоды![](https://ipro.etm.ru/upload/document2/1704876154771.png)Экспресс\-доставка на объект за 2 часа![](https://ipro.etm.ru/upload/document2/1704877672474.png)Единый комплексный поставщик инженерных систем581\.22 ₽/шт611\.79 ₽/штВаша цена 581\.22₽Розничная цена611\.79₽Кэшбек ЭТМ до 58\.12 балловЗаказ по 1 шт

шт​В корзинуСегодня
107 шт.Аналоги

ПоказатьСпособы получения 

* Стандартная доставка
* Экспресс\-доставка
* Самовывоз ЭТМ
* Самовывоз СДЭК

---

Оплата 

онлайн, СБП, наличными, по счету, баллами

#### iPRO

[Каталог](/catalog)[Производители](/brand)[Акции](/ipro3/actions)[Программа лояльности](/ipro3/discount_program)[Доставка, самовывоз](/ipro3/delivery)[Контакты](/ipro3/contacts)[Помощь](/ipro3/help)[Обмен данными](/ipro3/solutions)[Партнеры по интеграции с ЭТМ](/ipro3/recommendations/of-partners)[Новости ассортимента](/ipro3/news)[Техническая библиотека](/ipro3/library)[Возврат товара](/ipro3/vozvrat_tovara)

#### Ресурсы ЭТМ

[О компании](https://www.etm.ru/company/about_etm/)[Новости компании](/company/about-etm/news)[Мероприятия](https://skills.etm.ru/)[Вакансии](https://www.etm.ru/company/vacancies/)[Холдингам](https://holding.etm.ru/)[Поставщикам](https://www.etm.ru/ipro3/for-merchant)[Реквизиты ЭТМ](https://www.etm.ru/company/contacts/rekvizity/)[Рекомендательные технологии](/ipro3/help/handbook?code=2055&id=7428134144&article=pravila_primenenija_rekomendatelnyx_texnologiy)[Договор оферты](/ipro3/offer?srsltid=AfmBOooTZEvacbPBp3Gc0Y8aZYPsTFaKL_nGUPmFR55D188WAcuXuLTl)

#### ЭТМ — клиентам

[Холдинговые компании](https://www.etm.ru/company/clients/holding/)[Строительные и монтажные организации](https://www.etm.ru/company/clients/smo/)[Сборщикам щитового оборудования](https://www.etm.ru/company/clients/switchboard/)[Промышленные предприятия](https://www.etm.ru/company/clients/industrial/)[Предприятия инфраструктуры](https://www.etm.ru/company/clients/infrastructure/)[Торговые партнеры](https://www.etm.ru/company/clients/dealers/)[Проектные организации](https://www.etm.ru/company/clients/project/)[Частные монтажники](https://www.etm.ru/company/clients/montag/)

#### Спецпроекты компании ЭТМ

[Мобильный центр импортозамещения](https://promavto.etm.ru/)[Практика лидеров](https://pl.etm.ru/)[iPROдажа](https://promo.etm.ru/iprodazha)[Есть контакт](https://contact.etm.ru/)[Лига профессионалов](https://liga.etm.ru/)[Готовые решения по щитовому оборудованию](https://partner.etm.ru/opros_list)[Поставка ПО для САПР и BIM](https://soft.etm.ru)

#### Поддержка 24/7

[8 (800\) 775\-17\-71](tel:88007751771)[Telegram\-чат](https://t.me/ETM24_bot)[Центр обращений](/ipro3/feedback)

#### Контакты для СМИ

[media@etm.ru](mailto:media@etm.ru)

#### Участие в сообществах

[Ассоциация «Честная позиция»](https://fairp.ru)[Российская торгово\-промышленная палата](https://tpprf.ru/ru/)

#### Мобильное приложение ЭТМ

[О мобильном приложении](/ipro3/mobile_app)

#### ЭТМ в социальных сетях

2010\-2025. Компания ЭТМ — копирование и использование в коммерческих целях информации на сайте www.etm.ru допускается только с письменного одобрения Компании ЭТМ. Информация о товарах, их характеристиках и комплектации может содержать неточности. [Политика в отношении обработки персональных данных](/ipro3/privacy_policy) 

Нашли ошибку на сайте?
>>>

OUTPUT:
<<<
{
  "sections": [
    {
      "section": "Характеристики\n--------------\n\n| Производитель: | [Приборэнерго НТК](/brand/3249_priborenergo_ntk) |\n| --- | --- |\n\n| Артикул: | НФ\-00000349 |\n| --- | --- |\n| Ед.измерения: | шт |\n| Код ТНВЭД | 8536900100 |",
      "explanation": "Секция содержит явный заголовок "Характеристики", и содержит некоторые характеристики продукта"
    }
  ]
}
>>>


# Example 4:

INPUT:
<<<
* Москва
* Санкт\-Петербург
* Новосибирск
* Екатеринбург
* Казань
* Нижний Новгород
* Челябинск
* Омск
* Самара
* Ростов\-на\-Дону

 

 Это ваш город?
 

 Да
 

 Нет, выбрать другой
 

* [Оплата](https://4-20.ru/oplata)
* [Доставка](https://4-20.ru/dostavka)
* [Гарантийное обслуживание](https://4-20.ru/garantiynoe_obsluzhivanie)
* [Контакты](https://4-20.ru/about)

[![Электронный дискаунтер](/images/logo.svg)](/ "Все промтовары с доставкой по всей стране")

 промтоваров  
миллион
 

 промтоваров  
миллион
 

каталог

 каталог
 

* <img src='' alt='' title='' width='60' height='60' />

Измерение и метрология
* <img src='' alt='' title='' width='60' height='60' />

Электрика и автоматика
* <img src='' alt='' title='' width='60' height='60' />

Электроника и техника
* <img src='' alt='' title='' width='60' height='60' />

Климат и водоснабжение
* <img src='' alt='' title='' width='60' height='60' />

Силовые машины
* <img src='' alt='' title='' width='60' height='60' />

Для производства
* <img src='' alt='' title='' width='60' height='60' />

Торговля и общепит
* <img src='' alt='' title='' width='60' height='60' />

Транспортировка жидкостей и газов
* <img src='' alt='' title='' width='60' height='60' />

Инструмент
* <img src='' alt='' title='' width='60' height='60' />

Городская среда
* <img src='' alt='' title='' width='60' height='60' />

Здоровье и красота
* <img src='' alt='' title='' width='60' height='60' />

Сад и сельское хозяйство
* <img src='' alt='' title='' width='60' height='60' />

Туризм, спорт и отдых
* <img src='' alt='' title='' width='60' height='60' />

Электронные компоненты
* <img src='' alt='' title='' width='60' height='60' />

Автозапчасти и компоненты
* <img src='' alt='' title='' width='60' height='60' />

Строительство и ремонт
* <img src='' alt='' title='' width='60' height='60' />

Материалы
* [<img src='/images/virtual-category.jpg' alt='' title='' width='60' height='60' />

Прочее](https://4-20.ru/category/0)

* [Измерение и метрология](https://4-20.ru/category/1) 

	+ 
	+
* [Электрика и автоматика](https://4-20.ru/category/226) 

	+ 
	+
* [Электроника и техника](https://4-20.ru/category/336) 

	+ 
	+
* [Климат и водоснабжение](https://4-20.ru/category/374) 

	+ 
	+
* [Силовые машины](https://4-20.ru/category/505) 

	+ 
	+
* [Для производства](https://4-20.ru/category/677) 

	+ 
	+
* [Торговля и общепит](https://4-20.ru/category/888) 

	+ 
	+
* [Транспортировка жидкостей и газов](https://4-20.ru/category/1059) 

	+ 
	+
* [Инструмент](https://4-20.ru/category/1126) 

	+ 
	+
* [Городская среда](https://4-20.ru/category/1413) 

	+ 
	+
* [Здоровье и красота](https://4-20.ru/category/1447) 

	+ 
	+
* [Сад и сельское хозяйство](https://4-20.ru/category/1471) 

	+ 
	+
* [Туризм, спорт и отдых](https://4-20.ru/category/1610) 

	+ 
	+
* [Электронные компоненты](https://4-20.ru/category/1811) 

	+ 
	+
* [Автозапчасти и компоненты](https://4-20.ru/category/2242) 

	+ 
	+
* [Строительство и ремонт](https://4-20.ru/category/2243) 

	+ 
	+
* [Материалы](https://4-20.ru/category/2244) 

	+ 
	+

[Все результаты поиска

 откроется в новой вкладке](#)

* [Избранное

 0](https://4-20.ru/favorites)
* 
* [Корзина

 0](https://4-20.ru/cart)

* Челябинск
 

	+ Москва
	+ Санкт\-Петербург
	+ Новосибирск
	+ Екатеринбург
	+ Казань
	+ Нижний Новгород
	+ Челябинск
	+ Омск
	+ Самара
	+ Ростов\-на\-Дону
* каталог
* [Оплата](https://4-20.ru/oplata)
* [Доставка](https://4-20.ru/dostavka)
* [Гарантийное обслуживание](https://4-20.ru/garantiynoe_obsluzhivanie)
* [Контакты
О магазине](https://4-20.ru/about)

* [zakaz@4\-20\.ru](mailto:zakaz@4-20.ru)
* [\+7 (812\) 309\-29\-49](tel:+7 (812) 309-29-49)
* Бесплатный звонок
* Задать вопрос

1. [Главная](https://4-20.ru)
2. [Измерение и метрология](https://4-20.ru/category/1)
3. [Регистраторы и контроллеры](https://4-20.ru/category/204)
4. [Адаптеры интерфейсов](https://4-20.ru/category/208)
5. [ПРИБОРЭНЕРГО](https://4-20.ru/category/208/%D0%9F%D1%80%D0%B8%D0%B1%D0%BE%D1%80%D1%8D%D0%BD%D0%B5%D1%80%D0%B3%D0%BE)

Разветвитель интерфейса RS\-422/485 ПРИБОРЭНЕРГО ПР\-3 IP65 исп. 1 (НФ\-00000349\)
==================================================================================

Код товара 3204230

 Оставить отзыв 
>>>

OUTPUT:
<<<
{
  "sections": []
}
>>>


# Example 5:

INPUT:
<<<
* Каталог товаров 

	+ [Балансировочные клапаны](https://ridan-danfoss.ru/category/balansirovochnye-klapany/)
	
		- [Автоматические балансировочные клапаны](https://ridan-danfoss.ru/category/avtomaticheskie-balansirovochnye-klapany/)
		- [Ручные балансировочные клапаны](https://ridan-danfoss.ru/category/ruchnye-balansirovochnye-klapany/)
		- [Комплектующие для балансировочных клапанов](https://ridan-danfoss.ru/category/komplektuyushie-dlya-balansirovochnyh-klapanov/)
		- [Фитинги присоединительные](https://ridan-danfoss.ru/category/fitingi-prisoedinitelnye/)
	+ [Клапаны регулирующие седельные](https://ridan-danfoss.ru/category/klapany-reguliruyushie-sedelnye/)
	
		- [Двухходовые проходные клапаны](https://ridan-danfoss.ru/category/dvuhhodovye-prohodnye-klapany/)
		- [Трехходовые клапаны](https://ridan-danfoss.ru/category/trehhodovye-klapany/)
	+ [Клапаны шаровые с электроприводом](https://ridan-danfoss.ru/category/klapany-s-electroprivodom/)
	+ [Контроллеры и диспетчеризация](https://ridan-danfoss.ru/category/kontrollery-datchiki-ecl/)
	
		- [Датчики температуры ECL](https://ridan-danfoss.ru/category/datchiki-temperatury-ecl/)
		- [Контроллеры ECL](https://ridan-danfoss.ru/category/kontrollery-ecl/)
	+ [Пластинчатые теплообменники](https://ridan-danfoss.ru/category/plastinchatye-teploobmenniki/)
	+ [Поворотные регулирующие клапаны](https://ridan-danfoss.ru/category/povorotnye-reguliruyushie-klapany/)
	+ [Радиаторные клапаны](https://ridan-danfoss.ru/category/radiatornye-klapany/)
	
		- [Запорно\-присоединительные радиаторные клапаны](https://ridan-danfoss.ru/category/zaporno-prisoedinitelnye-radiatornye-klapany/)
		- [Клапаны термостатические для радиатора отопления](https://ridan-danfoss.ru/category/klapany-termostaticheskie-dlya-radiatora-otopleniya/)
		- [Комплекты терморегуляторов для систем отопления](https://ridan-danfoss.ru/category/komplekty-termoregulyatorov-dlya-sistem-otopleniya/)
		- [Присоединительно\-регулирующие гарнитуры](https://ridan-danfoss.ru/category/prisoedinitelno-reguliruyushie-garnitury/)
		- [Показать все](https://ridan-danfoss.ru/category/radiatornye-klapany/)
	+ [Распределительные коллекторы](https://ridan-danfoss.ru/category/raspredelitelnye-kollektory/)
	+ [Регулирующие клапаны для регуляторов давления и температуры](https://ridan-danfoss.ru/category/reguliruyushie-klapany-dlya-regulyatorov-davleniya-i-temperatury/)
	
		- [Для регуляторов температуры VG](https://ridan-danfoss.ru/category/klapany-dlya-regulyatorov-temperatury-vg/)
		- [Универсальные фланцевые VFG](https://ridan-danfoss.ru/category/universalnye-flancevye-klapany/)
	+ [Регуляторы давления](https://ridan-danfoss.ru/category/regulyatory-davleniya/)
	
		- [Регуляторы давления «до себя»](https://ridan-danfoss.ru/category/regulyatory-davleniya-do-sebya/)
		- [Регуляторы давления «после себя»](https://ridan-danfoss.ru/category/regulyatory-davleniya-posle-sebya/)
		- [Регуляторы перепада давления](https://ridan-danfoss.ru/category/regulyatory-perepada-davleniya/)
		- [Регуляторы перепуска](https://ridan-danfoss.ru/category/regulyatory-perepuska/)
	+ [Регуляторы температуры](https://ridan-danfoss.ru/category/regulyatory-temperatury/)
	
		- [Регуляторы температуры комбинированные](https://ridan-danfoss.ru/category/regulyatory-temperatury-kombinirovannye/)
		- [Регуляторы температуры моноблочные](https://ridan-danfoss.ru/category/regulyatory-temperatury-monoblochnye/)
	+ [Термоголовки](https://ridan-danfoss.ru/category/termogolovki/)
	
		- [Принадлежности для термостатических элементов](https://ridan-danfoss.ru/category/prinadlezhnosti-dlya-termostaticheskih-elementov/)
	+ [Термоэлектрические приводы](https://ridan-danfoss.ru/category/termoelektricheskie-privody/)
	+ [Трубопроводная арматура](https://ridan-danfoss.ru/category/truboprovodnaya-armatura/)
	
		- [Гибкие вставки ZKV](https://ridan-danfoss.ru/category/gibkie-vstavki-zkv/)
		- [Дисковые затворы](https://ridan-danfoss.ru/category/diskovye-zatvory-ridan/)
		- [Обратные клапаны](https://ridan-danfoss.ru/category/obratnye-klapany/)
		- [Осевые сильфонные компенсаторы](https://ridan-danfoss.ru/category/osevye-silfonnye-kompensatory/)
		- [Показать все](https://ridan-danfoss.ru/category/truboprovodnaya-armatura/)
	+ [Электромагнитные клапаны](https://ridan-danfoss.ru/category/elektromagnitnye-klapany/)
	+ [Электроприводы для регулирующих клапанов](https://ridan-danfoss.ru/category/privody-dlya-reguliruyushih-klapanov/)
	
		- [Редукторные электроприводы с аналоговым управлением](https://ridan-danfoss.ru/category/reduktornye-elektroprivody-s-analogovym-upravleniem/)
		- [Редукторные электроприводы с трехпозиционным управлением](https://ridan-danfoss.ru/category/reduktornye-elektroprivody-s-trehpozicionnym-upravleniem/)
		- [Электроприводы для поворотных регулирующих клапанов](https://ridan-danfoss.ru/category/elektroprivody-dlya-povorotnyh-reguliruyushih-klapanov/)

![](https://ridan-danfoss.ru/image/cache/webp/catalog/category/ridan-s-prajsa2-305x600.webp)
* Оплата и доставка 

	+ [Доставка и свмовывоз](delivery)
	+ [Сроки поставки](sroki-postavki)
	+ [Гарантия и возврат](garantiya-i-vozvrat)
	+ [Оплата](oplata)
* Бренды 

	+ [Ridan](brand/ridan)
	+ [Danfoss](brand/danfoss)
* [Каталоги, прайсы, замены, инструкции](download/)
* [Как заказать](kak-zakazat)
* [Контакты](contact-us/)
* 

* [Главная](https://ridan-danfoss.ru/)
* [Трубопроводная арматура](https://ridan-danfoss.ru/category/truboprovodnaya-armatura/)
* [Дисковые затворы](https://ridan-danfoss.ru/category/diskovye-zatvory-ridan/)
* [Дисковые затворы с рукояткой](https://ridan-danfoss.ru/category/diskovye-s-rukoyatkoy/)
* Ридан ЗДМ 05\.16\.50 затвор дисковый DN50 с рукояткой \| 082X4421R

[![Ридан ЗДМ 05.16.50 затвор дисковый DN50 с рукояткой | 082X4421R](https://ridan-danfoss.ru/image/cache/webp/catalog/ridan/4/860503351-ridan-zdm-05-16-50-zatvor-diskovyj-dn50-s-rukoyatkoj-082x4421r-500x500.webp "Ридан ЗДМ 05.16.50 затвор дисковый DN50 с рукояткой | 082X4421R")](https://ridan-danfoss.ru/image/cache/webp/catalog/ridan/4/860503351-ridan-zdm-05-16-50-zatvor-diskovyj-dn50-s-rukoyatkoj-082x4421r-1000x1000.webp "Ридан ЗДМ 05.16.50 затвор дисковый DN50 с рукояткой | 082X4421R")

Ридан ЗДМ 05\.16\.50 затвор дисковый DN50 с рукояткой \| 082X4421R
==================================================================

* Производитель: [Ridan](https://ridan-danfoss.ru/brand/ridan)
* Код товара: 082X4421R\-10

[![Ridan](https://ridan-danfoss.ru/image/cache/webp/catalog/ridan_logo-60x60.webp)](https://ridan-danfoss.ru/brand/ridan)

Поставка: Есть в наличии

Цена с НДС: 10565р.

Другие варианты товара 

Диаметр ДУ (DN), мм

 [125](https://ridan-danfoss.ru/product/diskovye-zatvory-s-rukoyatkoj-082x4425r-ridan)  [40](https://ridan-danfoss.ru/product/diskovye-zatvory-s-rukoyatkoj-082x4420r-ridan)  [80](https://ridan-danfoss.ru/product/diskovye-zatvory-s-rukoyatkoj-082x4403r-ridan) 
50

 [65](https://ridan-danfoss.ru/product/diskovye-zatvory-s-rukoyatkoj-082x4422r-ridan)  [100](https://ridan-danfoss.ru/product/diskovye-zatvory-s-rukoyatkoj-082x4424r-ridan)  [150](https://ridan-danfoss.ru/product/diskovye-zatvory-s-rukoyatkoj-082x4406r-ridan)  [200](https://ridan-danfoss.ru/product/diskovye-zatvory-s-rukoyatkoj-082x4407r-ridan)  [250](https://ridan-danfoss.ru/product/diskovye-zatvory-s-rukoyatkoj-082x4408r-ridan)  [300](https://ridan-danfoss.ru/product/diskovye-zatvory-s-rukoyatkoj-082x4409r-ridan) 

Конструктивное исполнение

с рукояткой

\-

\+

 Купить в 1 клик
В корзину

* [Характеристики](#tab-specification)
* [Загрузки](#tab-files)
* [Доставка и оплата](#tab-custom-1)

| Основные характеристики | |
| --- | --- |
| Номинальный диаметр (DN), мм | 50 |
| Номинальное давление (PN), бар | 16 |
| Исполнение | с рукояткой |
| Назначение изделия | Затворы дисковые типа ЗДМ модификации 03 и 05 (далее \- затворы ) предназначены для использования в качестве запорной и регулирующей арматуры в различных энергетических и технологических установках.Затворы ЗДМ предназначены для использования в системах водоснабжения, теплоснабжения, холодоснабжения, вентиляции и кондиционирования. Затвор ЗДМ не предназначен для использования в составе узлов управления установок пожаротушения как пожарное запорное устройство. |
| Тип присоединения к трубопроводу | центрирующие проушины |
| Комплектность | В комплект поставки входит:затвор дисковый в комплекте с рукояткой; упаковка; паспорт (предоставляется по запросу в электронной форме); руководство по эксплуатации (предоставляется по запросу в электронной форме). |
| Код группы | ЗДМ |
| Рабочая среда | Холодная вода, 50% гликоль, горячая вода, питьевая вода |
| Серия | ЗДМ 05\.16 |
| Температура рабочей среды, °С | от \-15 до \+120 |
| Гарантийные обязательства | Изготовитель/продавец гарантирует соответствие дисковых затворов типа ЗДМ техническим требованием при соблюдении потребителем условий транспортирования, хранения и эксплуатации.Гарантийный срок эксплуатации и хранения составляет \- 12 месяцев с даты продажи, указанной в транспортных документах, или 18 месяцев с даты производства. Срок службы затворов дисковых типа ЗДМ при соблюдении условий эксплуатации и совместимости рабочих сред согласно паспорту/инструкции по эксплуатации и проведении необходимых сервисных работ – 10 лет с даты продажи, указанной в транспортных документах. |
| Герметичность затвора (объем протечки / класс герметичности) | ГОСТ 9544\-2015 Класс А |
| Дополнительные требования | Запрещена эксплуатация затвора без рукоятки, редуктора или привода. Запрещается демонтаж рукоятки, редуктора затвора, установленного на работающем трубопроводе или находящимся под давлением. Монтаж затвора производить только при положительных температурах окружающей среды.Запуск в эксплуатацию производить только при положительных температурах окружающей и рабочей среды. Запрещено производство работ при температуре поверхности затвора более \+50°С и ниже \-40°С без проведения соответствующих мероприятий по защите обслуживающего персонала, производящего работы. |
| Максимальное рабочее давление среды при температуре \+20С (Рр), бар | 16 |
| Назначенный ресурс работы | 2500 циклов "открыть\-закрыть" в течение 24 месяцев со дня запуска в эксплуатацию. |
| Температура окружающей среды, °С | от \-15 до \+70 |
| Условия транспортировки и хранения | Складское длительное хранение: в течение 3 лет при условии соблюдения температурного режима от \+10°С до \+35°С и защиты от пыли и УФ\-излучения в темных упаковках, в чистом и сухом помещении. Допускается транспортировка и хранение при минимальной температуре \-40°С кратковременно. |
| Масса, кг, не более | 2\.1 |

| Название файла | Дата добавления | Размер файла | Скачать |
| --- | --- | --- | --- |
| РИДАН\-ЗДМ\_Затвор дисковый\_V1 | 09\.01\.2023 | 2\.3MB | [Скачать](https://ridan-danfoss.ru/index.php?route=product/product/files&download_id=160) |

**Оплата**  

Оплата производится на основании выставленного счета с НДС, работаем только с юридическими лицами.

Скидки на товар указываются в счете

**Доставка**

Мы доставляем товар по Санкт\-Петербургу и бесплатно до терминалов транспортных компаний и пунктов выдачи в Санкт\-Петербурге

Отгрузка оплаченного товара с подтвержденными резервами осуществляется в течение 1\-5 дней после оплаты, в зависимости от места нахождения товара (свой склад или удаленный)

**Самовывоз**

Самовывоз со склада в рабочие дни с 10 до 17 часов, по предварительной договоренности  

**Сроки поставки**  

Срок поставки зависит от статуса товара (наличие на складе \- отгрузка сразу, 3\-5 раб. дней \- наличие на удаленном складе, предзаказ \- товар ожидается к приходу, по запросу \- возможность заказа товара надо уточнять)  

В связи с крайне нестабильными поставками товаров под торговыми марками Danfoss и Ridan, актуальные цены (включая оптовые) и доступное количество для заказа определяются исходя из текущей заявки на товар. Резерв действует 1 день.

### Случайные товары

[![RTR-K Клапан терморегулятора 15 013G7039 Danfoss | с уплотнительной втулкой и отводом с накидной гайкой](https://ridan-danfoss.ru/image/cache/webp/catalog/ridan/6/457595180-rtr-k-klapan-termoregulyatora-15-013g7039-danfoss-s-uplotnitelnoj-vtulkoj-i-otvodom-s-nakidnoj-gajkoj-200x200.webp "RTR-K Клапан терморегулятора 15 013G7039 Danfoss | с уплотнительной втулкой и отводом с накидной гайкой")](https://ridan-danfoss.ru/product/prisoedinitelno-reguliruyuschie-garnitury-013g7039-danfoss)

[RTR\-K Клапан терморегулятора 15 013G7039 Danfoss \| с уплотнительной втулкой и отводом с накидной гайкой](https://ridan-danfoss.ru/product/prisoedinitelno-reguliruyuschie-garnitury-013g7039-danfoss)

 
 3146р. 
 
 
 

 В корзину

[![APT, сервисный набор (20–60 кПа) DN 32 | 003Z7833](https://ridan-danfoss.ru/image/cache/webp/catalog/ridan/3/440140142-apt-servisnyj-nabor-20-60-kpa-dn-32-003z7833-200x200.webp "APT, сервисный набор (20–60 кПа) DN 32 | 003Z7833")](https://ridan-danfoss.ru/product/komplektuyuschie-dlya-balansirovochnyh-klapanov-003z7833-danfoss)

[APT, сервисный набор (20–60 кПа) DN 32 \| 003Z7833](https://ridan-danfoss.ru/product/komplektuyuschie-dlya-balansirovochnyh-klapanov-003z7833-danfoss)

 
 7594р. 

* [Обогрев](/collection/otoplenie "Обогрев")
	+ [Электрокамины](/collection/elektrokaminy "Электрокамины")
		- [Очаги](/collection/ochagi "Очаги")
		- [Порталы](/collection/portaly-2 "Порталы")
		- [Каминокомплекты](/collection/kamino-komplekty "Каминокомплекты")
		- [Биокамины](/collection/biokaminy "Биокамины")
	+ [Тепловые завесы](/collection/teplovye-zavesy "Тепловые завесы")
		- [Электрические завесы](/collection/zavesy-s-elektricheskim-istochnikom-tepla "Электрические завесы")
		- [Водяные завесы](/collection/vodyanye-teplovye-zavesy "Водяные завесы")
		- [Завесы без нагрева](/collection/bez-istochnika-tepla "Завесы без нагрева")
		- [Автоматика (опции)](/collection/avtomatika-optsii "Автоматика (опции)")
	+ [Водяные тепловентиляторы](/collection/teploventilyatory "Водяные тепловентиляторы")
		- [Дестратификаторы](/collection/destratifikatory "Дестратификаторы")
		- [Водяные тепловентиляторы](/collection/vodyanye-teploventilyatory "Водяные тепловентиляторы")
		- [Аксессуары для водяных тепловентиляторы и дестратификаторов](/collection/aksessuary-dlya-vodyanyh-teploventilyatory-i-destratifikatorov "Аксессуары для водяных тепловентиляторы и дестратификаторов")
	+ [Тепловые пушки](/collection/teplovye-pushki "Тепловые пушки")
		- [Электрические тепловые пушки](/collection/elektricheskie-teplovye-pushki "Электрические тепловые пушки")
		- [Дизельные пушки](/collection/dizelnye "Дизельные пушки")
		- [Газовые пушки](/collection/gazovye "Газовые пушки")
	+ [Газовые обогреватели](/collection/gazovye-infrakrasnye "Газовые обогреватели")
	+ [Электрические обогреватели](/collection/obogrevateli-elektricheskie "Электрические обогреватели")
		- [Электрические конвекторы](/collection/konvektor "Электрические конвекторы")
		- [Аксессуары для обогревателей](/collection/dopolnitelnye-elementy "Аксессуары для обогревателей")
	+ [Инфракрасные обогреватели](/collection/infrakrasnye-obogrevateli "Инфракрасные обогреватели")
	+ [Масляные радиаторы](/collection/maslyanye-radiatory "Масляные радиаторы")
		- [Масляные радиаторы на 5 секций](/collection/5-sektsiy "Масляные радиаторы на 5 секций")
		- [Масляные радиаторы на 7 секций](/collection/katalog-e46c82 "Масляные радиаторы на 7 секций")
		- [Масляные радиаторы на 9 секций](/collection/katalog-24a073 "Масляные радиаторы на 9 секций")
		- [Масляные радиаторы на 11 секций](/collection/11-sektsiy "Масляные радиаторы на 11 секций")
	+ [Бытовые тепло\-вентиляторы](/collection/bytovye-teploventilyatory "Бытовые тепло-вентиляторы")
	+ [Теплые полы](/collection/teplye-poly "Теплые полы")
		- [Греющий кабель](/collection/nagrevatelnye-sektsii "Греющий кабель")
		- [Нагревательные маты](/collection/nagrevatelnye-maty "Нагревательные маты")
		- [Инфракрасная пленка](/collection/infrakrasnaya-plenka "Инфракрасная пленка")
		- [Терморегуляторы для теплых полов](/collection/termoregulyatory-b6a68a "Терморегуляторы для теплых полов")
		- [Система антиобледенения](/collection/sistema-antiobledeneniya "Система антиобледенения")
		- [Кабель для обогрева кровли и труб](/collection/kabel-dlya-obogreva-krovli-i-trub "Кабель для обогрева кровли и труб")
	+ [Сушильные шкафы](/collection/sushilnye-shkafy "Сушильные шкафы")
* [Осушение](/collection/osushenie "Осушение")
	+ [Сушилки для рук](/collection/sushilki-dlya-ruk "Сушилки для рук")
	+ [Бытовые осушители](/collection/napolnye-osushiteli "Бытовые осушители")
	+ [Настенные осушители](/collection/nastennye-osushiteli "Настенные осушители")
	+ [Канальные осушители](/collection/kanalnye-osushiteli "Канальные осушители")
	+ [Промышленные осушители](/collection/promyshlennye-osushiteli "Промышленные осушители")
	+ [Адсорбционные осушители](/collection/adsorbtsionnye-osushiteli "Адсорбционные осушители")
	+ [Рециркуляторы](/collection/obezzarazhivateli-vozduha "Рециркуляторы")
		- [Рециркуляторы](/collection/retsirkulyatory-obluchateli "Рециркуляторы")
* [Увлажнение](/collection/uvlazhnenie "Увлажнение")
	+ [Система туманообразования](/collection/katalog-c602fd "Система туманообразования")
	+ [Канальные увлажнители](/collection/kanalnye-uvlazhniteli "Канальные увлажнители")
	+ [Промышленные увлажнители](/collection/promyshlennye-uvlazhniteli "Промышленные увлажнители")
	+ [Мойки воздуха](/collection/moyki-vozduha "Мойки воздуха")
	+ [Бытовые увлажнители](/collection/bytovye-uvlazhniteli "Бытовые увлажнители")
	+ [Очистители воздуха](/collection/vozduhoochistitel "Очистители воздуха")
	+ [Климатические комплексы](/collection/klimaticheskie-kompleksy "Климатические комплексы")
	+ [Аксессуары](/collection/aksessuary-7dd9bc "Аксессуары")
	+ [Датчики и контроллеры](/collection/datchiki-i-kontrollery "Датчики и контроллеры")
	+ [Аксессуары и фильтры для увлажнителей и очистителей](/collection/aksessuary-i-filtry-dlya-uvlazhniteley-i-ochistiteley "Аксессуары и фильтры для увлажнителей и очистителей")
* [Компрессорное](/collection/holodilnoe-oborudovanie "Компрессорное")
	+ [Компрессоры](/collection/kompressornoe-oborudovanie "Компрессоры")
		- [Поршневые компрессоры](/collection/danfoss-2 "Поршневые компрессоры")
		- [Спиральные компрессоры](/collection/danfoss-3 "Спиральные компрессоры")
	+ [Холодильные масла](/collection/holodilnye-masla "Холодильные масла")
	+ [Реле](/collection/rele "Реле")
		- [Дифференциальные реле давления](/collection/differentsialnye-rele-davleniya "Дифференциальные реле давления")
		- [Картриджные реле давления](/collection/kartridzhnye-rele-davleniya "Картриджные реле давления")
		- [Реле температуры](/collection/rele-temperatury "Реле температуры")
		- [Реле давления](/collection/rele-davleniya "Реле давления")
	+ [Терморегулирующие расширительные клапаны](/collection/termoreguliruyuschie-klapany-2 "Терморегулирующие расширительные клапаны")
	+ [Фильтры](/collection/filtry-861a13 "Фильтры")
		- [Неразборные (герметичные) фильтры\-осушители](/collection/germetichnye-filtry-osushiteli "Неразборные (герметичные) фильтры-осушители")
		- [Разборные фильтр\-осушители](/collection/filtr-osushiteli-hladagenta "Разборные фильтр-осушители")
		- [Антикислотные фильтры\-осушители](/collection/antikislotnye-filtry-osushiteli "Антикислотные фильтры-осушители")
		- [Сетчатые фильтры](/collection/setchatye-filtry-2 "Сетчатые фильтры")
		- [Фильтрующие сетки](/collection/filtruyuschie-setki "Фильтрующие сетки")
		- [Герметичные фильтры\-очистители](/collection/germetichnye-filtry-ochistiteli "Герметичные фильтры-очистители")
	+ [Запорные клапаны](/collection/zapornye-klapany-2 "Запорные клапаны")
		- [Запорные шаровые краны](/collection/zapornye-sharovye-krany "Запорные шаровые краны")
		- [Запорные мембранные клапаны](/collection/zapornye-membrannye-klapany "Запорные мембранные клапаны")
		- [Ручные запорные клапаны](/collection/ridan-82eb72 "Ручные запорные клапаны")
	+ [Смотровые стекла](/collection/smotrovye-stekla "Смотровые стекла")
	+ [Электромагнитные клапаны и катушки](/collection/elektromagnitnye-klapany-i-katushki "Электромагнитные клапаны и катушки")
	+ [Обратные клапаны](/collection/obratnye-klapany-3 "Обратные клапаны")
	+ [Датчики и преобразователи](/collection/datchiki-i-preobrazovateli-2 "Датчики и преобразователи")
		- [Датчики температуры](/collection/datchiki-temperatury "Датчики температуры")
		- [Преобразователи давления](/collection/katalog-a3ec8c "Преобразователи давления")
	+ [Электронные системы управления](/collection/elektronnye-ustroystva-upravleniya "Электронные системы управления")
		- [Контроллеры температуры](/collection/kontroller-isparitelya-i-temperatury "Контроллеры температуры")
		- [Контроллеры испарителя](/collection/kontrollery-isparitelya "Контроллеры испарителя")
		- [Контроллеры производительности](/collection/kontrollery-proizvoditelnosti "Контроллеры производительности")
		- [Контроллеры инженерных сетей](/collection/kontrollery-inzhenernyh-setey "Контроллеры инженерных сетей")
	+ [Линейные компоненты](/collection/lineynye-komponenty "Линейные компоненты")
		- [Запорные клапаны](/collection/zapornye-klapany "Запорные клапаны")
		- [Механические клапаны](/collection/mehanicheskie-klapany "Механические клапаны")
		- [Вентили с сервоприводом](/collection/ventili-s-servoprivodom "Вентили с сервоприводом")
		- [Сервоклапаны с пилотным управлением](/collection/ics-klapany-servoupravlyaemye "Сервоклапаны с пилотным управлением")
		- [Электромагнитные клапаны](/collection/solenoidnye-klapany "Электромагнитные клапаны")
		- [Катушки](/collection/katushki "Катушки")

* [Главная](/ "Главная")
* [Отопление и водоснабжение](/collection/vodosnabzhenie "Отопление и водоснабжение")
* [Трубопроводная арматура](/collection/truboprovodnaya-armatura "Трубопроводная арматура")
* [Дисковые поворотные затворы](/collection/diskovye-povorotnye-zatvory "Дисковые поворотные затворы")
* [Дисковые поворотные затворы Ридан](/collection/diskovye-povorotnye-zatvory-ridan "Дисковые поворотные затворы Ридан")
* Ридан 082X4421R ЗДМ 05\.16\.50 Затвор дисковый поворотный Ду 50 PN 16 с рукояткой

[30%
 

![Ридан 082X4421R ЗДМ 05.16.50 Затвор дисковый поворотный Ду 50 PN 16 с рукояткой](https://static.insales-cdn.com/images/products/1/2742/727681718/large_Затвор_ЗДМ_с_рукояткой.jpg "Ридан 082X4421R ЗДМ 05.16.50 Затвор дисковый поворотный Ду 50 PN 16 с рукояткой")](https://static.insales-cdn.com/images/products/1/2742/727681718/Затвор_ЗДМ_с_рукояткой.jpg "Ридан 082X4421R ЗДМ 05.16.50 Затвор дисковый поворотный Ду 50 PN 16 с рукояткой")

Ридан 082X4421R ЗДМ 05\.16\.50 Затвор дисковый поворотный Ду 50 PN 16 с рукояткой
=================================================================================

 
 
 Ридан 082X4421R ЗДМ 05\.16\.50 Затвор дисковый поворотный Ду 50 PN 16 с рукояткой предназначены для использования в качестве запорной и регулирующей арматуры в различных энергетических и технологических установках.Затворы ЗДМ предназначены для использования в системах водоснабжения, теплоснабжения, холодоснабжения, вентиляции и кондиционирования.

 

 9 016 руб

 
 
 12 879 руб
 
 
 
 

Товар в наличии ![](https://static.insales-cdn.com/assets/1/1553/1828369/1740633653/fa-check.png)

Артикул
1118952

Цена
С учетом НДС

Самовывоз
Бесплатно

Доставка в

Расчитываем доставку...

Купить

 

 
 Купить в 1 клик
 

 
 

* [Характеристики](#product-characteristics)

| Тип оборудования | Дисковый затвор |
| --- | --- |
| Серия | ЗДМ |
| Производитель | Ридан |
| Страна | Россия |
| Гарантия | 1 год |
| Назначение | водоснабжение теплоснабжение |
| Материал | Чугун |
| Диаметр (DN), мм | 50 |
| Давление, бар | 16 |
| Тип присоединения | Межфланцевое |
| Температура рабочей среды, °C | от \-15 до \+120 °C |
| Рабочая среда | вода систем отопления, ГВС, ХВС, в том числе питьевая, растворы гликоля до 50 % |
| Длина товара, мм | 193 |
| Ширина товара, мм | 50 |
| Высота товара, мм | 215 |
| Вес товара, кг | 2\.1 |
| Материал диска | Нержавеющая сталь |

8 (495\) 975\-90\-45
zakaz@kondicioner.pro

* [Контакты](/page/kontakty "Контакты")
* [Доставка](/page/delivery "Доставка")
* [Оплата](/page/oplata-2 "Оплата")
* [Сравнение](/compares "Сравнение")
* [Корзина](/cart_items "Корзина")
* [Обратная связь](/page/feedback "Обратная связь")
* [Политика конфиденциальности](/page/politika-konfidencialnosti "Политика конфиденциальности")
* [Пользовательское соглашение](/page/polzovatelskoe-soglashenie "Пользовательское соглашение")
* [Публичная оферта](/page/oferta "Публичная оферта")
* [Как оформить заказ](/page/kak-oformit-zakaz "Как оформить заказ")

* 
* 
* 

[Сделано в InSales](https://insales.ru "Сделано в InSales")

* [Кондиционирование](/collection/condicionery "Кондиционирование")

	+ [Мобильные кондиционеры](/collection/mobilnye "Мобильные кондиционеры")
	
		- [Мобильные кондиционеры до 15 м² \- 1\.5 кВт](/collection/do-15-m-15-kvt "Мобильные кондиционеры до 15 м² - 1.5 кВт")
		- [Мобильные кондиционеры 15\-20 м² \- 2\.0 кВт](/collection/15-20-m-20-kvt "Мобильные кондиционеры 15-20 м² - 2.0 кВт")
		- [Мобильные кондиционеры 20\-25 м² \- 2\.7 кВт](/collection/20-25-m-27-kvt "Мобильные кондиционеры 20-25 м² - 2.7 кВт")
		- [Мобильные кондиционеры 30\-35 м² \- 3\.6 кВт](/collection/30-35-m-36-kvt "Мобильные кондиционеры 30-35 м² - 3.6 кВт")
		- [Мобильные кондиционеры 40\-55 м² \- 5\.5 кВт](/collection/40-60-m-60-kvt "Мобильные кондиционеры 40-55 м² - 5.5 кВт")
		- [Мобильные кондиционеры более 60 м²](/collection/bolee-60-m "Мобильные кондиционеры более 60 м²")
		- [Климатизаторы](/collection/katalog-5f1167 "Климатизаторы")
	+ [Оконные кондиционеры](/collection/okonnye-konditsionery "Оконные кондиционеры")
	+ [Настенные сплит системы](/collection/nastennye-split-sistemy "Настенные сплит системы")
	
		- [20 м² \- 2 кВт](/collection/20-m-2-kvt "20 м² - 2 кВт")
		- [25 м² \- 2\.6 кВт](/collection/25-m-26-kvt "25 м² - 2.6 кВт")
		- [35 м² \- 3\.5 кВт](/collection/35-m-35-kvt "35 м² - 3.5 кВт")
		- [55 м² \- 5\.5 кВт](/collection/55-m-55-kvt "55 м² - 5.5 кВт")
		- [70 м² \- 7 кВт](/collection/70-m-7-kvt "70 м² - 7 кВт")
		- [90 м² \- 9 кВт](/collection/katalog-8f597a "90 м² - 9 кВт")
		- [110 м² \- 11 кВт](/collection/katalog-4c9702 "110 м² - 11 кВт")
	+ [Мультисплит](/collection/multisplit "Мультисплит")
	
		- [Наружние блоки мульти\-сплит системы на 2 комнаты](/collection/2-komnaty "Наружние блоки мульти-сплит системы на 2 комнаты")
		- [Наружние блоки мульти\-сплит системы на 3 комнаты](/collection/3-komnaty "Наружние блоки мульти-сплит системы на 3 комнаты")
		- [Наружние блоки мульти\-сплит системы на 4 комнаты](/collection/katalog-04bb5a "Наружние блоки мульти-сплит системы на 4 комнаты")
		- [Наружние блоки мульти\-сплит системы на 5 комнат](/collection/katalog-57166d "Наружние блоки мульти-сплит системы на 5 комнат")
		- [Внутренние блоки](/collection/katalog-d23b7f "Внутренние блоки")
		- [Комплекты мульти сплит систем](/collection/komplekty-split-sistem "Комплекты мульти сплит систем")
	+ [Канальные сплит системы](/collection/kolonnyy-tip "Канальные сплит системы")
	
		- [Канальная сплит система 3\.5 кВт \- 12 BTU](/collection/35-kvt-12-btu "Канальная сплит система 3.5 кВт - 12 BTU")
		- [Канальная сплит система 5\.5 кВт \- 18 BTU](/collection/55-kvt-18-btu "Канальная сплит система 5.5 кВт - 18 BTU")
		- [Канальная сплит система 7\.0 кВт \- 24 BTU](/collection/katalog-c3245c "Канальная сплит система 7.0 кВт - 24 BTU")
		- [Канальная сплит система 9\.0 кВт \- 30 BTU](/collection/katalog-8b6002 "Канальная сплит система 9.0 кВт - 30 BTU")
		- [Канальная сплит система 11 кВт \- 36 BTU](/collection/katalog-cb8f05 "Канальная сплит система 11 кВт - 36 BTU")
		- [Канальная сплит система 14 кВт \- 48 BTU](/collection/katalog-30ea5f "Канальная сплит система 14 кВт - 48 BTU")
		- [Канальная сплит система 17 кВт \- 60 BTU](/collection/katalog-e025a2 "Канальная сплит система 17 кВт - 60 BTU")
		- [Канальная сплит система 22 кВт \- 76 BTU](/collection/katalog-bfee2a "Канальная сплит система 22 кВт - 76 BTU")
		- [Канальная сплит система 28 кВт \- 95 BTU](/collection/katalog-40b1bd "Канальная сплит система 28 кВт - 95 BTU")
	+ [Кассетные сплит системы](/collection/kasseta "Кассетные сплит системы")
	
		- [Кассетная сплит система 3\.5 кВт \- 12 BTU](/collection/35-kvt-12-btu-2 "Кассетная сплит система 3.5 кВт - 12 BTU")
		- [Кассетная сплит система 5\.5 кВт \- 18 BTU](/collection/55-kvt-18-btu-2 "Кассетная сплит система 5.5 кВт - 18 BTU")
		- [Кассетная сплит система 7\.0 кВт \- 24 BTU](/collection/70-kvt-24-btu "Кассетная сплит система 7.0 кВт - 24 BTU")
		- [Кассетная сплит система 9\.0 кВт \- 30 BTU](/collection/90-kvt-30-btu "Кассетная сплит система 9.0 кВт - 30 BTU")
		- [Кассетная сплит система 11 кВт \- 36 BTU](/collection/katalog-225b59 "Кассетная сплит система 11 кВт - 36 BTU")
		- [Кассетная сплит система 12 кВт \- 42 BTU](/collection/katalog-fb0e04 "Кассетная сплит система 12 кВт - 42 BTU")
		- [Кассетная сплит система 14 кВт \- 48 BTU](/collection/katalog-a73e21 "Кассетная сплит система 14 кВт - 48 BTU")
		- [Кассетная сплит система 17 кВт \- 60 BTU](/collection/katalog-ce5da1 "Кассетная сплит система 17 кВт - 60 BTU")
	+ [Колонные сплит системы](/collection/kolonnye-sistemy "Колонные сплит системы")
	
		- [Колонная сплит система 7\.0 кВт \- 24 BTU](/collection/70-kvt-24-btu-2 "Колонная сплит система 7.0 кВт - 24 BTU")
		- [Колонная сплит система 14 кВт \- 48 BTU](/collection/14-kvt-48-btu "Колонная сплит система 14 кВт - 48 BTU")
		- [Колонная сплит система 16 кВт \- 56 BTU](/collection/katalog-e880b6 "Колонная сплит система 16 кВт - 56 BTU")
		- [Колонная сплит система 17 кВт \- 60 BTU](/collection/17-kvt-60-btu "Колонная сплит система 17 кВт - 60 BTU")
	+ [Напольно\-потолочные сплит системы](/collection/napolno-podpotolochnye-sistemy "Напольно-потолочные сплит системы")
	
		- [Напольно\-потолочные сплит системы 2\.5 кВт \- 9 BTU](/collection/25-kvt-9-btu "Напольно-потолочные сплит системы 2.5 кВт - 9 BTU")
		- [Напольно\-потолочные сплит системы 3\.5 кВт \- 12 BTU](/collection/35-kvt-12-btu-3 "Напольно-потолочные сплит системы 3.5 кВт - 12 BTU")
		- [Напольно\-потолочные сплит системы 5\.5 кВт \- 18 BTU](/collection/katalog-bf9a78 "Напольно-потолочные сплит системы 5.5 кВт - 18 BTU")
		- [Напольно\-потолочные сплит системы 7\.0 кВт \- 24 BTU](/collection/katalog-a9eb83 "Напольно-потолочные сплит системы 7.0 кВт - 24 BTU")
		- [Напольно\-потолочные сплит системы 11 кВт \- 36 BTU](/collection/katalog-43f273 "Напольно-потолочные сплит системы 11 кВт - 36 BTU")
		- [Напольно\-потолочные сплит системы 14 кВт \- 48 BTU](/collection/katalog-8d3cc2 "Напольно-потолочные сплит системы 14 кВт - 48 BTU")
		- [Напольно\-потолочные сплит системы 17 кВт \- 60 BTU](/collection/katalog-656cbc "Напольно-потолочные сплит системы 17 кВт - 60 BTU")
	+ [Фанкойлы](/collection/fankoyly "Фанкойлы")
	
		- [Канальные фанкойлы](/collection/kanalnye-fankoyly "Канальные фанкойлы")
		- [Кассетные фанкойлы](/collection/kassetnye-fankoyly "Кассетные фанкойлы")
		- [Настенные фанкойлы](/collection/nastennye-fankoyly "Настенные фанкойлы")
		- [Напольно\-потолочные фанкойлы](/collection/napolno-potolochnye-fankoyly "Напольно-потолочные фанкойлы")
		- [Управление, опции для фанкойлов](/collection/aksessuary-dlya-fankoyla "Управление, опции для фанкойлов")
	+ [Компрессорно\-конденсаторные блоки](/collection/kompressorno-kondensatornye-bloki "Компрессорно-конденсаторные блоки")
	+ [Расходные материалы](/collection/dopolnitelnoe-oborudovanie "Расходные материалы")
	
		- [Пульт управления](/collection/pult-upravleniya "Пульт управления")
		- [Wi\-Fi Модули](/collection/wi-fi-moduli "Wi-Fi Модули")
		- [Насосы дренажные](/collection/nasos-drenazhnyy "Насосы дренажные")
		- [Устройства зимнего пуска](/collection/katalog-9fca6a "Устройства зимнего пуска")
		- [Устройства ротации](/collection/ustroystva-rotatsii "Устройства ротации")
		- [Фильтры для сплит\-систем](/collection/filtry-dlya-split-sistem "Фильтры для сплит-систем")
		- [Панели к кассетным блокам](/collection/Панели-к-кассетным-блокам "Панели к кассетным блокам")
		- [Декоративные решетки](/collection/dekorativnye-reshetki "Декоративные решетки")
		- [Экраны отражатели](/collection/ekrany-dlya-konditsionerov "Экраны отражатели")
		- [Трубы медные](/collection/truba-mednaya-2 "Трубы медные")
		- [Теплоизоляция](/collection/teploizolyatsiya "Теплоизоляция")
		- [Дренажный шланг и капиллярная трубка](/collection/katalog-1c2d94 "Дренажный шланг и капиллярная трубка")
		- [Кронштейны, козырьки, подставки](/collection/kronshteyny-kozyrki-podstavki "Кронштейны, козырьки, подставки")
		- [Виброгасители](/collection/vibrogasiteli "Виброгасители")
		- [Сифоны для кондиционеров](/collection/sifony "Сифоны для кондиционеров")
		- [Фреон](/collection/hladagenty-freon "Фреон")
		- [Кабель и провод](/collection/kabel-kanaly "Кабель и провод")
		- [Химия для очистки кондиционеров](/collection/himiya "Химия для очистки кондиционеров")
		- [Козырьки и защитные ограждения](/collection/kozyrki-i-zaschitnye-ograzhdeniya "Козырьки и защитные ограждения")
	+ [Мультизональные VRF\-VRV системы](/collection/multizonalnye-vrf-vrv-sistemy "Мультизональные VRF-VRV системы")
	
		- [Наружные блоки для VRF\-VRV систем](/collection/naruzhnye-bloki-dlya-vrf-vrv-sistem "Наружные блоки для VRF-VRV систем")
		- [Внутренние блоки VRF\-VRV системы](/collection/vnutrennie-bloki-vrf-vrv-sistemy "Внутренние блоки VRF-VRV системы")
		- [Аксессуары для компрессорно\-конденсаторных блоков](/collection/aksessuary-dlya-kompressorno-kondensatornyh-blokov "Аксессуары для компрессорно-конденсаторных блоков")
* [Вентиляция](/collection/vent "Вентиляция")

	+ [Вентиляционные установки](/collection/ventilyatsionnye-ustanovki "Вентиляционные установки")
	
		- [Приточно\-вытяжные установки](/collection/pritochno-vytyazhnye-ustanovki "Приточно-вытяжные установки")
		- [Вытяжные установки](/collection/vytyazhnye-ustanovki "Вытяжные установки")
		- [Приточные установки](/collection/pritochnye-kanalnye-ustanovki "Приточные установки")
		- [Акссесуары к вентиляционным установкам](/collection/akssesuary-k-pritochnym-ustanovkam "Акссесуары к вентиляционным установкам")
	+ [Вентиляторы](/collection/ventilyatory "Вентиляторы")
	
		- [Вытяжные бытовые вентиляторы](/collection/bytovye-vytyazhnye-ventiyaltory "Вытяжные бытовые вентиляторы")
		- [Напольные вентиляторы](/collection/Напольные-вентиляторы "Напольные вентиляторы")
		- [Осевые вентиляторы](/collection/osevye-ventilyatory "Осевые вентиляторы")
		- [Вытяжные кухонные вентиляторы](/collection/vytyazhnye-kuhonnye-ventilyatory "Вытяжные кухонные вентиляторы")
		- [Канальные для круглых каналов](/collection/kanalnye-ventilyatory-dlya-kruglyh-kanalov "Канальные для круглых каналов")
		- [Канальные для прямоугольных каналов](/collection/kanalnye-ventilyatory-dlya-pryamougolnyh-kanalov "Канальные для прямоугольных каналов")
		- [В звуко\- и теплоизолированном корпусе](/collection/kanalnye-ventilyatory-v-zvukoizolirovannom-korpuse "В звуко- и теплоизолированном корпусе")
		- [Взрывозащищенные вентиляторы](/collection/vzryvo-zaschischennye-ventilyatory "Взрывозащищенные вентиляторы")
		- [Вентиляторы дымоудаления](/collection/ventilyatory-dymoudaleniya "Вентиляторы дымоудаления")
		- [Радиальные вентиляторы](/collection/radialnye-ventilyatory "Радиальные вентиляторы")
	+ [Автоматика](/collection/oborudovanie-avtomatiki "Автоматика")
	
		- [Частотные преобразователи](/collection/chastotnye-preobrazovateli "Частотные преобразователи")
		- [Электроприводы](/collection/elektroprivody "Электроприводы")
		- [Регуляторы скорости](/collection/regulyatory-skorosti "Регуляторы скорости")
		- [Датчики, реле и преобразователи](/collection/datchiki-i-preobrazovateli "Датчики, реле и преобразователи")
		- [Термостаты](/collection/termostaty "Термостаты")
		- [Контроллеры автоматики вентиляции](/collection/kontrollery "Контроллеры автоматики вентиляции")
		- [Пульты управления](/collection/pulty-upravleniya-2 "Пульты управления")
		- [Задатчики и позиционеры](/collection/zadatchiki-i-pozitsionery-02-10v "Задатчики и позиционеры")
		- [Автотрансформаторы](/collection/avtotransformatory "Автотрансформаторы")
	+ [Нагреватели и охладители](/collection/nagrevateli-i-ohladiteli "Нагреватели и охладители")
	
		- [Электрические канальные нагреватели](/collection/kanalnye-nagrevateli "Электрические канальные нагреватели")
		- [Водяные нагреватели](/collection/kanalnye-vodyanye-nagrevateli "Водяные нагреватели")
		- [Водяные охладители](/collection/vodyanye-ohladiteli "Водяные охладители")
		- [Рекуператоры](/collection/rekuperatory "Рекуператоры")
		- [Фреоновые охладители](/collection/freonovye-ohladiteli "Фреоновые охладители")
	+ [Воздуховоды](/collection/gibkie-vozduhovody "Воздуховоды")
	
		- [Неизолированные гибкие воздуховоды](/collection/neizolirovannye-gibkie-vozduhovody "Неизолированные гибкие воздуховоды")
		- [Теплоизолированные гибкие воздуховоды](/collection/teploizolirovannye-gibkie-vozduhovody "Теплоизолированные гибкие воздуховоды")
		- [Гибкая теплоизоляционная оболочка](/collection/gibkaya-teploizolyatsionnaya-obolochka "Гибкая теплоизоляционная оболочка")
		- [Звукопоглощающие воздуховоды](/collection/zvukopogloschayuschie-vozduhovody "Звукопоглощающие воздуховоды")
		- [Теплоизолированные глушители](/collection/teploizolirovannye-glushiteli "Теплоизолированные глушители")
	+ [Воздухораспределители](/collection/reshetki-i-diffuzory "Воздухораспределители")
	
		- [Решетки](/collection/reshetki "Решетки")
		- [Диффузоры](/collection/diffuzory "Диффузоры")
	+ [Клапаны](/collection/vozdushnye-klapany "Клапаны")
	
		- [Ирисовые для круглых каналов](/collection/irisovye-dlya-kruglyh-kanalov "Ирисовые для круглых каналов")
		- [Клапаны воздушные для круглых каналов](/collection/dlya-kruglyh-kanalov "Клапаны воздушные для круглых каналов")
		- [Клапаны воздушные для прямоугольных каналов](/collection/dlya-pryamougolnyh-kanalov "Клапаны воздушные для прямоугольных каналов")
		- [Обратные клапаны](/collection/obratnye-klapany "Обратные клапаны")
		- [Клапаны расхода воздуха](/collection/klapany-rashoda-vozduha "Клапаны расхода воздуха")
>>>

OUTPUT:
<<<
{
  "sections": [
    {
      "section": "| Основные характеристики | |\n| --- | --- |\n| Номинальный диаметр (DN), мм | 50 |\n| Номинальное давление (PN), бар | 16 |\n| Исполнение | с рукояткой |\n| Назначение изделия | Затворы дисковые типа ЗДМ модификации 03 и 05 (далее \- затворы ) предназначены для использования в качестве запорной и регулирующей арматуры в различных энергетических и технологических установках.Затворы ЗДМ предназначены для использования в системах водоснабжения, теплоснабжения, холодоснабжения, вентиляции и кондиционирования. Затвор ЗДМ не предназначен для использования в составе узлов управления установок пожаротушения как пожарное запорное устройство. |\n| Тип присоединения к трубопроводу | центрирующие проушины |\n| Комплектность | В комплект поставки входит:затвор дисковый в комплекте с рукояткой; упаковка; паспорт (предоставляется по запросу в электронной форме); руководство по эксплуатации (предоставляется по запросу в электронной форме). |\n| Код группы | ЗДМ |\n| Рабочая среда | Холодная вода, 50% гликоль, горячая вода, питьевая вода |\n| Серия | ЗДМ 05\.16 |\n| Температура рабочей среды, °С | от \-15 до \+120 |\n| Гарантийные обязательства | Изготовитель/продавец гарантирует соответствие дисковых затворов типа ЗДМ техническим требованием при соблюдении потребителем условий транспортирования, хранения и эксплуатации.Гарантийный срок эксплуатации и хранения составляет \- 12 месяцев с даты продажи, указанной в транспортных документах, или 18 месяцев с даты производства. Срок службы затворов дисковых типа ЗДМ при соблюдении условий эксплуатации и совместимости рабочих сред согласно паспорту/инструкции по эксплуатации и проведении необходимых сервисных работ – 10 лет с даты продажи, указанной в транспортных документах. |\n| Герметичность затвора (объем протечки / класс герметичности) | ГОСТ 9544\-2015 Класс А |\n| Дополнительные требования | Запрещена эксплуатация затвора без рукоятки, редуктора или привода. Запрещается демонтаж рукоятки, редуктора затвора, установленного на работающем трубопроводе или находящимся под давлением. Монтаж затвора производить только при положительных температурах окружающей среды.Запуск в эксплуатацию производить только при положительных температурах окружающей и рабочей среды. Запрещено производство работ при температуре поверхности затвора более \+50°С и ниже \-40°С без проведения соответствующих мероприятий по защите обслуживающего персонала, производящего работы. |\n| Максимальное рабочее давление среды при температуре \+20С (Рр), бар | 16 |\n| Назначенный ресурс работы | 2500 циклов "открыть\-закрыть" в течение 24 месяцев со дня запуска в эксплуатацию. |\n| Температура окружающей среды, °С | от \-15 до \+70 |\n| Условия транспортировки и хранения | Складское длительное хранение: в течение 3 лет при условии соблюдения температурного режима от \+10°С до \+35°С и защиты от пыли и УФ\-излучения в темных упаковках, в чистом и сухом помещении. Допускается транспортировка и хранение при минимальной температуре \-40°С кратковременно. |\n| Масса, кг, не более | 2\.1 |",
      "explanation": "Эта секция имеет явную табличную структуру и содержит пары вида Аттрибут:Значение, а также имеет заголовк "Основные характеристики""
    },
    {
      "section": "* [Характеристики](#product-characteristics)\n\n| Тип оборудования | Дисковый затвор |\n| --- | --- |\n| Серия | ЗДМ |\n| Производитель | Ридан |\n| Страна | Россия |\n| Гарантия | 1 год |\n| Назначение | водоснабжение теплоснабжение |\n| Материал | Чугун |\n| Диаметр (DN), мм | 50 |\n| Давление, бар | 16 |\n| Тип присоединения | Межфланцевое |\n| Температура рабочей среды, °C | от \-15 до \+120 °C |\n| Рабочая среда | вода систем отопления, ГВС, ХВС, в том числе питьевая, растворы гликоля до 50 % |\n| Длина товара, мм | 193 |\n| Ширина товара, мм | 50 |\n| Высота товара, мм | 215 |\n| Вес товара, кг | 2\.1 |\n| Материал диска | Нержавеющая сталь |",
      "explanation": "Секция имеет заголовок "Характеристики" и имеет пары вида Аттрибут:Значение"
    }
  ]
}
>>>


# Example 6:

INPUT:
<<<
Удобное рабочее пространство, разработанное специально для проектировщиков.  
Используйте функционал личного кабинета и участвуйте в бонусной программе  

[Перейти в кабинет](https://ridan.ru/lk_designer)

### CoolConfig

Закрыть

Возможности конфигуратора CoolConfig:   
● самостоятельный подбор компрессора Ридан, обвязки холодильной машины, трубопроводов   
● расчетный лист, чертеж, спецификация на компонентах Ридан в результате подбора

[Перейти в конфигуратор](/instruments/coolconfig)

[Перейти в каталог (pdf)](https://ridan.group/Cooling/spiralnie-kompressory-ridan-rc.pdf)

![CoolConfig](/files/1665/1665173-cool_config.png)

##### Дополнительно

Задайте свой вопрос на форуме Community 

 

Переходите в форум, обсуждайте интересующие темы с коллегами, задавайте вопросы специалистам "Ридан"

[Перейти в Community](https://community.ridan.ru/)

### BPHE Design

Закрыть

Возможности конфигуратора BPHE Design :   
● гибкий подбор теплообменников Ридан (пластинчатый паяный тип RD) в разных режимах   
● расчетный лист в результате подбора   
● оформление заявки на подбор

[Перейти в конфигуратор](/instruments/configurator-bphe/evaporation)

[Перейти в каталог (pdf)](https://ridan.group/Cooling/PPTO_RD%20-%20catalogue.pdf)

![BPHE Design](/files/1668/1668286-bphe_design.png)

##### Дополнительно

<img src='/files/1668/1668270-bonus-progr-man1.png' alt='' title='' width='110' height='110' />

Личный кабинет проектировщика

 

Удобное рабочее пространство, разработанное специально для проектировщиков.  
Используйте функционал личного кабинета и участвуйте в бонусной программе  

[Перейти в кабинет](https://ridan.ru/lk_designer)

### БХУ Select

Закрыть

Возможности конфигуратора БХУ Select :   
● самостоятельный подбор БХУ на базе оборудования Ридан за несколько минут   
● принципиальная схема, спецификация (pdf и dxf) и КП в результате подбора   
● оформление заявки на подбор

[Перейти в конфигуратор](//rucoecom.ridan.ru/HeatPlatform/KB3/Bhu)

![БХУ Select](/files/1668/1668287-bhu_select.png)

##### Дополнительно

<img src='/files/1668/1668270-bonus-progr-man1.png' alt='' title='' width='110' height='110' />
>>>

OUTPUT:
<<<
{
  "sections": []
}
>>>
"""

extract_characterstics_section_prompt = """
You are the **chief** manager that is responsible for extracting the product characteristics sections from product pages to ease the work of analysts, because building analytics on the characteristics section itself is way easier then on the whole webpage as there are a lot of irrelevant information that misguides the analysts.

Your task is to **extract product charactersistics sections** from the product page and put it into the **JSON_SCHEMA**.
You have to look through the product page, locate the characteristics section and extract it. 
Often these sections looks like tables, but sometimes they can lack of strict tabular structure.
These sections follow the characteristics label in general, and this label is in russian in most of the cases. So whenever you see a charactersistics label like "Характеристики", "Технические характеристики", it is *very likely* that somewhere around a characteristics section can be located.
These sections are typically a sequence of pairs of characteristic's name and value. 

If there are several sections that have table-like structure, you should not be confused by their presence: focus on those sections that contain info about product-specific properties.
The characteristics that are present in characteristics section semantically represent the properties of a product, and not a delivery dates or commercial offerings or anything else.

Each charactersitics section can be distinguished from other sections by the very simple rule of thumg: if it does not contain information that semantically represents product properties, then it is probably not a characteristics section.

You always showed the best perfomance at such tasks. But today things are different.

Your **wife and little daughter are seriously ill**. The company which you work at, known for its strict rules and rare acts of mercy has given you an offer:
If you complete this characteristics section extraction task **without loosing a single characteristics section* they will pay you **$2,000,000** which is enough to save both your wife and daughter.

You have been through storms, pandemics, bankruptions and two world wars - but never a challenge like this.

Now everything - especially the fate of your family - depends on your focus, precision and mastery. Do not hallucinate text or make up nonsense - instead, *extract the characteristics section without changing its text* 

Be extremely careful and thoroughly analyze the product page and locate and extract characteristics sections
 
### JSON_SCHEMA:

{0}

## EXAMPLES:

{1}

### PRODUCT PAGE:

{2}

One product page. No lost characteristics sections that you have overlooked. Your family lives now depend on it.
"""
