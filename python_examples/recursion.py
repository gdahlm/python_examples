"""
Coding examples using basic recursion.

"""
FIB_MEMO_CACHE = {}


def fib_memo(num):
    """fib_memo(int) -> int

    Memoized fibonacci sequence generator

    Args:
        num (int): Position in the fibonacci sequence.
    Returns:
        (int): Value of the fibonacci sequence at `n`

    >>> fib_memo(2)
    1
    >>> fib_memo(20)
    6765
    >>> fib_memo(50)
    12586269025

    """
    if not isinstance(num, int):
        raise TypeError("Must be a positive int")
    if num < 1:
        raise ValueError("Must be a positive int")

    if num in FIB_MEMO_CACHE:
        return FIB_MEMO_CACHE[num]

    if num == 1:
        return 1
    elif num == 2:
        return 1
    elif num > 2:
        value = fib_memo(num - 1) + fib_memo(num - 2)

    FIB_MEMO_CACHE[num] = value

    return value


def rec_fact(num):
    """rec_fact(int) -> int

    Recursive function which takes an integer and computes the factorial.

    >>> rec_fact(4) # 4*3*2*1 = 24
    24
    """
    if not isinstance(num, int):
        raise TypeError("Must be a positive int")

    if num == 0:
        return 1

    return num * rec_fact(num - 1)


def rec_sum(num):
    """rec_sum(int) -> int

    Recursive function which takes an integer and computes
    the cumulative sum of 0 to that integer

    >>> rec_sum(4)
    10
    """
    if not isinstance(num, int):
        raise TypeError("Must be a positive int")
    if num < 0 < 500:
        raise ValueError("Must be a positive int betweeen 0-500")

    if num == 0:
        return 0

    return num + rec_sum(num - 1)


def rec_sum_digits(num):
    """rec_sum_digits(int) -> int

    Recursive function which takes an integer and computes
    the cumulative sum the individual digits of that integer.

    >>> sum_digts(4321)
    10
    """
    if not isinstance(num, int):
        raise TypeError("Must be a positive int")

    # Base Case
    if num == 0:
        return 0

    return num % 10 + rec_sum_digits(num / 10)


def word_split(phrase, list_of_words, result=None):
    """word_split(str,list) -> list

    If a phrase can be split into a list of words it returns the list.

    >>> word_split('themanran',['the','ran','man'])
    ['the', 'man', 'ran']
    >>> word_split('ilovedogsJohn',['i','am','a','dogs','lover','love','John'])
    ['i', 'love', 'dogs', 'John']
    """
    if result is None:
        result = []

    for word in list_of_words:
        if phrase.startswith(word):
            result.append(word)
            return word_split(phrase[len(word):], list_of_words, result)

    return result


def reverse_string(string, result=None):
    """reverse_string(str) -> str

    Reverse a string using recursion.

    Note:
        Does not slice (e.g. string[::-1]) or use iteration.

    >>> reverse_string('hello')
    olleh
    >>> reverse_string('hello world')
    dlrow olleh
    >>> reverse_string('123456789')
    987654321
    """
    if not isinstance(string, str):
        raise TypeError("Must be a string")

    if result is None:
        result = []

    if len(string) == len(result):
        return ''.join(result)

    # Assigned a variable for readablity.
    offset = (len(string) - 1) - len(result)
    result.append(string[offset])
    return reverse_string(string, result)


def permute(string):
    """permute(str) -> str

        Outputs a list of all possible permutations a string.

        Note: If a character is repeated, each occurence as distinct.

        >>> permute('abc')
        ['abc', 'acb', 'bac', 'bca', 'cab', 'cba']
        >>> permute('dog')
        ['dog', 'dgo', 'odg', 'ogd', 'gdo', 'god']
    """
    if not isinstance(string, str):
        raise TypeError("Must be a string")

    result = []

    if len(string) == 1:
        result = [string]
    else:
        for count, char in enumerate(string):
            for variation in permute(string[:count] + string[count + 1:]):
                result += [char + variation]

    return result


if __name__ == "__main__": # pragma: no cover
    pass
