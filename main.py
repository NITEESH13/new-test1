import re
import long_responses as long


def message_probability(user_message, recognised_words, single_response=False, required_words=[]):
    message_certainty = 0
    has_required_words = True

    # Counts how many words are present in each predefined message
    for word in user_message:
        if word in recognised_words:
            message_certainty += 1

    # Calculates the percent of recognised words in a user message
    percentage = float(message_certainty) / float(len(recognised_words))

    # Checks that the required words are in the string
    for word in required_words:
        if word not in user_message:
            has_required_words = False
            break

    # Must either have the required words, or be a single response
    if has_required_words or single_response:
        return int(percentage * 100)
    else:
        return 0


def check_all_messages(message):
    highest_prob_list = {}

    # Simplifies response creation / adds it to the dict
    def response(bot_response, list_of_words, single_response=False, required_words=[]):
        nonlocal highest_prob_list
        highest_prob_list[bot_response] = message_probability(message, list_of_words, single_response, required_words)

    # Responses -------------------------------------------------------------------------------------------------------
    response('Hello!', ['hello', 'hi', 'hey', 'sup', 'heyo'], single_response=True)
    response('See you!', ['bye', 'goodbye'], single_response=True)
    response('I\'m doing fine, and you?', ['how', 'are', 'you', 'doing'], required_words=['how'])
    response('hotel timings are 6 to 9', ['what', 'are', 'timings', 'of','hotel'], required_words=['what'])
    response('dinner timings are 6 to 9pm', ['what', 'are', 'timings', 'of', 'dinner'], required_words=['what'])
    response('lunch timings are 12 to 1', ['what', 'are', 'timings', 'of', 'lunch'], required_words=['what'])
    response('hotel menu at the time of breakfast   : dosa,idly,vada,puri', ['breakfast', 'menu'],
             required_words=['varieties'])
    response('hotel menu at the time of lunch   : rice,dal,curries,biryani', ['lunch', 'menu'],
             required_words=['varieties'])
    response('hotel menu at the time of dinner   : capathi,dahi,lemon rice,rice', ['dinner', 'menu'],
             required_words=['varieties'])

    response('hotel timings are 6 to 9am', ['what', 'are', 'timings', 'of', 'breakfast'], required_words=['what'])
    response('welcome to sodexo', ['name', 'of', 'hotel', 'is', 'sodexo'], required_words=['what'])
    response('You\'re welcome!', ['thank', 'thanks'], single_response=True)
    response('Thank you!', ['i', 'love', 'code', 'palace'], required_words=['code', 'palace'])
    response('1st bus travels from madurai to chennai at morning : around 9 am  ', ['morning'],
             required_words=['bus'])
    response('2nd bus travels from madurai to chennai at afternoon : around 1 pm  ', ['afternoon'],
             required_words=['bus'])
    response('3rd bus travels from madurai to chennai at night : around 9 pm  ', ['night'],
             required_words=['bus'])

    # Longer responses
    response(long.R_ADVICE, ['give', 'advice'], required_words=['advice'])
    response(long.R_EATING, ['what', 'you', 'eat'], required_words=['you', 'eat'])

    best_match = max(highest_prob_list, key=highest_prob_list.get)
    # print(highest_prob_list)
    # print(f'Best match = {best_match} | Score: {highest_prob_list[best_match]}')

    return long.unknown() if highest_prob_list[best_match] < 1 else best_match


# Used to get the response
def get_response(user_input):
    split_message = re.split(r'\s+|[,;?!.-]\s*', user_input.lower())
    response = check_all_messages(split_message)
    return response


# Testing the response system
while True:
    print('Bot: ' + get_response(input('You: ')))