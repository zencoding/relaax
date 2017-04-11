import sys
sys.path.append('../lib')
import tensorflow as tf
import numpy as np

from relaax.common.algorithms import subgraph
#from ..lib import graph
import graph
from relaax.server.common import session

STATE_SIZE = 2   # state_size
ACTION_SIZE = 1  # action_size

HIDDEN_1 = []    # hidden_sizes
HIDDEN_2 = [2]   # hidden_sizes

BATCH_SIZE = 10  # batch_size
LEARN_RATE = 1e-2
EPOCHS = 10


class DiffLoss(subgraph.Subgraph):
    def build_graph(self, action, network):
        return tf.reduce_sum(tf.abs(action.node - network.node), axis=[1])


class Policy(subgraph.Subgraph):
    def build_graph(self, network, loss):
        self.gradients = tf.gradients(loss.node, network.weights.node)
        return network.node

    def get_action(self, state):
        return subgraph.Subgraph.Op(self.node, state=state)

    def compute_gradients(self, state, action):
        return subgraph.Subgraph.Op(
            self.gradients,
            state=state,
            action=action
        )


class Model(subgraph.Subgraph):
    def build_graph(self, hidden_sizes):
        ph_gradients = graph.Placeholders(zip(
            [STATE_SIZE] + hidden_sizes,
            hidden_sizes + [ACTION_SIZE]
        ))
        sg_weights = graph.Variables(placeholders=ph_gradients,
                                     initializer=graph.XavierInitializer())

        ph_state = graph.Placeholder((None, STATE_SIZE))
        ph_action = graph.Placeholder((None, ACTION_SIZE))

        sg_network = graph.FullyConnected(ph_state, sg_weights)
        sg_policy_loss = DiffLoss(
            action=ph_action,
            network=sg_network
        )

        sg_policy = Policy(sg_network, sg_policy_loss)

        sg_apply_gradients = graph.ApplyGradients(
            graph.AdamOptimizer(learning_rate=LEARN_RATE),
            sg_weights,
            ph_gradients
        )

        sg_initialize = graph.Initialize()

        # Expose public API
        self.op_get_action = sg_policy.get_action(ph_state)
        self.op_compute_gradients = sg_policy.compute_gradients(ph_state, ph_action)
        self.op_apply_gradients = sg_apply_gradients.apply_gradients(ph_gradients)
        self.op_initialize = sg_initialize.initialize()

    # computes gradients
    def compute_gradients(self, sess, states, actions):
        return sess.op_compute_gradients(
            state=states,
            action=actions
        )

    # applies gradients
    def apply_gradients(self, gradients):
        self.op_apply_gradients(gradients=gradients)


def run(hidden_sizes):
    # Build TF graph
    model = Model(hidden_sizes)
    # Initialize TF
    sess = session.Session(model)

    for i in range(EPOCHS):
        states = np.random.randint(2, size=(BATCH_SIZE, STATE_SIZE))
        target = np.vstack(np.remainder(np.sum(states, axis=1), 2))
        #act_probs = sess.op_get_action(state=states)
        #print('Test', act_probs)
        model.apply_gradients(model.compute_gradients(sess, states, target))

    print('Model {} loss error:'.format(hidden_sizes))

if __name__ == '__main__':
    run(HIDDEN_1)
    run(HIDDEN_2)
