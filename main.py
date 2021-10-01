import docker ##pip install docker
import itertools

CLIENT = docker.from_env()


def list_images() -> dict:
    print('\nCount:\tID:\t\tNAME:')
    num_to_image_map = dict(zip(itertools.count(start=1), CLIENT.images.list(all=True)))
    for count, image in num_to_image_map.items():
        for image_tag in image.tags:
            print('{}\t{}\t{}'.format(count, image.short_id[7:], image_tag))
    print('\n')
    return num_to_image_map


def list_containers() -> dict:
    print('\nCount:\tID:\t\tNAME:\t\t\tSTATUS:')
    num_to_container_map = dict(zip(itertools.count(start=1), CLIENT.containers.list(all=True)))
    for count, container in num_to_container_map.items():
        print('{}\t{}\t{}{}'.format(count, container.short_id, container.name.ljust(24), container.status))
    print('\n')
    return num_to_container_map


def pull_image():
    repo_list = ['1', '2', '3', '4', '5', '6', 'Q', 'q']
    image_name = ''
    chosen_repo = input(f'''
        Please select one of the following repositories:
        {'-' * 69}
        1 - Debian; 2 - Ubuntu; 3 - CentOS; 4- Fedora, 5 - Mageia, 6 - Alpine
        {'-' * 69}
        Please use numeric digits: from 1 to 6 only.
        Or just type "Q/q" to quit from the function\n
        ''')
    while chosen_repo not in repo_list:
        if chosen_repo == 'Q' or 'q':
            break
    if chosen_repo == '1':
        image_name = 'debian'
    elif chosen_repo == '2':
        image_name = 'ubuntu'
    elif chosen_repo == '3':
        image_name = 'centos'
    elif chosen_repo == '4':
        image_name = 'fedora'
    elif chosen_repo == '5':
        image_name = 'mageia'
    elif chosen_repo == '6':
        image_name = 'alpine'
    print(f'Pulling down the {image_name.capitalize()} image\n')
    CLIENT.images.pull(image_name)
    list_images()


def delete_image():
    num_to_image_map = list_images()
    image_num = int(input('Select the image number to delete: \n'))
    image_id = num_to_image_map[image_num].id
    CLIENT.images.remove(image_id, force=True)
    print(f'The selected image {image_id[7:17]} has been removed.\nThe updated image list\n')
    list_images()


def run_container():
    num_to_image_map = list_images()
    if len(num_to_image_map) != 0:
        image_num = int(input('Select the image number to run container: '))
        image_id = ''.join(num_to_image_map[image_num].tags)
        print(f'Running container from the selected image {image_id}\n')
        CLIENT.containers.run(image_id)
        list_containers()
    else:
        print('No images found on your system')
        main()


def stop_container():
    running_containers = CLIENT.containers.list(filters={'status': 'running'})
    num_to_container_map = list_containers()
    if len(running_containers) != 0:
        container_num = int(input('Select the container number to stop: '))
        container_name = num_to_container_map[container_num].name
        for container in running_containers:
            print(f'\tStopping container:\tID\t{container.short_id}\tNAME:\t{container.name}')
            container.stop()
            print(f'The container {container_name} has been stopped.')
            list_containers()
    else:
        print('No running containers found on your system')
        main()


def delete_container():
    num_to_container_map = list_containers()
    container_num = int(input('Select the container number to delete: '))
    container_name = num_to_container_map[container_num].name
    exited_filter = {'status': 'exited', 'name': container_name}
    for container in CLIENT.containers.list(filters=exited_filter):
        print(f'\tRemoving container:\tID\t{container.short_id}\tNAME:\t{container.name}')
        container.stop()
        container.remove()
        print('\t...successfully removed')
    list_containers()


def quit_or_no():
    yes_or_now_choice = input('Are you sure you want to quit?\n')
    choice_list = ['y', 'Y', 'YES', 'Yes', 'yes']
    if yes_or_now_choice in choice_list:
        print('Quitting from the program')
        quit()
    else:
        main()


def main():
    actions = {
        'q': quit_or_no,
        'li': list_images,
        'lc': list_containers,
        'pi': pull_image,
        'di': delete_image,
        'rc': run_container,
        'sc': stop_container,
        'dc': delete_container
    }
    while True:
        choice = input(f'''
        Please input command\n\t{'-' * 25}
        'q': quit,
        'li': list all images,
        'lc': list all containers,
        'pi': pull new image,
        'di': delete image,
        'rc': run container,
        'sc': stop container,
        'dc': delete container\n\t{'-' * 25}
        ''').lower()
        if choice in actions.keys():
           actions[choice]()
        else:
            print('Invalid input. Please try again')


if __name__ == '__main__':
    main()
