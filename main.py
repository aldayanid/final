import os
import docker

client = docker.from_env()


def list_images():
    print('The list of all local images:\n', os.system('docker images'))
    return_or_quit()


def list_containers():
    print('List containers\n', os.system('docker container ls -a'))
    return_or_quit()


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
        print('Wrong choice, try again')
    image = client.images.pull(image_name)
    print(f'The image {image} has been pulled, and been added to the list:', os.system('docker images'))


def delete_image():
    print('To delete, please copy/paste one of the listed image IDs:\n', os.system('docker images'))
    while True:
        image_id = str(input("Delete image by IMAGE ID - 12 symbols:\n"))
        try:
            if len(image_id) != 12:
                raise ValueError()
        except ValueError:
            print('Invalid input. Try again - 12 symbols only')
        else:
            client.images.remove(image_id)
            print(f'The selected image {image_id} has been removed.\nThe updated image list', os.system('docker images'))
            return_or_quit()


def run_container():
    print('To run a new container, please copy/paste one of the listed image IDs:\n', os.system('docker images'))
    while True:
        image_id = str(input("Select the image to run a new container:\n"))
        try:
            if len(image_id) != 12:
                raise ValueError()
        except ValueError:
            print('Invalid input. Try again - 12 symbols only')
        else:
            client.containers.run(image_id, 'echo Hello RT-ED')
            print('The container has been ran.\nThe updated containers list:\n',
                  os.system('docker ps -a'))
            return_or_quit()


def stop_container():
    print('To stop a container, please copy/paste one of the listed container IDs:\n',
          os.system('docker ps -a'))

    while True:
        container_id = str(input("Select the container name to stop: "))
        try:
            if len(container_id) != 12:
                raise ValueError()
        except ValueError:
            print('Invalid input. Try again - 12 symbols only')
        else:
            client.containers.stop(container_id)
            print('The container has been ran.\nThe updated containers list:\n',
                  os.system('docker ps -a'))
            return_or_quit()


def delete_container():
    print('To delete a container, please copy/paste one of the listed container IDs:\n',
          os.system('docker ps -a'))
    while True:
        container_id = input("Select the container name to delete: ")
        try:
            if len(container_id) != 12:
                raise ValueError()
        except ValueError:
            print('Invalid input. Try again - 12 symbols only')
        else:
            os.system(f'docker rm -fv {container_id}')
            print('The container has been deleted.\nThe updated containers list:\n',
                  os.system('docker ps -a'))
            return_or_quit()


def return_or_quit():
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
        1) First action: list all images
        2) Second action: list all containers
        3) Third action: pull new image
        4) Fourth action: delete image
        5) Fifth action: run container
        6) Sixth action: stop container
        7) Seventh action:delete container
        0) Quit
    """)
    choice = int(input("Enter option: "))
    if choice == 1:
        list_images()
    elif choice == 2:
        list_containers()
    elif choice == 3:
        pull_image()
    elif choice == 4:
        delete_image()
    elif choice == 5:
        run_container()
    elif choice == 6:
        stop_container()
    elif choice == 7:
        delete_container()
    elif choice == 0:
        print("Action number 0.\nQuitting...")
        quit()
    else:
        print("Error")


if __name__ == '__main__':
    main()