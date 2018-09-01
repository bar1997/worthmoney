class Validation (object):
    __KEY_DOESNT_EXISTS = 'Key "{0}" not found'
    __INVALID_KEY_TYPE = 'Invalid key type for "{0}", expected {1}, found {2}'
    __NOT_SAME_TYPE_IN_LIST = 'Invalid key type for "{0}", expected {1}, found {2}'
    __EMPTY_STRING_IN_LIST = 'The list "{0}" contains empty string'
    __NONE_IN_LIST = 'The list "{0}" contains none'
    __NONE_IN_KEYS = 'The key "{0}" contains none'

    def __init__(self, user_input_dict):
        self.__user_input__dict = user_input_dict
        self.__last_message = ''

    def keys_exists(self, keys):
        for key in keys:
            if key not in self.__user_input__dict.keys():
                self.__last_message = str.format(Validation.__KEY_DOESNT_EXISTS, key)
                return False

        return True

    def get_last_message(self):
        return self.__last_message

    def is_valid_type(self, keys, key_type):
        for key in keys:
            if type(self.__user_input__dict[key]) != key_type:
                expected = str(key_type.__name__)
                found = str(type(self.__user_input__dict[key]).__name__)
                self.__last_message = str.format(Validation.__INVALID_KEY_TYPE, key, expected, found)
                return False
        return True

    def is_list_contains_empty_string(self, key):
        for item in self.__user_input__dict[key]:
            if (type(item) is str or type(item) is unicode) and 0 == len(str(item)):
                self.__last_message = str.format(Validation.__EMPTY_STRING_IN_LIST, key)
                return True
        return False

    def is_list_contains_none(self, key):
        for item in self.__user_input__dict[key]:
            if item is None:
                self.__last_message = str.format(Validation.__NONE_IN_LIST, key)
                return True
        return False

    def is_list_items_same_type(self, key, key_type):
        for item in self.__user_input__dict[key]:
            if type(item) != key_type:
                expected = str(key_type.__name__)
                found = str(type(item).__name__)
                self.__last_message = str.format(Validation.__NOT_SAME_TYPE_IN_LIST, key, expected, found)
                return False
        return True

    def are_keys_none(self, keys):
        for key in keys:
            if self.__user_input__dict[key] is None:
                self.__last_message = str.format(Validation.__NONE_IN_KEYS, key)
                return True
        return False

    def is_text_in_range(self, key, min, max):
        return min <= len(self.__user_input__dict[key]) <= max
