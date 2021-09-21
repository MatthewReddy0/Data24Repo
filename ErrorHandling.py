try:
    with open('document.txt') as file:

        file.readlines()
except FileNotFoundError as error_message:
    print('File doesn\'t exist, fool\n', error_message)
    raise

except IndexError as error_message:
    print('Not that many elements, mate\n', error_message)

finally:
    print('Execution has stopped.')
