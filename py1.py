import os
os.system('cls')
# print("Hello World")
# # os.mkdir('New folder (2)')

# # os.rmdir('New folder (2)')

# # os.rename('New folder (2)', 'New folder (3)')

# # for i in range(100):
# #     os.mkdir(f'New folder {i}')

# # for i in range(100):
# #     os.rmdir(f'New folder {i}')


# for i in range(101, 200, 1):
#     os.mkdir(f'New folder {i}')
    
#     for j in range(10, 100, 10):
#             os.mkdir(f'New {j}')
            

#     os.mkdir(f'New folder {i}')


# for j in range(1, 100, 2):
#             os.rmdir(f'New {j}')





for i in range(101, 200):
    os.mkdir(f'New folder {i}')
    #   os.rmdir(f'New folder {i}')  # Create parent folder

    for j in range(10, 100, 2):
        subfolder = os.path.join(f'New folder {i}', f'New {j}')
        os.mkdir(subfolder)  # Create subfolders inside parent