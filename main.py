import docker
client = docker.from_env()
APIClient = docker.APIClient()


def list_images():
    images_list = client.images.list(all=True)
    for image in images_list:
        for image_obj in image.tags:
            image_str = ''.join([str(item) for item in image_obj])
            print(f'Image ID: {image.short_id[7:]},\t tag: {image_str}')


def list_containers():
    containers_list = client.containers.list(all=True)
    for containers in containers_list:
        print(f'Container ID: {containers.short_id},\t name: {containers.name},\t tag: {str(containers.image)[9:-2]}')


def pull_image():
    repo_num = int(input('''
    Please choose one of the follows repositories, input:\n
    ----------------------------------\n
    1 - Debian; 2 - Ubuntu; 3 - CentOS\n'''))
    image_name = ''

    if repo_num == 1:
        image_name = 'debian'
    elif repo_num == 2:
        image_name = 'ubuntu'
    elif repo_num == 3:
        image_name = 'centos'
    else:
        print('Wrong choice, try again')    ## TODO: Make action check
    client.images.pull(image_name)
    print(f'The image {image_name} has been pulled, and been added to the list:\n {list_images()}')


def delete_image():
    print('To delete, please copy/paste one of the listed image IDs:\n')
    list_images()
    while True:
        image_id = str(input("Delete image by IMAGE ID - 12 symbols:\n"))
        try:
            if len(image_id) != 12:
                raise ValueError()
        except ValueError:
            print('Invalid input. Try again - 12 symbols only')
        else:
            client.images.remove(image_id)
            print(f'The selected image {image_id} has been removed.\nThe updated image list\n {list_images()}')
            break


def run_container():
    print('To run a new container, please copy/paste one of the listed image IDs:\n')
    list_images()
    while True:
        image_id = str(input("Select the image to run a new container:\n"))
        try:
            if len(image_id) != 12:
                raise ValueError()
        except ValueError:
            print('Invalid input. Try again - 12 symbols only')
        else:
            client.containers.run(image_id, 'echo Hello RT-ED')
            print(f'The container has been ran.\nThe updated containers list:\n{list_containers()}')
            break


def stop_container():
    print(f'To stop a container, please copy/paste one of the listed container IDs:\n{list_containers()}')
    while True:
        container_id = str(input('Select the container name to stop: '))
        try:
            if len(container_id) != 10:
                raise ValueError()
        except ValueError:
            print('Invalid input. Try again - 10 symbols only')
        else:
            client.containers.stop(container_id)
            print(f'The container has been ran.\nThe updated containers list:\n{list_containers()}')
            break


def delete_container():
    containers_list = client.containers.list()
    for containers in containers_list:
        print(f'Container ID: {containers.short_id}, name: {containers.name}, tag: {str(containers.image)[9:-2]}')

    while True:
        container_id = input('Select the container name to delete: ')
        if len(container_id) != 10:
            print('Invalid input. Try again - 10 symbols only')
        else:
            APIClient.kill(container_id)
            print(f'The container has been deleted.\nThe updated containers list:')


def selector_yes_no():
    yes_list = ['Yes', 'YES', 'yes', 'y']
    no_list = ['No', 'NO', 'no', 'n']
    choice = input('Please input\nYes/y to go back to the main menu, or\nNo/n to quit:\n')
    if choice in yes_list:
        main()
    elif choice in no_list:
        quit()
    else:
        print('Invalid input.\nQuitting...')
        quit()


def main():
    print("""
        Menu title:
        -----------
        1st action: list all images
        2nd action: list all containers
        3rd action: pull new image
        4th action: delete image
        5th action: run container
        6th action: stop container
        7th action:delete container
        0 - Quit
    """)
    choice = int(input("Enter option:\n"))
    if choice == 1:
        list_images()
        selector_yes_no()
    elif choice == 2:
        list_containers()
        selector_yes_no()
    elif choice == 3:
        pull_image()
        selector_yes_no()
    elif choice == 4:
        delete_image()
    elif choice == 5:
        run_container()
        selector_yes_no()
    elif choice == 6:
        stop_container()
        selector_yes_no()
    elif choice == 7:
        delete_container()
        selector_yes_no()
    elif choice == 0:
        print("Action number 0.\nQuitting...")
        quit()
    else:
        print("Error")


if __name__ == '__main__':
    main()
