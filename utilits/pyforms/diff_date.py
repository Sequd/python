import pyforms
import datetime
from pyforms import BaseWidget
import pyforms.controls
from pyforms.controls import *
from pyforms.utils.settings_manager import conf
import settings

conf += settings


class DiffDate(BaseWidget):

    def __init__(self):
        super(DiffDate, self).__init__('Calc days ago')

        self.set_margin(5)
        # Definition of the forms fields

        self._fullname = ControlText('Different:')
        self._button = ControlButton('Calc')
        self._label_select = ControlLabel('Select:')
        self._combo_day_1 = ControlCombo('day')
        self._combo_month_1 = ControlCombo('month')
        self._combo_year_1 = ControlCombo('year')
        self._combo_day_2 = ControlCombo('day')
        self._combo_month_2 = ControlCombo('month')
        self._combo_year_2 = ControlCombo('year')

        self._init_date_combo()
        # Define the button action
        self._button.value = self.__buttonAction

        # Define the organization of the forms
        self.formset = ['_label_select',
                        ('_combo_day_1', '_combo_month_1', '_combo_year_1'),
                        ('_combo_day_2', '_combo_month_2', '_combo_year_2'),
                        '_button',
                        '_fullname',
                        ' ']
        # The ' ' is used to indicate that a empty space should be placed at the bottom of the window
        # If you remove the ' ' the forms will occupy the entire window

        # self._fullname.addPopupSubMenuOption('Path',
        #                                      {
        #                                          'Delete': self.__dummyEvent,
        #                                          'Edit': self.__dummyEvent,
        #                                          'Interpolate': self.__dummyEvent
        #                                      })

    def _init_date_combo(self):
        for i in range(1, 32):
            self._combo_day_1.add_item(str(i), i)
            self._combo_day_2.add_item(str(i), i)
        for i in range(1, 13):
            self._combo_month_1.add_item(str(i), i)
            self._combo_month_2.add_item(str(i), i)
        for i in range(1970, 2100):
            self._combo_year_1.add_item(str(i), i)
            self._combo_year_2.add_item(str(i), i)

        date_now = datetime.datetime.now().date()
        self._combo_day_2.value = date_now.day
        self._combo_month_2.value = date_now.month
        self._combo_year_2.value = date_now.year
        self._combo_year_1.value = date_now.year

    def __dummyEvent(self):
        ...

    def __buttonAction(self):
        """Button action event"""
        first = datetime.datetime(self._combo_year_1.value, self._combo_month_1.value, self._combo_day_1.value)
        second = datetime.datetime(self._combo_year_2.value, self._combo_month_2.value, self._combo_day_2.value)
        # Кол-во времени между датами.
        delta = second - first
        self._fullname.value = str(delta.days)


# Execute the application
if __name__ == "__main__":   pyforms.start_app(DiffDate, geometry=(800, 400, 400, 400))
