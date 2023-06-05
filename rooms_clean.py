import pandas as pd

room = pd.read_excel('C:/Users/infin/Downloads/project_5/room_types.xlsx')

# Cleaning room_type str
room['room_type'] = room['room_type'].str.title()
print(room.info())
print(room.head())

# Save changes
room.to_excel('C:/Users/infin/Downloads/project_5/room_types.xlsx', index=False)
