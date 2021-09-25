import docker

client = docker.from_env()
APIClient = docker.APIClient()


def main():

    containers_list = client.containers.list()
    for containers in containers_list:
        print(f'Container ID: {containers.short_id}, name: {containers.name}, tag: {str(containers.image)[9:-2]}')

    while True:
        container_id = input('Select the container name to delete: ')
        if len(container_id) != 10:
            print('Invalid input. Try again - 10 symbols only')
        else:
            APIClient.kill(container_id)
            # os.system(f'docker rm --e5a108f688force {container_id}')
            print(f'The container has been deleted.\nThe updated containers list:')


# def main():
#     images_list = client.images.list(all=True)
#     for image in images_list:
#         for image_obj in image.tags:
#             image_str = ''.join([str(item) for item in image_obj])
#             print(f'Image ID: {image.short_id[7:]} tag: {image_str}')

# left = '<bound method Image.tag of <Image: \''
# right = ':latest\'>>'

# def main():
#     images_list = client.images.list(all=True)
#
#     print(images_list)
#     for image in images_list:
#         image_tag_str = str(image.tag)
#         print(f'Image ID: {image.short_id[7:]}; '
#               f'repository: {image_tag_str[image_tag_str.index(left)+len(left):image_tag_str.index(right)]}; '
#               f'tag: {image.tags}')


if __name__ == '__main__':
    main()
