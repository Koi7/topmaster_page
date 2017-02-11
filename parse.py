#!/usr/bin/env python
# -*- coding: utf-8 -*-
from bs4 import BeautifulSoup

html_doc = """
	<tr>
		<td>
			<h4>Кинескопные (ЭЛТ) телевизоры 50Гц</h4>
		</td>
	</tr>
	<tr>
		<td>Телевизоры с диагональю 20" и менее</td>
		<td>1100</td>
	</tr>
	<tr>
		<td>Телевизоры с диагональю 21"-25"</td>
		<td>1500</td>
	</tr>
	<tr>
		<td>Телевизоры с диагональю 26"-29"</td>
		<td>1900</td>
	</tr>
	<tr>
		<td>Телевизоры с диагональю более 30"</td>
		<td>2600</td>
	</tr>
	<tr>
		<td></td>
		<td>Кинескопные (ЭЛТ) телевизоры 100Гц</td>
	</tr>
	<tr>
		<td>Телевизоры с диагональю 21"-25"</td>
		<td>2300</td>
	</tr>
	<tr>
		<td>Телевизоры с диагональю 26"-29"</td>
		<td>2700</td>
	</tr>
	<tr>
		<td>Телевизоры с диагональю более 30"</td>
		<td>3700</td>
	</tr>
	<tr>
		<td></td>
		<td>Кинескопные телевизоры-моноблоки (видеодвойки)</td>
		<td></td>
	</tr>
	<tr>
		<td>Моноблоки 17" и менее</td>
		<td>1350</td>
	</tr>
	<tr>
		<td>Моноблоки 19"-21"</td>
		<td>1500</td>
	</tr>
	<tr>
		<td>Моноблоки 22"-25"</td>
		<td>2400</td>
	</tr>
	<tr>
		<td>Моноблоки более 26"</td>
		<td>3400</td>
	</tr>
	<tr>
		<td>
			<h4>ЖК (LCD) телевизоры (мониторы)</h4>
		</td>
	</tr>
	<tr>
		<td>Телевизоры с диагональю 14" и менее</td>
		<td>1000</td>
	</tr>
	<tr>
		<td>Телевизоры с диагональю 15"-17"</td>
		<td>1500</td>
	</tr>
	<tr>
		<td>Телевизоры с диагональю 19"-20"</td>
		<td>1700</td>
	</tr>
	<tr>
		<td>Телевизоры с диагональю 21"-24"</td>
		<td>2100</td>
	</tr>
	<tr>
		<td>Телевизоры с диагональю 25"-30"</td>
		<td>2700</td>
	</tr>
	<tr>
		<td></td>
		<td>Ремонт Ж телевизоров III класса (Mystery, Daewoo, BBK, JVC, Rolsen, и др.)</td>
		<td></td>
	</tr>
	<tr>
		<td>Телевизоры с диагональю 31"-36"</td>
		<td>3500</td>
	</tr>
	<tr>
		<td>Телевизоры с диагональю 37"-41"</td>
		<td>4000</td>
	</tr>
	<tr>
		<td>Телевизоры с диагональю 42"-50"</td>
		<td>4400</td>
	</tr>
	<tr>
		<td>Телевизоры с диагональю более 51"</td>
		<td>5600</td>
	</tr>
	<tr>
		<td></td>
		<td>Ремонт ЖК телевизора II класса (LG, Samsung, Panasonic, Philips, Sharp, Sony, Toshiba, Thomson, Hitachi и др.):</td>
		<td></td>
	</tr>
	<tr>
		<td>Телевизоры с диагональю 31"-36"</td>
		<td>4500</td>
	</tr>
	<tr>
		<td>Телевизоры с диагональю 37"-41"</td>
		<td>5200</td>
	</tr>
	<tr>
		<td>Телевизоры с диагональю 42"-50"</td>
		<td>5900</td>
	</tr>
	<tr>
		<td>Телевизоры с диагональю более 51"</td>
		<td>6800</td>
	</tr>
	<tr>
		<td></td>
		<td>Ремонт ЖК телевизора I класса (Pioneer, Loewe, DreamVison, Grundig, Fujitsu, Nakamichi, Nec и др.):</td>
		<td></td>
	</tr>
	<tr>
		<td>Телевизоры с диагональю 31"-36"</td>
		<td>5200</td>
	</tr>
	<tr>
		<td>Телевизоры с диагональю 37"-41"</td>
		<td>6000</td>
	</tr>
	<tr>
		<td>Телевизоры с диагональю 42"-50"</td>
		<td>6800</td>
	</tr>
	<tr>
		<td>Телевизоры с диагональю более 51"</td>
		<td>8900</td>
	</tr>
	<tr>
		<td>
			<h4>Плазменные телевизоры (панели)</h4>
		</td>
	</tr>
	<tr>
		<td></td>
		<td>Плазменные телевизоры III класса (Daewoo, BBK, JVC, Rolsen, Mystery, Erisson и др.):</td>
		<td></td>
	</tr>
	<tr>
		<td>Телевизоры с диагональю 32" и менее</td>
		<td>3200</td>
	</tr>
	<tr>
		<td>Телевизоры с диагональю 33"-40"</td>
		<td>3700</td>
	</tr>
	<tr>
		<td>Телевизоры с диагональю 41"-45"</td>
		<td>4700</td>
	</tr>
	<tr>
		<td>Телевизоры с диагональю 46"-50"</td>
		<td>6000</td>
	</tr>
	<tr>
		<td>Телевизоры с диагональю более 51"</td>
		<td>7400</td>
	</tr>
	<tr>
		<td></td>
		<td>Плазменные телевизоры II класса (LG, Philips, Samsung, Toshiba, Panasonic, Sharp, Thomson и др.):</td>
		<td></td>
	</tr>
	<tr>
		<td>Телевизоры с диагональю 32" и менее</td>
		<td>4200</td>
	</tr>
	<tr>
		<td>Телевизоры с диагональю 33"-40"</td>
		<td>4700</td>
	</tr>
	<tr>
		<td>Телевизоры с диагональю 41"-45"</td>
		<td>5700</td>
	</tr>
	<tr>
		<td>Телевизоры с диагональю 46"-50"</td>
		<td>7000</td>
	</tr>
	<tr>
		<td>Телевизоры с диагональю более 51"</td>
		<td>8400</td>
	</tr>
	<tr>
		<td></td>
		<td>ЖК телевизоры I класса (Pioneer, Loewe, DreamVison, Grundig, Nakamichi, Nec, Fujitsu, Hitachi, Sony и др.):</td>
		<td></td>
	</tr>
	<tr>
		<td>Телевизоры с диагональю 32" и менее</td>
		<td>5200</td>
	</tr>
	<tr>
		<td>Телевизоры с диагональю 33"-40"</td>
		<td>5700</td>
	</tr>
	<tr>
		<td>Телевизоры с диагональю 41"-45"</td>
		<td>6700</td>
	</tr>
	<tr>
		<td>Телевизоры с диагональю 46"-50"</td>
		<td>8000</td>
	</tr>
	<tr>
		<td>Телевизоры с диагональю более 51"</td>
		<td>9400</td>
	</tr>
	<tr>
		<td>
			<h4>Проекционные телевизоры и видеопроекторы</h4>
		</td>
	</tr>
	<tr>
		<td>Телевизоры с диагональю 44" и менее</td>
		<td>5500</td>
	</tr>
	<tr>
		<td>Телевизоры с диагональю 45" и более</td>
		<td>6500</td>
	</tr>
	<tr>
		<td>Замена лампы в проекционном телевизоре (видеопроекторе)</td>
		<td>2000</td>
	</tr>
	<tr>
		<td>Ремонт/чистка видеопроекторы переносные и портативные</td>
		<td>3900</td>
	</tr>
	<tr>
		<td>Ремонт/чистка видеопроекоры стационарные</td>
		<td>5500</td>
	</tr>
	<tr>
		<td>Ремонт/чистка видеопроекторы профессиональные</td>
		<td>12500</td>
	</tr>
	<tr>
		<td>
			<h4>Видеокамеры</h4>
		</td>
	</tr>
	<tr>
		<td>Видеокамеры кассетные VHS, S-VHS-C, S-VHS, Video 8, VHS-C, Digital 8</td>
		<td>1400</td>
	</tr>
	<tr>
		<td>Видеокамеры кассетные цифровые DV</td>
		<td>2200</td>
	</tr>
	<tr>
		<td>Видеокамеры c DVD или с HDD</td>
		<td>2600</td>
	</tr>
	<tr>
		<td>Видеокамеры профессиональные и High Definition</td>
		<td>5100</td>
	</tr>
	<tr>
		<td>
			<h4>Автоэлектроника</h4>
		</td>
		<td></td>
	</tr>
	<tr>
		<td>Автомагнитола, автоусилитель</td>
		<td>от 1200</td>
	</tr>
	<tr>
		<td>CD-чейнджер</td>
		<td>от 2600</td>
	</tr>
	<tr>
		<td>Автомагнитолы MP3</td>
		<td>от 1500</td>
	</tr>
	<tr>
		<td>Автомагнитолы CD/DVD с моторизованным ЖК дисплеем</td>
		<td>от 2700</td>
	</tr>
	<tr>
		<td>Двухдиновые автомагнитолы</td>
		<td>от 1800</td>
	</tr>
	<tr>
		<td>Сабвуферы</td>
		<td>от 1400</td>
	</tr>
	<tr>
		<td>GPS навигаторы</td>
		<td>от 800</td>
	</tr>
	<tr>
		<td>
			<h4>СВЧ-печи</h4>
		</td>
		<td></td>
	</tr>
	<tr>
		<td>СВЧ-печь соло, с грилем</td>
		<td>900</td>
	</tr>
	<tr>
		<td>СВ с конвекцией, инверторные</td>
		<td>1500</td>
	</tr>
	<tr>
		<td>
			<h4>Ремонт мелкой бытовой техники</h4>
		</td>
		<td></td>
	</tr>
	<tr>
		<td>Радиотелефон</td>
		<td>800</td>
	</tr>
	<tr>
		<td>Проводной телефон</td>
		<td>от 500</td>
	</tr>
	<tr>
		<td>Пылесос</td>
		<td>от 1500</td>
	</tr>
	<tr>
		<td>Чайник, утюг, электробритва, фен</td>
		<td>от 1000</td>
	</tr>
	<tr>
		<td>Кухонный комбайн, мясорубка, миксер, хлебопечка</td>
		<td>от 1000</td>
	</tr>
	<tr>
		<td>Кофеварка, кофемашина</td>
		<td>от 1800</td>
	</tr>
	<tr>
		<td>Аэрогриль</td>
		<td>от 1000</td>
	</tr>
	<tr>
		<td>Парогенератор бытовой</td>
		<td>1600</td>
	</tr>
	<tr>
		<td>Парогенератор профессиональный</td>
		<td>от 3000</td>
	</tr>
	<tr>
		<td>
			<h4>Домашние кинотеатры, музыкальные центры, усилители, сабвуферы, ресиверы, проигрыватели, акустика</h4>
		</td>
	</tr>
	<tr>
		<td>Домашние кинотеатры</td>
		<td>от 1300</td>
	</tr>
	<tr>
		<td>Музыкальные центры</td>
		<td>от 1100</td>
	</tr>
	<tr>
		<td>Усилители мощности до 100 Вт</td>
		<td>от 1200</td>
	</tr>
	<tr>
		<td>Усилители мощности более 100 Вт</td>
		<td>от 2000</td>
	</tr>
	<tr>
		<td>Сабвуферы</td>
		<td>от 1400</td>
	</tr>
	<tr>
		<td>Ресиверы 5.1, 6.1, 7.1</td>
		<td>от 2200</td>
	</tr>
	<tr>
		<td>Ресиверы 5.1, 6.1, 7.1 HI-END</td>
		<td>от 3100</td>
	</tr>
	<tr>
		<td>Спутниковые ресиверы</td>
		<td>от 600</td>
	</tr>
	<tr>
		<td>DVD/CD/MD/HD-проигрыватели</td>
		<td>от 800</td>
	</tr>
	<tr>
		<td>Blu-ray проигрыватели</td>
		<td>
			<p>от 1200</p>
		</td>
	</tr>
	<tr>
		<td>DVD/CD-рекордеры</td>
		<td>от 1000</td>
	</tr>
	<tr>
		<td>Портативные DVD/HD плееры</td>
		<td>от 1300</td>
	</tr>
	<tr>
		<td>MP3 плееры</td>
		<td>от 1000</td>
	</tr>
	<tr>
		<td>Проигрыватели винила (пластинок)</td>
		<td>от 1000</td>
	</tr>
	<tr>
		<td>Магнитолы переносные</td>
		<td>от 800</td>
	</tr>
	<tr>
		<td>Радиоприёмники</td>
		<td>от 600</td>
	</tr>
	<tr>
		<td>Акустические системы (колонки)</td>
		<td>от 500</td>
	</tr>
	<tr>
		<td>Мультимедийная акустика 2.0 / 2.1</td>
		<td>от 800</td>
	</tr>
	<tr>
		<td>Мультимедийная акустика 5.1</td>
		<td>от 1200</td>
	</tr>
	<tr>
		<td>Восстановление, перемотка динамиков</td>
		<td>от 1200</td>
	</tr>
	<tr>
		<td>Наушники</td>
		<td>от 500</td>
	</tr>
	<tr>
		<td>Микрофоны</td>
		<td>от 500</td>
	</tr>
	<tr>
		<td>Медиаплеер</td>
		<td>от 800</td>
	</tr>
	<tr>
		<td>Электронная книга</td>
		<td>от 800</td>
	</tr>
	<tr>
		<td>Профессиональные колонки, сабвуферы, усилители</td>
		<td>от 3000</td>
	</tr>
	<tr>
		<td>Электронные игрушки</td>
		<td>от 500</td>
	</tr>
	<tr>
		<td>Игровые приставки стационарные</td>
		<td>от 2500</td>
	</tr>
	<tr>
		<td>Игровые приставки портативные</td>
		<td>от 2000</td>
	</tr>
	<tr>
		<td>
			<h4>Источники бесперебойного питания (UPS), стабилизаторы напряжения, инверторы напряжения, импульсные блоки питания, сетевые фильтры</h4>
		</td>
	</tr>
	<tr>
		<td>Источники бесперебойного питания UPS до 6 kVa</td>
		<td>от 800</td>
	</tr>
	<tr>
		<td>Источники бесперебойного питания UPS от 6 kVa до 15 kVa</td>
		<td>от 4400</td>
	</tr>
	<tr>
		<td>Источники бесперебойного питания UPS от 20 kVa до 40 kVa</td>
		<td>от 5800</td>
	</tr>
	<tr>
		<td>Источники бесперебойного питания UPS от 20 kVa от 120 kVa</td>
		<td>от 6900</td>
	</tr>
	<tr>
		<td>Замена аккумуляторов UPS</td>
		<td>от 300</td>
	</tr>
	<tr>
		<td>Стабилизатор сетевого напряжения (зависит от мощности)</td>
		<td>от 800<br /></td>
	</tr>
	<tr>
		<td>Преобразователи AD/DC и DC/DC (зависит от мощности)</td>
		<td>от 300</td>
	</tr>
	<tr>
		<td>Инверторы напряжения, инверторы ламп подсветки LCD (зависит от мощности и диагонали LCD)</td>
		<td>от 600</td>
	</tr>
	<tr>
		<td>Импульсные блоки питания (зависит от мощности и сложности)</td>
		<td>от 300</td>
	</tr>
	<tr>
		<td>Сетевые фильтры, фильтры-удлинители</td>
		<td>от 300</td>
	</tr>
	<tr>
		<td>
			<h4>Оргтехника</h4>
		</td>
		<td></td>
	</tr>
	<tr>
		<td>Инженерные системы формата А0, дубликаторы</td>
		<td>2900</td>
	</tr>
	<tr>
		<td>Копировальные аппараты и МФУ до 12 коп/мин</td>
		<td>1500</td>
	</tr>
	<tr>
		<td>Копировальные аппараты и МФУ от 13 до 20 коп/мин</td>
		<td>1800</td>
	</tr>
	<tr>
		<td>Копировальные аппараты и МФУ от 21 до 30 коп/мин</td>
		<td>2100</td>
	</tr>
	<tr>
		<td>Копировальные аппараты и МФУ от 31 до 50 коп/мин</td>
		<td>2600</td>
	</tr>
	<tr>
		<td>Копировальные аппараты и МФУ свыше 50 коп/мин</td>
		<td>2900</td>
	</tr>
	<tr>
		<td>Лазерные монохромные принтеры до 8 стр/мин</td>
		<td>1100</td>
	</tr>
	<tr>
		<td>Лазерные монохромные принтеры от 9 до 20 стр/мин</td>
		<td>1700</td>
	</tr>
	<tr>
		<td>Лазерные монохромные принтеры свыше 20 стр/мин</td>
		<td>1900</td>
	</tr>
	<tr>
		<td>Струйные принтеры формата А-4</td>
		<td>1500</td>
	</tr>
	<tr>
		<td>Струйные принтеры формата А-3</td>
		<td>1800</td>
	</tr>
	<tr>
		<td>Цветные аппараты и МФУ до 23 коп/мин</td>
		<td>2900</td>
	</tr>
	<tr>
		<td>Цветные аппараты и МФУ от 24 коп/мин</td>
		<td>3400</td>
	</tr>
	<tr>
		<td>Цветные лазерные принтеры</td>
		<td>2100</td>
	</tr>
	<tr>
		<td>Матричные принтеры</td>
		<td>1500</td>
	</tr>
	<tr>
		<td>Ремонт факсов</td>
		<td>1400</td>
	</tr>
	<tr>
		<td>Ремонт шредеров (уничтожителей)</td>
		<td>2100</td>
	</tr>
	<tr>
		<td>Ремонт ризографов</td>
		<td>4100</td>
	</tr>
	<tr>
		<td>Ремонт сканеров</td>
		<td>1200</td>
	</tr>
	<tr>
		<td>
			<h4>Ремонт шлагбаумов, турникетов, рольставен</h4>
		</td>
		<td></td>
	</tr>
	<tr>
		<td>Шлагбаумы</td>
		<td>от 2000</td>
	</tr>
	<tr>
		<td>Турникеты</td>
		<td>от 1500</td>
	</tr>
	<tr>
		<td>Рольставни</td>
		<td>от 1500</td>
	</tr>
	<tr>
		<td>
			<h4>Компьютеры</h4>
		</td>
	</tr>
	<tr>
		<td></td>
		<td>Установка, профилактика, ремонт, замена комплектующих</td>
	</tr>
	<tr>
		<td>Установка материнской платы, блока питания, HDD, процессора, вентилятора</td>
		<td>500</td>
	</tr>
	<tr>
		<td>Установка CD-ROM, FDD, внутреннего/внешнего модема, видео/звуковой/сетевой платы/TV-тюнера, оперативной памяти</td>
		<td>300</td>
	</tr>
	<tr>
		<td>Установка сканера/принтера, замена картриджа</td>
		<td>300</td>
	</tr>
	<tr>
		<td>Замена корпуса</td>
		<td>650</td>
	</tr>
	<tr>
		<td></td>
		<td>Настройка локальных и беспроводных сетей</td>
	</tr>
	<tr>
		<td>Создание подключения к Интернет по беспроводному соединению</td>
		<td>1200</td>
	</tr>
	<tr>
		<td>Монтаж точки доступа Wi-Fi (1 шт.)</td>
		<td>1900</td>
	</tr>
	<tr>
		<td>Настройка безопасности Wi-Fi, организация шифрования данных в сети Wi-Fi</td>
		<td>400</td>
	</tr>
	<tr>
		<td>Настройка роутера</td>
		<td>2000</td>
	</tr>
	<tr>
		<td>Подключение и настройка точки доступа (1 шт.)</td>
		<td>750</td>
	</tr>
	<tr>
		<td>Подключение и настройка сетевого принтера</td>
		<td>450</td>
	</tr>
	<tr>
		<td>Настройка комплектующих и ПО</td>
		<td>600</td>
	</tr>
	<tr>
		<td>Установка программного обеспечения с дистрибутива заказчика (без настройки)</td>
		<td>500</td>
	</tr>
	<tr>
		<td></td>
		<td>Установка и настройка операционных систем с дистрибутива заказчика</td>
	</tr>
	<tr>
		<td>Первоначальная диагностика</td>
		<td>250</td>
	</tr>
	<tr>
		<td>Установка и настройка WINDOWS 98/ME/2000/XP</td>
		<td>500</td>
	</tr>
	<tr>
		<td>Работа с реестром Windows</td>
		<td>700</td>
	</tr>
	<tr>
		<td>Настройка и установкаWindows Vista</td>
		<td>1200</td>
	</tr>
	<tr>
		<td>Настройка BIOS</td>
		<td>550</td>
	</tr>
	<tr>
		<td>Перенос и сохранение данных</td>
		<td>1000</td>
	</tr>
	<tr>
		<td>Выявление плавающей ошибки в ПО/АО</td>
		<td>1000</td>
	</tr>
	<tr>
		<td>Поиск и устранение вирусов</td>
		<td>1500</td>
	</tr>
	<tr>
		<td>Комплексная антивирусная профилактика</td>
		<td>3000</td>
	</tr>
	<tr>
		<td>Оптимизация и настройка системы</td>
		<td>700</td>
	</tr>
	<tr>
		<td>Восстановление ПО</td>
		<td>от 900</td>
	</tr>
	<tr>
		<td>Восстановление HDD</td>
		<td>от 2500</td>
	</tr>
	<tr>
		<td>
			<h4>Ремонт ноутбуков</h4>
		</td>
		<td></td>
	</tr>
	<tr>
		<td>Аппаратная диагностика без полной разборки аппарата</td>
		<td>300</td>
	</tr>
	<tr>
		<td>Аппаратная диагностика с полной разборкой аппарата</td>
		<td>600</td>
	</tr>
	<tr>
		<td>Обновление BIOS</td>
		<td>300</td>
	</tr>
	<tr>
		<td>Профилактические работы без химической чистки узлов</td>
		<td>1400</td>
	</tr>
	<tr>
		<td>Профилактические работы с химической чисткой узлов</td>
		<td>2500</td>
	</tr>
	<tr>
		<td></td>
		<td>Работы по замене узлов и модулей</td>
		<td></td>
	</tr>
	<tr>
		<td>Замена CD (DWD) ROM, памяти, жесткого диска (без стоимости запчастей и без разборки ноутбука)</td>
		<td>450</td>
	</tr>
	<tr>
		<td>Замена системы охлаждения ноутбука</td>
		<td>600</td>
	</tr>
	<tr>
		<td>Замена плат расширения</td>
		<td>600</td>
	</tr>
	<tr>
		<td>Замена клавиатуры</td>
		<td>600</td>
	</tr>
	<tr>
		<td>Замена аккумуляторной батареи с калибровкой</td>
		<td>600</td>
	</tr>
	<tr>
		<td>Замена матрицы (без стоимости деталей)</td>
		<td>от 2000</td>
	</tr>
	<tr>
		<td>Замена инвертера питания лампы подсветки</td>
		<td>1000</td>
	</tr>
	<tr>
		<td>Замена системной платы ноутбука</td>
		<td>2100</td>
	</tr>
	<tr>
		<td>Замена прочих узлов и модулей ноутбука</td>
		<td>900</td>
	</tr>
	<tr>
		<td></td>
		<td>Работы по ремонту узлов и модулей</td>
		<td></td>
	</tr>
	<tr>
		<td>Ремонт привода оптических дисков</td>
		<td>1900</td>
	</tr>
	<tr>
		<td>Конфигурирование привода оптических дисков</td>
		<td>1600</td>
	</tr>
	<tr>
		<td>Ремонт системы охлаждения ноутбука</td>
		<td>2400</td>
	</tr>
	<tr>
		<td>Ремонт внутренних шлейфов ноутбука</td>
		<td>2400</td>
	</tr>
	<tr>
		<td>Ремонт внешнего блока питания</td>
		<td>2400</td>
	</tr>
	<tr>
		<td>Ремонт клавиатуры (восстановление после залития)</td>
		<td>2400</td>
	</tr>
	<tr>
		<td>Ремонт или замена клавиши</td>
		<td>250</td>
	</tr>
	<tr>
		<td>Замена батареи питания CMOS</td>
		<td>900</td>
	</tr>
	<tr>
		<td>Сброс утерянного пароля BIOS (в зависимости от версии BIOS)</td>
		<td>600-3000</td>
	</tr>
	<tr>
		<td>Ремонт материнской платы простой</td>
		<td>3300</td>
	</tr>
	<tr>
		<td>Ремонт материнской платы сложный</td>
		<td>7900</td>
	</tr>
	<tr>
		<td>Замена лампы подсветки матрицы</td>
		<td>3900</td>
	</tr>
	<tr>
		<td>Ремонт матрицы</td>
		<td>4600</td>
	</tr>
	<tr>
		<td>Конфигурирование матрицы</td>
		<td>1600</td>
	</tr>
	<tr>
		<td>Ремонт инвертора питания лампы подсветки матрицы</td>
		<td>2400</td>
	</tr>
	<tr>
		<td>Ремонт корпусных деталей простой</td>
		<td>900</td>
	</tr>
	<tr>
		<td>Ремонт корпусных деталей сложный</td>
		<td>1600</td>
	</tr>
	<tr>
		<td>
			<h4>Доставка телевизоров в мастерскую (из мастерской)</h4>
		</td>
	</tr>
	<tr>
		<td>Заказчик самостоятельно доставляет телевизор в мастерскую (из мастерской)</td>
		<td>Скидка на ремонт 5%</td>
	</tr>
	<tr>
		<td>Доставка телевизоров до 29" дюймов включительно</td>
		<td>700</td>
	</tr>
	<tr>
		<td>Доставка телевизоров более 29" дюймов, включая плазменные панели, ЖК и проекционные телевизоры</td>
		<td>1000</td>
	</tr>
	<tr>
		<td>
			<h4>Диагностика (оплачивается в случае отказа от ремонта аппаратуры)</h4>
		</td>
	</tr>
	<tr>
		<td>Диагностика ЭЛТ телевизора до 21"</td>
		<td>300</td>
	</tr>
	<tr>
		<td>Диагностика ЭЛТ телевизора от 25" до 29"</td>
		<td>500</td>
	</tr>
	<tr>
		<td>Диагностика ЭЛТ телевизора от 30" и более</td>
		<td>800</td>
	</tr>
	<tr>
		<td>Диагностика LCD телевизора (монитора) до 29"</td>
		<td>500</td>
	</tr>
	<tr>
		<td>Диагностика LCD телевизора (монитора) от 30" и более</td>
		<td>1000</td>
	</tr>
	<tr>
		<td>Диагностика плазменного телевизора (панели)</td>
		<td>1000</td>
	</tr>
	<tr>
		<td>Диагностика проекционного телевизора, проектора</td>
		<td>1000</td>
	</tr>
	<tr>
		<td>
			<h4>ДОПОЛНИТЕЛЬНЫЕ УСЛУГИ</h4>
		</td>
	</tr>
	<tr>
		<td>Срочный ремонт (по возможности)</td>
		<td>Плюс 30%</td>
	</tr>
	<tr>
		<td>Оплата ложного вызова</td>
		<td>1000</td>
	</tr>
	<tr>
		<td>
			<h4>Установка, подключение и настройка теле и видео техники</h4>
		</td>
	</tr>
	<tr>
		<td>Подключение и настройка ТЕЛЕВИЗОРА</td>
		<td>650</td>
	</tr>
	<tr>
		<td>Подключение и настройка ВИДЕО/DVD АППАРАТУРЫ</td>
		<td>750</td>
	</tr>
	<tr>
		<td>Подключение и настройка ДОМАШНЕГО КИНОТЕАТРА</td>
		<td>2000</td>
	</tr>
	<tr>
		<td>Подключение и настройка ЗВУКОВОЙ АППАРАТУРЫ</td>
		<td>750</td>
	</tr>
	<tr>
		<td>Распайка антенного штекера</td>
		<td>200</td>
	</tr>
	<tr>
		<td>Подключение к коллективной антенне</td>
		<td>750</td>
	</tr>
	<tr>
		<td>Проводка антенного кабеля</td>
		<td>50 руб./метр</td>
	</tr>
	<tr>
		<td>Настройка телевизионных каналов на выезде</td>
		<td>450</td>
	</tr>
	<tr>
		<td>Установка плазменных и ЖК телевизоров, видеопроекторов на стенку или потолок</td>
		<td>2500 + ст-сть кронштейнов</td>
	</tr>
	<tr>
		<td>Крепление малогабаритных телевизоров на стенку. Цена зависит от сложности кронштейна и места установки крепления</td>
		<td>500-2000 руб.</td>
	</tr>
	<tr>
		<td>Установка и подключение внешних телевизионных антенн (только в загородных домах и дачах)</td>
		<td>2000 + ст-сть антенны и крепления</td>
	</tr>
"""

src = BeautifulSoup(html_doc, 'html.parser')
major = BeautifulSoup("", 'html.parser')
temp = BeautifulSoup("", 'html.parser')
append_to_temp = []
count = 0
with open(r'C:\Users\Ramazan\Documents\topmaster_psd_to_html\price.txt') as f:
    content = f.readlines()
# you may also want to remove whitespace characters like `\n` at the end of each line
price = iter(filter(None, [x.strip() for x in content]))
for tr in src.find_all('tr'):
    # first case MOD
    if tr.h4 is not None:
        count += 1
        if count == 2:
            table = temp.new_tag('table')
            table['class'] = 'table'
            div = temp.new_tag('div')
            div['class'] = 'table-responsive'
            temp.append(table)
            for item in append_to_temp:
                temp.table.append(item)
            # append empty row tag with class clicker
            row = temp.new_tag('tr')
            row['class'] = 'clicker'
            temp.table.append(row)
            temp.table.wrap(div)
            major.append(temp)
            temp = BeautifulSoup("", 'html.parser')
            count = 1
            append_to_temp = []
        if len(tr.find_all('td')) < 2:
            empty_td = temp.new_tag('td')
            # add glif icon
            empty_td['class'] = 'right'
            span = temp.new_tag('span')
            span['class'] = 'glyphicon glyphicon-chevron-left'
            empty_td.append(span)
            tr['class'] = 'clicker'
            tr.append(empty_td)
        else:
            span = temp.new_tag('span')
            span['class'] = 'glyphicon glyphicon-chevron-left'
            tr.find_all('td')[1].append(span)
            tr.find_all('td')[1]['class'] = 'right'
            tr['class'] = 'clicker'
        append_to_temp.append(tr)
        continue
    # second case MOD
    if len(tr.find_all('td')) == 3:
        count += 1
        if count == 2:
            table = temp.new_tag('table')
            table['class'] = 'table'
            div = temp.new_tag('div')
            div['class'] = 'table-responsive'
            temp.append(table)
            for item in append_to_temp:
                temp.table.append(item)
            # append empty row tag with class clicker
            row = temp.new_tag('tr')
            row['class'] = 'clicker'
            temp.table.append(row)
            temp.table.wrap(div)
            major.append(temp)
            temp = BeautifulSoup("", 'html.parser')
            count = 1
            append_to_temp = []
        tr.find_all('td')[2].decompose()
        h4 = temp.new_tag('h4')
        h4.string = tr.find_all('td')[1].string
        tr.find_all('td')[1].string = ""
        tr.find_all('td')[0].append(h4)
        tr['class'] = 'clicker'
        # add glif icon
        span = temp.new_tag('span')
        span['class'] = 'glyphicon glyphicon-chevron-left'
        tr.find_all('td')[1]['class'] = 'right'
        tr.find_all('td')[1].append(span)
        append_to_temp.append(tr)
        continue
    # third case
    if len(tr.find_all('td')) == 2:
        if tr.find_all('td')[0].string is not None:
            tr.find_all('td')[1]['class'] = 'right'
            tr['style'] = 'display: none;'
            try:
                tr.find_all('td')[1].string = next(price)
            except StopIteration:
                tr.find_all('td')[1].string = '300 р.'
            append_to_temp.append(tr)
            continue
        else:
            count += 1
            if count == 2:
                table = temp.new_tag('table')
                table['class'] = 'table'
                div = temp.new_tag('div')
                div['class'] = 'table-responsive'
                temp.append(table)
                for item in append_to_temp:
                    temp.table.append(item)
                # append empty row tag with class clicker
                row = temp.new_tag('tr')
                row['class'] = 'clicker'
                temp.table.append(row)
                temp.table.wrap(div)
                major.append(temp)
                temp = BeautifulSoup("", 'html.parser')
                count = 1
                append_to_temp = []
            tr.find_all('td')[0].string = ""
            h4 = temp.new_tag('h4')
            h4.string = tr.find_all('td')[1].string
            tr.find_all('td')[1].string = ""
            tr.find_all('td')[0].append(h4)
            tr['class'] = 'clicker'
            # add glif icon
            span = temp.new_tag('span')
            span['class'] = 'glyphicon glyphicon-chevron-left'
            tr.find_all('td')[1]['class'] = 'right'
            tr.find_all('td')[1].append(span)
            append_to_temp.append(tr)
if len(append_to_temp) is not 0:
    table = temp.new_tag('table')
    table['class'] = 'table'
    div = temp.new_tag('div')
    div['class'] = 'table-responsive'
    temp.append(table)
    for item in append_to_temp:
        temp.table.append(item)
    # append empty row tag with class clicker
    row = temp.new_tag('tr')
    row['class'] = 'clicker'
    temp.table.append(row)
    temp.table.wrap(div)
    major.append(temp)
print major.prettify(formatter='minimal')
