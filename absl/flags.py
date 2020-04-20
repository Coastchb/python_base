from absl import app, flags, logging

flags.DEFINE_string('type', 'wav', 'input type.')
flags.DEFINE_integer('index', 0, 'input idnex')

FLAGS = flags.FLAGS
FLAGS.index = 0
FLAGS.mark_as_parsed()
print(FLAGS.is_parsed())
print(FLAGS.type)
print(FLAGS.index)