import docker
client = docker.from_env()


def list_images(): ## TODO: Try somehow to "tabulate" the output
    images = client.images.list(all=True)
    for image in images:
        for image_obj in image.tags:
            image_str = ''.join([str(item) for item in image_obj])
            print(f'Image ID: {image.short_id[7:]}\t tag: {image_str}')
    print('\n')


def list_containers(): ## TODO: Try somehow to "tabulate" the output
    print('\nID:\t\t\tNAME:\t\t\tIMAGE:')
    # print('\tID\t\tNAME\t\tSTATUS\t\tIMAGE\t') ##TODO .format
    for containers in client.containers.list(all=True):
        # print(f'ID {containers.short_id} Name: {containers.name} Image{containers.image}')
        # containers_list_trim = [containers['Id'][0:12], str(containers['Names'])[3:-2],
        #                            containers['Status'][0:6], containers['ImageID'][7:19]]
        print('{}\t{}\t{}'.format(containers.short_id, repr(containers.name).rjust(20), containers.image))
    print('\n')


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
    print(f'The image {image_name} has been pulled, and been added to the list:\n')
    list_images()


def delete_image():
    print('To delete, please copy/paste one of the listed image IDs:\n')
    list_images()
    image_id = input("Delete image by IMAGE ID - 10 symbols:\n").replace(" ", "")
    if len(image_id) == 10:     ##TODO: Nafig!
        client.images.remove(image_id)
        print(f'The selected image {image_id} has been removed.\nThe updated image list\n')
        list_images()
    else:
        print('Invalid input. Try again - 10 symbols only')


def run_container():
    print('To run a new container, please copy/paste one of the listed image IDs:\n')
    list_images()
    image_id = str(input("Select the image to run a new container:\n")).replace(" ", "")
    if len(image_id) == 10: ##TODO: Nafig!
        print(f'Running container from the selected image {image_id}\n{client.containers.run(image_id)}')
        list_containers()
    else:
        print('Invalid input. Try again - 10 symbols only')


def stop_container():
    print(f'To stop a container, please copy/paste one of the listed container IDs:\n')
    list_containers()
    container_id = input('Select the container name to stop: ').replace(" ", "")
    if len(container_id) == 10: ##TODO: Nafig!
        client.containers.stop(container_id)
        print(f'The container has been ran.\nThe updated containers list:\n')
        list_containers()
    else:
        print('Invalid input. Try again - 10 symbols only')


def delete_container(): ## TODO: check if running, stop and then delete
    containers_list = client.containers.list()
    for containers in containers_list:
        print(f'Container ID: {containers.short_id}, name: {containers.name}, tag: {str(containers.image)[9:-2]}')
        container_id = str(input('Select the container name to delete: ')).replace(" ", "") ## TODO:
        if len(container_id) == 10: ##TODO: Nafig!
            APIClient.kill(container_id)  ##TODO: add remove!
            print(f'The container has been deleted.\nThe updated containers list:')
        else:
            print('Invalid input. Try again - 10 symbols only')


def main():
    while True:
        print("""
            Please choose
            -----------
            Press for:
            'li': list all images
            'lc': list all containers
            'pi': pull new image
            'di': delete image
            'rc': run container
            'sc': stop container
            'dc': delete container
            'q': quit
        """)
        select_list = ['li', 'lc', 'pi', 'di', 'rc', 'dc', 'q']
        choice = input("Enter option:\n")
        if choice.replace(" ", "").lower() in select_list:
            if choice == 'li':
                list_images()
            elif choice == 'lc':
                list_containers()
            elif choice == 'pi':
                pull_image()
            elif choice == 'di':
                delete_image()
            elif choice == 'rc':
                run_container()
            elif choice == 'sc':
                stop_container()
            elif choice == 'dc':
                delete_container()
            elif choice == 'q':
                print('Quitting...')
                quit()
            else:
                print('Error')
        else:
            print('Invalid input. Please try again')
            quit()


if __name__ == '__main__':
    main()
