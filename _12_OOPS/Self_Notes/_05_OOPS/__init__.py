class Student:

    def __init__(self, student_name='Rakesh', age = 16, marks = 76):  # constructor overloading
        self.student_name = student_name
        self.age = age
        self.marks = marks
        print(self.student_name, self.age, self.marks)

# Constructor Overloading
rakesh = Student()
rakesh = Student('Ravi')
rakesh = Student('Akash', 17)
rakesh = Student('Kiran', 16, 83)

# class Messenger:
#
#     def use_keyboard(self):
#         print('using keyboard')
#
#     def send_message(self):
#         print('text message sent')
#
#     def receive_message(self):
#         print('text message received')
#
# class Whatsapp(Messenger):
#
#     def send_message(self):
#         print('Text, video & audio sent using wa')
#
#     def receive_message(self):
#         print('Text, video & audio received using wa')
#
# class FacebookMessenger(Messenger):
#
#     def send_message(self):
#         print('Text, video & audio sent using fb')
#
#     def receive_message(self):
#         print('Text, video & audio received using fb')
#
# class InstaMessenger(Messenger):
#
#     def send_message(self):
#         print('Text, video & audio sent using Insta')
#
#     def receive_message(self):
#         print('Text, video & audio received using Insta')
#
# def use_messenger(ref):
#     ref.use_keyboard()
#     ref.send_message()
#     ref.receive_message()
#
# wa = Whatsapp()
# fb = FacebookMessenger()
# insta = InstaMessenger()
#
# use_messenger(wa)
# use_messenger(fb)
# use_messenger(insta)

# class Messenger:
#
#     def use_keyboard(self):
#         print('using keyboard')
#
#     def send_message(self):
#         print('text message sent')
#
#     def receive_message(self):
#         print('text message received')
#
# class Whatsapp(Messenger):
#
#     def send_message(self):
#         print('Text, video & audio sent using wa')
#
#     def receive_message(self):
#         print('Text, video & audio received using wa')
#
#     def send_live_location(self):
#         print('Live location sent using wa')
#
# class FacebookMessenger(Messenger):
#
#     def send_message(self):
#         print('Text, video & audio sent using fb')
#
#     def receive_message(self):
#         print('Text, video & audio received using fb')
#
#     def use_builtin_apps(self):
#         print('Using builtin apps using fb')
#
# class InstaMessenger(Messenger):
#
#     def send_message(self):
#         print('Text, video & audio sent using Insta')
#
#     def receive_message(self):
#         print('Text, video & audio received using Insta')
#
#     def add_filters(self):
#         print('Filters using insta')
#
# def use_messenger(ref):
#     ref.use_keyboard()
#     ref.send_message()
#     ref.receive_message()
#
# wa = Whatsapp()
# fb = FacebookMessenger()
# insta = InstaMessenger()
#
# use_messenger(wa)
# use_messenger(fb)
# use_messenger(insta)

# class Messenger:
#
#     def use_keyboard(self):
#         print('using keyboard')
#
#     def send_message(self):
#         print('text message sent')
#
#     def receive_message(self):
#         print('text message received')
#
# class Whatsapp(Messenger):
#
#     def send_message(self):
#         print('Text, video & audio sent using wa')
#
#     def receive_message(self):
#         print('Text, video & audio received using wa')
#
#     def send_live_location(self):
#         print('Live location sent using wa')
#
# class FacebookMessenger(Messenger):
#
#     def send_message(self):
#         print('Text, video & audio sent using fb')
#
#     def receive_message(self):
#         print('Text, video & audio received using fb')
#
#     def use_builtin_apps(self):
#         print('Using builtin apps using fb')
#
# class InstaMessenger(Messenger):
#
#     def send_message(self):
#         print('Text, video & audio sent using Insta')
#
#     def receive_message(self):
#         print('Text, video & audio received using Insta')
#
#     def add_filters(self):
#         print('Filters using insta')
#
# def use_messenger(ref):
#     ref.use_keyboard()
#     ref.send_message()
#     ref.receive_message()
#     ref.send_live_location() #'Whatsapp','FacebookMessenger' & 'InstaMessenger' object has no attribute 'use_builtin_apps'
#     ref.use_builtin_apps()
#     ref.add_filters()
#
# wa = Whatsapp()
# fb = FacebookMessenger()
# insta = InstaMessenger()
#
# #use_messenger(wa)
# use_messenger(fb)
# use_messenger(insta)

# class Messenger:
#
#     def use_keyboard(self):
#         print('using keyboard')
#
#     def send_message(self):
#         print('text message sent')
#
#     def receive_message(self):
#         print('text message received')
#
# class Whatsapp(Messenger):
#
#     def send_message(self):
#         print('Text, video & audio sent using wa')
#
#     def receive_message(self):
#         print('Text, video & audio received using wa')
#
#     def send_live_location(self):
#         print('Live location sent using wa')
#
# class FacebookMessenger(Messenger):
#
#     def send_message(self):
#         print('Text, video & audio sent using fb')
#
#     def receive_message(self):
#         print('Text, video & audio received using fb')
#
#     def use_builtin_apps(self):
#         print('Using builtin apps using fb')
#
# class InstaMessenger(Messenger):
#
#     def send_message(self):
#         print('Text, video & audio sent using Insta')
#
#     def receive_message(self):
#         print('Text, video & audio received using Insta')
#
#     def add_filters(self):
#         print('Filters using insta')
#
# def use_messenger(ref):
#     ref.use_keyboard()
#     ref.send_message()
#     ref.receive_message()
#     if type(ref) == Whatsapp:
#         ref.send_live_location()
#     if type(ref) == FacebookMessenger:
#         ref.use_builtin_apps()
#     if type(ref) == InstaMessenger:
#         ref.add_filters()
#
# wa = Whatsapp()
# fb = FacebookMessenger()
# insta = InstaMessenger()
#
# use_messenger(wa)
# use_messenger(fb)
# use_messenger(insta)