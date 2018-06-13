from pyforms.utils.settings_manager import conf
import settings

conf += settings

import pyforms
from pyforms import BaseWidget
from pyforms.controls import ControlText
from pyforms.controls import ControlButton


class SimpleExample1(BaseWidget):

    def __init__(self):
        super(SimpleExample1, self).__init__('Simple example 1')

        self.set_margin(5)
        # Definition of the forms fields
        self._firstname = ControlText('First name', 'Default value')
        self._middlename = ControlText('Middle name')
        self._lastname = ControlText('Lastname name')
        self._fullname = ControlText('Full name')
        self._button = ControlButton('Press this button')

        # Define the button action
        self._button.value = self.__buttonAction

        # Define the organization of the forms
        # self.formset = [('_firstname', '_middlename', '_lastname'), '_button', '_fullname', ' ']
        # The ' ' is used to indicate that a empty space should be placed at the bottom of the window
        # If you remove the ' ' the forms will occupy the entire window

        # self._fullname.addPopupSubMenuOption('Path',
        #                                      {
        #                                          'Delete': self.__dummyEvent,
        #                                          'Edit': self.__dummyEvent,
        #                                          'Interpolate': self.__dummyEvent
        #                                      })

    def __dummyEvent(self):
        ...

    def __buttonAction(self):
        """Button action event"""
        self._fullname.value = self._firstname.value + " " + self._middlename.value + \
                               " " + self._lastname.value


# Execute the application
if __name__ == "__main__":   pyforms.start_app(SimpleExample1, geometry=(800, 400, 400, 400))
