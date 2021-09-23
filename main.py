import os


def list_images():
    print("List images\n")
    os.system('docker images')
    return_or_quit()


def list_containers():
    print("List containers\n")
    os.system('docker ls -a')
    return_or_quit()


def pull_image():
    image_name = input("Provide a name for the new image: ")
    os.system('docker image pull {} && docker images'.format(image_name))
    return_or_quit()


def delete_image():
    print("Choose one of the listed images to delete:")
    os.system('docker images')
    image_id = input("Delete image by ID: ")
    os.system('docker image rm -f {}'.format(image_id))
    os.system('docker images -a')
    return_or_quit()


def run_container():
    os.system('docker images -a')
    container_name = input("Select the image to run a new container: ")
    os.system('docker run {} && docker ls -l'.format(container_name))
    return_or_quit()


def stop_container():
    container_name = input("Select the container name to stop: ")
    os.system('docker stop {}'.format(container_name))
    return_or_quit()


def delete_container():
    os.system('docker container ls -a')
    container_name = input("Select the container name to delete: ")
    os.system('docker rm -fv {}'.format(container_name))
    return_or_quit()


def return_or_quit():
    yes_choice = ['Yes', 'YES', 'yes', 'y']
    no_choice = ['No', 'NO', 'no', 'n']
    choice = input('Please input\nYes/y to go back to the main menu, or\nNo/n to quit:\n')
    if choice in yes_choice:
        main()
    elif choice in no_choice:
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
    choice = input("Enter option: ")
    if choice == '1':
        list_images()
    elif choice == '2':
        list_containers()
    elif choice == '3':
        pull_image()
    elif choice == '4':
        delete_image()
    elif choice == '5':
        run_container()
    elif choice == '6':
        stop_container()
    elif choice == '7':
        delete_container()
    elif choice == '0':
        print("Action number 0.\nQuitting...")
        quit()
    else:
        print("Error")


if __name__ == '__main__':
    main()

