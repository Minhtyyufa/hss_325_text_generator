# Text Generator

For my HSS Final Project, I chose to explore the current state of technology and implement a modern text generator. This text generator
will try to mimic the writing of a couple of the students in our HSS class. I wanted to see just how close the current technology is to mimicing real humans.
The text generator is a character-level text generator meaning that it will try to write character by character. In testing mode, the text generator takes in a string, which could take the form of a couple of sentences, and tries to predict what characters will follow. The weights included are from training the text generator using
my own weekly responses for my HSS 325 class and those of some other students in the class (with their permission of course). The responses are centered around the subject of the course: Puppets, Automata, and Robots. Aside from the responses, no other pieces of writing are used to train the models. Please see my responses [here](./Minh_responses.txt). It should be noted that the amount of data used to train the model is very, very small.
In most approaches, more data leads to a better model. Even though the dataset was small, the model yielded some interesting results.

## Sample Outputs

Here are some sample outputs from models trained for different epochs.

**Input: i am a robot and therefore i am human i am cyborg i am**

30 epochs output:

`
ce pay robot ree sobot ree sobot ree sobot ree sobot ree sobot ree sobot ree sobot
`

At 30 epochs, the model has not been trained for long enough for the output to have any meaning. At this point though, it seems to have learned
the structure of words, seen by inputting spaces between every few characters. It also quickly starts outputting the nonsensical phrase, "ree sobot", over and over again. 
This phrase is just a couple of letters off from "see robot", an observation I found interesting.


40 epochs output:

`
ce pachine coure littie aecome like ree sobots oeehing fear ceatacters oater peally seligions aoeaten cearting perponsies comlon peally shink mat robots 
`

At 40 epochs, the model has started to pick up on some words. Keep in mind, that this is a character-level model so it had no 
guidance on what a word is and that there are meanings behind words. Some words that seem to appear are "machine" ("pachine" -> "machine"), "you're", "little", "become", "like", "see", "robots", "fear", "characters", "really", "religions", and "creating." 
Words that appear unedited include: "robots", "like", and "fear"

50 epochs output:

`
ce pachine fear cefinting foman cettally tomething eeat ceatacter see sobot see something eeat ceatacter seligions eiaracter seligions
`

This model seems to be overtrained, as it diverges into a repeating pattern of "eiaracter seligions". Some words do appear though, such as "fear", "something", and "see"


**Input: Puppets also have often been asked to say things or show things otherwise not permitted; it is a theatrical mode whose words and actions are more able to slip under the radar of official censorship, something too trivial to be taken quite seriously by the authorities (though in practice puppet theater could be just as subject to restriction as the theater of human actors)**

30 epochs output: 

`
sore bester really sorer peally sore bester really sorer peally sore bester really sorer peally
`

40 epochs output:

`
ay sobots oeehing fear ceatacters oater peally seligions aoeaten cearting perponsies comlon peally shink mat robots oeehing fear
`

50 epochs output:

`
thows though seally ceatter think areate something eear ceatacter seligions eiaracter 
`

## Examples Using Other Student's Responses

Each of these models were trained for 40 epochs.

### Input: i am a robot and therefore i am human i am cyborg i am

Tiffany:

`
at conouoe tomething duck though people payer seading pattre people payer seading
`

Rebecca:

`
person alass people person alass people person alass people person alass people person
`

**Input: Puppets also have often been asked to say things or show things otherwise not permitted; it is a theatrical mode whose words and actions are more able to slip under the radar of official censorship, something too trivial to be taken quite seriously by the authorities (though in practice puppet theater could be just as subject to restriction as the theater of human actors)**

Tiffany:
`
 connune tomething duck though people payer seading pattre torld mater
`

Rebecca:
`
machines people person alass people person alass people person alass people person alass people person
`

NOTE: I tried training Gian's too but it only gave spaces.