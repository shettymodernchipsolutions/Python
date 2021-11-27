'''
The methods which contains only the name is called as abstract
methods and a class which contains abstract methods are called as
abstract class.
'''

from abc import ABC, abstractmethod


class VoiceAssistant(ABC):

    @abstractmethod
    def activate_assistant(self):
        pass

    @abstractmethod
    def perform_task(self):
        pass

    @abstractmethod
    def use_builtin_apps(self):
        pass


class Siri(VoiceAssistant):
    def activate_assistant(self):
        print('Hey Siri, Activates Siri')

    def perform_task(self):
        print('Siri is performing the task using apple servers')

    def use_builtin_apps(self):
        print('Siri uses the builtin_apps of ios')


class Alexa(VoiceAssistant):
    def activate_assistant(self):
        print('Hey Alexa, Activates Alexa')

    def perform_task(self):
        print('Alexa is performing the task using amazon servers')

    def use_builtin_apps(self):
        print('Alexa uses the builtin_apps of fire-os')


class GoogleAssistant(VoiceAssistant):
    def activate_assistant(self):
        print('Ok Google, Activates GA')

    def perform_task(self):
        print('GA is performing the task using google servers')

    def use_builtin_apps(self):
        print('Google uses the builtin_apps of an-os')


def use_assistant(ref):
    ref.activate_assistant()
    ref.perform_task()
    ref.use_builtin_apps()


def main():
    s = Siri()
    a = Alexa()
    ga = GoogleAssistant()

    use_assistant(s)
    use_assistant(a)
    use_assistant(ga)


if __name__ == '__main__':
    main()
