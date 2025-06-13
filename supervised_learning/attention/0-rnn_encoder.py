#!/usr/bin/env python3
"""
Create a class RNNEncoder that inherits from tensorflow.keras.layers.Layer
to encode for machine translation
"""


import tensorflow as tf


class RNNEncoder(tf.keras.layers.Layer):
    """
    Class constructor def __init__(self, vocab, embedding, units, batch):
    vocab is an integer representing the size of the input vocabulary
    embedding is an integer representing the dimensionality
    of the embedding vector
    units is an integer representing the number of hidden units in the RNN cell
    batch is an integer representing the batch size

    Sets the following public instance attributes:
    batch - the batch size
    units - the number of hidden units in the RNN cell
    embedding - a keras Embedding layer that converts
    words from the vocabulary into an embedding vector
    gru - a keras GRU layer with units units

    Should return both the full sequence of outputs
    as well as the last hidden state
    Recurrent weights should be initialized with glorot_uniform
    """

    def __init__(self, vocab, embedding, units, batch):
        """
        Class constructor

        parameters:
            vocab [int]:
                represents the size of the input vocabulary
            embedding [int]:
                represents the dimensionality of the embedding vector
            units [int]:
                represents the number of hidden units in the RNN cell
            batch [int]:
                represents the batch size

        sets the public instance attributes:
            batch: the batch size
            units: the number of hidden units in the RNN cell
            embedding: a keras Enbedding layer that
                converts words from the vocabulary into an embedding vector
            gru: a keras GRU layer with units number of units
        """
        if type(vocab) is not int:
            raise TypeError(
                "vocab must be int representing the size of input vocabulary")
        if type(embedding) is not int:
            raise TypeError(
                "embedding must be int representing dimensionality of vector")
        if type(units) is not int:
            raise TypeError(
                "units must be int representing the number of hidden units")
        if type(batch) is not int:
            raise TypeError(
                "batch must be int representing the batch size")
        super(RNNEncoder, self).__init__()
        self.batch = batch
        self.units = units
        self.embedding = tf.keras.layers.Embedding(input_dim=vocab,
                                                   output_dim=embedding)
        self.gru = tf.keras.layers.GRU(units=units,
                                       return_state=True,
                                       return_sequences=True,
                                       recurrent_initializer="glorot_uniform")

    def initialize_hidden_state(self):
        """
        Public instance method def initialize_hidden_state(self):
            Initializes the hidden states for the RNN cell to a tensor of zeros
            Returns: a tensor of shape (batch, units)containing
            the initialized hidden states
        """
        hidden_states = tf.zeros(shape=(self.batch, self.units))
        return hidden_states

    def call(self, x, initial):
        """
        Public instance method def call(self, x, initial):
            x is a tensor of shape (batch, input_seq_len)
            containing the input to
            the encoder layer as word indices within the vocabulary
            initial is a tensor of shape (batch, units)
            containing the initial hidden state

            Returns: outputs, hidden
            outputs is a tensor of shape (batch, input_seq_len, units)
            containing the outputs of the encoder
            hidden is a tensor of shape (batch, units)
            containing the last hidden state of the encoder
        """
        x = self.embedding(x)
        outputs, hidden = self.gru(x, initial_state=initial)
        return outputs, hidden
