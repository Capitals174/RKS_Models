import pickle
from pathlib import Path

import numpy as np
from flask_wtf import FlaskForm
from wtforms import FloatField


def load_model(name):
    return pickle.load(open(payload_dir.joinpath(name), 'rb'))


payload_dir = Path(__file__).resolve().parent.joinpath('payload')
line_1_OCA = load_model('line_1_OCA_ver3.sav')
line_2_OCA = load_model('line_2_OCA_ver3.sav')
line_2_SA = load_model('line_2_SA_ver3.sav')
line_1_SA = load_model('line_1_SA_ver3.sav')
line_1_SA_per = load_model('line_1_SA_per3.sav')
line_2_SA_per = load_model('line_2_SA_per3.sav')


class MyFloatField(FloatField):
    def process_formdata(self, valuelist):
        if valuelist:
            try:
                self.data = float(valuelist[0].replace(',', '.'))
            except ValueError:
                self.data = None
                raise ValueError(self.gettext('Введите вещественное число'))


# Line_1_OCA
class Form1(FlaskForm):
    label = 'dedefeffew'
    atr1 = MyFloatField('Цветность, град. ', default="0.0")
    atr2 = MyFloatField('Мутность, мг/л ', default="0.0")
    atr3 = MyFloatField('PH ', default="0.0")
    atr4 = MyFloatField('Железо общее, мг/л ', default="0.0")
    atr5 = MyFloatField('Щелочность, мг-экв./л ', default="0.0")
    atr6 = MyFloatField('Аммоний, мг/л ', default="0.0")
    atr7 = MyFloatField('Известь, мг/л ', default="0.0")

    def get_values(self):
        return [
            self.atr1.data,
            self.atr2.data,
            self.atr3.data,
            self.atr4.data,
            self.atr5.data,
            self.atr6.data,
            self.atr7.data,
        ]

    def predict(self):
        inp = np.array([self.get_values()])
        model = line_1_OCA
        res = model.predict(inp)
        return round(res[0], 3)


# Line_1_SA
class Form2(FlaskForm):
    atr1 = MyFloatField('Цветность, град. ', default="0.0")
    atr2 = MyFloatField('Мутность, мг/л ', default="0.0")
    atr4 = MyFloatField('Марганец, мг/л. ', default="0.0")
    atr5 = MyFloatField('Железо общее, мг/л. ', default="0.0")
    atr6 = MyFloatField('Щелочность, мг-экв./л. ', default="0.0")
    atr7 = MyFloatField('Аммоний, мг/л. ', default="0.0")
    atr8 = MyFloatField('Известь, мг/л. ', default="0.0")
    atr9 = MyFloatField('Фактическая производительность станции, тыс. куб.м/сут.', default="0.0")
    atr10 = MyFloatField('Цена сульфата алюминия руб/тонн без НДС', default="12690.0")
    atr11 = MyFloatField('Цена извести руб/тонн без НДС', default="10791.6")

    def get_values(self):
        return [
            self.atr1.data,
            self.atr2.data,
            self.atr4.data,
            self.atr5.data,
            self.atr6.data,
            self.atr7.data,
            self.atr8.data,
        ]

    def predict(self):
        inp = np.array([self.get_values()])
        model = line_1_SA
        model_per = line_1_SA_per
        res = model.predict(inp)
        res_per = model_per.predict(inp)

        q = self.atr9.data  # Фактическая производительность станции
        coag = model.predict(inp)[0]
        flok = self.atr7.data
        coag_price = self.atr10.data  # Цена сульфата алюминия руб/тонн без НДС
        flok_price = self.atr11.data  # Цена извести руб/тонн без НДС
        # Cтоимость комбинации сульфат алюминия + известь, тыс. руб без НДС/сут.
        day_coast = (coag * q * (100 / 16.1) * coag_price / 1000 + flok * (100 / 67) * flok_price / 1000) * q / 1000
        return round(res[0], 3), round(res_per[0], 3), round(day_coast, 3)


# Line_2_SA
class Form3(FlaskForm):
    atr1 = MyFloatField('Цветность, град. ', default="0.0")
    atr2 = MyFloatField('Мутность, мг/л ', default="0.0")
    atr4 = MyFloatField('Марганец, мг/л. ', default="0.0")
    atr5 = MyFloatField('Железо общее, мг/л. ', default="0.0")
    atr6 = MyFloatField('Щелочность, мг-экв./л. ', default="0.0")
    atr7 = MyFloatField('Аммоний, мг/л. ', default="0.0")
    atr8 = MyFloatField('Известь, мг/л. ', default="0.0")
    atr9 = MyFloatField('Фактическая производительность станции, тыс. куб.м/сут.', default="0.0")
    atr10 = MyFloatField('Цена сульфата алюминия руб/тонн без НДС', default="12690.0")
    atr11 = MyFloatField('Цена извести руб/тонн без НДС', default="10791.6")

    def get_values(self):
        return [
            self.atr1.data,
            self.atr2.data,
            self.atr4.data,
            self.atr5.data,
            self.atr6.data,
            self.atr7.data,
            self.atr8.data,
        ]

    def predict(self):
        inp = np.array([self.get_values()])
        model = line_2_SA
        model_per = line_2_SA_per
        res = model.predict(inp)
        res_per = model_per.predict(inp)

        q = self.atr9.data  # Фактическая производительность станции
        coag = model.predict(inp)[0]
        flok = self.atr8.data
        coag_price = self.atr10.data  # Цена сульфата алюминия руб/тонн без НДС
        flok_price = self.atr11.data  # Цена извести руб/тонн без НДС

        # Cтоимость комбинации сульфат алюминия + известь, тыс. руб без НДС/сут.
        day_coast = (coag * q * (100 / 16.1) * coag_price / 1000 + flok * (100 / 67) * flok_price / 1000) * q / 1000
        return round(res[0], 3), round(res_per[0], 3), round(day_coast, 3)


# Line_2_OCA
class Form4(FlaskForm):
    atr1 = MyFloatField('Цветность, град. ', default="0.0")
    atr2 = MyFloatField('Мутность, мг/л ', default="0.0")
    atr3 = MyFloatField('PH ', default="0.0")
    atr4 = MyFloatField('Железо общее, мг/л. ', default="0.0")
    atr5 = MyFloatField('Щелочность, мг-экв./л. ', default="0.0")
    atr6 = MyFloatField('Аммоний, мг/л. ', default="0.0")
    atr7 = MyFloatField('Известь, мг/л. ', default="0.0")

    def get_values(self):
        return [
            self.atr1.data,
            self.atr2.data,
            self.atr3.data,
            self.atr4.data,
            self.atr5.data,
            self.atr6.data,
            self.atr7.data,
        ]

    def predict(self):
        inp = np.array([self.get_values()])
        model = line_2_OCA
        res = model.predict(inp)
        return round(res[0], 3)
