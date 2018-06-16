from __future__ import division

import os
import sys
import tensorflow as tf
import skimage.io as io
import numpy as np
import time

def main(argv):

    sys.path.append("./tf-image-segmentation/")
    sys.path.append("./models/slim/")

    os.environ["CUDA_VISIBLE_DEVICES"] = '1'

    import logging

    logging.basicConfig(filename='log_examp.log', level=logging.INFO)
    logging.debug('This message should go to the log file')
    logging.info('So should this')
    logging.warning('And this, too')

    from tf_image_segmentation.models.fcn_8s import FCN_8s
    from tf_image_segmentation.utils.inference import adapt_network_for_any_size_input

    number_of_classes = 21

    image_filename = argv[1]

    image_filename_placeholder = tf.placeholder(tf.string)

    feed_dict_to_use = {image_filename_placeholder: image_filename}

    image_tensor = tf.read_file(image_filename_placeholder)

    image_tensor = tf.image.decode_jpeg(image_tensor, channels=3)

    image_batch_tensor = tf.expand_dims(image_tensor, axis=0)

    FCN_8s = adapt_network_for_any_size_input(FCN_8s, 32)

    pred, fcn_16s_variables_mapping = FCN_8s(image_batch_tensor=image_batch_tensor,
                                             number_of_classes=number_of_classes,
                                             is_training=False)

    initializer = tf.local_variables_initializer()

    saver = tf.train.Saver()

    with tf.Session() as sess:
        sess.run(initializer)

        saver.restore(sess,
                      './fcn_8s_checkpoint/model_fcn8s_final.ckpt')

        image_np, pred_np = sess.run([image_tensor, pred], feed_dict=feed_dict_to_use)

        # io.imshow(image_np)
        # io.show()
        #
        # io.imshow(pred_np.squeeze())
        # io.show()

        import skimage.morphology

        imageSegmentationSign = int(argv[2])

        prediction_mask = (pred_np.squeeze() == imageSegmentationSign)

        cropped_object = image_np * np.dstack((prediction_mask,) * 3)

        square = skimage.morphology.square(5)

        temp = skimage.morphology.binary_erosion(prediction_mask, square)

        negative_mask = (temp != True)

        eroding_countour = negative_mask * prediction_mask

        eroding_countour_img = np.dstack((eroding_countour,) * 3)

        cropped_object[eroding_countour_img] = 248

        png_transparancy_mask = np.uint8(prediction_mask * 255)

        image_shape = cropped_object.shape

        png_array = np.zeros(shape=[image_shape[0], image_shape[1], 4], dtype=np.uint8)

        png_array[:, :, :3] = cropped_object

        png_array[:, :, 3] = png_transparancy_mask

        # io.imshow(cropped_object)

        nowTime = time.strftime('%Y_%m_%d_%H%M%S', time.localtime(time.time()))

        io.imsave('image_' +argv[3], png_array)

if __name__ == '__main__':
    main(sys.argv)
