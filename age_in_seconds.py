__author__ = 'ryan gorden'


def what_your_age():
    age = input(" Enter your age: ")
    age_in_seconds = int(age) * 365 * 24 * 60 * 60
    print('Your age is ' + str(age_in_seconds) + ' in seconds')

what_your_age()
