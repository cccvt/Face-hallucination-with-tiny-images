from models import *


model_zoo = ['WGAN-GP']

def get_model(mtype, name, training):
    model = None
    if mtype == 'WGAN-GP':
        model = wgan_gp.WGAN_GP

    else:
        assert False, mtype + ' is not in the model zoo'

    assert model, mtype + ' is work in progress'

    return model(name=name, training=training)


def get_dataset(dataset_name):
    # celebA_64 = './data/celebA_tfrecords/*.tfrecord'
    # celebA_64 = '/home/xujinchang/GAN_lanc/lan_tfrecords_8_64/*.tfrecord'
    celebA_64 = '/home/xujinchang/GAN_celeA_LR_HR/celebA_tfrecords_8_64/*.tfrecord'
    lsun_bedroom_128 = './data/lsun/bedroom_128_tfrecords/*.tfrecord'

    if dataset_name == 'celeba':
        path = celebA_64
        n_examples = 202599
    # if dataset_name == 'celeba':
    #    path = celebA_64
    #    n_examples = 40000
    elif dataset_name == 'lsun':
        path = lsun_bedroom_128
        n_examples = 3033042
    else:
        raise ValueError('{} is does not supported. dataset must be celeba or lsun.'.format(dataset_name))

    return path, n_examples


def pprint_args(FLAGS):
    print("\nParameters:")
    for attr, value in sorted(vars(FLAGS).items()):
        print("{}={}".format(attr.upper(), value))
    print("")
