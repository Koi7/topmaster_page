#!/usr/bin/env python
# -*- coding: utf-8 -*-
from bs4 import BeautifulSoup
import sys

html = """
  <body>
  <p id="fake">
  Ремонт Севастополь Repair Sevastopol  Большая Морская  Центр Ремонт телефонов Ремонт планшетов телефонов смартфонов компьтеров ноутбуков бытовой техникиРемонт Севастополь Repair Sevastopol  Большая Морская  Центр Ремонт телефонов Ремонт планшетов телефонов смартфонов компьтеров ноутбуков бытовой техникиРемонт Севастополь Repair Sevastopol  Большая Морская  Центр Ремонт телефонов Ремонт планшетов телефонов смартфонов компьтеров ноутбуков бытовой техникиРемонт Севастополь Repair Sevastopol  Большая Морская  Центр Ремонт телефонов Ремонт планшетов телефонов смартфонов компьтеров ноутбуков бытовой техникиРемонт Севастополь Repair Sevastopol  Большая Морская  Центр Ремонт телефонов Ремонт планшетов телефонов смартфонов компьтеров ноутбуков бытовой техникиРемонт Севастополь Repair Sevastopol  Большая Морская  Центр Ремонт телефонов Ремонт планшетов телефонов смартфонов компьтеров ноутбуков бытовой техникиРемонт Севастополь Repair Sevastopol  Большая Морская  Центр Ремонт телефонов Ремонт планшетов телефонов смартфонов компьтеров ноутбуков бытовой техникиРемонт Севастополь Repair Sevastopol  Большая Морская  Центр Ремонт телефонов Ремонт планшетов телефонов смартфонов компьтеров ноутбуков бытовой техникиРемонт Севастополь Repair Sevastopol  Большая Морская  Центр Ремонт телефонов Ремонт планшетов телефонов смартфонов компьтеров ноутбуков бытовой техникиРемонт Севастополь Repair Sevastopol  Большая Морская  Центр Ремонт телефонов Ремонт планшетов телефонов смартфонов компьтеров ноутбуков бытовой техникиРемонт Севастополь Repair Sevastopol  Большая Морская  Центр Ремонт телефонов Ремонт планшетов телефонов смартфонов компьтеров ноутбуков бытовой техникиРемонт Севастополь Repair Sevastopol  Большая Морская  Центр Ремонт телефонов Ремонт планшетов телефонов смартфонов компьтеров ноутбуков бытовой техникиРемонт Севастополь Repair Sevastopol  Большая Морская  Центр Ремонт телефонов Ремонт планшетов телефонов смартфонов компьтеров ноутбуков бытовой техникиРемонт Севастополь Repair Sevastopol  Большая Морская  Центр Ремонт телефонов Ремонт планшетов телефонов смартфонов компьтеров ноутбуков бытовой техникиРемонт Севастополь Repair Sevastopol  Большая Морская  Центр Ремонт телефонов Ремонт планшетов телефонов смартфонов компьтеров ноутбуков бытовой техникиРемонт Севастополь Repair Sevastopol  Большая Морская  Центр Ремонт телефонов Ремонт планшетов телефонов смартфонов компьтеров ноутбуков бытовой техникиРемонт Севастополь Repair Sevastopol  Большая Морская  Центр Ремонт телефонов Ремонт планшетов телефонов смартфонов компьтеров ноутбуков бытовой техникиРемонт Севастополь Repair Sevastopol  Большая Морская  Центр Ремонт телефонов Ремонт планшетов телефонов смартфонов компьтеров ноутбуков бытовой техникиРемонт Севастополь Repair Sevastopol  Большая Морская  Центр Ремонт телефонов Ремонт планшетов телефонов смартфонов компьтеров ноутбуков бытовой техникиРемонт Севастополь Repair Sevastopol  Большая Морская  Центр Ремонт телефонов Ремонт планшетов телефонов смартфонов компьтеров ноутбуков бытовой техникиРемонт Севастополь Repair Sevastopol  Большая Морская  Центр Ремонт телефонов Ремонт планшетов телефонов смартфонов компьтеров ноутбуков бытовой техникиРемонт Севастополь Repair Sevastopol  Большая Морская  Центр Ремонт телефонов Ремонт планшетов телефонов смартфонов компьтеров ноутбуков бытовой техникиРемонт Севастополь Repair Sevastopol  Большая Морская  Центр Ремонт телефонов Ремонт планшетов телефонов смартфонов компьтеров ноутбуков бытовой техникиРемонт Севастополь Repair Sevastopol  Большая Морская  Центр Ремонт телефонов Ремонт планшетов телефонов смартфонов компьтеров ноутбуков бытовой техникиРемонт Севастополь Repair Sevastopol  Большая Морская  Центр Ремонт телефонов Ремонт планшетов телефонов смартфонов компьтеров ноутбуков бытовой техникиРемонт Севастополь Repair Sevastopol  Большая Морская  Центр Ремонт телефонов Ремонт планшетов телефонов смартфонов компьтеров ноутбуков бытовой техникиРемонт Севастополь Repair Sevastopol  Большая Морская  Центр Ремонт телефонов Ремонт планшетов телефонов смартфонов компьтеров ноутбуков бытовой техникиРемонт Севастополь Repair Sevastopol  Большая Морская  Центр Ремонт телефонов Ремонт планшетов телефонов смартфонов компьтеров ноутбуков бытовой техникиРемонт Севастополь Repair Sevastopol  Большая Морская  Центр Ремонт телефонов Ремонт планшетов телефонов смартфонов компьтеров ноутбуков бытовой техникиРемонт Севастополь Repair Sevastopol  Большая Морская  Центр Ремонт телефонов Ремонт планшетов телефонов смартфонов компьтеров ноутбуков бытовой техникиРемонт Севастополь Repair Sevastopol  Большая Морская  Центр Ремонт телефонов Ремонт планшетов телефонов смартфонов компьтеров ноутбуков бытовой техники замена дисплея замена клавиатуры замена сенсора Восстановление после попадания воды  замена дисплея замена клавиатуры замена сенсора Восстановление после попадания воды  замена дисплея замена клавиатуры замена сенсора Восстановление после попадания воды  замена дисплея замена клавиатуры замена сенсора Восстановление после попадания воды  замена дисплея замена клавиатуры замена сенсора Восстановление после попадания воды  замена дисплея замена клавиатуры замена сенсора Восстановление после попадания воды  замена дисплея замена клавиатуры замена сенсора Восстановление после попадания воды  замена дисплея замена клавиатуры замена сенсора Восстановление после попадания воды  замена дисплея замена клавиатуры замена сенсора Восстановление после попадания воды  замена дисплея замена клавиатуры замена сенсора Восстановление после попадания воды  замена дисплея замена клавиатуры замена сенсора Восстановление после попадания воды  замена дисплея замена клавиатуры замена сенсора Восстановление после попадания воды  замена дисплея замена клавиатуры замена сенсора Восстановление после попадания воды  замена дисплея замена клавиатуры замена сенсора Восстановление после попадания воды  замена дисплея замена клавиатуры замена сенсора Восстановление после попадания воды  замена дисплея замена клавиатуры замена сенсора Восстановление после попадания воды  замена дисплея замена клавиатуры замена сенсора Восстановление после попадания воды  замена дисплея замена клавиатуры замена сенсора Восстановление после попадания воды  замена дисплея замена клавиатуры замена сенсора Восстановление после попадания воды  замена дисплея замена клавиатуры замена сенсора Восстановление после попадания воды  замена дисплея замена клавиатуры замена сенсора Восстановление после попадания воды  замена дисплея замена клавиатуры замена сенсора Восстановление после попадания воды  замена дисплея замена клавиатуры замена сенсора Восстановление после попадания воды  замена дисплея замена клавиатуры замена сенсора Восстановление после попадания воды  замена дисплея замена клавиатуры замена сенсора Восстановление после попадания воды  замена дисплея замена клавиатуры замена сенсора Восстановление после попадания воды  замена дисплея замена клавиатуры замена сенсора Восстановление после попадания воды 
  </p>

    <div class="container-fluid">

      <div id="top" class="row">

        <div class="col-md-12">

          <img width="700" class="img-responsive" src="images/logo.png" alt="логотип">

        </div>

      </div>

      <div class="row">

        <div class="info-column col-md-8">

            <h3 class="info-title bg-info">

              <span class="glyphicon glyphicon-list"></span>

              <br>

              Услуги и цены

            </h3>

<div class="table-responsive">
 <table class="table">
  <tr class="clicker">
   <td>
    <h4>
     Кинескопные (ЭЛТ) телевизоры 50Гц
    </h4>
   </td>
   <td class="right">
    <span class="glyphicon glyphicon-chevron-left">
    </span>
   </td>
  </tr>
  <tr style="display: none;">
   <td>
    Телевизоры с диагональю 20" и менее
   </td>
   <td class="right">
    350 р.
   </td>
  </tr>
  <tr style="display: none;">
   <td>
    Телевизоры с диагональю 21"-25"
   </td>
   <td class="right">
    350 р.
   </td>
  </tr>
  <tr style="display: none;">
   <td>
    Телевизоры с диагональю 26"-29"
   </td>
   <td class="right">
    600 р.
   </td>
  </tr>
  <tr style="display: none;">
   <td>
    Телевизоры с диагональю более 30"
   </td>
   <td class="right">
    800 р.
   </td>
  </tr>
 </table>
</div>
<div class="table-responsive">
 <table class="table">
  <tr class="clicker">
   <td>
    <h4>
     Кинескопные (ЭЛТ) телевизоры 100Гц
    </h4>
   </td>
   <td class="right">
    <span class="glyphicon glyphicon-chevron-left">
    </span>
   </td>
  </tr>
  <tr style="display: none;">
   <td>
    Телевизоры с диагональю 21"-25"
   </td>
   <td class="right">
    600 р.
   </td>
  </tr>
  <tr style="display: none;">
   <td>
    Телевизоры с диагональю 26"-29"
   </td>
   <td class="right">
    800 р.
   </td>
  </tr>
  <tr style="display: none;">
   <td>
    Телевизоры с диагональю более 30"
   </td>
   <td class="right">
    1000 р.
   </td>
  </tr>
 </table>
</div>
<div class="table-responsive">
 <table class="table">
  <tr class="clicker">
   <td>
    <h4>
     Кинескопные телевизоры-моноблоки (видеодвойки)
    </h4>
   </td>
   <td class="right">
    <span class="glyphicon glyphicon-chevron-left">
    </span>
   </td>
  </tr>
  <tr style="display: none;">
   <td>
    Моноблоки 17" и менее
   </td>
   <td class="right">
    350 р.
   </td>
  </tr>
  <tr style="display: none;">
   <td>
    Моноблоки 19"-21"
   </td>
   <td class="right">
    350 р.
   </td>
  </tr>
  <tr style="display: none;">
   <td>
    Моноблоки 22"-25"
   </td>
   <td class="right">
    600 р.
   </td>
  </tr>
  <tr style="display: none;">
   <td>
    Моноблоки более 26"
   </td>
   <td class="right">
    800 р.
   </td>
  </tr>
 </table>
</div>
<div class="table-responsive">
 <table class="table">
  <tr class="clicker">
   <td>
    <h4>
     ЖК (LCD) телевизоры (мониторы)
    </h4>
   </td>
   <td class="right">
    <span class="glyphicon glyphicon-chevron-left">
    </span>
   </td>
  </tr>
  <tr style="display: none;">
   <td>
    Телевизоры с диагональю 14" и менее
   </td>
   <td class="right">
    350 р.
   </td>
  </tr>
  <tr style="display: none;">
   <td>
    Телевизоры с диагональю 15"-17"
   </td>
   <td class="right">
    400 р.
   </td>
  </tr>
  <tr style="display: none;">
   <td>
    Телевизоры с диагональю 19"-20"
   </td>
   <td class="right">
    600 р.
   </td>
  </tr>
  <tr style="display: none;">
   <td>
    Телевизоры с диагональю 21"-24"
   </td>
   <td class="right">
    600 р.
   </td>
  </tr>
  <tr style="display: none;">
   <td>
    Телевизоры с диагональю 25"-30"
   </td>
   <td class="right">
    800 р.
   </td>
  </tr>
 </table>
</div>
<div class="table-responsive">
 <table class="table">
  <tr class="clicker">
   <td>
    <h4>
     Ремонт ЖК телевизоров III класса (Mystery, Daewoo, BBK, JVC, Rolsen, и др.)
    </h4>
   </td>
   <td class="right">
    <span class="glyphicon glyphicon-chevron-left">
    </span>
   </td>
  </tr>
  <tr style="display: none;">
   <td>
    Телевизоры с диагональю 31"-36"
   </td>
   <td class="right">
    800 р.
   </td>
  </tr>
  <tr style="display: none;">
   <td>
    Телевизоры с диагональю 37"-41"
   </td>
   <td class="right">
    1000 р.
   </td>
  </tr>
  <tr style="display: none;">
   <td>
    Телевизоры с диагональю 42"-50"
   </td>
   <td class="right">
    1300 р.
   </td>
  </tr>
  <tr style="display: none;">
   <td>
    Телевизоры с диагональю более 51"
   </td>
   <td class="right">
    1500 р.
   </td>
  </tr>
 </table>
</div>
<div class="table-responsive">
 <table class="table">
  <tr class="clicker">
   <td>
    <h4>
     Ремонт ЖК телевизора II класса (LG, Samsung, Panasonic, Philips, Sharp, Sony, Toshiba, Thomson, Hitachi и др.):
    </h4>
   </td>
   <td class="right">
    <span class="glyphicon glyphicon-chevron-left">
    </span>
   </td>
  </tr>
  <tr style="display: none;">
   <td>
    Телевизоры с диагональю 31"-36"
   </td>
   <td class="right">
    800 р.
   </td>
  </tr>
  <tr style="display: none;">
   <td>
    Телевизоры с диагональю 37"-41"
   </td>
   <td class="right">
    1200 р.
   </td>
  </tr>
  <tr style="display: none;">
   <td>
    Телевизоры с диагональю 42"-50"
   </td>
   <td class="right">
    1500 р.
   </td>
  </tr>
  <tr style="display: none;">
   <td>
    Телевизоры с диагональю более 51"
   </td>
   <td class="right">
    1800 р.
   </td>
  </tr>
 </table>
</div>
<div class="table-responsive">
 <table class="table">
  <tr class="clicker">
   <td>
    <h4>
     Ремонт ЖК телевизора I класса (Pioneer, Loewe, DreamVison, Grundig, Fujitsu, Nakamichi, Nec и др.):
    </h4>
   </td>
   <td class="right">
    <span class="glyphicon glyphicon-chevron-left">
    </span>
   </td>
  </tr>
  <tr style="display: none;">
   <td>
    Телевизоры с диагональю 31"-36"
   </td>
   <td class="right">
    800 р.
   </td>
  </tr>
  <tr style="display: none;">
   <td>
    Телевизоры с диагональю 37"-41"
   </td>
   <td class="right">
    1300 р.
   </td>
  </tr>
  <tr style="display: none;">
   <td>
    Телевизоры с диагональю 42"-50"
   </td>
   <td class="right">
    1500 р.
   </td>
  </tr>
  <tr style="display: none;">
   <td>
    Телевизоры с диагональю более 51"
   </td>
   <td class="right">
    1900 р.
   </td>
  </tr>
 </table>
</div>
<div class="table-responsive">
 <table class="table">
  <tr class="clicker">
   <td>
    <h4>
     Плазменные телевизоры (панели)
    </h4>
   </td>
   <td class="right">
    <span class="glyphicon glyphicon-chevron-left">
    </span>
   </td>
  </tr>
 </table>
</div>
<div class="table-responsive">
 <table class="table">
  <tr class="clicker">
   <td>
    <h4>
     Плазменные телевизоры III класса (Daewoo, BBK, JVC, Rolsen, Mystery, Erisson и др.):
    </h4>
   </td>
   <td class="right">
    <span class="glyphicon glyphicon-chevron-left">
    </span>
   </td>
  </tr>
  <tr style="display: none;">
   <td>
    Телевизоры с диагональю 32" и менее
   </td>
   <td class="right">
    800 р.
   </td>
  </tr>
  <tr style="display: none;">
   <td>
    Телевизоры с диагональю 33"-40"
   </td>
   <td class="right">
    1300 р.
   </td>
  </tr>
  <tr style="display: none;">
   <td>
    Телевизоры с диагональю 41"-45"
   </td>
   <td class="right">
    1500 р.
   </td>
  </tr>
  <tr style="display: none;">
   <td>
    Телевизоры с диагональю 46"-50"
   </td>
   <td class="right">
    1900 р.
   </td>
  </tr>
  <tr style="display: none;">
   <td>
    Телевизоры с диагональю более 51"
   </td>
   <td class="right">
    2500р.
   </td>
  </tr>
 </table>
</div>
<div class="table-responsive">
 <table class="table">
  <tr class="clicker">
   <td>
    <h4>
     Плазменные телевизоры II класса (LG, Philips, Samsung, Toshiba, Panasonic, Sharp, Thomson и др.):
    </h4>
   </td>
   <td class="right">
    <span class="glyphicon glyphicon-chevron-left">
    </span>
   </td>
  </tr>
  <tr style="display: none;">
   <td>
    Телевизоры с диагональю 32" и менее
   </td>
   <td class="right">
    900 р.
   </td>
  </tr>
  <tr style="display: none;">
   <td>
    Телевизоры с диагональю 33"-40"
   </td>
   <td class="right">
    1400 р.
   </td>
  </tr>
  <tr style="display: none;">
   <td>
    Телевизоры с диагональю 41"-45"
   </td>
   <td class="right">
    1600 р.
   </td>
  </tr>
  <tr style="display: none;">
   <td>
    Телевизоры с диагональю 46"-50"
   </td>
   <td class="right">
    2000 р.
   </td>
  </tr>
  <tr style="display: none;">
   <td>
    Телевизоры с диагональю более 51"
   </td>
   <td class="right">
    2600 р.
   </td>
  </tr>
 </table>
</div>
<div class="table-responsive">
 <table class="table">
  <tr class="clicker">
   <td>
    <h4>
     ЖК телевизоры I класса (Pioneer, Loewe, DreamVison, Grundig, Nakamichi, Nec, Fujitsu, Hitachi, Sony и др.):
    </h4>
   </td>
   <td class="right">
    <span class="glyphicon glyphicon-chevron-left">
    </span>
   </td>
  </tr>
  <tr style="display: none;">
   <td>
    Телевизоры с диагональю 32" и менее
   </td>
   <td class="right">
    1000 р.
   </td>
  </tr>
  <tr style="display: none;">
   <td>
    Телевизоры с диагональю 33"-40"
   </td>
   <td class="right">
    1500 р.
   </td>
  </tr>
  <tr style="display: none;">
   <td>
    Телевизоры с диагональю 41"-45"
   </td>
   <td class="right">
    1700 р.
   </td>
  </tr>
  <tr style="display: none;">
   <td>
    Телевизоры с диагональю 46"-50"
   </td>
   <td class="right">
    2100 р.
   </td>
  </tr>
  <tr style="display: none;">
   <td>
    Телевизоры с диагональю более 51"
   </td>
   <td class="right">
    2700 р.
   </td>
  </tr>
 </table>
</div>
<div class="table-responsive">
 <table class="table">
  <tr class="clicker">
   <td>
    <h4>
     Проекционные телевизоры и видеопроекторы
    </h4>
   </td>
   <td class="right">
    <span class="glyphicon glyphicon-chevron-left">
    </span>
   </td>
  </tr>
  <tr style="display: none;">
   <td>
    Телевизоры с диагональю 44" и менее
   </td>
   <td class="right">
    1200 р.
   </td>
  </tr>
  <tr style="display: none;">
   <td>
    Телевизоры с диагональю 45" и более
   </td>
   <td class="right">
    1500 р.
   </td>
  </tr>
  <tr style="display: none;">
   <td>
    Замена лампы в проекционном телевизоре (видеопроекторе)
   </td>
   <td class="right">
    800 р.
   </td>
  </tr>
  <tr style="display: none;">
   <td>
    Ремонт/чистка видеопроекторы переносные и портативные
   </td>
   <td class="right">
    800 р.
   </td>
  </tr>
  <tr style="display: none;">
   <td>
    Ремонт/чистка видеопроекторы стационарные
   </td>
   <td class="right">
    800 р.
   </td>
  </tr>
  <tr style="display: none;">
   <td>
    Ремонт/чистка видеопроекторы профессиональные
   </td>
   <td class="right">
    от 3000 р.
   </td>
  </tr>
 </table>
</div>
<div class="table-responsive">
 <table class="table">
  <tr class="clicker">
   <td>
    <h4>
     Видеокамеры
    </h4>
   </td>
   <td class="right">
    <span class="glyphicon glyphicon-chevron-left">
    </span>
   </td>
  </tr>
  <tr style="display: none;">
   <td>
    Видеокамеры кассетные VHS, S-VHS-C, S-VHS, Video 8, VHS-C, Digital 8
   </td>
   <td class="right">
    600 р.
   </td>
  </tr>
  <tr style="display: none;">
   <td>
    Видеокамеры кассетные цифровые DV
   </td>
   <td class="right">
    1000 р.
   </td>
  </tr>
  <tr style="display: none;">
   <td>
    Видеокамеры c DVD или с HDD
   </td>
   <td class="right">
    800 р.
   </td>
  </tr>
  <tr style="display: none;">
   <td>
    Видеокамеры профессиональные и High Definition
   </td>
   <td class="right">
    от 1000 р.
   </td>
  </tr>
 </table>
</div>
<div class="table-responsive">
 <table class="table">
  <tr class="clicker">
   <td>
    <h4>
     Автоэлектроника
    </h4>
   </td>
   <td class="right">
    <span class="glyphicon glyphicon-chevron-left">
    </span>
   </td>
  </tr>
  <tr style="display: none;">
   <td>
    Автомагнитола, автоусилитель
   </td>
   <td class="right">
    от 300 р.
   </td>
  </tr>
  <tr style="display: none;">
   <td>
    CD-чейнджер
   </td>
   <td class="right">
    от 500 р.
   </td>
  </tr>
  <tr style="display: none;">
   <td>
    Автомагнитолы MP3
   </td>
   <td class="right">
    от 300 р.
   </td>
  </tr>
  <tr style="display: none;">
   <td>
    Автомагнитолы CD/DVD с моторизованным ЖК дисплеем
   </td>
   <td class="right">
    от 800 р.
   </td>
  </tr>
  <tr style="display: none;">
   <td>
    Двухдиновые автомагнитолы
   </td>
   <td class="right">
    от 800 р.
   </td>
  </tr>
  <tr style="display: none;">
   <td>
    Сабвуферы
   </td>
   <td class="right">
    от 500 р.
   </td>
  </tr>
  <tr style="display: none;">
   <td>
    GPS навигаторы
   </td>
   <td class="right">
    от 300 р.
   </td>
  </tr>
 </table>
</div>
<div class="table-responsive">
 <table class="table">
  <tr class="clicker">
   <td>
    <h4>
     СВЧ-печи
    </h4>
   </td>
   <td class="right">
    <span class="glyphicon glyphicon-chevron-left">
    </span>
   </td>
  </tr>
  <tr style="display: none;">
   <td>
    СВЧ-печь соло, с грилем
   </td>
   <td class="right">
    500 р.
   </td>
  </tr>
  <tr style="display: none;">
   <td>
    СВЧ с конвекцией, инверторные
   </td>
   <td class="right">
    600 р.
   </td>
  </tr>
 </table>
</div>
<div class="table-responsive">
 <table class="table">
  <tr class="clicker">
   <td>
    <h4>
     Ремонт мелкой бытовой техники
    </h4>
   </td>
   <td class="right">
    <span class="glyphicon glyphicon-chevron-left">
    </span>
   </td>
  </tr>
  <tr style="display: none;">
   <td>
    Радиотелефон
   </td>
   <td class="right">
    300 р.
   </td>
  </tr>
  <tr style="display: none;">
   <td>
    Проводной телефон
   </td>
   <td class="right">
    от 300 р.
   </td>
  </tr>
  <tr style="display: none;">
   <td>
    Пылесос
   </td>
   <td class="right">
    от 500 р.
   </td>
  </tr>
  <tr style="display: none;">
   <td>
    Чайник, утюг, электробритва, фен
   </td>
   <td class="right">
    от 300 р.
   </td>
  </tr>
  <tr style="display: none;">
   <td>
    Кухонный комбайн, мясорубка, миксер, хлебопечка
   </td>
   <td class="right">
    от 500 р.
   </td>
  </tr>
  <tr style="display: none;">
   <td>
    Кофеварка, кофемашина
   </td>
   <td class="right">
    от 400 р.
   </td>
  </tr>
  <tr style="display: none;">
   <td>
    Аэрогриль
   </td>
   <td class="right">
    от 300 р.
   </td>
  </tr>
  <tr style="display: none;">
   <td>
    Парогенератор бытовой
   </td>
   <td class="right">
    от 500 р.
   </td>
  </tr>
  <tr style="display: none;">
   <td>
    Парогенератор профессиональный
   </td>
   <td class="right">
    от 1000 р.
   </td>
  </tr>
 </table>
</div>
<div class="table-responsive">
 <table class="table">
  <tr class="clicker">
   <td>
    <h4>
     Домашние кинотеатры, музыкальные центры, усилители, сабвуферы, ресиверы, проигрыватели, акустика
    </h4>
   </td>
   <td class="right">
    <span class="glyphicon glyphicon-chevron-left">
    </span>
   </td>
  </tr>
  <tr style="display: none;">
   <td>
    Домашние кинотеатры
   </td>
   <td class="right">
    от 300 р.
   </td>
  </tr>
  <tr style="display: none;">
   <td>
    Музыкальные центры
   </td>
   <td class="right">
    от 300 р.
   </td>
  </tr>
  <tr style="display: none;">
   <td>
    Усилители мощности до 100 Вт
   </td>
   <td class="right">
    от 300 р.
   </td>
  </tr>
  <tr style="display: none;">
   <td>
    Усилители мощности более 100 Вт
   </td>
   <td class="right">
    от 500 р.
   </td>
  </tr>
  <tr style="display: none;">
   <td>
    Сабвуферы
   </td>
   <td class="right">
    от 500 р.
   </td>
  </tr>
  <tr style="display: none;">
   <td>
    Ресиверы,,
   </td>
   <td class="right">
    от 600 р.
   </td>
  </tr>
  <tr style="display: none;">
   <td>
    Ресиверы,, HI-END
   </td>
   <td class="right">
    от 800 р.
   </td>
  </tr>
  <tr style="display: none;">
   <td>
    Спутниковые ресиверы
   </td>
   <td class="right">
    от 300 р.
   </td>
  </tr>
  <tr style="display: none;">
   <td>
    DVD/CD/MD/HD-проигрыватели
   </td>
   <td class="right">
    от 300 р.
   </td>
  </tr>
  <tr style="display: none;">
   <td>
    Blu-ray проигрыватели
   </td>
   <td class="right">
    от 500 р.
   </td>
  </tr>
  <tr style="display: none;">
   <td>
    DVD/CD-рекордеры
   </td>
   <td class="right">
    от 300 р.
   </td>
  </tr>
  <tr style="display: none;">
   <td>
    Портативные DVD/HD плееры
   </td>
   <td class="right">
    от 500 р.
   </td>
  </tr>
  <tr style="display: none;">
   <td>
    MP3 плееры
   </td>
   <td class="right">
    от 300 р.
   </td>
  </tr>
  <tr style="display: none;">
   <td>
    Магнитолы переносные
   </td>
   <td class="right">
    от 300 р.
   </td>
  </tr>
  <tr style="display: none;">
   <td>
    Радиоприёмники
   </td>
   <td class="right">
    от 300 р.
   </td>
  </tr>
  <tr style="display: none;">
   <td>
    Акустические системы (колонки)
   </td>
   <td class="right">
    от 300 р.
   </td>
  </tr>
  <tr style="display: none;">
   <td>
    Мультимедийная акустика
   </td>
   <td class="right">
    от 300 р.
   </td>
  </tr>
  <tr style="display: none;">
   <td>
    Мультимедийная акустика
   </td>
   <td class="right">
    от 500 р.
   </td>
  </tr>
  <tr style="display: none;">
   <td>
    Восстановление, перемотка динамиков
   </td>
   <td class="right">
    от 800 р.
   </td>
  </tr>
  <tr style="display: none;">
   <td>
    Наушники
   </td>
   <td class="right">
    от 200 р.
   </td>
  </tr>
  <tr style="display: none;">
   <td>
    Микрофоны
   </td>
   <td class="right">
    от 200 р.
   </td>
  </tr>
  <tr style="display: none;">
   <td>
    Медиаплеер
   </td>
   <td class="right">
    от 300 р.
   </td>
  </tr>
  <tr style="display: none;">
   <td>
    Электронная книга
   </td>
   <td class="right">
    от 500 р.
   </td>
  </tr>
  <tr style="display: none;">
   <td>
    Профессиональные колонки, сабвуферы, усилители
   </td>
   <td class="right">
    от 1500 р.
   </td>
  </tr>
  <tr style="display: none;">
   <td>
    Электронные игрушки
   </td>
   <td class="right">
    от 300 р.
   </td>
  </tr>
  <tr style="display: none;">
   <td>
    Игровые приставки стационарные
   </td>
   <td class="right">
    от 500 р.
   </td>
  </tr>
  <tr style="display: none;">
   <td>
    Игровые приставки портативные
   </td>
   <td class="right">
    от 500 р.
   </td>
  </tr>
 </table>
</div>
<div class="table-responsive">
 <table class="table">
  <tr class="clicker">
   <td>
    <h4>
     Источники бесперебойного питания (UPS), стабилизаторы напряжения, инверторы напряжения, импульсные блоки питания, сетевые фильтры
    </h4>
   </td>
   <td class="right">
    <span class="glyphicon glyphicon-chevron-left">
    </span>
   </td>
  </tr>
  <tr style="display: none;">
   <td>
    Источники бесперебойного питания UPS до 6 kVa
   </td>
   <td class="right">
    от 300 р.
   </td>
  </tr>
  <tr style="display: none;">
   <td>
    Источники бесперебойного питания UPS от 6 kVa до 15 kVa
   </td>
   <td class="right">
    от 500 р.
   </td>
  </tr>
  <tr style="display: none;">
   <td>
    Источники бесперебойного питания UPS от 20 kVa до 40 kVa
   </td>
   <td class="right">
    от 800 р.
   </td>
  </tr>
  <tr style="display: none;">
   <td>
    Источники бесперебойного питания UPS от 20 kVa от 120 kVa
   </td>
   <td class="right">
    от 1000 р.
   </td>
  </tr>
  <tr style="display: none;">
   <td>
    Замена аккумуляторов UPS
   </td>
   <td class="right">
    от 300 р.
   </td>
  </tr>
  <tr style="display: none;">
   <td>
    Стабилизатор сетевого напряжения (зависит от мощности)
   </td>
   <td class="right">
    от 300 р.
   </td>
  </tr>
  <tr style="display: none;">
   <td>
    Преобразователи AD/DC и DC/DC (зависит от мощности)
   </td>
   <td class="right">
    от 300 р.
   </td>
  </tr>
  <tr style="display: none;">
   <td>
    Инверторы напряжения, инверторы ламп подсветки LCD (зависит от мощности и диагонали LCD)
   </td>
   <td class="right">
    от 300 р.
   </td>
  </tr>
  <tr style="display: none;">
   <td>
    Импульсные блоки питания (зависит от мощности и сложности)
   </td>
   <td class="right">
    от 300 р.
   </td>
  </tr>
  <tr style="display: none;">
   <td>
    Сетевые фильтры, фильтры-удлинители
   </td>
   <td class="right">
    от 100 р.
   </td>
  </tr>
 </table>
</div>
<div class="table-responsive">
 <table class="table">
  <tr class="clicker">
   <td>
    <h4>
     Оргтехника
    </h4>
   </td>
   <td class="right">
    <span class="glyphicon glyphicon-chevron-left">
    </span>
   </td>
  </tr>
  <tr style="display: none;">
   <td>
    Инженерные системы формата А0, дубликаторы
   </td>
   <td class="right">
    от 1000 р.
   </td>
  </tr>
  <tr style="display: none;">
   <td>
    Копировальные аппараты и МФУ до 12 коп/мин
   </td>
   <td class="right">
    500 р.
   </td>
  </tr>
  <tr style="display: none;">
   <td>
    Копировальные аппараты и МФУ от 13 до 20 коп/мин
   </td>
   <td class="right">
    500 р.
   </td>
  </tr>
  <tr style="display: none;">
   <td>
    Копировальные аппараты и МФУ от 21 до 30 коп/мин
   </td>
   <td class="right">
    500 р.
   </td>
  </tr>
  <tr style="display: none;">
   <td>
    Копировальные аппараты и МФУ от 31 до 50 коп/мин
   </td>
   <td class="right">
    800 р.
   </td>
  </tr>
  <tr style="display: none;">
   <td>
    Копировальные аппараты и МФУ свыше 50 коп/мин
   </td>
   <td class="right">
    1000 р.
   </td>
  </tr>
  <tr style="display: none;">
   <td>
    Лазерные монохромные принтеры до 8 стр/мин
   </td>
   <td class="right">
    от 300 р.
   </td>
  </tr>
  <tr style="display: none;">
   <td>
    Лазерные монохромные принтеры от 9 до 20 стр/мин
   </td>
   <td class="right">
    от 400 р.
   </td>
  </tr>
  <tr style="display: none;">
   <td>
    Лазерные монохромные принтеры свыше 20 стр/мин
   </td>
   <td class="right">
    от 500 р.
   </td>
  </tr>
  <tr style="display: none;">
   <td>
    Струйные принтеры формата А-4
   </td>
   <td class="right">
    от 500 р.
   </td>
  </tr>
  <tr style="display: none;">
   <td>
    Струйные принтеры формата А-3
   </td>
   <td class="right">
    от 1000 р.
   </td>
  </tr>
  <tr style="display: none;">
   <td>
    Цветные аппараты и МФУ от 24 коп/мин
   </td>
   <td class="right">
    от 500 р.
   </td>
  </tr>
  <tr style="display: none;">
   <td>
    Цветные лазерные принтеры
   </td>
   <td class="right">
    от 600 р.
   </td>
  </tr>
  <tr style="display: none;">
   <td>
    Матричные принтеры
   </td>
   <td class="right">
    300 р.
   </td>
  </tr>
  <tr style="display: none;">
   <td>
    Ремонт факсов
   </td>
   <td class="right">
    от 300 р.
   </td>
  </tr>
  <tr style="display: none;">
   <td>
    Ремонт шредеров (уничтожителей)
   </td>
   <td class="right">
    от 300 р.
   </td>
  </tr>
  <tr style="display: none;">
   <td>
    Ремонт ризографов
   </td>
   <td class="right">
    от 1000 р.
   </td>
  </tr>
  <tr style="display: none;">
   <td>
    Ремонт сканеров
   </td>
   <td class="right">
    от 300 р.
   </td>
  </tr>
 </table>
</div>
<div class="table-responsive">
 <table class="table">
  <tr class="clicker">
   <td>
    <h4>
     Ремонт шлагбаумов, турникетов, рольставен
    </h4>
   </td>
   <td class="right">
    <span class="glyphicon glyphicon-chevron-left">
    </span>
   </td>
  </tr>
  <tr style="display: none;">
   <td>
    Шлагбаумы
   </td>
   <td class="right">
    от 1000 р.
   </td>
  </tr>
  <tr style="display: none;">
   <td>
    Турникеты
   </td>
   <td class="right">
    от 1000 р.
   </td>
  </tr>
  <tr style="display: none;">
   <td>
    Рольставни
   </td>
   <td class="right">
    от 1500 р.
   </td>
  </tr>
 </table>
</div>
<div class="table-responsive">
 <table class="table">
  <tr class="clicker">
   <td>
    <h4>
     Компьютеры
    </h4>
   </td>
   <td class="right">
    <span class="glyphicon glyphicon-chevron-left">
    </span>
   </td>
  </tr>
 </table>
</div>
<div class="table-responsive">
 <table class="table">
  <tr class="clicker">
   <td>
    <h4>
     Установка, профилактика, ремонт, замена комплектующих
    </h4>
   </td>
   <td class="right">
    <span class="glyphicon glyphicon-chevron-left">
    </span>
   </td>
  </tr>
  <tr style="display: none;">
   <td>
    Установка материнской платы, блока питания, HDD, процессора, вентилятора
   </td>
   <td class="right">
    300 р.
   </td>
  </tr>
  <tr style="display: none;">
   <td>
    Установка CD-ROM, FDD, внутреннего/внешнего модема, видео/звуковой/сетевой платы/TV-тюнера, оперативной памяти
   </td>
   <td class="right">
    300 р.
   </td>
  </tr>
  <tr style="display: none;">
   <td>
    Установка сканера/принтера, замена картриджа
   </td>
   <td class="right">
    300 р.
   </td>
  </tr>
  <tr style="display: none;">
   <td>
    Замена корпуса
   </td>
   <td class="right">
    650 р.
   </td>
  </tr>
 </table>
</div>
<div class="table-responsive">
 <table class="table">
  <tr class="clicker">
   <td>
    <h4>
     Настройка локальных и беспроводных сетей
    </h4>
   </td>
   <td class="right">
    <span class="glyphicon glyphicon-chevron-left">
    </span>
   </td>
  </tr>
  <tr style="display: none;">
   <td>
    Создание подключения к Интернет по беспроводному соединению
   </td>
   <td class="right">
    300 р.
   </td>
  </tr>
  <tr style="display: none;">
   <td>
    Монтаж точки доступа Wi-Fi (1 шт.)
   </td>
   <td class="right">
    800 р.
   </td>
  </tr>
  <tr style="display: none;">
   <td>
    Настройка безопасности Wi-Fi, организация шифрования данных в сети Wi-Fi
   </td>
   <td class="right">
    300 р.
   </td>
  </tr>
  <tr style="display: none;">
   <td>
    Настройка роутера
   </td>
   <td class="right">
    300 р.
   </td>
  </tr>
  <tr style="display: none;">
   <td>
    Подключение и настройка точки доступа (1 шт.)
   </td>
   <td class="right">
    800 р.
   </td>
  </tr>
  <tr style="display: none;">
   <td>
    Подключение и настройка сетевого принтера
   </td>
   <td class="right">
    300 р.
   </td>
  </tr>
  <tr style="display: none;">
   <td>
    Настройка комплектующих и ПО
   </td>
   <td class="right">
    от 200 р.
   </td>
  </tr>
  <tr style="display: none;">
   <td>
    Установка программного обеспечения с дистрибутива заказчика (без настройки)
   </td>
   <td class="right">
    200 р.
   </td>
  </tr>
 </table>
</div>
<div class="table-responsive">
 <table class="table">
  <tr class="clicker">
   <td>
    <h4>
     Установка и настройка операционных систем с дистрибутива заказчика
    </h4>
   </td>
   <td class="right">
    <span class="glyphicon glyphicon-chevron-left">
    </span>
   </td>
  </tr>
  <tr style="display: none;">
   <td>
    Первоначальная диагностика
   </td>
   <td class="right">
    250 р.
   </td>
  </tr>
  <tr style="display: none;">
   <td>
    Установка и настройка WINDOWS
   </td>
   <td class="right">
    300 р.
   </td>
  </tr>
  <tr style="display: none;">
   <td>
    Работа с реестром Windows
   </td>
   <td class="right">
    500 р.
   </td>
  </tr>
  <tr style="display: none;">
   <td>
    Настройка BIOS
   </td>
   <td class="right">
    200 р.
   </td>
  </tr>
  <tr style="display: none;">
   <td>
    Перенос и сохранение данных
   </td>
   <td class="right">
    500 р.
   </td>
  </tr>
  <tr style="display: none;">
   <td>
    Выявление плавающей ошибки в ПО/АО
   </td>
   <td class="right">
    300 р.
   </td>
  </tr>
  <tr style="display: none;">
   <td>
    Поиск и устранение вирусов
   </td>
   <td class="right">
    500 р.
   </td>
  </tr>
  <tr style="display: none;">
   <td>
    Комплексная антивирусная профилактика
   </td>
   <td class="right">
    800 р.
   </td>
  </tr>
  <tr style="display: none;">
   <td>
    Оптимизация и настройка системы
   </td>
   <td class="right">
    300 р.
   </td>
  </tr>
  <tr style="display: none;">
   <td>
    Восстановление ПО
   </td>
   <td class="right">
    от 300 р.
   </td>
  </tr>
  <tr style="display: none;">
   <td>
    Восстановление HDD
   </td>
   <td class="right">
    от 500 р.
   </td>
  </tr>
 </table>
</div>
<div class="table-responsive">
 <table class="table">
  <tr class="clicker">
   <td>
    <h4>
     Ремонт ноутбуков
    </h4>
   </td>
   <td class="right">
    <span class="glyphicon glyphicon-chevron-left">
    </span>
   </td>
  </tr>
  <tr style="display: none;">
   <td>
    Аппаратная диагностика без полной разборки аппарата
   </td>
   <td class="right">
    300 р.
   </td>
  </tr>
  <tr style="display: none;">
   <td>
    Аппаратная диагностика с полной разборкой аппарата
   </td>
   <td class="right">
    500 р.
   </td>
  </tr>
  <tr style="display: none;">
   <td>
    Обновление BIOS
   </td>
   <td class="right">
    300 р.
   </td>
  </tr>
  <tr style="display: none;">
   <td>
    Профилактические работы без химической чистки узлов
   </td>
   <td class="right">
    от 500 р.
   </td>
  </tr>
  <tr style="display: none;">
   <td>
    Профилактические работы с химической чисткой узлов
   </td>
   <td class="right">
    от 800 р.
   </td>
  </tr>
 </table>
</div>
<div class="table-responsive">
 <table class="table">
  <tr class="clicker">
   <td>
    <h4>
     Работы по замене узлов и модулей
    </h4>
   </td>
   <td class="right">
    <span class="glyphicon glyphicon-chevron-left">
    </span>
   </td>
  </tr>
  <tr style="display: none;">
   <td>
    Замена CD (DWD) ROM, памяти, жесткого диска (без стоимости запчастей и без разборки ноутбука)
   </td>
   <td class="right">
    300 р.
   </td>
  </tr>
  <tr style="display: none;">
   <td>
    Замена системы охлаждения ноутбука
   </td>
   <td class="right">
    600 р.
   </td>
  </tr>
  <tr style="display: none;">
   <td>
    Замена плат расширения
   </td>
   <td class="right">
    300 р.
   </td>
  </tr>
  <tr style="display: none;">
   <td>
    Замена клавиатуры
   </td>
   <td class="right">
    450 р.
   </td>
  </tr>
  <tr style="display: none;">
   <td>
    Замена матрицы (без стоимости деталей)
   </td>
   <td class="right">
    от 500 р.
   </td>
  </tr>
  <tr style="display: none;">
   <td>
    Замена системной платы ноутбука
   </td>
   <td class="right">
    1000 р.
   </td>
  </tr>
  <tr style="display: none;">
   <td>
    Замена прочих узлов и модулей ноутбука
   </td>
   <td class="right">
    от 500 р.
   </td>
  </tr>
 </table>
</div>
<div class="table-responsive">
 <table class="table">
  <tr class="clicker">
   <td>
    <h4>
     Работы по ремонту узлов и модулей
    </h4>
   </td>
   <td class="right">
    <span class="glyphicon glyphicon-chevron-left">
    </span>
   </td>
  </tr>
  <tr style="display: none;">
   <td>
    Ремонт системы охлаждения ноутбука
   </td>
   <td class="right">
    600 р.
   </td>
  </tr>
  <tr style="display: none;">
   <td>
    Ремонт внутренних шлейфов ноутбука
   </td>
   <td class="right">
    от 600 р.
   </td>
  </tr>
  <tr style="display: none;">
   <td>
    Ремонт внешнего блока питания
   </td>
   <td class="right">
    от 300 р.
   </td>
  </tr>
  <tr style="display: none;">
   <td>
    Ремонт или замена клавиши
   </td>
   <td class="right">
    от 100 р.
   </td>
  </tr>
  <tr style="display: none;">
   <td>
    Замена батареи питания CMOS
   </td>
   <td class="right">
    400 р.
   </td>
  </tr>
  <tr style="display: none;">
   <td>
    Сброс утерянного пароля BIOS (в зависимости от версии BIOS)
   </td>
   <td class="right">
    от 600 р.
   </td>
  </tr>
  <tr style="display: none;">
   <td>
    Ремонт материнской платы (простой)
   </td>
   <td class="right">
    800 р.
   </td>
  </tr>
  <tr style="display: none;">
   <td>
    Ремонт материнской платы (сложный)
   </td>
   <td class="right">
    от 1000 р.
   </td>
  </tr>
  <tr style="display: none;">
   <td>
    Ремонт матрицы
   </td>
   <td class="right">
    от 500 р.
   </td>
  </tr>
  <tr style="display: none;">
   <td>
    Ремонт корпусных деталей (простой)
   </td>
   <td class="right">
    900 р.
   </td>
  </tr>
  <tr style="display: none;">
   <td>
    Ремонт корпусных деталей (сложный)
   </td>
   <td class="right">
    1600 р.
   </td>
  </tr>
 </table>
</div>
<div class="table-responsive">
 <table class="table">
  <tr class="clicker">
   <td>
    <h4>
     Доставка техники в мастерскую (из мастерской)
    </h4>
   </td>
   <td class="right">
    <span class="glyphicon glyphicon-chevron-left">
    </span>
   </td>
  </tr>
  <tr style="display: none;">
   <td>
    Доставка легкой и малогабаритной техники
   </td>
   <td class="right">
    200 р.
   </td>
  </tr>
  <tr style="display: none;">
   <td>
    Доставка тяжелой и крупногабаритной
   </td>
   <td class="right">
    от 300 р.
   </td>
  </tr>
 </table>
</div>
<div class="table-responsive">
 <table class="table">
  <tr class="clicker">
   <td>
    <h4>
     Диагностика (оплачивается в случае отказа от ремонта аппаратуры)
    </h4>
   </td>
   <td class="right">
    <span class="glyphicon glyphicon-chevron-left">
    </span>
   </td>
  </tr>
  <tr style="display: none;">
   <td>
    Диагностика устройств без полной разборки
   </td>
   <td class="right">
    300 р.
   </td>
  </tr>
  <tr style="display: none;">
   <td>
    Диагностика устройств с полной разборкой
   </td>
   <td class="right">
    600 р.
   </td>
  </tr>
 </table>
</div>
<div class="table-responsive">
 <table class="table">
  <tr class="clicker">
   <td>
    <h4>
     ДОПОЛНИТЕЛЬНЫЕ УСЛУГИ
    </h4>
   </td>
   <td class="right">
    <span class="glyphicon glyphicon-chevron-left">
    </span>
   </td>
  </tr>
  <tr style="display: none;">
   <td>
    Срочный ремонт (по возможности)
   </td>
   <td class="right">
    Плюс 30%
   </td>
  </tr>
  <tr style="display: none;">
   <td>
    Вызов мастера на дом (в зависимости от адреса клиента)
   </td>
   <td class="right">
    от 200 р.
   </td>
  </tr>
  <tr style="display: none;">
   <td>
    Оплата ложного вызова
   </td>
   <td class="right">
    500 р.
   </td>
  </tr>
 </table>
</div>
<div class="table-responsive">
 <table class="table">
  <tr class="clicker">
   <td>
    <h4>
     Установка, подключение и настройка теле и видео техники
    </h4>
   </td>
   <td class="right">
    <span class="glyphicon glyphicon-chevron-left">
    </span>
   </td>
  </tr>
  <tr style="display: none;">
   <td>
    Подключение и настройка ТЕЛЕВИЗОРА
   </td>
   <td class="right">
    500 р.
   </td>
  </tr>
  <tr style="display: none;">
   <td>
    Подключение и настройка ВИДЕО/DVD АППАРАТУРЫ
   </td>
   <td class="right">
    500 р.
   </td>
  </tr>
  <tr style="display: none;">
   <td>
    Подключение и настройка ДОМАШНЕГО КИНОТЕАТРА
   </td>
   <td class="right">
    от 500 р.
   </td>
  </tr>
  <tr style="display: none;">
   <td>
    Подключение и настройка ЗВУКОВОЙ АППАРАТУРЫ
   </td>
   <td class="right">
    от 500 р.
   </td>
  </tr>
  <tr style="display: none;">
   <td>
    Установка плазменных и ЖК телевизоров, видеопроекторов на стенку или потолок
   </td>
   <td class="right">
    ст-сть кронштейнов + 1500р.
   </td>
  </tr>
 </table>
</div>

        </div>

        <div class="info-column col-md-4">

            <h3 class="info-title bg-info">

              <span class="glyphicon glyphicon-earphone"></span>

              <br>

              Контакты

            </h3>

            <div class="table-responsive">

              <table class="table">

                <tr>

                  <td><h5 class="text-muted">Тел.:</h5></td>

                  <td>

                    <h4 class="text-primary">+7 978 700 66 30</h4>

                  </td>

                  <td></td>

                </tr>

                <tr>

                  <td><h5 class="text-muted">Адрес:</h5></td>

                  <td>

                    <h4 class="text-primary">г. Севастополь,<br> ул. Очаковцев, д. 36,<br> офис №18</h4>

                  </td>

                  <td></td>

                </tr>

                <tr>

                  <td><h5 class="text-muted">Группа в ВК:</h5></td>

                  <td><a target="_blank" href="https://vk.com/sctop"><img width="150" class="img-responsive" src="images/vk.png"></td>

                  <td>
                    
                  </td>

                </tr>

                <tr>

                  <td><h5 class="text-muted">Либра:</h5></td>

                  <td><a target="_blank" href="https://librasevastopol.ru/?key=1306"><img width="150" class="img-responsive" src="images/libra_croped.png"></td>

                  <td>
                    
                  </td>

                </tr>

                <tr>

                  <td><h5 class="text-muted">Мы на Либра:</h5></td>

                  <td><a target="_blank" href="https://librasevastopol.ru/?151759"><img width="150" class="img-responsive" src="images/libra_croped.png"></td>

                  <td>
                    
                  </td>

                </tr>

              </table>

            </div>

            <h3 class="info-title bg-info">

                <span class="glyphicon glyphicon-map-marker"></span>

                <br>

                Карта

            </h3>

            <div class="table-responsive">

              <table>

                <tr>

                  <td>

                    <a href="https://yandex.ru/maps/?um=constructor%3AekGzjY4nkkn9atKkUN95HSZihpvuFKos&amp;source=constructorStatic" target="_blank"><img src="https://api-maps.yandex.ru/services/constructor/1.0/static/?sid=ekGzjY4nkkn9atKkUN95HSZihpvuFKos&amp;width=600&amp;height=450&amp;lang=ru_RU&amp;sourceType=constructor" alt="" style="border: 0;" /></a>

                  </td>

                </tr>

              </table>

            </div>

        </div>

      </div>

      <div id="bottom" class="row">

        <h3>

          <span class="v-center">&copy TOPMASTER, 2017</span>

        </h3>

      </div>

    </div>

  </body>

  </html>
"""

major = BeautifulSoup(html, 'html.parser')

with open('pretty.txt', 'w+') as out:
	out.write(major.prettify(formatter='html').encode('utf8'))