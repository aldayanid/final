import docker
import itertools

CLIENT = docker.from_env()


def list_images() -> dict:
    print('\nCount:\tID:\t\tNAME:')
    num_to_image_map = dict(zip(itertools.count(start=1), CLIENT.images.list(all=True)))
    for count, image in num_to_image_map.items():
        for image_tag in image.tags:
            print('{}\t{}\t{}'.format(count, image.short_id[7:], image_tag))
    return num_to_image_map


def list_containers() -> dict:
    print('\nCount:\tID:\t\tNAME:\t\t\tSTATUS:')
    num_to_container_map = dict(zip(itertools.count(start=1), CLIENT.containers.list(all=True)))
    for count, container in num_to_container_map.items():
        print('{}\t{}\t{}{}'.format(count, container.short_id, container.name.ljust(24), container.status))
    return num_to_container_map


def main():
    num_to_container_map = list_containers()
    container_num = int(input('Select the container count number to start: '))
    container_name = num_to_container_map[container_num].name
    exited_filter = {'status': 'exited', 'name': container_name}
    for container in CLIENT.containers.list(filters=exited_filter):
        print(f'\tStarting the container: {container.name}')
        container.start()
        print('\t...successfully started.')
    list_containers()


if __name__ == '__main__':
    main()
