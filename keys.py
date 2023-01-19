file = open('data.txt', 'r')
list = [i.strip() for i in file]
file.close()

my_token = list[0]
my_googlesheet_id = list[1]
path_to_file = list[2]

