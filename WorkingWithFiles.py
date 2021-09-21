import csv


def transform_user_details(csv_file_name):
    new_user_details = []

    with open(csv_file_name) as csvfile:
        user_details = csv.reader(csvfile, delimiter=',')

        for user in user_details:
            transformed_details = [user[1], user[2], user[-1]]
            new_user_details.append(transformed_details)

    return new_user_details


def create_new_user_details_csv(old_user_details_file='user_details.csv', new_user_details_file='new_user_details.csv'):
    new_user_details_file = transform_user_details(old_user_details_file)

    with open('new_user_details_file.csv', 'w') as new_file:
        csv_writer = csv.writer(new_file)
        csv_writer.writerows(new_user_details_file)


create_new_user_details_csv()

# Opens things in a 'stream'
# r, w, x (create), a (append), + (r/w)

with open('order.txt', 'w') as file:
    order_items = ['Fries', 'Onion rings', 'A Drink']

    for item in order_items:
        file.write(item + '\n')

with open('order.txt', 'r') as file:
    file_content = file.readlines()

    for line in file_content:
        print(line.replace('\n', ''))
