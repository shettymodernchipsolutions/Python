'''
Let us understand the abstraction by taking an example of voice assistant, we have several voice assistants built-in in
our mobile phones like siri in iPhone, google assistant in android phone, alexa in amazon products.
'''


class VoiceAssistant:

    def activate_assistant(self):
        print('VA activated')

    def perform_task(self):
        print('VA is performing the task')

    def use_builtin_apps(self):
        print('VA is using builtin_apps')


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
