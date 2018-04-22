import Tensor
import tensorflow.contrib.eager as tfe
import tensorflow as tf
import os

train_dataset_url = "http://download.tensorflow.org/data/iris_training.csv"

train_dataset_fp = tf.keras.utils.get_file(fname=os.path.basename(train_dataset_url), origin=train_dataset_url)


train_dataset = tf.data.TextLineDataset(train_dataset_fp)
train_dataset = train_dataset.skip(1)             # skip the first header row
train_dataset = train_dataset.map(Tensor.parse_csv)      # parse each row
train_dataset = train_dataset.shuffle(buffer_size=1000)  # randomize
train_dataset = train_dataset.batch(32)

# View a single example entry from a batch
features, label = tfe.Iterator(train_dataset).next()
print("example features:", features[0])
print("example label:", label[0])


# keep results for plotting
train_loss_results = []
train_accuracy_results = []

num_epochs = 201

model = Tensor.Model().getmodel()

for epoch in range(num_epochs):

  epoch_loss_avg = tfe.metrics.Mean()
  epoch_accuracy = tfe.metrics.Accuracy()

  print("epoch: %f" % epoch)

  # Training loop - using batches of 32
  for x, y in tfe.Iterator(train_dataset):
    # Optimize the model
    grads = Tensor.grad(model, x, y)
    # optimizer = Tensor.Optimizer().getoptimizer()
    optimizer = Tensor.Optimizer().getoptimizer().apply_gradients(zip(grads, model.variables), global_step=tf.train.get_or_create_global_step())

    # Track progress
    epoch_loss_avg(Tensor.loss(model, x, y))  # add current batch loss
    # compare predicted label to actual label
    epoch_accuracy(tf.argmax(model(x), axis=1, output_type=tf.int32), y)

  # end epoch
  train_loss_results.append(epoch_loss_avg.result())
  train_accuracy_results.append(epoch_accuracy.result())

  if epoch % 50 == 0:
    print("Epoch {:03d}: Loss: {:.3f}, Accuracy: {:.3%}".format(epoch, epoch_loss_avg.result(), epoch_accuracy.result()))
