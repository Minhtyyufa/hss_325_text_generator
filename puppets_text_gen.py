import numpy
import sys
from nltk.tokenize import RegexpTokenizer
from nltk.corpus import stopwords
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, Dropout, LSTM
from tensorflow.keras.utils import to_categorical
from tensorflow.keras.callbacks import ModelCheckpoint
from tensorflow.keras.models import load_model
import string

class TextGenerator:

    def __init__(self, type):
        self.type = type
    def preprocess_data(self, file_path, seq_length):
        file = open(file_path, encoding="utf8").read()
        processed_inputs = self.tokenize_words(file)

        if self.type == "character":
            chars = sorted(list(set(processed_inputs)))
            input_len = len(processed_inputs)
        else:
            chars = processed_inputs.split(" ")
            chars = set(chars)
            input_len = len(processed_inputs.split(" "))
            print(chars)


        self.char_to_num = dict((c, i) for i, c in enumerate(chars))
        self.num_to_char = dict((i, c) for i, c in enumerate(chars))

        self.vocab_len = len(chars)
        print("Total number of characters:", input_len)
        print("Total vocab:", self.vocab_len)

        if self.type == "character":
            x_data, y_data = self.get_sequence_data(processed_inputs, seq_length, self.char_to_num, input_len)
        else:
            x_data, y_data = self.get_sequence_data(processed_inputs.split(" "), seq_length, self.char_to_num, input_len)

        n_patterns = len(x_data)
        print("Total Patterns:", n_patterns)

        X = numpy.reshape(x_data, (n_patterns, seq_length, 1))
        X = X / float(self.vocab_len)
        y = to_categorical(y_data)

        return (X, y)

    def train(self, file_path, model_directory , seq_length = 50, epochs=20, batch_size=256, start_from = None):
        X, y = self.preprocess_data(file_path, seq_length)

        if start_from == None:

            self.model = Sequential()
            self.model.add(LSTM(256, input_shape=(X.shape[1], X.shape[2]), return_sequences=True))
            self.model.add(Dropout(0.2))
            self.model.add(LSTM(256, return_sequences=True))
            self.model.add(Dropout(0.2))
            self.model.add(LSTM(128))
            self.model.add(Dropout(0.2))
            self.model.add(Dense(y.shape[1], activation='softmax'))

            self.model.compile(loss='categorical_crossentropy', optimizer='adam')
        else:
            self.model = load_model(start_from)

        checkpoint = ModelCheckpoint(model_directory, monitor='loss', verbose=1, save_best_only=False, save_weights_only=False,save_freq="epoch", mode='min')
        desired_callbacks = [checkpoint]

        self.model.fit(X, y, epochs=epochs, batch_size=batch_size, callbacks=desired_callbacks)

    def test(self, model_path, input_string, original_file_path):
        self.preprocess_data(original_file_path, 100)

        self.model = load_model(model_path)

        input_string = input_string.lower()
        input_string = input_string.translate(str.maketrans('', '', string.punctuation))
        print(input_string)
        if self.type == "character":
            x_data = [self.char_to_num[char] for char in input_string]
        else:
            x_data = []
            for char in input_string.split(" "):
                if char in self.char_to_num:
                    x_data.append(self.char_to_num[char])
        print("Seed:")
        print("\"", ''.join([self.num_to_char[value] for value in x_data]), "\"")

        for i in range(1000):
            x = numpy.reshape(x_data, (1, len(x_data), 1))
            x = x / float(self.vocab_len)
            prediction = self.model.predict(x, verbose=0)
            index = numpy.argmax(prediction)
            result = self.num_to_char[index]

            sys.stdout.write(result)
            if self.type == "word":
                sys.stdout.write(" ")

            x_data.append(index)
            x_data = x_data[1:len(x_data)]
    def get_sequence_data(self, processed_inputs, seq_length,char_to_num,input_len):
        x_data = []
        y_data = []

        for i in range(0, input_len - seq_length, 1):
            # Define input and output sequences
            # Input is the current character plus desired sequence length
            in_seq = processed_inputs[i:i + seq_length]

            # Out sequence is the initial character plus total sequence length
            out_seq = processed_inputs[i + seq_length]

            # We now convert list of characters to integers based on
            # previously and add the values to our lists
            x_data.append([char_to_num[char] for char in in_seq])

            y_data.append(char_to_num[out_seq])
        return (x_data, y_data)
    def tokenize_words(self, words):
        words = words.lower()
        tokenizer = RegexpTokenizer(r'\w+')
        tokens = tokenizer.tokenize(words)
        filtered_tokens = filter(lambda token: token not in stopwords.words("english"), tokens)
        return " ".join(filtered_tokens)

if __name__ == "__main__":
    text_gen = TextGenerator("character")
    #text_gen.train("Minh_responses.txt", "minh_seq_50_epoch_80", epochs= 10, seq_length=50, start_from="minh_seq_50_epoch_70")
    text_gen.test("minh_seq_50_epoch_80", "To create life is inherently divine and to some it is the ultimate goal to become like their","Minh_responses.txt")