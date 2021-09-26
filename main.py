import docker

CLIENT = docker.from_env()


def list_images():
    images = CLIENT.images.list(all=True)
    print('\n    ID:\t\tNAME:')
    for image in images:
        for image_obj in image.tags:
            image_str = ''.join([str(item) for item in image_obj])
            print('{}\t{}'.format(image.short_id[7:], image_str))
    print('\n')


def list_containers():
    print('\nID:\t\t\tNAME:\t\t\tIMAGE:')
    for containers in CLIENT.containers.list(all=True):
        print('{}\t{}\t{}'.format(containers.short_id, repr(containers.name).rjust(25), containers.image))
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
        print('Wrong choice, try again')
    CLIENT.images.pull(image_name)
    print(f'The image {image_name} has been pulled, and been added to the list:\n')
    list_images()


def delete_image():
    print('To delete, please copy/paste one of the listed image IDs:\n')
    list_images()
    image_id = input('Delete image by IMAGE ID - 10 symbols:\n').strip()
    CLIENT.images.remove(image_id)
    print(f'The selected image {image_id} has been removed.\nThe updated image list\n')
    list_images()


def run_container():
    print('To run a new container, please copy/paste one of the listed image IDs:\n')
    list_images()
    image_id = input('Select the image to run a new container:\n').strip()
    print(f'Running container from the selected image {image_id}\n{CLIENT.containers.run(image_id)}')
    list_containers()


def stop_container():
    print(f'To stop a container, please copy/paste one of the listed container IDs:\n')
    list_containers()
    container_id = input('Select the container name to stop: ').strip()
    CLIENT.containers.stop(container_id)
    print(f'The container has been ran.\nThe updated containers list:\n')
    list_containers()


def delete_container(): ## TODO: check if running, stop and then delete
    list_containers()
    container_name = input('Select the container name to delete: ').strip()
    exited_filter = {
        'status': 'exited',
        'name': container_name
    }
    print('\nFiltered containers:')
    for container in CLIENT.containers.list(filters=exited_filter):
        print(f'\tRemoving container:\tID\t{container.short_id}\tNAME:\t{container.name}')
        container.remove()
        print('\t...successfully removed')
    list_containers()


def main():
    actions = {
        'q': quit,
        'li': list_images,
        'lc': list_containers,
        'pi': pull_image,
        'di': delete_image,
        'rc': run_container,
        'sc': stop_container,
        'dc': delete_container
    }
    choice = input(f'''
        Please input command\n\t{'-' * 25}
        'q': quit,
        'li': list_images,
        'lc': list_containers,
        'pi': pull_image,
        'di': delete_image,
        'rc': run_container,
        'sc': stop_container,
        'dc': delete_container\n\t{'-' * 25}
        ''').lower()

    if choice in actions.keys():
        actions[choice]()
    else:
        print('Invalid input. Please try again')
        quit()


if __name__ == '__main__':
    main()
